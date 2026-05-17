#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
OVERRIDES_FILE = OUTPUT_DIR / "company_page_overrides.json"
AUDIT_FILE = OUTPUT_DIR / "company_page_readability_audit.json"
AUDIT_MD_FILE = OUTPUT_DIR / "company_page_readability_audit.md"
PORTAL_AUDIT_FILE = PROJECT_ROOT / "研究门户" / "company-readability-audit-data.js"

MAX_AUTO_ITEMS_PER_COMPANY = 12
MAX_TEXT_LENGTH = 920
WARN_TEXT_LENGTH = 720
MAX_TEXT_SAMPLES = 5

WEAK_PHRASES = [
    "值得关注",
    "长期逻辑强化",
    "需要后续验证",
    "对估值有积极影响",
    "维持观察",
]


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


def text_entries(value, path: str = "") -> list[dict]:
    entries = []
    if isinstance(value, str):
        entries.append({"path": path, "length": len(value), "text": value})
    elif isinstance(value, list):
        for index, item in enumerate(value):
            entries.extend(text_entries(item, f"{path}[{index}]"))
    elif isinstance(value, dict):
        for key, item in value.items():
            next_path = f"{path}.{key}" if path else str(key)
            entries.extend(text_entries(item, next_path))
    return entries


def text_preview(text: str, limit: int = 90) -> str:
    cleaned = " ".join(str(text or "").split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1].rstrip() + "…"


def section_counts(company: dict) -> dict[str, int]:
    deposits = company.get("sectionDeposits", {})
    finance = deposits.get("financeMap", {})
    business = deposits.get("businessMap", {})
    valuation = deposits.get("valuationModel", {})
    return {
        "finance_rows": len(finance.get("rows", []) or []),
        "finance_bridge": len(finance.get("bridge", []) or []),
        "finance_notes": len(finance.get("notes", []) or []),
        "business_segments": len(business.get("segments", []) or []),
        "business_moat": len(business.get("moat", []) or []),
        "valuation_current": len(valuation.get("currentBreakdown", []) or []),
        "valuation_scenarios": len(valuation.get("scenarios", []) or []),
        "valuation_triggers": len(valuation.get("triggers", []) or []),
    }


def audit_company(company_id: str, company: dict) -> dict:
    counts = section_counts(company)
    total_auto_items = sum(counts.values())
    texts = text_values(company.get("sectionDeposits", {}))
    entries = text_entries(company.get("sectionDeposits", {}))
    warnings: list[str] = []
    suggestions: list[str] = []

    long_entries = [entry for entry in entries if entry["length"] > MAX_TEXT_LENGTH]
    warn_long_entries = [entry for entry in entries if WARN_TEXT_LENGTH < entry["length"] <= MAX_TEXT_LENGTH]
    long_count = len(long_entries)
    warn_long_count = len(warn_long_entries)
    weak_hits = sorted({phrase for phrase in WEAK_PHRASES for text in texts if phrase in text})
    omitted = company.get("depositPolicy", {}).get("omitted", {})

    if total_auto_items > MAX_AUTO_ITEMS_PER_COMPANY:
        warnings.append(f"自动沉淀内容偏多：{total_auto_items} 条")
        suggestions.append("继续压缩自动沉淀预算，优先保留当前结论、财务证据和估值触发。")
    if long_count:
        warnings.append(f"存在 {long_count} 条超过 {MAX_TEXT_LENGTH} 字的自动沉淀文本")
        suggestions.append("把长文本拆成事实、判断、验证点，避免单卡片阅读负担过重。")
    if warn_long_count:
        warnings.append(f"有 {warn_long_count} 条文本接近过长阈值")
    if weak_hits:
        warnings.append(f"出现模板化表达：{'、'.join(weak_hits)}")
        suggestions.append("保留这些词可以，但必须配套事实、数字和原文证据，不能让它们成为主要内容。")
    if omitted:
        suggestions.append("已有内容被预算压缩；如发现重要事件消失，应提高该板块预算或强化事件优先级。")
    if counts["finance_rows"] and counts["finance_notes"] == 0:
        warnings.append("有财务证据行，但缺少财务读法")
        suggestions.append("补一条财务读法，解释这些数字如何影响公司判断。")
    if counts["business_segments"] and counts["business_moat"] == 0:
        warnings.append("有业务变化，但缺少护城河/业务主线判断")
        suggestions.append("补充这条业务变化到底是强化护城河、验证客户需求，还是只是营销新闻。")
    if counts["valuation_current"] and counts["valuation_triggers"] == 0:
        warnings.append("有估值影响，但缺少下一步触发条件")
        suggestions.append("补充什么数据会让估值中枢上修、维持或下调。")

    status = "healthy"
    if warnings:
        status = "review"
    if total_auto_items > MAX_AUTO_ITEMS_PER_COMPANY or long_count or len(weak_hits) >= 3:
        status = "at_risk"

    return {
        "company": company_id,
        "sourceEventTitle": company.get("sourceEventTitle", ""),
        "sourceEventDate": company.get("sourceEventDate", ""),
        "status": status,
        "counts": counts,
        "totalAutoItems": total_auto_items,
        "omitted": omitted,
        "longTextSamples": [
            {"path": item["path"], "length": item["length"], "preview": text_preview(item["text"])}
            for item in sorted(long_entries + warn_long_entries, key=lambda row: row["length"], reverse=True)[
                :MAX_TEXT_SAMPLES
            ]
        ],
        "warnings": warnings,
        "suggestions": suggestions,
    }


