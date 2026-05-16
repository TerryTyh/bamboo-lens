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


FINANCE_KEYWORDS = [
    "收入",
    "营收",
    "利润",
    "毛利",
    "利润率",
    "现金流",
    "自由现金流",
    "capex",
    "资本开支",
    "订单",
    "backlog",
    "EPS",
    "指引",
    "财报",
    "月度营收",
    "应收",
    "存货",
]

BUSINESS_KEYWORDS = [
    "产品",
    "平台",
    "客户",
    "合作",
    "生态",
    "技术",
    "发布",
    "供应链",
    "AI",
    "agent",
    "网络",
    "Rubin",
    "Spectrum",
    "NVLink",
    "CoWoS",
]

VALUATION_KEYWORDS = [
    "估值",
    "回购",
    "分红",
    "并购",
    "收购",
    "资本配置",
    "PPA",
    "合同",
    "价格",
    "股价",
    "中枢",
    "安全边际",
]

HARD_WRITEBACK_KEYWORDS = [
    "财报",
    "收入",
    "营收",
    "EPS",
    "毛利",
    "现金流",
    "订单",
    "backlog",
    "capex",
    "资本开支",
    "指引",
    "月度营收",
    "董事会",
    "并购",
    "收购",
    "回购",
    "PPA",
    "长期合同",
]


def load_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def compact(text: str, limit: int = 220) -> str:
    cleaned = " ".join(str(text or "").split())
    if limit <= 0 or len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rstrip()


def filled_items(value) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def text_blob(event: dict, impact: dict = None) -> str:
    impact = impact or {}
    parts = [
        event.get("title", ""),
        event.get("type", ""),
        event.get("fact", ""),
        event.get("judgment", ""),
        event.get("business_analysis", ""),
        event.get("valuation_analysis", ""),
        impact.get("business_impact", ""),
        impact.get("valuation_impact", ""),
    ]
    parts.extend(filled_items(event.get("source_summary")))
    parts.extend(filled_items(event.get("evidence")))
    parts.extend(filled_items(event.get("verification")))
    return " ".join(str(part) for part in parts if str(part).strip())


def has_number(text: str) -> bool:
    return any(ch.isdigit() for ch in text)


def hard_writeback_blob(event: dict) -> str:
    parts = [
        event.get("title", ""),
        event.get("type", ""),
        event.get("fact", ""),
    ]
    parts.extend(filled_items(event.get("source_summary")))
    parts.extend(filled_items(event.get("evidence")))
    return " ".join(str(part) for part in parts if str(part).strip())


def is_hard_writeback_event(event: dict) -> bool:
    blob = hard_writeback_blob(event)
    return has_number(blob) and any(keyword in blob for keyword in HARD_WRITEBACK_KEYWORDS)


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


def quality_score(event: dict) -> int:
    source_summary = filled_items(event.get("source_summary"))
    evidence = filled_items(event.get("evidence"))
    verification = filled_items(event.get("verification"))
    blob = text_blob(event)
    score = 0
    if event.get("source_url") or event.get("source_doc"):
        score += 2
    if len(source_summary) >= 2:
        score += 2
    elif len(source_summary) == 1:
        score += 1
    if len(evidence) >= 3:
        score += 2
    elif len(evidence) >= 1:
        score += 1
    if has_number(blob):
        score += 1
    if len(str(event.get("business_analysis") or "").strip()) >= 80:
        score += 1
    if len(str(event.get("valuation_analysis") or "").strip()) >= 80:
        score += 1
    if len(verification) >= 2:
        score += 1
    return score


def writeback_blockers(event: dict) -> list[str]:
    blockers = []
    if not (event.get("source_url") or event.get("source_doc")):
        blockers.append("缺少可追溯原文链接或本地来源文档")
    if len(filled_items(event.get("source_summary"))) < 1:
        blockers.append("缺少原文摘要")
    if len(filled_items(event.get("evidence"))) < 2:
        blockers.append("证据点不足，至少需要 2 条具体证据")
    if len(str(event.get("business_analysis") or "").strip()) < 60:
        blockers.append("业务影响分析过短")
    if len(str(event.get("valuation_analysis") or "").strip()) < 60:
        blockers.append("估值/动作影响分析过短")
    if len(filled_items(event.get("verification"))) < 1:
        blockers.append("缺少下一步验证点")
    return blockers


