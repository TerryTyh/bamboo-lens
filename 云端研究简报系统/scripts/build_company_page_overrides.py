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


FINANCE_TERMS = [
    "收入",
    "营收",
    "利润",
    "毛利",
    "利润率",
    "现金流",
    "EPS",
    "capex",
    "资本开支",
    "订单",
    "backlog",
    "应收",
    "存货",
    "指引",
    "月度营收",
]

BUSINESS_TERMS = [
    "客户",
    "合作",
    "产品",
    "平台",
    "技术",
    "生态",
    "AI",
    "agent",
    "网络",
    "供应链",
    "产能",
]

VALUATION_TERMS = [
    "估值",
    "回购",
    "分红",
    "收购",
    "并购",
    "资本配置",
    "PPA",
    "长期合同",
    "股价",
    "中枢",
]


def load_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def compact(text: str, limit: int = 1200) -> str:
    cleaned = " ".join(str(text or "").split())
    if limit <= 0 or len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rstrip()


def stable_key(*parts: str) -> str:
    raw = ":".join(str(part or "").strip().lower() for part in parts if str(part or "").strip())
    return (
        raw.replace(" ", "-")
        .replace("/", "-")
        .replace("｜", "-")
        .replace("：", "-")
        .replace(":", "-")
    )


def item_key(item: dict) -> str:
    if item.get("key"):
        return str(item["key"])
    return stable_key(
        item.get("title", ""),
        item.get("metric", ""),
        item.get("label", ""),
        item.get("scale", ""),
    )


def merge_keyed_items(items: list[dict]) -> list[dict]:
    merged = []
    seen = set()
    for item in items:
        key = item_key(item)
        if key and key in seen:
            continue
        if key:
            seen.add(key)
        merged.append(item)
    return merged


def contains_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def event_blob(event: dict) -> str:
    parts = [
        event.get("title", ""),
        event.get("type", ""),
        event.get("fact", ""),
        event.get("judgment", ""),
        event.get("business_analysis", ""),
        event.get("valuation_analysis", ""),
    ]
    for field in ["source_summary", "evidence", "verification"]:
        value = event.get(field)
        if isinstance(value, list):
            parts.extend(str(item) for item in value if str(item).strip())
    return " ".join(str(part) for part in parts if str(part).strip())


def event_theme(event: dict) -> str:
    blob = event_blob(event)
    event_type = str(event.get("type") or "").strip()
    if contains_any(blob, ["财报", "EPS", "收入", "营收", "毛利", "现金流", "月度营收", "指引"]):
        return "财报/经营验证"
    if contains_any(blob, ["收购", "并购", "回购", "分红", "资本配置", "PPA", "长期合同"]):
        return "资本配置/合同验证"
    if contains_any(blob, ["客户", "合作", "订单", "backlog"]):
        return "客户/订单验证"
    if contains_any(blob, ["产品", "平台", "技术", "AI", "agent", "网络", "生态"]):
        return "产品/平台验证"
    return event_type or "正式事件"


def evidence_blob(event: dict) -> str:
    parts = [
        event.get("title", ""),
        event.get("type", ""),
        event.get("fact", ""),
    ]
    for field in ["source_summary", "evidence"]:
        value = event.get(field)
        if isinstance(value, list):
            parts.extend(str(item) for item in value if str(item).strip())
    return " ".join(str(part) for part in parts if str(part).strip())


def has_finance_signal(event: dict) -> bool:
    return contains_any(evidence_blob(event), FINANCE_TERMS)


def has_business_signal(event: dict) -> bool:
    return contains_any(evidence_blob(event), BUSINESS_TERMS)


def has_valuation_signal(event: dict) -> bool:
    return contains_any(evidence_blob(event), VALUATION_TERMS + FINANCE_TERMS)


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


def selected_evidence(event: dict, terms: list[str], limit: int = 3) -> list[str]:
    evidence = [str(v).strip() for v in event.get("evidence", []) if str(v).strip()]
    matched = [item for item in evidence if contains_any(item, terms)]
    return (matched or evidence)[:limit]


def event_can_writeback(item: dict) -> bool:
    return bool(item.get("writeback_ready")) or item.get("status") in {"ready", "needs_model_update"}


def finance_rows(event: dict, date: str, event_type: str, theme: str) -> list[dict]:
    rows = []
    for index, evidence in enumerate(selected_evidence(event, FINANCE_TERMS, 3), start=1):
        rows.append(
            {
                "key": stable_key("finance-row", theme, index),
                "metric": f"事件证据 {index}",
                "value": compact(evidence, 180),
                "change": f"{date}｜{event_type}",
                "read": compact(event.get("judgment", ""), 260),
            }
        )
    return rows


def finance_bridge(event: dict, theme: str) -> list[dict]:
    summary = [str(v).strip() for v in event.get("source_summary", []) if str(v).strip()]
    judgment = str(event.get("judgment") or "").strip()
    steps = []
    if summary:
        steps.append({"key": stable_key("finance-bridge", theme, "source"), "label": f"第一层：原文发生了什么｜{theme}", "text": compact(summary[0], 300)})
    if len(summary) > 1:
        steps.append({"key": stable_key("finance-bridge", theme, "evidence"), "label": "第二层：哪些事实最关键", "text": compact(summary[1], 300)})
    if judgment:
        steps.append({"key": stable_key("finance-bridge", theme, "judgment"), "label": "第三层：它改变了什么判断", "text": compact(judgment, 320)})
    return steps[:3]


