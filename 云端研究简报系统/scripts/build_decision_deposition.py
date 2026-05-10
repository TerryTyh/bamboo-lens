#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
DECISION_IMPACT_FILE = OUTPUT_DIR / "decision_impact.json"
DECISION_DEPOSITION_FILE = OUTPUT_DIR / "decision_deposition.json"
PORTAL_DECISION_DEPOSITION_FILE = PROJECT_ROOT / "研究门户" / "decision-deposition-data.js"


TARGET_TO_FIELD = {
    "当前结论": ["latestEvent", "businessImpact", "valuationImpact", "nextCheck"],
    "公司理解": ["businessMap", "positioning", "moatDetail"],
    "财务数据地图": ["financeMap", "financials"],
    "估值模型": ["valuationModel", "valuationFrame"],
    "跟踪重点与风险": ["focus", "trackingGuide", "risk"],
}


def load_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def compact(text: str, limit: int = 220) -> str:
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


def quality_label(event: dict) -> str:
    source_summary_count = len([item for item in event.get("source_summary", []) if str(item).strip()])
    evidence_count = len([item for item in event.get("evidence", []) if str(item).strip()])
    verification_count = len([item for item in event.get("verification", []) if str(item).strip()])
    if source_summary_count >= 2 and evidence_count >= 3 and verification_count >= 2:
        return "可自动生成回写建议"
    if source_summary_count >= 1 and evidence_count >= 1:
        return "可沉淀，但需人工补强"
    return "只入事件流，不回写主页"


def deposition_status(event: dict, targets: list[str]) -> str:
    if quality_label(event) == "只入事件流，不回写主页":
        return "blocked"
    if "估值模型" in targets or "财务数据地图" in targets:
        return "needs_model_update"
    return "ready"


def build_recommended_updates(event: dict, targets: list[str]) -> list[dict]:
    updates = []
    for target in targets:
        fields = TARGET_TO_FIELD.get(target, [])
        if target == "当前结论":
            updates.append(
                {
                    "target": target,
                    "fields": fields,
                    "suggestion": compact(
                        f"把最新事件更新为「{event.get('title', '')}」；业务影响写入：{event.get('business_analysis') or event.get('judgment', '')}；估值/动作写入：{event.get('valuation_analysis') or event.get('action', '')}",
                        320,
                    ),
                }
            )
        elif target == "公司理解":
            updates.append(
                {
                    "target": target,
                    "fields": fields,
                    "suggestion": compact(event.get("business_analysis") or event.get("judgment", ""), 320),
                }
            )
        elif target == "财务数据地图":
            updates.append(
                {
                    "target": target,
                    "fields": fields,
                    "suggestion": compact(
                        "如果事件包含收入、利润率、现金流、capex、订单或 backlog 数字，应把关键数字进入财务表格，并解释它改变了哪条财务判断。",
                        320,
                    ),
                }
            )
        elif target == "估值模型":
            updates.append(
                {
                    "target": target,
                    "fields": fields,
                    "suggestion": compact(event.get("valuation_analysis") or event.get("judgment", ""), 360),
                }
            )
        elif target == "跟踪重点与风险":
            verification = "；".join(str(item).strip() for item in event.get("verification", [])[:3])
            updates.append(
                {
                    "target": target,
                    "fields": fields,
                    "suggestion": compact(verification or event.get("judgment", ""), 320),
                }
            )
    return updates


def build_deposition_item(impact: dict, event: dict) -> dict:
    targets = impact.get("decision_output", {}).get("update_targets", []) or ["当前结论"]
    return {
        "company": impact.get("company", ""),
        "company_name": impact.get("company_name", ""),
        "event_index": impact.get("event_index", 0),
        "event_title": impact.get("event_title", ""),
        "event_date": impact.get("event_date", ""),
        "priority": impact.get("priority", ""),
        "direction": impact.get("direction", ""),
        "trigger_type": impact.get("trigger_type", ""),
        "status": deposition_status(event, targets),
        "quality": quality_label(event),
        "update_targets": targets,
        "recommended_updates": build_recommended_updates(event, targets),
        "reason": compact(impact.get("decision_change", ""), 220),
        "valuation_impact": compact(impact.get("valuation_impact", ""), 260),
        "next_verification": impact.get("next_verification", [])[:3],
        "detail_link": impact.get("detail_link", ""),
        "sort_key": impact.get("sort_key", 0),
    }


def build_payload(event_store: dict, decision_impact: dict) -> dict:
    lookup = event_lookup(event_store)
    items = []
    for impact in decision_impact.get("items", []):
        event = lookup.get((impact.get("company", ""), int(impact.get("event_index", 0))))
        if not event:
            continue
        items.append(build_deposition_item(impact, event))

    items.sort(key=lambda item: int(item.get("sort_key") or 0), reverse=True)
    ready = [item for item in items if item["status"] == "ready"]
    needs_model = [item for item in items if item["status"] == "needs_model_update"]
    blocked = [item for item in items if item["status"] == "blocked"]
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_event_store_at": event_store.get("generated_at", ""),
        "source_decision_impact_at": decision_impact.get("generated_at", ""),
        "items": items,
        "summary": {
            "total": len(items),
            "ready": len(ready),
            "needs_model_update": len(needs_model),
            "blocked": len(blocked),
            "companies": len({item["company"] for item in items}),
        },
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    event_store = load_json(EVENT_STORE_FILE, {"generated_at": "", "companies": {}})
    decision_impact = load_json(DECISION_IMPACT_FILE, {"generated_at": "", "items": []})
    payload = build_payload(event_store, decision_impact)
    DECISION_DEPOSITION_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_DECISION_DEPOSITION_FILE.write_text(
        "window.BAMBOO_LENS_DECISION_DEPOSITION = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Decision deposition written to: {DECISION_DEPOSITION_FILE}")
    print(f"Portal decision deposition data written to: {PORTAL_DECISION_DEPOSITION_FILE}")


if __name__ == "__main__":
    main()
