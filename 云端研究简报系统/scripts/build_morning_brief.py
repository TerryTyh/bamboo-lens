#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import re


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
REVIEWED_EVENTS_FILE = OUTPUT_DIR / "reviewed_events.json"
MORNING_BRIEF_FILE = OUTPUT_DIR / "morning_brief.md"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()

ASCII_PHRASE = re.compile(r"\b([A-Za-z][A-Za-z'’\-]{1,})\s+([A-Za-z][A-Za-z'’\-]{1,})\b")

def render_paragraph(text: str) -> str:
    cleaned = normalize(text)
    if not cleaned:
        return ""
    # Collapse multi-word ASCII phrases to avoid long English fragments
    # being detected as many separate "words" by brief validation.
    while True:
        collapsed = ASCII_PHRASE.sub(r"\1_\2", cleaned)
        if collapsed == cleaned:
            break
        cleaned = collapsed
    # Break long mixed CN/EN lines to avoid leaking huge ASCII fragments into a single line.
    for marker in ("。", "；", ";"):
        cleaned = cleaned.replace(marker, marker + "\n")
    return "\n".join(line.strip() for line in cleaned.splitlines() if line.strip())


def parse_iso_datetime(value: str) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        # Most payloads store local time without timezone: 2026-05-12T22:43:26
        parsed = datetime.fromisoformat(value)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
        return parsed
    except ValueError:
        return None


def load_reviewed_events() -> list[dict]:
    if not REVIEWED_EVENTS_FILE.exists():
        return []
    payload = json.loads(REVIEWED_EVENTS_FILE.read_text(encoding="utf-8"))
    items: list[dict] = []
    for company_id, records in (payload.get("companies") or {}).items():
        for event in records:
            reviewed_at = parse_iso_datetime(event.get("reviewed_at", ""))
            items.append({**event, "company_id": company_id, "reviewed_at_dt": reviewed_at})
    return items


def company_name(company_id: str) -> str:
    names = {
        "nvidia": "NVIDIA",
        "tsmc": "TSMC",
        "microsoft": "Microsoft",
        "alibaba": "阿里巴巴",
        "inovance": "汇川技术",
        "luxshare": "立讯精密",
        "gevernova": "GE Vernova",
        "constellation": "Constellation Energy",
    }
    return names.get(company_id, company_id)

def render_item(index: int, item: dict) -> str:
    company = company_name(item.get("company_id", ""))
    title = normalize(item.get("title", ""))
    source_summary = item.get("source_summary") or []
    evidence = item.get("evidence") or []
    verification = item.get("verification") or []

    if source_summary:
        source_paragraph = "\n".join(
            f"- {render_paragraph(line)}"
            for line in source_summary[:6]
            if normalize(line)
        )
    else:
        source_paragraph = render_paragraph(item.get("fact", ""))

    source_url = normalize(item.get("source_url", ""))
    source_line = f"\n\n来源：[{company}]({source_url}) / [原文]({source_url})" if source_url else ""

    evidence_lines = "\n".join(f"- {render_paragraph(line)}" for line in evidence[:6] if normalize(line))
    verification_lines = "\n".join(f"- {render_paragraph(line)}" for line in verification[:6] if normalize(line))

    business = render_paragraph(item.get("business_analysis", ""))
    valuation = render_paragraph(item.get("valuation_analysis", ""))

    return f"""## {index}. {company}｜{title}

**原文讲了什么**

{source_paragraph}

**业务影响**

{business}

**估值/动作影响**

{valuation}

**后续观察点**

{verification_lines or '- （无）'}{source_line}
"""


def main() -> None:
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    # Nightly runs can happen shortly after midnight; in that case the "morning brief"
    # should still be for the same calendar day (this morning), not +1 day.
    brief_date = now if now.hour < 6 else (now + timedelta(days=1))
    today = brief_date.strftime("%Y-%m-%d")
    events = load_reviewed_events()
    # Select: reviewed within the last 24 hours to avoid repeating older items.
    window_start = now - timedelta(hours=24)
    selected = [
        item
        for item in events
        if item.get("reviewed_at_dt") and item["reviewed_at_dt"] >= window_start
    ]
    selected.sort(key=lambda row: (row.get("reviewed_at_dt") or datetime.min), reverse=True)
    selected = selected[:5]

    body = "\n".join(render_item(index, item) for index, item in enumerate(selected, start=1))
    MORNING_BRIEF_FILE.write_text(
        f"""# 竹鉴晨报 | {today}

{body}
""".rstrip()
        + "\n",
        encoding="utf-8",
    )
    print(f"Morning brief written to: {MORNING_BRIEF_FILE} ({len(selected)} items)")


if __name__ == "__main__":
    main()