def target_sections(impact: dict, event: dict, targets: list[str]) -> list[str]:
    blob = text_blob(event, impact)
    dimensions = set(impact.get("dimensions", []))
    sections: list[str] = []

    def add(section: str) -> None:
        if section not in sections:
            sections.append(section)

    if "当前结论" in targets:
        add("当前结论")
    if "业务" in dimensions or "公司理解" in targets or any(keyword in blob for keyword in BUSINESS_KEYWORDS):
        add("公司理解")
    if "财务" in dimensions or "财务数据地图" in targets or any(keyword in blob for keyword in FINANCE_KEYWORDS):
        add("财务数据地图")
    if (
        "估值" in dimensions
        or "估值模型" in targets
        or impact.get("valuation_update_needed")
        or any(keyword in blob for keyword in VALUATION_KEYWORDS)
    ):
        add("估值模型")
    if "跟踪重点与风险" in targets or filled_items(event.get("verification")):
        add("跟踪重点与风险")
    return sections or ["当前结论"]


def writeback_ready(event: dict, impact: dict, targets: list[str]) -> bool:
    priority = str(event.get("priority") or impact.get("priority") or "").upper()
    if writeback_blockers(event):
        return False
    if quality_score(event) < 7:
        return False
    if priority in {"P1", "P2"}:
        return True
    # P3 叙事类事件保留在事件流；只有财务/估值证据很硬时才允许写入主页。
    return is_hard_writeback_event(event) and quality_score(event) >= 9


def deposition_status(event: dict, impact: dict, targets: list[str]) -> str:
    if not writeback_ready(event, impact, targets):
        if quality_label(event) == "只入事件流，不回写主页" or writeback_blockers(event):
            return "blocked"
        return "watch_only"
    if "估值模型" in targets or "财务数据地图" in targets:
        return "needs_model_update"
    return "ready"


def writeback_plan(event: dict, impact: dict, sections: list[str]) -> list[dict]:
    plan = []
    title = event.get("title", "")
    if "当前结论" in sections:
        plan.append(
            {
                "section": "当前结论",
                "plan": compact(
                    f"用「{title}」更新最新事件；当前结论只写这条事件对主线判断的增量，不覆盖长期判断底稿。",
                    260,
                ),
            }
        )
    if "公司理解" in sections:
        plan.append(
            {
                "section": "公司理解",
                "plan": compact(event.get("business_analysis") or impact.get("business_impact", ""), 360),
            }
        )
    if "财务数据地图" in sections:
        plan.append(
            {
                "section": "财务数据地图",
                "plan": compact("提取收入、利润率、现金流、订单、backlog、capex、应收或存货等可核验数字，写成财务地图的增量注释。", 260),
            }
        )
    if "估值模型" in sections:
        plan.append(
            {
                "section": "估值模型",
                "plan": compact(event.get("valuation_analysis") or impact.get("valuation_impact", ""), 360),
            }
        )
    if "跟踪重点与风险" in sections:
        verification = "；".join(filled_items(event.get("verification"))[:3])
        plan.append({"section": "跟踪重点与风险", "plan": compact(verification, 320)})
    return plan


def display_status(status: str) -> str:
    labels = {
        "ready": "可自动回写",
        "needs_model_update": "可回写，需同步估值/财务",
        "watch_only": "仅进入事件流",
        "blocked": "不回写主页",
    }
    return labels.get(status, status)


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
    sections = target_sections(impact, event, targets)
    status = deposition_status(event, impact, targets)
    blockers = writeback_blockers(event)
    score = quality_score(event)
    return {
        "company": impact.get("company", ""),
        "company_name": impact.get("company_name", ""),
        "event_index": impact.get("event_index", 0),
        "event_title": impact.get("event_title", ""),
        "event_date": impact.get("event_date", ""),
        "priority": impact.get("priority", ""),
        "direction": impact.get("direction", ""),
        "trigger_type": impact.get("trigger_type", ""),
        "status": status,
        "status_label": display_status(status),
        "writeback_ready": status in {"ready", "needs_model_update"},
        "writeback_quality_score": score,
        "writeback_blockers": blockers,
        "quality": quality_label(event),
        "update_targets": sections,
        "raw_update_targets": targets,
        "recommended_updates": build_recommended_updates(event, sections),
        "writeback_plan": writeback_plan(event, impact, sections),
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
    ready = [item for item in items if item["writeback_ready"]]
    needs_model = [item for item in items if item["status"] == "needs_model_update"]
    watch_only = [item for item in items if item["status"] == "watch_only"]
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
            "watch_only": len(watch_only),
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
