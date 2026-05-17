#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
OVERRIDES_FILE = OUTPUT_DIR / "company_page_overrides.json"
AUDIT_FILE = OUTPUT_DIR / "company_page_mainline_audit.json"
AUDIT_MD_FILE = OUTPUT_DIR / "company_page_mainline_audit.md"
PORTAL_AUDIT_FILE = PROJECT_ROOT / "研究门户" / "company-mainline-audit-data.js"

CORE_SECTIONS = ["当前结论", "公司理解", "财务数据地图", "估值模型", "跟踪重点与风险"]
SECTION_TO_DEPOSIT = {
    "公司理解": ("businessMap", ["segments", "moat"]),
    "财务数据地图": ("financeMap", ["rows", "bridge", "notes"]),
    "估值模型": ("valuationModel", ["currentBreakdown", "scenarios", "triggers"]),
}
GENERIC_TRIGGER_PHRASES = [
    "等待下一轮正式披露",
    "后续正式披露继续验证",
    "维持观察",
    "需要后续验证",
]
MIN_BUSINESS_IMPACT = 80
MIN_VALUATION_IMPACT = 80
MIN_NEXT_CHECK = 40


def load_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def text_values(value) -> list[str]:
    values = []
    if isinstance(value, str):
        values.append(value)
    elif isinstance(value, list):
        for item in value:
            values.extend(text_values(item))
    elif isinstance(value, dict):
        for item in value.values():
            values.extend(text_values(item))
    return values


def section_count(deposits: dict, section: str, fields: list[str]) -> int:
    section_data = deposits.get(section, {})
    return sum(len(section_data.get(field, []) or []) for field in fields)


def section_presence(deposits: dict) -> dict[str, int]:
    return {
        section_name: section_count(deposits, deposit_section, fields)
        for section_name, (deposit_section, fields) in SECTION_TO_DEPOSIT.items()
    }


