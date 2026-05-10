#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
DECISION_IMPACT_FILE = OUTPUT_DIR / "decision_impact.json"
PORTAL_DECISION_IMPACT_FILE = PROJECT_ROOT / "研究门户" / "decision-impact-data.js"

VALUATION_UP_WORDS = ["提升", "强化", "上调", "溢价", "增长", "兑现", "改善", "高质量", "支撑"]
VALUATION_DOWN_WORDS = ["压制", "拖累", "下调", "恶化", "稀释", "放缓", "风险", "压力", "扣减"]
FINANCE_WORDS = ["收入", "营收", "利润", "毛利率", "现金流", "EPS", "capex", "FCF", "回购"]
FINANCE_METRIC_PATTERNS = [
    r"\d+(?:\.\d+)?\s*(?:亿|万亿|billion|million|美元|新台币|元)",
    r"\d+(?:\.\d+)?\s*%",
    r"nt\$\s*\d+",
    r"us\$\s*\d+",
]
BUSINESS_WORDS = ["业务", "客户", "平台", "产品", "订单", "backlog", "合作", "合同", "生态"]
VALUATION_WORDS = ["估值", "市值", "PE", "P/FCF", "倍数", "价值", "价格", "合理"]
RISK_WORDS = ["风险", "警惕", "拖累", "压制", "放缓", "下滑", "不确定"]


SECTION_LABELS = {
    "业务": "公司理解",
    "财务": "财务数据地图",
    "估值": "估值模型",
    "风险": "跟踪重点与风险",
}


def load_event_store() -> dict:
    if not EVENT_STORE_FILE.exists():
        return {"generated_at": "", "companies": {}}
    return json.loads(EVENT_STORE_FILE.read_text(encoding="utf-8"))


def first_sentence(text: str, limit: int = 220) -> str:
    cleaned = " ".join(str(text or "").split())
    if limit <= 0 or len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rstrip()


def parse_sort_key(value: str | int | None) -> int:
    if isinstance(value, int):
        return value
    text = str(value or "")
    matches = re.findall(r"\d{4}[-年]?\d{1,2}(?:[-月]?\d{1,2})?", text)
    if not matches:
        return 0
    keys = []
    for item in matches:
        parts = re.findall(r"\d+", item)
        year = parts[0] if parts else "0"
        month = (parts[1] if len(parts) > 1 else "1").zfill(2)
        day = (parts[2] if len(parts) > 2 else "1").zfill(2)
        keys.append(int(f"{year}{month}{day}"))
    return max(keys) if keys else 0


def count_words(text: str, words: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for word in words if word.lower() in lowered)


def has_financial_metrics(event: dict) -> bool:
    text = " ".join(
        str(event.get(field, ""))
        for field in ["type", "fact"]
    )
    evidence_text = " ".join(str(item) for item in event.get("evidence", []))
    metric_text = f"{text} {evidence_text}".lower()
    has_finance_word = count_words(metric_text, FINANCE_WORDS) > 0
    has_metric = any(re.search(pattern, metric_text, flags=re.I) for pattern in FINANCE_METRIC_PATTERNS)
    no_metric_disclaimer = any(
        phrase in metric_text
        for phrase in ["没有披露投资金额", "没有金额", "没有披露项目合同金额", "没有披露收入规模"]
    )
    return has_finance_word and has_metric and not no_metric_disclaimer


def impact_direction(event: dict) -> str:
    text = " ".join(
        str(event.get(field, ""))
        for field in ["fact", "judgment", "business_analysis", "valuation_analysis", "action"]
    )
    up = count_words(text, VALUATION_UP_WORDS)
    down = count_words(text, VALUATION_DOWN_WORDS)
    if up >= down + 2:
        return "正向强化"
    if down >= up + 2:
        return "负向压制"
    return "中性验证"


def impact_dimensions(event: dict) -> list[str]:
    text = " ".join(str(event.get(field, "")) for field in ["type", "fact", "judgment", "business_analysis"])
    dimensions = []
    if count_words(text, BUSINESS_WORDS):
        dimensions.append("业务")
    if has_financial_metrics(event):
        dimensions.append("财务")
    if count_words(str(event.get("valuation_analysis", "")), VALUATION_WORDS):
        dimensions.append("估值")
    if count_words(text, RISK_WORDS):
        dimensions.append("风险")
    return dimensions or ["业务"]


def trigger_type(event: dict, direction: str) -> str:
    action = str(event.get("action", ""))
    priority = str(event.get("priority", ""))
    if "提升" in action:
        return "上调研究优先级"
    if "二次验证" in action or "等待" in action:
        return "等待验证"
    if direction == "负向压制":
        return "下调或风控观察"
    if priority == "P1" and direction == "正向强化":
        return "维持核心并观察加仓条件"
    return "维持观察"


