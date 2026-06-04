#!/usr/bin/env python3
from __future__ import annotations

import json
import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
INPUT_FILE = ROOT / "outputs" / "official_candidates.json"
EVENT_STORE_FILE = ROOT / "outputs" / "event_store.json"
OUTPUT_FILE = PROJECT_ROOT / "研究门户" / "candidate-data.js"

IMPORTANT_KEYWORDS = {
    "财报": 5,
    "业绩": 5,
    "收入": 4,
    "毛利率": 4,
    "现金流": 4,
    "年度报告": 5,
    "季度报告": 5,
    "半年度报告": 4,
    "业绩预告": 5,
    "业绩快报": 5,
    "投资者关系活动记录表": 5,
    "投资者关系管理信息": 5,
    "向特定对象发行股票": 5,
    "定增": 4,
    "募集说明书": 4,
    "重大合同": 4,
    "中标": 3,
    "订单": 3,
    "回购": 3,
    "earnings": 5,
    "results": 5,
    "outlook": 5,
    "guidance": 5,
    "revenue": 4,
    "eps": 4,
    "annual report": 3,
    "20-f": 3,
    "technology symposium": 3,
    "conference call": 3,
    "annual meeting": 2,
    "acquisition": 4,
    "contract": 3,
    "customer": 2,
    "collaborate": 2,
    "partnership": 2,
}

