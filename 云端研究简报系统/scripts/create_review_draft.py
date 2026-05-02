#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
DECISION_QUEUE_FILE = OUTPUT_DIR / "decision_queue.json"
DRAFT_DIR = OUTPUT_DIR / "review_drafts"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a formal-event review draft from the decision queue.")
    parser.add_argument("--index", type=int, default=0, help="0-based index in decision_queue.json. Defaults to 0.")
    parser.add_argument("--company", help="Optional company id filter.")
    parser.add_argument("--title-contains", help="Optional title keyword filter.")
    parser.add_argument("--out", type=Path, help="Optional output draft path.")
    return parser.parse_args()


def load_queue() -> dict:
    if not DECISION_QUEUE_FILE.exists():
        raise FileNotFoundError(f"Decision queue not found: {DECISION_QUEUE_FILE}")
    return json.loads(DECISION_QUEUE_FILE.read_text(encoding="utf-8"))


def slugify(text: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", text).strip("-")
    return slug[:72] or "review-draft"


def select_item(items: list[dict], index: int, company: str | None, title_contains: str | None) -> dict:
    filtered = items
    if company:
        filtered = [item for item in filtered if item.get("company") == company]
    if title_contains:
        needle = title_contains.lower()
        filtered = [item for item in filtered if needle in item.get("title", "").lower()]
    if not filtered:
        raise ValueError("No decision queue item matched the filters.")
    if index < 0 or index >= len(filtered):
        raise IndexError(f"Index {index} out of range for {len(filtered)} matched items.")
    return filtered[index]


def placeholder_list(label: str, count: int) -> list[str]:
    return [f"TODO: {label} {idx}" for idx in range(1, count + 1)]


def build_draft(item: dict) -> dict:
    now = datetime.now().isoformat(timespec="seconds")
    is_formal = item.get("source_type") == "formal_event"
    return {
        "draft_status": "draft",
        "created_at": now,
        "reviewed_at": "",
        "source_queue_item": {
            "company": item.get("company", ""),
            "source_type": item.get("source_type", ""),
            "stage": item.get("stage", ""),
            "title": item.get("title", ""),
            "score": item.get("score"),
            "event_index": item.get("event_index"),
        },
        "source_candidate_title": item.get("title", ""),
        "company": item.get("company", ""),
        "company_name": item.get("company_name", ""),
        "title": item.get("title", ""),
        "date": item.get("date", ""),
        "type": item.get("type", "已研判事件"),
        "priority": item.get("priority", "P2") if is_formal else "P2",
        "action": item.get("decision_action", "维持跟踪"),
        "sort_key": item.get("sort_key") or 0,
        "source_url": item.get("source_url", ""),
        "source_doc": item.get("source_doc", ""),
        "source_summary": [
            item.get("why", "") if is_formal else "TODO: 先说明原文到底说了什么，不要先写判断。",
            "TODO: 补充原文里的关键背景、管理层口径、业务范围或财务口径。",
        ],
        "fact": item.get("why", "") if is_formal else "TODO: 用具体事实、数字、日期和来源概括事件本身。",
        "evidence": placeholder_list("补一条来自原文的证据，必须包含数字/口径/日期/产品/客户/合同等具体信息", 3),
        "judgment": item.get("why", "") if is_formal else "TODO: 说明这条事件改变了什么、没有改变什么。",
        "business_analysis": "TODO: 说明影响哪条业务线、产品、客户、市场或成本结构。",
        "valuation_analysis": "TODO: 说明对估值区间、确信度、仓位动作或等待验证姿态的影响。",
        "verification": placeholder_list("下一次需要验证的具体指标或事实", 3),
        "quality_check": {
            "has_source": bool(item.get("source_url") or item.get("source_doc")),
            "needs_primary_source_reading": not is_formal,
            "notes": "把所有 TODO 改成证据充分的内容后，再运行 promote_reviewed_event.py。",
        },
    }


def main() -> None:
    args = parse_args()
    payload = load_queue()
    item = select_item(payload.get("items", []), args.index, args.company, args.title_contains)
    draft = build_draft(item)
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    out = args.out or DRAFT_DIR / f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{draft['company']}-{slugify(draft['title'])}.json"
    out.write_text(json.dumps(draft, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Review draft written to: {out}")
    print(f"Company: {draft['company_name']} / {draft['company']}")
    print(f"Title: {draft['title']}")
    print("Next: fill every TODO, then run promote_reviewed_event.py with this draft.")


if __name__ == "__main__":
    main()
