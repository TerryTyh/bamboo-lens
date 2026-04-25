#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timedelta
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
                    "fetched_at": event.get("fetched_at", ""),
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
                    "fetched_at": event.get("fetched_at", ""),
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


def parse_date_like(value: str) -> datetime | None:
    if not value:
        return None
    text = value.strip()
    candidates = [
        "%Y-%m-%d",
        "%Y-%m",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y%m%d-%H%M%S",
    ]
    for fmt in candidates:
        try:
            parsed = datetime.strptime(text, fmt)
            if fmt == "%Y-%m":
                return parsed.replace(day=1)
            return parsed
        except ValueError:
            continue
    if len(text) >= 10:
        try:
            return datetime.strptime(text[:10], "%Y-%m-%d")
        except ValueError:
            return None
    return None


def is_recent_event(item: dict, today: datetime, days: int = 2) -> bool:
    parsed = parse_date_like(item.get("date", ""))
    if parsed is not None:
        age = today.date() - parsed.date()
        return timedelta(days=0) <= age <= timedelta(days=days)

    parsed = parse_date_like(item.get("fetched_at", ""))
    if parsed is not None:
        age = today.date() - parsed.date()
        return timedelta(days=0) <= age <= timedelta(days=days)
    return False


def is_recent_candidate(item: dict, today: datetime, days: int = 2) -> bool:
    for key in ("fetched_at", "date"):
        parsed = parse_date_like(item.get(key, ""))
        if parsed is None:
            continue
        age = today.date() - parsed.date()
        return timedelta(days=0) <= age <= timedelta(days=days)
    return False


def render_brief(companies: list[dict], events: list[dict], official_candidates: list[dict]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now()
    names = "、".join(company["name"] for company in companies)
    fresh_events = [item for item in events if is_recent_event(item, now, days=2)]
    fresh_candidates = [item for item in official_candidates if is_recent_candidate(item, now, days=2)]
    top_events = fresh_events[:3]
    top_candidates = fresh_candidates[:5]

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
        conclusion = f"今天在已判断事件里，最值得先看的是 {top_events[0]['company_name']}。"
        no_action = "- 其余公司今天暂不新增高优先级已判断事件，维持观察。"
        validation_questions = derive_validation_questions(top_events[0])
        next_check = "\n".join(f"  {idx}. {question}" for idx, question in enumerate(validation_questions, start=1))
        tomorrow_focus = f"- 继续跟踪 {top_events[0]['company_name']} 后续是否有新增官方披露\n- 继续提升官方候选去噪与升级质量"
    else:
        changes_block = """1. 公司：系统层
   事件：今日未发现新增可直接入库的已判断事件
   核心内容：当前选定公司范围内，没有出现足够明确、足够重要、且已完成研判的当日/近期新事件。
   为什么重要：日报应优先反映最新变化，而不是重复播报历史研究内容。
   动作：维持观察"""
        conclusion = "今天没有新增值得直接推送的已判断研究事件。"
        no_action = "- 当前不重复播报旧研究内容，避免把存量结论伪装成今日新闻。"
        next_check = "继续看下一轮官方披露、财报、电话会和管理层口径是否出现新增变化"
        tomorrow_focus = "- 继续扫描官方来源中的新增线索\n- 只有出现当日/近期新变化时才升级为重点简报"

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
    elif top_events:
        candidate_block = "- 今天没有新增可入库的官方候选事件；系统已完成扫描，但没有发现足够新的、足够清晰的官方线索。"

    if not top_events:
        return f"""# 竹鉴日报 | {today}

一句话结论：

今天没有新增值得直接推送的已判断研究事件。

明日重点：

- 当前覆盖公司：{names}
- 延续跟踪最近一轮官方候选里最值得研判的线索，优先看 NVIDIA 当天新增候选是否能升级为正式研究事件
- 继续补强 TSMC、立讯精密、汇川技术、Constellation Energy 的官方来源抓取稳定性
- 只有出现当日/近期新变化时，才恢复完整日报展开
"""

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
- 资金动作建议：继续观察；若当天没有新变化，则不做额外动作
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
