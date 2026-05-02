#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
COMPANY_STATE_FILE = OUTPUT_DIR / "company_state.json"
PORTAL_COMPANY_STATE_FILE = PROJECT_ROOT / "研究门户" / "company-state-data.js"


def load_event_store() -> dict:
    if not EVENT_STORE_FILE.exists():
        return {"generated_at": "", "companies": {}}
    return json.loads(EVENT_STORE_FILE.read_text(encoding="utf-8"))


def first_sentence(text: str, limit: int = 180) -> str:
    cleaned = " ".join(str(text or "").split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rstrip() + "..."


def verification_text(event: dict) -> str:
    items = event.get("verification") or []
    if items:
        return "；".join(str(item).strip() for item in items[:3] if str(item).strip())
    return "下一次重点验证：" + first_sentence(event.get("fact") or event.get("judgment"), 120)


def event_link(company_id: str, event_index: int) -> str:
    return f"./event.html?company={company_id}&event={event_index}&return=company&v=20260412-24"


def build_company_state(event_store: dict) -> dict:
    companies = {}
    for company_id, company in event_store.get("companies", {}).items():
        events = company.get("events", [])
        if not events:
            continue

        latest = events[0]
        business_analysis = latest.get("business_analysis") or latest.get("judgment") or latest.get("fact")
        valuation_analysis = latest.get("valuation_analysis") or latest.get("judgment") or latest.get("action")
        companies[company_id] = {
            "name": company.get("name", company_id),
            "updated_at": datetime.now().isoformat(timespec="seconds"),
            "source_event_index": 0,
            "source_event_title": latest.get("title", ""),
            "source_event_date": latest.get("date", ""),
            "latestEvent": f"{latest.get('date', '')}｜{latest.get('title', '')}",
            "businessImpact": first_sentence(business_analysis, 240),
            "valuationImpact": first_sentence(valuation_analysis, 240),
            "nextCheck": verification_text(latest),
            "action": latest.get("action", ""),
            "priority": latest.get("priority", ""),
            "sourceLink": event_link(company_id, 0),
        }
    return companies


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    event_store = load_event_store()
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_generated_at": event_store.get("generated_at", ""),
        "companies": build_company_state(event_store),
    }
    COMPANY_STATE_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_COMPANY_STATE_FILE.write_text(
        "window.BAMBOO_LENS_COMPANY_STATE = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Company state written to: {COMPANY_STATE_FILE}")
    print(f"Portal company state written to: {PORTAL_COMPANY_STATE_FILE}")


if __name__ == "__main__":
    main()