def valuation_update_needed(event: dict, dimensions: list[str]) -> bool:
    valuation_text = str(event.get("valuation_analysis", ""))
    if "不能直接上调估值" in valuation_text or "不因该新闻加仓" in valuation_text:
        return False
    return "估值" in dimensions and has_financial_metrics(event)


def confidence_change(direction: str, event: dict) -> str:
    action = str(event.get("action", ""))
    if direction == "负向压制":
        return "下调确信度"
    if "提升" in action:
        return "上调确信度"
    if direction == "正向强化":
        return "小幅上调确信度"
    return "维持确信度"


def portfolio_hint(direction: str, event: dict) -> str:
    valuation = str(event.get("valuation_analysis", ""))
    if direction == "负向压制":
        return "暂停加仓，优先排查风险是否破坏原逻辑。"
    if "不应该" in valuation or "不因" in valuation or "不是" in valuation:
        return "研究优先级上调，但资金动作保持克制，等下一次财报或合同数据验证。"
    if "加仓" in valuation or "更积极" in valuation:
        return "可进入更积极分批候选，但仍需价格与估值安全边际配合。"
    return "维持观察，只有验证点继续兑现时才考虑提高动作强度。"


def update_targets(dimensions: list[str], valuation_needed: bool) -> list[str]:
    targets = [SECTION_LABELS[dimension] for dimension in dimensions if dimension in SECTION_LABELS]
    if valuation_needed and "估值模型" not in targets:
        targets.append("估值模型")
    if "当前结论" not in targets:
        targets.insert(0, "当前结论")
    return targets


def decision_output(event: dict, direction: str, dimensions: list[str], valuation_needed: bool) -> dict:
    return {
        "confidence_change": confidence_change(direction, event),
        "portfolio_hint": portfolio_hint(direction, event),
        "update_targets": update_targets(dimensions, valuation_needed),
        "next_work": (
            "更新公司页相关板块，并把验证点放入下一轮财报/公告跟踪。"
            if valuation_needed
            else "先沉淀到事件流，等待更多证据再调整估值模型。"
        ),
    }


def build_company_impacts(company_id: str, company: dict) -> list[dict]:
    impacts = []
    for index, event in enumerate(company.get("events", [])):
        if event.get("review_status") != "reviewed":
            continue
        direction = impact_direction(event)
        dimensions = impact_dimensions(event)
        valuation_needed = valuation_update_needed(event, dimensions)
        verification = [str(item).strip() for item in event.get("verification", []) if str(item).strip()]
        impacts.append(
            {
                "company": company_id,
                "company_name": company.get("name", company_id),
                "event_index": index,
                "event_title": event.get("title", ""),
                "event_date": event.get("date", ""),
                "event_type": event.get("type", ""),
                "priority": event.get("priority", ""),
                "direction": direction,
                "dimensions": dimensions,
                "trigger_type": trigger_type(event, direction),
                "valuation_update_needed": valuation_needed,
                "decision_output": decision_output(event, direction, dimensions, valuation_needed),
                "decision_change": first_sentence(event.get("judgment", ""), 180),
                "business_impact": first_sentence(event.get("business_analysis", ""), 220),
                "valuation_impact": first_sentence(event.get("valuation_analysis", ""), 240),
                "next_verification": verification[:3],
                "source_url": event.get("source_url", ""),
                "sort_key": parse_sort_key(event.get("sort_key") or event.get("date")),
                "detail_link": f"./event.html?company={company_id}&event={index}&return=company&v=20260505-1",
            }
        )
    return sorted(impacts, key=lambda item: item["sort_key"], reverse=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    event_store = load_event_store()
    companies = {}
    items = []
    for company_id, company in event_store.get("companies", {}).items():
        company_impacts = build_company_impacts(company_id, company)
        if not company_impacts:
            continue
        companies[company_id] = company_impacts
        items.extend(company_impacts)

    items = sorted(items, key=lambda item: item["sort_key"], reverse=True)
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_generated_at": event_store.get("generated_at", ""),
        "items": items,
        "companies": companies,
        "summary": {
            "total": len(items),
            "companies": len(companies),
            "valuation_update_needed": sum(1 for item in items if item["valuation_update_needed"]),
            "positive": sum(1 for item in items if item["direction"] == "正向强化"),
            "watch": sum(1 for item in items if item["trigger_type"] == "等待验证"),
        },
    }

    DECISION_IMPACT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_DECISION_IMPACT_FILE.write_text(
        "window.BAMBOO_LENS_DECISION_IMPACT = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Decision impact written to: {DECISION_IMPACT_FILE}")
    print(f"Portal decision impact data written to: {PORTAL_DECISION_IMPACT_FILE}")


if __name__ == "__main__":
    main()
