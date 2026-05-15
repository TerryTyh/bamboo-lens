#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "outputs" / "official_candidates.json"
REVIEWED_EVENTS_FILE = ROOT / "outputs" / "reviewed_events.json"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


def parse_date(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.strptime(value[:10], "%Y-%m-%d")
    except ValueError:
        return None


def is_recent(item: dict, today: datetime, days: int = 2) -> bool:
    parsed = parse_date(item.get("date", "")) or parse_date(item.get("fetched_at", ""))
    if parsed is None:
        return False
    age = today.date() - parsed.date()
    return timedelta(days=0) <= age <= timedelta(days=days)


def call_openai(api_key: str, title: str, source_url: str, source_text: str) -> list[str]:
    prompt = f"""
你是 Bamboo Lens 的投资研究助理。请只基于给定原文内容，写中文内容摘要。

要求：
1. 不要写“为什么值得看”“下一步动作”“候选/研判”等流程话术。
2. 先讲文章本身到底说了什么，再讲对公司理解的影响。
3. 如果原文没有金额、规模、客户、产品、时间，不要编造。
4. 输出 5 到 8 条，每条尽量有事实密度。
5. 语言要像给投资人读的简报，不要像机器模板。

标题：{title}
来源：{source_url}

原文内容：
{source_text[:6000]}
""".strip()

    payload = {
        "model": os.environ.get("OPENAI_SUMMARY_MODEL", "gpt-4.1-mini"),
        "messages": [
            {"role": "system", "content": "你擅长把公司公告、新闻稿和财报电话会内容压缩成高信息密度的中文投资摘要。"},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    last_error: Exception | None = None
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                result = json.loads(response.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as error:
            last_error = error
            if error.code != 429 or attempt == 3:
                raise
            time.sleep(attempt * 8)
    else:
        assert last_error is not None
        raise last_error
    content = normalize(result["choices"][0]["message"]["content"])
    lines = []
    for raw in content.replace("；", "\n").splitlines():
        line = raw.strip(" -0123456789.、")
        if line:
            lines.append(line)
    return lines[:8]

def backfill_from_reviewed_events(payload: dict) -> int:
    if not REVIEWED_EVENTS_FILE.exists():
        return 0

    reviewed = json.loads(REVIEWED_EVENTS_FILE.read_text(encoding="utf-8"))
    by_candidate_title: dict[str, dict] = {}
    by_source_url: dict[str, dict] = {}
    for records in (reviewed.get("companies") or {}).values():
        for event in records:
            candidate_title = normalize(event.get("source_candidate_title", ""))
            source_url = normalize(event.get("source_url", ""))
            if candidate_title:
                by_candidate_title[candidate_title] = event
            if source_url:
                by_source_url[source_url] = event

    def to_lines(event: dict) -> list[str]:
        lines: list[str] = []
        for raw in (event.get("source_summary") or [])[:6]:
            line = normalize(raw)
            if line:
                lines.append(line)
        for raw in [event.get("business_analysis", ""), event.get("valuation_analysis", "")]:
            text = normalize(raw)
            if not text:
                continue
            # Keep it short and punchy for candidate summaries.
            lines.append(text[:120])
        for raw in (event.get("verification") or [])[:2]:
            line = normalize(raw)
            if line:
                lines.append(line)
        deduped = []
        seen = set()
        for line in lines:
            if line in seen:
                continue
            seen.add(line)
            deduped.append(line)
        return deduped[:8]

    updated = 0
    for company in (payload.get("companies") or {}).values():
        for item in company:
            if item.get("content_summary"):
                continue
            source_url = normalize(item.get("source_url", ""))
            title = normalize(item.get("title", ""))
            matched = by_source_url.get(source_url) or by_candidate_title.get(title)
            if not matched:
                continue
            lines = to_lines(matched)
            if not lines:
                continue
            item["content_summary"] = lines
            item.pop("summary_error", None)
            updated += 1
    return updated


def main() -> None:
    if not OUTPUT_FILE.exists():
        return
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()

    payload = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
    if not api_key:
        updated = backfill_from_reviewed_events(payload)
        if updated:
            OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Missing OPENAI_API_KEY; backfilled from reviewed events: {updated}")
        return

    today = datetime.now(ZoneInfo("Asia/Shanghai"))
    updated = 0
    failed = 0
    for company in (payload.get("companies") or {}).values():
        for item in company:
            if item.get("content_summary") or not is_recent(item, today):
                continue
            source_text = normalize(item.get("source_body") or item.get("source_excerpt") or "")
            if len(source_text) < 120:
                continue
            try:
                item["content_summary"] = call_openai(
                    api_key,
                    item.get("title", ""),
                    item.get("source_url", ""),
                    source_text,
                )
                item.pop("summary_error", None)
                updated += 1
            except Exception as error:  # noqa: BLE001
                item["summary_error"] = str(error)[:240]
                failed += 1

    if updated or failed:
        OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Candidate summaries enriched: {updated}, failed: {failed}")


if __name__ == "__main__":
    main()
