#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "outputs" / "official_candidates.json"


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
    with urllib.request.urlopen(request, timeout=45) as response:
        result = json.loads(response.read().decode("utf-8"))
    content = normalize(result["choices"][0]["message"]["content"])
    lines = []
    for raw in content.replace("；", "\n").splitlines():
        line = raw.strip(" -0123456789.、")
        if line:
            lines.append(line)
    return lines[:8]


def main() -> None:
    if not OUTPUT_FILE.exists():
        return
    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("Missing OPENAI_API_KEY; skipped candidate summary enrichment.")
        return

    payload = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
    today = datetime.now()
    updated = 0
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
                updated += 1
            except Exception as error:  # noqa: BLE001
                item["summary_error"] = str(error)[:240]

    if updated:
        OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Candidate summaries enriched: {updated}")


if __name__ == "__main__":
    main()
