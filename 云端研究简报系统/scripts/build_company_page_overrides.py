#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
DEPOSITION_FILE = OUTPUT_DIR / "decision_deposition.json"
OVERRIDES_FILE = OUTPUT_DIR / "company_page_overrides.json"
PORTAL_OVERRIDES_FILE = PROJECT_ROOT / "研究门户" / "company-page-overrides-data.js"


def load_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def compact(text: str, limit: int = 1200) -> str:
    cleaned = " ".join(str(text or "").split())
    if limit <= 0 or len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rstrip()


def event_lookup(event_store: dict) -> dict[tuple[str, int], dict]:
    lookup = {}
    for company_id, company in event_store.get("companies", {}).items():
        for index, event in enumerate(company.get("events", [])):
            lookup[(company_id, index)] = event
    return lookup


def verification_text(event: dict) -> str:
    verification = [str(item).strip() for item in event.get("verification", []) if str(item).strip()]
    if verification:
        return "；".join(verification[:2])
    return compact(event.get("judgment", ""), 220)


def build_override(item: dict, event: dict) -> dict:
    action = str(event.get("action") or "").strip()
    valuation = str(event.get("valuation_analysis") or item.get("valuation_impact") or "").strip()
    return {
        "source": "decision_deposition",
        "sourceEventIndex": item.get("event_index", 0),
        "sourceEventTitle": item.get("event_title", ""),
        "sourceEventDate": item.get("event_date", ""),
        "sourceEventLink": item.get("detail_link", ""),
        "updatedAt": datetime.now().isoformat(timespec="seconds"),
        "latestEvent": f"{item.get('event_date', '')}｜{item.get('event_title', '')}",
        "businessImpact": compact(event.get("business_analysis") or item.get("reason", ""), 560),
        "valuationImpact": compact(valuation, 680),
        "nextCheck": verification_text(event),
        "action": action or None,
        "depositionNotice": "已根据最新正式事件自动更新当前结论；完整公司档案仍可继续人工精修。",
        "updatedSections": item.get("update_targets", []),
    }


def build_payload(event_store: dict, deposition: dict) -> dict:
    lookup = event_lookup(event_store)
    companies = {}
    for item in deposition.get("items", []):
        company_id = item.get("company", "")
        if company_id in companies:
            continue
        if item.get("status") == "blocked":
            continue
        event = lookup.get((company_id, int(item.get("event_index", 0))))
        if not event:
            continue
        companies[company_id] = build_override(item, event)

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_event_store_at": event_store.get("generated_at", ""),
        "source_deposition_at": deposition.get("generated_at", ""),
        "companies": companies,
        "summary": {
            "companies": len(companies),
            "events_applied": len(companies),
        },
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    event_store = load_json(EVENT_STORE_FILE, {"generated_at": "", "companies": {}})
    deposition = load_json(DEPOSITION_FILE, {"generated_at": "", "items": []})
    payload = build_payload(event_store, deposition)
    OVERRIDES_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_OVERRIDES_FILE.write_text(
        "window.BAMBOO_LENS_COMPANY_PAGE_OVERRIDES = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Company page overrides written to: {OVERRIDES_FILE}")
    print(f"Portal company page overrides written to: {PORTAL_OVERRIDES_FILE}")


if __name__ == "__main__":
    main()
