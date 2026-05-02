#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
OFFICIAL_CANDIDATES_FILE = OUTPUT_DIR / "official_candidates.json"
DAILY_BRIEF_FILE = OUTPUT_DIR / "daily_brief.md"
SUMMARY_FILE = OUTPUT_DIR / "weekend_sync_summary.md"


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return payload if isinstance(payload, dict) else {}


def parse_date(value: str) -> datetime | None:
    text = (value or "").strip()
    for item in text.replace("/", "-").split():
        if len(item) >= 10:
            try:
                return datetime.strptime(item[:10], "%Y-%m-%d")
            except ValueError:
                continue
    return None


def recent_events(store: dict, days: int = 7) -> list[dict]:
    today = datetime.now().date()
    rows: list[dict] = []
    for company_id, payload in (store.get("companies") or {}).items():
        for event in payload.get("events", []):
            parsed = parse_date(event.get("date", ""))
            if parsed is None:
                continue
            age = today - parsed.date()
            if timedelta(days=0) <= age <= timedelta(days=days):
                rows.append(
                    {
                        "company_id": company_id,
                        "company": payload.get("name", company_id),
                        "date": event.get("date", ""),
                        "title": event.get("title", ""),
                        "type": event.get("type", ""),
                        "priority": event.get("priority", ""),
                        "sort_key": event.get("sort_key", 0),
                    }
                )
    return sorted(rows, key=lambda item: item["sort_key"], reverse=True)


def candidate_stats(candidates: dict) -> tuple[int, int]:
    companies = candidates.get("companies") or {}
    total = sum(len(items) for items in companies.values())
    covered = sum(1 for items in companies.values() if items)
    return total, covered


def latest_brief_excerpt() -> str:
    if not DAILY_BRIEF_FILE.exists():
        return "尚未找到云端日报文件。"
    lines = [
        line.rstrip()
        for line in DAILY_BRIEF_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    return "\n".join(lines[:12]) if lines else "日报文件为空。"


def render_summary() -> str:
    event_store = load_json(EVENT_STORE_FILE)
    candidates = load_json(OFFICIAL_CANDIDATES_FILE)
    events = recent_events(event_store)
    total_candidates, covered_candidates = candidate_stats(candidates)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M")

    if events:
        event_lines = "\n".join(
            f"- {item['date']}｜{item['company']}｜{item['title']}（{item['priority']}，{item['type']}）"
            for item in events[:12]
        )
    else:
        event_lines = "- 过去 7 天暂无新的正式事件入库；优先查看候选池与最新日报。"

    return f"""# 竹鉴周末同步摘要

生成时间：{generated_at}

## 本次同步后先看什么

1. 先看首页「估值决策总览」，确认哪些公司处在偏低、合理或偏高区间。
2. 再看「最近更新」和「官方候选池」，判断本周有没有新线索需要升级为正式事件。
3. 最后进入与你持仓或候选动作相关的公司主页，重点看财务地图、估值模型和动作触发条件。

## 过去 7 天正式事件

{event_lines}

## 官方候选池

- 当前候选总数：{total_candidates}
- 有候选覆盖的公司数：{covered_candidates}
- 候选不是结论；只有读完原文、形成证据和影响分析后，才会升级为正式事件。

## 最新云端日报摘录

{latest_brief_excerpt()}
"""


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_FILE.write_text(render_summary(), encoding="utf-8")
    print(f"Weekend sync summary written to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
