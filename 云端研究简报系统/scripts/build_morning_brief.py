#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
REVIEWED_EVENTS_FILE = OUTPUT_DIR / "reviewed_events.json"
MORNING_BRIEF_FILE = OUTPUT_DIR / "morning_brief.md"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


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

    source_paragraph = normalize(" ".join(source_summary)) if source_summary else normalize(item.get("fact", ""))
    source_url = normalize(item.get("source_url", ""))
    source_line = f"\n\n来源：[{company} 原文]({source_url})" if source_url else ""

    evidence_lines = "\n".join(f"- {normalize(line)}" for line in evidence[:6] if normalize(line))
    verification_lines = "\n".join(f"- {normalize(line)}" for line in verification[:6] if normalize(line))

    business = normalize(item.get("business_analysis", ""))
    valuation = normalize(item.get("valuation_analysis", ""))

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
