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
MAX_DEPOSITS_PER_COMPANY = 3


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


def join_items(items: list[str], limit: int = 3) -> str:
    cleaned = [str(item).strip() for item in items if str(item).strip()]
    return "；".join(cleaned[:limit])


def source_summary_text(event: dict, limit: int = 3) -> str:
    summaries = [str(item).strip() for item in event.get("source_summary", []) if str(item).strip()]
    if summaries:
        return "；".join(summaries[:limit])
    return str(event.get("fact") or "").strip()


def event_can_writeback(item: dict) -> bool:
    return bool(item.get("writeback_ready")) or item.get("status") in {"ready", "needs_model_update"}


def event_deposits(item: dict, event: dict) -> dict:
    event_type = str(event.get("type") or "正式事件").strip()
    date = str(item.get("event_date") or event.get("date") or "").strip()
    title = str(item.get("event_title") or event.get("title") or "").strip()
    fact = str(event.get("fact") or "").strip()
    business = str(event.get("business_analysis") or item.get("reason") or "").strip()
    valuation = str(event.get("valuation_analysis") or item.get("valuation_impact") or "").strip()
    judgment = str(event.get("judgment") or item.get("reason") or "").strip()
    evidence = [str(v).strip() for v in event.get("evidence", []) if str(v).strip()]
    verification = [str(v).strip() for v in event.get("verification", []) if str(v).strip()]
    targets = set(item.get("update_targets", []))
    source_text = source_summary_text(event)

    finance_note_text = "；".join(verification[:3]) or valuation or judgment
    deposit = {
        "financeMap": {"notes": []},
        "businessMap": {"segments": [], "moat": []},
        "valuationModel": {"currentBreakdown": [], "triggers": []},
    }

    if "财务数据地图" in targets:
        deposit["financeMap"]["notes"].append(
            {
                "title": f"财务增量｜{title}",
                "text": compact(
                    f"原文事实：{source_text} 证据：{join_items(evidence, 3)}。读法：{judgment} 后续验证：{finance_note_text}",
                    900,
                ),
            }
        )

    if "公司理解" in targets:
        deposit["businessMap"]["segments"].append(
            {
                "title": f"业务变化｜{title}",
                "scale": f"{date}｜{event_type}",
                "text": compact(f"{business} 原文要点：{source_text}", 900),
            }
        )
        deposit["businessMap"]["moat"].append(
            {
                "title": f"判断变化｜{event_type}",
                "text": judgment,
            }
        )

    if "估值模型" in targets:
        deposit["valuationModel"]["currentBreakdown"].append(
            {
                "title": f"估值/动作影响｜{title}",
                "text": compact(valuation, 900),
            }
        )
        deposit["valuationModel"]["triggers"].append(
            {
                "title": f"下一步验证｜{event_type}",
                "text": "；".join(verification[:3]) or "等待下一轮正式披露验证这条事件能否进入收入、利润率、现金流或估值中枢。",
            }
        )

    return deposit


def merge_deposits(deposits: list[dict]) -> dict:
    merged = {
        "financeMap": {"notes": []},
        "businessMap": {"segments": [], "moat": []},
        "valuationModel": {"currentBreakdown": [], "triggers": []},
    }
    for deposit in deposits:
        merged["financeMap"]["notes"].extend(deposit.get("financeMap", {}).get("notes", []))
        merged["businessMap"]["segments"].extend(deposit.get("businessMap", {}).get("segments", []))
        merged["businessMap"]["moat"].extend(deposit.get("businessMap", {}).get("moat", []))
        merged["valuationModel"]["currentBreakdown"].extend(
            deposit.get("valuationModel", {}).get("currentBreakdown", [])
        )
        merged["valuationModel"]["triggers"].extend(deposit.get("valuationModel", {}).get("triggers", []))
    return merged


def build_override(item: dict, event: dict, all_items: list[tuple[dict, dict]]) -> dict:
    action = str(event.get("action") or "").strip()
    valuation = str(event.get("valuation_analysis") or item.get("valuation_impact") or "").strip()
    deposits = [event_deposits(deposit_item, deposit_event) for deposit_item, deposit_event in all_items]
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
        "depositionNotice": "已根据通过质量门槛的正式事件自动更新当前结论，并按事件性质沉淀到对应的业务、财务或估值板块。",
        "writebackQuality": {
            "status": item.get("status", ""),
            "statusLabel": item.get("status_label", ""),
            "score": item.get("writeback_quality_score", 0),
            "blockers": item.get("writeback_blockers", []),
        },
        "updatedSections": item.get("update_targets", []),
        "sectionDeposits": merge_deposits(deposits),
        "depositEvents": [
            {
                "eventIndex": deposit_item.get("event_index", 0),
                "title": deposit_item.get("event_title", ""),
                "date": deposit_item.get("event_date", ""),
                "priority": deposit_item.get("priority", ""),
                "detailLink": deposit_item.get("detail_link", ""),
            }
            for deposit_item, _ in all_items
        ],
    }


def build_payload(event_store: dict, deposition: dict) -> dict:
    lookup = event_lookup(event_store)
    grouped: dict[str, list[tuple[dict, dict]]] = {}
    for item in deposition.get("items", []):
        company_id = item.get("company", "")
        if not event_can_writeback(item):
            continue
        event = lookup.get((company_id, int(item.get("event_index", 0))))
        if not event:
            continue
        grouped.setdefault(company_id, []).append((item, event))

    companies = {}
    for company_id, items in grouped.items():
        items.sort(key=lambda row: int(row[0].get("sort_key") or 0), reverse=True)
        current_item, current_event = items[0]
        companies[company_id] = build_override(
            current_item,
            current_event,
            items[:MAX_DEPOSITS_PER_COMPANY],
        )

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_event_store_at": event_store.get("generated_at", ""),
        "source_deposition_at": deposition.get("generated_at", ""),
        "companies": companies,
        "summary": {
            "companies": len(companies),
            "events_applied": sum(len(company.get("depositEvents", [])) for company in companies.values()),
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
