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
DECISION_QUEUE_FILE = OUTPUT_DIR / "decision_queue.json"
PORTAL_DECISION_DATA_FILE = PROJECT_ROOT / "研究门户" / "decision-data.js"

IMPORTANT_KEYWORDS = {
    "财报": 5,
    "业绩": 5,
    "results": 5,
    "earnings": 5,
    "guidance": 5,
    "outlook": 5,
    "revenue": 4,
    "eps": 4,
    "margin": 4,
    "cash flow": 4,
    "annual report": 3,
    "20-f": 3,
    "acquisition": 4,
    "merger": 4,
    "conference call": 3,
    "investor": 2,
    "technology symposium": 2,
    "customer": 2,
    "contract": 3,
    "power": 2,
    "ai": 2,
    "cloud": 2,
    "capex": 4,
}

ACTION_WEIGHT = {
    "提升优先级": 5,
    "需要二次验证": 4,
    "等待验证": 3,
    "维持原判断": 2,
    "加入待研判队列": 1,
}

PRIORITY_WEIGHT = {
    "P1": 5,
    "P2": 3,
    "P3": 1,
    "候选": 1,
}


def load_event_store() -> dict:
    if not EVENT_STORE_FILE.exists():
        return {"generated_at": "", "companies": {}}
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


def action_score(action: str) -> int:
    return ACTION_WEIGHT.get(action, 0)


def priority_score(priority: str) -> int:
    return PRIORITY_WEIGHT.get(priority, 0)


def build_formal_item(company_id: str, company: dict, event: dict, index: int) -> dict:
    score = (
        priority_score(event.get("priority", ""))
        + action_score(event.get("action", ""))
        + keyword_score(" ".join([event.get("title", ""), event.get("type", ""), event.get("fact", "")]))
        + 2
    )
    if event.get("review_status") == "reviewed":
        score += 6
    if event.get("source_url") and event.get("evidence"):
        score += 3
    decision_action = event.get("action") or "继续跟踪"
    if event.get("priority") == "P1" and decision_action == "维持原判断":
        decision_action = "保持核心跟踪"

    return {
        "company": company_id,
        "company_name": company.get("name", company_id),
        "source_type": "formal_event",
        "stage": "已入库事件",
        "title": event.get("title", ""),
        "date": event.get("date", ""),
        "type": event.get("type", ""),
        "priority": event.get("priority", ""),
        "decision_action": decision_action,
        "why": event.get("judgment", ""),
        "read_next": "打开事件详情，核对事实、判断、估值/动作影响，并决定是否回写公司主页当前结论。",
        "source_url": event.get("source_url", ""),
        "source_doc": event.get("source_doc", ""),
        "event_index": index,
        "sort_key": parse_sort_key(event.get("sort_key") or event.get("date")),
        "score": score,
    }


def candidate_read_next(candidate: dict) -> str:
    text = " ".join([candidate.get("title", ""), candidate.get("type", ""), candidate.get("fact", "")]).lower()
    if any(word in text for word in ["earnings", "results", "eps", "revenue", "outlook", "guidance"]):
        return "优先读原文里的收入、利润率、指引、现金流和管理层口径；够具体后再升级为正式事件。"
    if any(word in text for word in ["annual report", "20-f", "report"]):
        return "适合周末深读：补风险、业务结构、资本开支和治理信息，先不要直接写成短期动作。"
    if any(word in text for word in ["conference call", "annual meeting", "webcast"]):
        return "这是日程/电话会线索：先记录验证日期，等 transcript 或会议材料出来再研判。"
    if any(word in text for word in ["acquisition", "contract", "customer", "collaborate", "partnership"]):
        return "先读交易/客户/合作的规模、期限、收入路径和利润影响；避免只凭标题判断。"
    return "先打开官方来源阅读全文，提取事实和数字；如果只有标题或营销话术，就保留候选不升级。"


def build_candidate_item(company_id: str, company: dict, candidate: dict) -> dict:
    title = candidate.get("title", "")
    text = " ".join([title, candidate.get("type", ""), candidate.get("fact", "")])
    score = keyword_score(text) + priority_score(candidate.get("priority", "")) + 1
    if parse_sort_key(candidate.get("sort_key") or candidate.get("date")) >= 20260425:
        score += 2

    return {
        "company": company_id,
        "company_name": company.get("name", company_id),
        "source_type": "official_candidate",
        "stage": "待读原文",
        "title": title,
        "date": candidate.get("date", "") or candidate.get("fetched_at", ""),
        "type": candidate.get("type", "官方候选"),
        "priority": candidate.get("priority", "候选"),
        "decision_action": "进入研判队列" if score >= 5 else "先存档观察",
        "why": candidate.get("judgment", "这是官方候选线索，尚未完成原文阅读和正式研判。"),
        "read_next": candidate_read_next(candidate),
        "source_url": candidate.get("source_url", ""),
        "source_doc": candidate.get("source_file", ""),
        "event_index": None,
        "sort_key": parse_sort_key(candidate.get("sort_key") or candidate.get("date")),
        "score": score,
    }


def reviewed_candidate_titles(events: list[dict]) -> set[str]:
    titles = set()
    for event in events:
        for field in ("title", "source_candidate_title"):
            title = str(event.get(field, "")).strip()
            if title:
                titles.add(title)
    return titles


def build_queue(payload: dict) -> list[dict]:
    items: list[dict] = []
    for company_id, company in payload.get("companies", {}).items():
        reviewed_titles = reviewed_candidate_titles(company.get("events", []))
        for index, event in enumerate(company.get("events", [])):
            item = build_formal_item(company_id, company, event, index)
            if item["score"] >= 8 or item["priority"] in {"P1", "P2"}:
                items.append(item)

        for candidate in company.get("official_candidates", []):
            if candidate.get("title", "").strip() in reviewed_titles:
                continue
            item = build_candidate_item(company_id, company, candidate)
            if item["score"] >= 5:
                items.append(item)

    return sorted(items, key=lambda row: (row["score"], row["sort_key"]), reverse=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    event_store = load_event_store()
    queue = build_queue(event_store)
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "source_generated_at": event_store.get("generated_at", ""),
        "items": queue,
        "summary": {
            "total": len(queue),
            "formal_events": sum(1 for item in queue if item["source_type"] == "formal_event"),
            "official_candidates": sum(1 for item in queue if item["source_type"] == "official_candidate"),
            "companies": len({item["company"] for item in queue}),
        },
    }

    DECISION_QUEUE_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_DECISION_DATA_FILE.write_text(
        "window.BAMBOO_LENS_DECISION_QUEUE = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Decision queue written to: {DECISION_QUEUE_FILE}")
    print(f"Portal decision data written to: {PORTAL_DECISION_DATA_FILE}")


if __name__ == "__main__":
    main()
