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


def event_priority_score(priority: str) -> int:
    mapping = {
        "P1": 30,
        "P2": 20,
        "P3": 10,
        "候选": 5,
    }
    return mapping.get((priority or "").strip(), 0)


def event_type_score(event_type: str) -> int:
    value = (event_type or "").strip()
    if "财报指引" in value:
        return 26
    if "财报" in value:
        return 24
    if "并购" in value or "业务扩张" in value:
        return 22
    if "产品" in value or "平台" in value or "技术" in value:
        return 20
    if "月度营收" in value:
        return 18
    if "资本配置" in value or "董事会" in value:
        return 16
    if "管理层表述" in value or "投资者沟通" in value:
        return 12
    if "预告" in value or "验证点" in value:
        return 4
    return 10


def rank_event(event: dict) -> tuple[int, int]:
    return (
        event_priority_score(event.get("priority", "")) + event_type_score(event.get("type", "")),
        event.get("sort_key", 0),
    )


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
    return sorted(items, key=rank_event, reverse=True)


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


def derive_validation_questions(event: dict) -> list[str]:
    company = event.get("company_name", "")
    title = normalize(event.get("title", ""))
    fact = normalize(event.get("fact", ""))
    event_type = normalize(event.get("type", ""))
    questions: list[str] = []

    if company == "NVIDIA":
        questions = [
            "下次财报里数据中心收入能否继续维持高增速，而不是只靠个别大客户拉动。",
            "GAAP / non-GAAP 毛利率是否仍能维持在高位，平台扩张是否开始侵蚀盈利质量。",
            "超大客户资本开支口径有没有变化，推理需求是否真的接上训练需求。"
        ]
    elif company == "TSMC":
        questions = [
            "下一次法说会里 2nm 和 CoWoS 的需求口径是否继续偏紧。",
            "毛利率和营业利润率能否维持高位，海外扩产是否开始明显稀释盈利。",
            "高资本开支之后，自由现金流和资本回报是否仍然稳得住。"
        ]
    elif company == "阿里巴巴":
        questions = [
            "云业务增速是否能继续高于集团整体，AI 收入是否还能保持高景气。",
            "云和 AI 的增长能否继续转化为估值中枢上移，而不只是阶段性情绪催化。",
            "回购和资本配置是否持续执行，港股 / 中概折价修复逻辑是否还成立。"
        ]
    elif "财报" in event_type or "指引" in event_type:
        questions = [
            "下一次财报里收入、利润率和现金流是否继续朝同一方向改善。",
            "本次强化信息是否只是一次性高点，还是已经开始形成连续兑现。",
        ]
    elif "预告" in event_type or "验证点" in event_type:
        questions = [
            f"{company} 下一次正式披露里，最重要的经营指标会不会支持当前判断。",
            "管理层最新口径是否会改变我们对增长质量或资本回报的看法。"
        ]
    else:
        questions = [
            f"{company} 这次变化会不会继续出现在下一次正式披露里，而不是一次性新闻。",
            "这条变化对业务质量和估值逻辑的影响，能否被后续数据继续验证。"
        ]

    return questions[:3]


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
   事件：{normalize(event["title"])}
   核心内容：{normalize(event["fact"])}
   为什么重要：{normalize(event["judgment"])}
   动作：{event["action"]}"""
            )
        changes_block = "\n\n".join(key_changes)
        conclusion = f"当前事件库已整理出 {len(events)} 条已判断事件，今天最值得先看的是 {top_events[0]['company_name']}。"
        no_action = "- 其余公司今天暂不新增高优先级动作，维持原判断。"
        validation_questions = derive_validation_questions(top_events[0])
        next_check = "\n".join(f"  {idx}. {question}" for idx, question in enumerate(validation_questions, start=1))
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
        candidate_block = "- 今天没有新增可入库的官方候选事件。当前云端快照链路是通的，但还需要继续增强网页抓取和候选抽取质量。"

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
- 下一次验证点：
{next_check}

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
