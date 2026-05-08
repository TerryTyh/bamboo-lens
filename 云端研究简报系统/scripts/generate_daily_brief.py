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
                    "source_doc": event.get("source_doc", ""),
                    "source_candidate_title": event.get("source_candidate_title", ""),
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
                    "source_excerpt": event.get("source_excerpt", ""),
                    "content_summary": event.get("content_summary", []),
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


def has_specific_evidence(text: str) -> bool:
    value = normalize(text)
    evidence_markers = [
        "%",
        "亿元",
        "亿美元",
        "NT$",
        "EPS",
        "收入",
        "利润",
        "毛利率",
        "现金流",
        "应收",
        "应付",
        "存货",
        "订单",
        "backlog",
        "capex",
        "客户",
        "指引",
    ]
    return any(marker in value for marker in evidence_markers)


def is_publishable_event(event: dict) -> bool:
    """Only fully-read events should appear as daily key changes."""
    fact = normalize(event.get("fact", ""))
    judgment = normalize(event.get("judgment", ""))
    source_doc = normalize(event.get("source_doc", ""))
    priority = normalize(event.get("priority", ""))

    if priority == "候选":
        return False
    if len(fact) < 80 or len(judgment) < 40:
        return False
    if not source_doc:
        return False
    if not has_specific_evidence(fact):
        return False

    hollow_phrases = [
        "这是云端从官方页面自动抓到的候选更新",
        "需进一步研判后再升级",
        "说明月度营收已有新增官方披露",
        "通常会直接影响",
    ]
    return not any(phrase in fact or phrase in judgment for phrase in hollow_phrases)


def extract_key_evidence(event: dict) -> str:
    fact = normalize(event.get("fact", ""))
    if not fact:
        return "暂无可展示证据。"
    sentences = [item.strip(" 。；;") for item in fact.replace("；", "。").split("。") if item.strip()]
    evidence = [sentence for sentence in sentences if has_specific_evidence(sentence)]
    selected = evidence[:3] or sentences[:2]
    return "；".join(selected)


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


def is_recent_candidate(item: dict, today: datetime, days: int = 2, upcoming_days: int = 7) -> bool:
    # If the source provides an event date, prefer it over fetched_at.
    # Otherwise old conference pages re-fetched today will look like fresh news.
    parsed_date = parse_date_like(item.get("date", ""))
    if parsed_date is not None:
        age = today.date() - parsed_date.date()
        return -timedelta(days=upcoming_days) <= age <= timedelta(days=days)

    parsed_fetched_at = parse_date_like(item.get("fetched_at", ""))
    if parsed_fetched_at is not None:
        age = today.date() - parsed_fetched_at.date()
        return timedelta(days=0) <= age <= timedelta(days=days)
    return False


def candidate_signal_score(item: dict) -> int:
    text = " ".join(
        normalize(item.get(field, ""))
        for field in ["title", "type", "fact"]
    ).lower()
    score = 0
    keyword_weights = {
        "earnings": 5,
        "results": 5,
        "revenue": 4,
        "eps": 4,
        "outlook": 4,
        "guidance": 4,
        "annual report": 3,
        "20-f": 3,
        "partnership": 3,
        "collaborate": 3,
        "long-term": 3,
        "manufacturing": 2,
        "ai infrastructure": 3,
        "cloud": 2,
        "ai": 2,
        "conference call": 2,
    }
    low_signal = [
        "games hit the cloud",
        "protecting the planet",
        "rainforests",
        "recycling plants",
        "golden responsibility award",
        "esg",
    ]
    for keyword, weight in keyword_weights.items():
        if keyword in text:
            score += weight
    if any(keyword in text for keyword in low_signal):
        score -= 6
    if item.get("sort_key", 0) >= 20260501:
        score += 2
    if has_candidate_content(item):
        score += 8
    else:
        score -= 8
    return score


def candidate_reason(item: dict) -> str:
    text = normalize(item.get("title", "")).lower()
    if any(word in text for word in ["earnings", "results", "eps", "revenue", "outlook", "guidance"]):
        return "这类信息可能直接影响收入、利润率、现金流或下一季验证点，值得优先读原文。"
    if any(word in text for word in ["partnership", "collaborate", "long-term"]):
        return "这类信息可能影响客户绑定、供应链位置或平台化能力，但必须读原文确认规模和商业路径。"
    if any(word in text for word in ["annual report", "20-f"]):
        return "这类信息适合周末深读，用来补风险、资本开支、业务结构和治理信息。"
    if any(word in text for word in ["ai", "cloud", "infrastructure", "manufacturing"]):
        return "这类信息可能影响长期业务边界，但不能只凭标题下判断，需要看客户、金额、部署路径。"
    return "这是今日新增官方候选，先作为待读线索保留，不直接形成投资结论。"