def status_label(status: str) -> str:
    return {
        "healthy": "健康",
        "review": "需复核",
        "at_risk": "有稀释风险",
    }.get(status, status)


def build_markdown(payload: dict) -> str:
    lines = [
        "# 公司页可读性审计",
        "",
        f"生成时间：{payload.get('generated_at', '')}",
        "",
        "这份报告只检查自动沉淀内容是否可能稀释公司主页主线，不替代正式研究判断。",
        "",
        "## 总览",
        "",
        f"- 覆盖公司：{payload['summary']['companies']} 家",
        f"- 健康：{payload['summary']['healthy']} 家",
        f"- 需复核：{payload['summary']['review']} 家",
        f"- 有稀释风险：{payload['summary']['at_risk']} 家",
        "",
        "## 公司明细",
        "",
    ]
    for item in payload.get("items", []):
        counts = item["counts"]
        lines.extend(
            [
                f"### {item['company']}｜{status_label(item['status'])}",
                "",
                f"- 最新自动沉淀事件：{item.get('sourceEventDate', '')}｜{item.get('sourceEventTitle', '')}",
                f"- 自动沉淀条目：{item['totalAutoItems']} 条",
                f"- 财务：证据 {counts['finance_rows']}、拆解 {counts['finance_bridge']}、读法 {counts['finance_notes']}",
                f"- 业务：主线 {counts['business_segments']}、护城河 {counts['business_moat']}",
                f"- 估值：影响 {counts['valuation_current']}、情景 {counts['valuation_scenarios']}、触发 {counts['valuation_triggers']}",
            ]
        )
        if item.get("omitted"):
            lines.append(f"- 已压缩内容：{json.dumps(item['omitted'], ensure_ascii=False)}")
        if item.get("longTextSamples"):
            lines.append("- 长文本定位：")
            for sample in item["longTextSamples"]:
                lines.append(
                    f"  - {sample['path']}｜{sample['length']} 字｜{sample['preview']}"
                )
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
            "at_risk": sum(1 for item in items if item["status"] == "at_risk"),
        },
    }


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    overrides = load_json(OVERRIDES_FILE, {"companies": {}})
    payload = build_payload(overrides)
    AUDIT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    AUDIT_MD_FILE.write_text(build_markdown(payload), encoding="utf-8")
    PORTAL_AUDIT_FILE.write_text(
        "window.BAMBOO_LENS_COMPANY_READABILITY_AUDIT = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Company page readability audit written to: {AUDIT_FILE}")
    print(f"Company page readability audit markdown written to: {AUDIT_MD_FILE}")
    print(f"Portal readability audit data written to: {PORTAL_AUDIT_FILE}")


if __name__ == "__main__":
    main()
