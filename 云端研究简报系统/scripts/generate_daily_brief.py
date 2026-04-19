#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT / "config" / "companies.json"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "daily_brief.md"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"


def load_companies() -> list[dict]:
    data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return data["companies"]


def load_event_store() -> dict:
    if not EVENT_STORE_FILE.exists():
        return {"companies": {}}
    return json.loads(EVENT_STORE_FILE.read_text(encoding="utf-8"))


def flatten_events(store: dict) -> list[dict]:
    items = []
    for company_id, payload in store.get("companies", {}).items():
        for event in payload.get("events", []):
            items.append(
                {
                    "company_id": company_id,
                    "company_name": payload["name"],
                    "title": event["title"],
                    "date": event["date"],
                    "type": event["type"],
                    "fact": event["fact"],
                    "judgment": event["judgment"],
                    "action": event["action"],
                    "priority": event["priority"],
                    "sort_key": event.get("sort_key", 0),
                }
            )
    return sorted(items, key=lambda item: item["sort_key"], reverse=True)


def flatten_official_candidates(store: dict) -> list[dict]:
    items = []
    for company_id, payload in store.get("companies", {}).items():
        for event in payload.get("official_candidates", []):
            items.append(
                {
                    "company_id": company_id,
                    "company_name": payload["name"],
                    "title": event["title"],
                    "date": event["date"],
                    "type": event["type"],
                    "fact": event["fact"],
                    "judgment": event["judgment"],
                    "action": event["action"],
                    "priority": event["priority"],
                    "sort_key": event.get("sort_key", 0),
                    "source_url": event.get("source_url", ""),
                }
            )
    return sorted(items, key=lambda item: item["sort_key"], reverse=True)


def compact(text: str, limit: int = 82) -> str:
    value = " ".join((text or "").split())
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


def render_brief(companies: list[dict], events: list[dict], official_candidates: list[dict]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    names = "、".join(company["name"] for company in companies)
    top_events = events[:3]
    top_candidates = official_candidates[:3]

    if top_events:
        key_changes = []
        for index, event in enumerate(top_events, start=1):
            key_changes.append(
                f"""{index}. 公司：{event["company_name"]}
   事实：{normalize(event["fact"])}
   判断：{normalize(event["judgment"])}
   动作：{event["action"]}"""
            )
        changes_block = "\n\n".join(key_changes)
        conclusion = f"当前事件库已整理出 {len(events)} 条已判断事件，今天最值得先看的是 {top_events[0]['company_name']}。"
        no_action = "- 其余公司今天暂不新增高优先级动作，维持原判断。"
        next_check = f"{top_events[0]['company_name']}：{compact(top_events[0]['title'], 48)}"
        tomorrow_focus = f"- 继续补第一版真实来源抓取，让日报从样例事件过渡到官方实时事件\n- 优先增强 {top_events[0]['company_name']} 的后续验证链路"
    else:
        changes_block = f"""1. 公司：系统层
   事实：当前已加载 {len(companies)} 家核心跟踪公司配置：{names}。
   判断：公司池和官方来源入口已经具备云端执行所需的基础结构。
   动作：维持原判断"""
        conclusion = "当前云端版日报骨架已跑通，但事件库还没有生成出可用的已判断事件。"
        no_action = "- 当前不生成伪研究结论，避免在无真实事件时制造噪音。"
        next_check = "事件库生成、企业微信推送链路、GitHub Actions 定时运行"
        tomorrow_focus = "- 先跑通事件库生成\n- 再接企业微信机器人"

    if top_candidates:
        candidate_lines = []
        for index, event in enumerate(top_candidates, start=1):
            source = f" 来源：{event['source_url']}" if event.get("source_url") else ""
            candidate_lines.append(
                f"""{index}. 公司：{event["company_name"]}
   候选：{normalize(event["title"])}
   说明：{normalize(event["judgment"])}{source}"""
            )
        candidate_block = "\n\n".join(candidate_lines)
    else:
        candidate_block = "- 今天没有新增官方候选事件进入待研判队列。"

    return f"""# 竹鉴日报 | {today}

一句话结论：

{conclusion}

今日关键变化：

{changes_block}

官方来源新候选：

{candidate_block}

今日无需动作：

{no_action}

决策提示：

- 研究动作：优先推进真实来源抓取、事件抽取与公司状态回写
- 资金动作建议：继续观察
- 下一次验证点：{next_check}

明日重点：

- 当前覆盖公司：{names}
{tomorrow_focus}
"""


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    companies = load_companies()
    event_store = load_event_store()
    events = flatten_events(event_store)
    official_candidates = flatten_official_candidates(event_store)
    brief = render_brief(companies, events, official_candidates)
    OUTPUT_FILE.write_text(brief, encoding="utf-8")
    print(f"Daily brief written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