def has_any(text: str, phrases: list[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def audit_company(company_id: str, company: dict) -> dict:
    deposits = company.get("sectionDeposits", {})
    updated_sections = company.get("updatedSections", []) or []
    deposit_events = company.get("depositEvents", []) or []
    business_impact = str(company.get("businessImpact") or "").strip()
    valuation_impact = str(company.get("valuationImpact") or "").strip()
    next_check = str(company.get("nextCheck") or "").strip()
    source_link = str(company.get("sourceEventLink") or "").strip()
    writeback_quality = company.get("writebackQuality", {}) or {}
    presence = section_presence(deposits)

    warnings: list[str] = []
    suggestions: list[str] = []
    strengths: list[str] = []

    if not deposit_events:
        warnings.append("没有沉淀事件来源")
        suggestions.append("公司页回写必须保留来源事件，避免页面结论脱离事实链。")
    else:
        strengths.append(f"已关联 {len(deposit_events)} 条正式事件。")
    if not source_link:
        warnings.append("最新回写缺少事件详情入口")
        suggestions.append("保留事件详情入口，便于从公司页追溯到原文、事实和判断。")

    missing_core = [section for section in CORE_SECTIONS if section in updated_sections and section not in ["当前结论", "跟踪重点与风险"] and presence.get(section, 0) == 0]
    if missing_core:
        warnings.append(f"声明更新但缺少实际沉淀：{'、'.join(missing_core)}")
        suggestions.append("update_targets 不能只停留在声明；对应板块必须有可读内容。")

    if len(business_impact) < MIN_BUSINESS_IMPACT:
        warnings.append("业务影响过薄")
        suggestions.append("补足它影响哪条业务线、客户/产品/成本结构或护城河。")
    else:
        strengths.append("业务影响有独立判断。")
    if len(valuation_impact) < MIN_VALUATION_IMPACT:
        warnings.append("估值/动作影响过薄")
        suggestions.append("补足它如何影响估值中枢、仓位动作或等待验证。")
    else:
        strengths.append("估值/动作影响有独立判断。")
    if len(next_check) < MIN_NEXT_CHECK or has_any(next_check, GENERIC_TRIGGER_PHRASES):
        warnings.append("下一步验证点不够具体")
        suggestions.append("验证点应落到下一份财报、具体指标、合同、客户、利润率或现金流。")
    else:
        strengths.append("下一步验证点较具体。")

    if presence["财务数据地图"] > 0 and presence["估值模型"] == 0:
        warnings.append("有财务沉淀但没有估值动作承接")
        suggestions.append("财务数字进入公司页后，需要说明它是否影响估值中枢或动作。")
    if presence["公司理解"] > 0 and "跟踪重点与风险" not in updated_sections:
        warnings.append("有业务主线但未声明更新跟踪重点")
        suggestions.append("业务主线变化应转成后续跟踪重点，而不是停在描述。")

    all_text = " ".join(text_values(deposits))
    generic_hits = sorted({phrase for phrase in GENERIC_TRIGGER_PHRASES if phrase in all_text})
    if generic_hits:
        warnings.append(f"主线文本仍有泛化表达：{'、'.join(generic_hits)}")
        suggestions.append("泛化表达可以保留在结论后半句，但前面必须有具体事实与触发条件。")

    score = 100
    score -= len(warnings) * 12
    score -= max(0, 10 - int(writeback_quality.get("score") or 0)) * 4
    score = max(0, min(100, score))

    status = "healthy"
    if score < 82 or warnings:
        status = "review"
    if score < 65 or len(warnings) >= 4:
        status = "weak"

    return {
        "company": company_id,
        "sourceEventTitle": company.get("sourceEventTitle", ""),
        "sourceEventDate": company.get("sourceEventDate", ""),
        "status": status,
        "score": score,
        "updatedSections": updated_sections,
        "sectionPresence": presence,
        "depositEvents": len(deposit_events),
        "writebackQuality": writeback_quality,
        "warnings": warnings,
        "suggestions": suggestions,
        "strengths": strengths,
    }


def status_label(status: str) -> str:
    return {
        "healthy": "主线清晰",
        "review": "需复核",
        "weak": "主线偏弱",
    }.get(status, status)


def build_markdown(payload: dict) -> str:
    summary = payload["summary"]
    lines = [
        "# 公司页主线复核",
        "",
        f"生成时间：{payload.get('generated_at', '')}",
        "",
        "这份报告检查自动沉淀是否真正服务公司主页主线：业务理解、财务地图、估值模型和后续验证是否互相承接。",
        "",
        "## 总览",
        "",
        f"- 覆盖公司：{summary['companies']} 家",
        f"- 主线清晰：{summary['healthy']} 家",
        f"- 需复核：{summary['review']} 家",
        f"- 主线偏弱：{summary['weak']} 家",
        "",
        "## 公司明细",
        "",
    ]
    for item in payload.get("items", []):
        lines.extend(
            [
                f"### {item['company']}｜{status_label(item['status'])}｜{item['score']} 分",
                "",
                f"- 最新回写事件：{item.get('sourceEventDate', '')}｜{item.get('sourceEventTitle', '')}",
                f"- 关联正式事件：{item['depositEvents']} 条",
                f"- 实际沉淀：公司理解 {item['sectionPresence']['公司理解']}、财务地图 {item['sectionPresence']['财务数据地图']}、估值模型 {item['sectionPresence']['估值模型']}",
            ]
        )
        if item.get("strengths"):
            lines.append(f"- 已满足：{'；'.join(item['strengths'])}")
        if item.get("warnings"):
            lines.append(f"- 警示：{'；'.join(item['warnings'])}")
        if item.get("suggestions"):
            lines.append(f"- 建议：{'；'.join(item['suggestions'])}")
        lines.append("")
    return "\n".join(lines)


def build_payload(overrides: dict) -> dict:
    items = [
        audit_company(company_id, company)
        for company_id, company in sorted(overrides.get("companies", {}).items())
    ]
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_overrides_at": overrides.get("generated_at", ""),
        "items": items,
        "summary": {
            "companies": len(items),
            "healthy": sum(1 for item in items if item["status"] == "healthy"),
            "review": sum(1 for item in items if item["status"] == "review"),
            "weak": sum(1 for item in items if item["status"] == "weak"),
        },
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    overrides = load_json(OVERRIDES_FILE, {"companies": {}})
    payload = build_payload(overrides)
    AUDIT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    AUDIT_MD_FILE.write_text(build_markdown(payload), encoding="utf-8")
    PORTAL_AUDIT_FILE.write_text(
        "window.BAMBOO_LENS_COMPANY_MAINLINE_AUDIT = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Company page mainline audit written to: {AUDIT_FILE}")
    print(f"Company page mainline audit markdown written to: {AUDIT_MD_FILE}")
    print(f"Portal mainline audit data written to: {PORTAL_AUDIT_FILE}")


if __name__ == "__main__":
    main()