def candidate_next_step(item: dict) -> str:
    text = normalize(item.get("title", "")).lower()
    if any(word in text for word in ["earnings", "results", "conference call"]):
        return "打开原文或会议材料，提取收入、利润率、指引、现金流和管理层口径。"
    if any(word in text for word in ["partnership", "collaborate", "manufacturing"]):
        return "重点确认合作对象、期限、产能/金额、收入路径和是否强化护城河。"
    if any(word in text for word in ["annual report", "20-f"]):
        return "放入周末深读，补公司风险、业务结构、资本开支和现金流质量。"
    return "先读原文正文；如果只有营销标题或日程信息，就留在候选池不升级。"


def candidate_content(item: dict) -> str:
    content_summary = item.get("content_summary") or []
    if content_summary:
        return "\n   ".join(f"- {normalize(line)}" for line in content_summary if normalize(line))

    excerpt = normalize(item.get("source_excerpt", ""))
    if is_readable_candidate_content(excerpt) and contains_chinese(excerpt):
        return excerpt

    fact = normalize(item.get("fact", ""))
    marker = "原文内容："
    if marker in fact:
        extracted = fact.split(marker, 1)[1].split("；来源：", 1)[0].strip()
        if is_readable_candidate_content(extracted) and contains_chinese(extracted):
            return extracted
    return "已抓到原文链接，但云端日报不再直接搬运英文片段；等待夜间智能沉淀生成中文读后摘要。"


def contains_chinese(text: str) -> bool:
    return any("\u4e00" <= char <= "\u9fff" for char in text or "")


def is_readable_candidate_content(text: str) -> bool:
    value = normalize(text)
    if len(value) < 60:
        return False
    bad_patterns = [
        "PLATFORMS Autonomous Machines",
        "View All Products GPU TECHNOLOGY CONFERENCE",
        "NVIDIA in Brief Exec Bios",
        "Skip to main content",
    ]
    return not any(pattern.lower() in value.lower() for pattern in bad_patterns)


def has_candidate_content(item: dict) -> bool:
    if item.get("content_summary"):
        return True
    return (
        "原文内容：" in normalize(item.get("fact", ""))
        and contains_chinese(normalize(item.get("fact", "")).split("原文内容：", 1)[1].split("；来源：", 1)[0])
    )


def rank_candidate(item: dict) -> tuple[int, int]:
    return candidate_signal_score(item), item.get("sort_key", 0)


def render_candidate_block(candidates: list[dict]) -> str:
    if not candidates:
        return "- 今天云端已扫描官方来源，但没有发现足够新的候选线索。"

    lines = []
    for index, event in enumerate(candidates, start=1):
        source = f"\n   来源：[打开原文]({event['source_url']})" if event.get("source_url") else ""
        lines.append(
            f"""{index}. 公司：{event["company_name"]}
   标题：{normalize(event["title"])}
   中文摘要：{candidate_content(event)}{source}"""
        )
    return "\n\n".join(lines)


def render_brief(companies: list[dict], events: list[dict], official_candidates: list[dict]) -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    now = datetime.now()
    names = "、".join(company["name"] for company in companies)
    fresh_events = [
        item for item in events
        if is_recent_event(item, now, days=2) and is_publishable_event(item)
    ]
    reviewed_titles = {
        normalize(title).lower()
        for event in events
        for title in [event.get("title", ""), event.get("source_candidate_title", "")]
        if normalize(title)
    }
    fresh_candidates = sorted(
        [
            item for item in official_candidates
            if is_recent_candidate(item, now, days=2)
            and normalize(item.get("title", "")).lower() not in reviewed_titles
        ],
        key=rank_candidate,
        reverse=True,
    )
    readable_candidates = [item for item in fresh_candidates if has_candidate_content(item)]
    top_events = fresh_events[:3]
    top_candidates = readable_candidates[:5]

    if top_events:
        key_changes = []
        for index, event in enumerate(top_events, start=1):
            key_changes.append(
                f"""{index}. 公司：{event["company_name"]}
   事件：{normalize(event["title"])}
   核心内容：{normalize(event["fact"])}
   关键证据：{extract_key_evidence(event)}
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
        candidate_block = render_candidate_block(top_candidates)
    elif top_events:
        candidate_block = "- 今天没有其他值得展开阅读的新内容。"

    if not top_events:
        candidate_block = render_candidate_block(top_candidates)
        if top_candidates:
            tomorrow_focus = "\n".join(
                f"- 优先阅读：{event['company_name']}｜{normalize(event['title'])}"
                for event in top_candidates[:3]
            )
        else:
            tomorrow_focus = "- 继续扫描官方来源中的新增内容\n- 只在读到正文并形成中文摘要后，才进入晨报主体"
            return f"""# 竹鉴日报 | {today}

今日没有新的可读内容。

明日重点：

- 当前覆盖公司：{names}
{tomorrow_focus}
"""
        return f"""# 竹鉴日报 | {today}

今日可读内容：

{candidate_block}

明日重点：

- 当前覆盖公司：{names}
{tomorrow_focus}
"""

    return f"""# 竹鉴日报 | {today}

今日关键变化：

{changes_block}

更多可读线索：

{candidate_block}

下一次验证点：

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