LOW_SIGNAL_KEYWORDS = [
    "公告包括",
    "承诺报告内容真实可靠",
    "定期报告",
    "临时公告",
    "法律意见书",
    "工作细则",
    "公司章程",
    "独立董事",
    "审计委员会",
    "提名委员会",
    "战略委员会",
    "薪酬与考核委员会",
    "股权激励",
    "限制性股票归属",
    "作废部分",
    "工商变更",
    "工商登记",
    "营业执照",
    "权益分派实施公告",
    "非经营性资金占用",
    "专项意见",
    "内部控制",
    "games hit the cloud",
    "protecting the planet",
    "national robotics week",
    "rainforests",
    "recycling plants",
]
GENERIC_CN_TITLES = {"年度报告", "半年度报告", "季度报告", "业绩预告", "业绩快报", "临时公告", "定期报告"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export official candidates for the research portal.")
    parser.add_argument(
        "--input",
        type=Path,
        default=INPUT_FILE,
        help="Path to official_candidates.json. Defaults to the local outputs file.",
    )
    return parser.parse_args()


def load_candidates(input_file: Path) -> dict:
    if not input_file.exists():
        return {"generated_at": "", "companies": {}}
    return json.loads(input_file.read_text(encoding="utf-8"))


def load_event_store() -> dict:
    if not EVENT_STORE_FILE.exists():
        return {"companies": {}}
    return json.loads(EVENT_STORE_FILE.read_text(encoding="utf-8"))


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


def keyword_score(text: str) -> int:
    lowered = text.lower()
    return sum(weight for keyword, weight in IMPORTANT_KEYWORDS.items() if keyword in lowered)


def reviewed_keys(event_store: dict, company_id: str) -> set[tuple[str, str]]:
    keys = set()
    for event in event_store.get("companies", {}).get(company_id, {}).get("events", []):
        if event.get("review_status") != "reviewed":
            continue
        for field in ("title", "source_candidate_title"):
            title = str(event.get(field, "")).strip()
            if title:
                keys.add(("title", title))
        source_url = str(event.get("source_url", "")).strip()
        if source_url:
            keys.add(("source_url", source_url))
    return keys


def read_next(candidate: dict) -> str:
    text = " ".join([candidate.get("title", ""), candidate.get("type", ""), candidate.get("fact", "")]).lower()
    raw_text = " ".join([candidate.get("title", ""), candidate.get("type", ""), candidate.get("fact", "")])
    if any(word in raw_text for word in ["投资者关系活动记录表", "投资者关系管理信息"]):
        return "优先读问答记录里的客户需求、800G/1.6T、订单能见度、毛利率、现金流、存货和应收变化；够具体后再升级。"
    if any(word in raw_text for word in ["年度报告", "季度报告", "半年度报告", "业绩预告", "业绩快报"]):
        return "打开报告原文，提取收入、利润率、现金流、存货、应收和经营指引；不要只凭标题升级。"
    if any(word in raw_text for word in ["向特定对象发行股票", "定增", "募集说明书"]):
        return "先读募投项目、金额、稀释、产能用途和客户验证；确认是否改善长期竞争位置。"
    if "关于召开" in raw_text and "业绩说明会" in raw_text:
        return "先记录会议日期；等说明会纪要、问答或材料出来后再做正式研判。"
    if any(word in text for word in ["earnings", "results", "eps", "revenue", "outlook", "guidance"]):
        return "优先读原文里的收入、利润率、指引、现金流和管理层口径；够具体后再升级为正式事件。"
    if any(word in text for word in ["annual report", "20-f", "report"]):
        return "适合周末深读：补风险、业务结构、资本开支和治理信息，先不要直接写成短期动作。"
    if any(word in text for word in ["conference call", "annual meeting", "webcast"]):
        return "这是日程/电话会线索：先记录验证日期，等 transcript 或会议材料出来再研判。"
    if any(word in text for word in ["acquisition", "contract", "customer", "collaborate", "partnership"]):
        return "先读交易/客户/合作的规模、期限、收入路径和利润影响；避免只凭标题判断。"
    return "先打开官方来源阅读全文，提取事实和数字；如果只有标题或营销话术，就保留候选不升级。"


def classify_candidate(candidate: dict, reviewed: set[tuple[str, str]]) -> dict:
    title = candidate.get("title", "").strip()
    text = " ".join([title, candidate.get("type", ""), candidate.get("fact", "")])
    lowered = text.lower()
    score = keyword_score(text) + 1
    if parse_sort_key(candidate.get("sort_key") or candidate.get("date")) >= 20260425:
        score += 2

    source_url = candidate.get("source_url", "").strip()
    if ("title", title) in reviewed or ("source_url", source_url) in reviewed:
        return {
            "candidate_status": "promoted",
            "status_label": "已入库",
            "review_lane": "正式事件",
            "review_score": score + 10,
            "review_reason": "这条候选已经完成原文研判，并沉淀为正式事件；不再作为待读候选重复出现。",
            "read_next": "可直接进入对应公司主页或事件详情阅读正式研判。",
        }

    if title in GENERIC_CN_TITLES or any(keyword in lowered for keyword in LOW_SIGNAL_KEYWORDS):
        return {
            "candidate_status": "skipped",
            "status_label": "暂不研判",
            "review_lane": "低信号",
            "review_score": score,
            "review_reason": "这类内容更偏品牌、生态或营销更新，暂时看不到足够直接的业务、财务或估值影响。",
            "read_next": "保留存档；除非后续出现客户、金额、产品路线或财务影响，否则不升级。",
        }

    if "关于召开" in text and "业绩说明会" in text:
        return {
            "candidate_status": "waiting_material",
            "status_label": "待材料",
            "review_lane": "日程线索",
            "review_score": score,
            "review_reason": "这更像业绩说明会日程，不能只凭通知写成正式事件，需要等问答纪要或会议材料。",
            "read_next": read_next(candidate),
        }

    if any(word in lowered for word in ["conference call", "annual meeting", "webcast"]) and not any(
        word in lowered for word in ["outlook", "results", "earnings"]
    ):
        return {
            "candidate_status": "waiting_material",
            "status_label": "待材料",
            "review_lane": "日程线索",
            "review_score": score,
            "review_reason": "这更像会议/电话会日程，不能只凭日程写成正式事件，需要等材料、transcript 或财报内容。",
            "read_next": read_next(candidate),
        }

    if score >= 5:
        return {
            "candidate_status": "pending",
            "status_label": "待研判",
            "review_lane": "优先阅读",
            "review_score": score,
            "review_reason": "标题中包含财报、展望、技术路线、客户合作或交易等投资相关信号，值得打开原文判断是否升级。",
            "read_next": read_next(candidate),
        }

    return {
        "candidate_status": "archived",
        "status_label": "先存档",
        "review_lane": "低优先级",
        "review_score": score,
        "review_reason": "当前信号不足以进入优先研判；先保存来源，避免把普通新闻包装成投资事件。",
        "read_next": read_next(candidate),
    }


def candidate_sort_key(item: dict) -> tuple[int, int, int]:
    status_rank = {
        "pending": 4,
        "waiting_material": 3,
        "promoted": 2,
        "archived": 1,
        "skipped": 0,
    }.get(item.get("candidate_status", ""), 0)
    return (status_rank, int(item.get("review_score") or 0), parse_sort_key(item.get("sort_key") or item.get("date")))


def enrich_candidates(payload: dict, event_store: dict) -> dict:
    enriched = {**payload, "companies": {}}
    for company_id, items in payload.get("companies", {}).items():
        reviewed = reviewed_keys(event_store, company_id)
        enriched["companies"][company_id] = []
        company_name = event_store.get("companies", {}).get(company_id, {}).get("name", company_id)
        for item in items or []:
            enriched["companies"][company_id].append(
                {
                    **item,
                    "company": company_id,
                    "company_name": item.get("company_name") or company_name,
                    **classify_candidate(item, reviewed),
                }
            )
        enriched["companies"][company_id].sort(key=candidate_sort_key, reverse=True)
    return enriched


def main() -> None:
    args = parse_args()
    payload = enrich_candidates(load_candidates(args.input), load_event_store())
    OUTPUT_FILE.write_text(
        "window.BAMBOO_LENS_CANDIDATES = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Portal candidate data written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