def valuation_scenario(event: dict, verification: list[str]) -> list[dict]:
    valuation = str(event.get("valuation_analysis") or "").strip()
    if not valuation:
        return []
    return [
        {
            "key": stable_key("valuation-scenario", "upside"),
            "title": "估值中枢上修条件",
            "text": compact(verification[0] if verification else "后续正式披露继续验证收入、利润率、现金流或合同质量。", 260),
        },
        {
            "key": stable_key("valuation-scenario", "watch"),
            "title": "维持观察条件",
            "text": compact(valuation, 320),
        },
    ]


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
    theme = event_theme(event)

    finance_note_text = "；".join(verification[:3]) or valuation or judgment
    deposit = {
        "financeMap": {"rows": [], "bridge": [], "notes": []},
        "businessMap": {"segments": [], "moat": []},
        "valuationModel": {"currentBreakdown": [], "scenarios": [], "triggers": []},
    }

    if "财务数据地图" in targets and has_finance_signal(event):
        deposit["financeMap"]["rows"].extend(finance_rows(event, date, event_type, theme))
        deposit["financeMap"]["bridge"].extend(finance_bridge(event, theme))
        deposit["financeMap"]["notes"].append(
            {
                "key": stable_key("finance-note", theme),
                "title": f"{theme}｜财务读法",
                "text": compact(
                    f"原文事实：{source_text} 证据：{join_items(selected_evidence(event, FINANCE_TERMS, 3), 3)}。读法：{judgment} 后续验证：{finance_note_text}",
                    900,
                ),
            }
        )

    if "公司理解" in targets and has_business_signal(event):
        deposit["businessMap"]["segments"].append(
            {
                "key": stable_key("business-segment", theme),
                "title": f"{theme}｜{title}",
                "scale": f"{date}｜{event_type}",
                "text": compact(f"{business} 原文要点：{source_text}", 900),
            }
        )
        deposit["businessMap"]["moat"].append(
            {
                "key": stable_key("business-moat", theme),
                "title": f"护城河/业务主线是否变化｜{theme}",
                "text": compact(judgment, 520),
            }
        )

    if "估值模型" in targets and has_valuation_signal(event):
        deposit["valuationModel"]["currentBreakdown"].append(
            {
                "key": stable_key("valuation-current", theme),
                "title": f"{theme}｜估值/动作影响",
                "text": compact(valuation, 900),
            }
        )
        deposit["valuationModel"]["scenarios"].extend(valuation_scenario(event, verification))
        deposit["valuationModel"]["triggers"].append(
            {
                "key": stable_key("valuation-trigger", theme),
                "title": f"下一步验证｜{theme}",
                "text": "；".join(verification[:3]) or "等待下一轮正式披露验证这条事件能否进入收入、利润率、现金流或估值中枢。",
            }
        )

    return deposit


def merge_deposits(deposits: list[dict]) -> dict:
    merged = {
        "financeMap": {"rows": [], "bridge": [], "notes": []},
        "businessMap": {"segments": [], "moat": []},
        "valuationModel": {"currentBreakdown": [], "scenarios": [], "triggers": []},
    }
    for deposit in deposits:
        merged["financeMap"]["rows"].extend(deposit.get("financeMap", {}).get("rows", []))
        merged["financeMap"]["bridge"].extend(deposit.get("financeMap", {}).get("bridge", []))
        merged["financeMap"]["notes"].extend(deposit.get("financeMap", {}).get("notes", []))
        merged["businessMap"]["segments"].extend(deposit.get("businessMap", {}).get("segments", []))
        merged["businessMap"]["moat"].extend(deposit.get("businessMap", {}).get("moat", []))
        merged["valuationModel"]["currentBreakdown"].extend(
            deposit.get("valuationModel", {}).get("currentBreakdown", [])
        )
        merged["valuationModel"]["scenarios"].extend(deposit.get("valuationModel", {}).get("scenarios", []))
        merged["valuationModel"]["triggers"].extend(deposit.get("valuationModel", {}).get("triggers", []))
    merged["financeMap"]["rows"] = merge_keyed_items(merged["financeMap"]["rows"])
    merged["financeMap"]["bridge"] = merge_keyed_items(merged["financeMap"]["bridge"])
    merged["financeMap"]["notes"] = merge_keyed_items(merged["financeMap"]["notes"])
    merged["businessMap"]["segments"] = merge_keyed_items(merged["businessMap"]["segments"])
    merged["businessMap"]["moat"] = merge_keyed_items(merged["businessMap"]["moat"])
    merged["valuationModel"]["currentBreakdown"] = merge_keyed_items(merged["valuationModel"]["currentBreakdown"])
    merged["valuationModel"]["scenarios"] = merge_keyed_items(merged["valuationModel"]["scenarios"])
    merged["valuationModel"]["triggers"] = merge_keyed_items(merged["valuationModel"]["triggers"])
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
