#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
CANDIDATES_FILE = OUTPUT_DIR / "official_candidates.json"
MORNING_BRIEF_FILE = OUTPUT_DIR / "morning_brief.md"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


def parse_date(value: str) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%Y%m%d-%H%M%S"):
        try:
            return datetime.strptime(value[: len(fmt)], fmt)
        except ValueError:
            continue
    return None


def is_recent(item: dict, now: datetime, days: int = 2) -> bool:
    parsed = parse_date(item.get("date", "")) or parse_date(item.get("fetched_at", ""))
    if parsed is None:
        return False
    age = now.date() - parsed.date()
    return timedelta(days=0) <= age <= timedelta(days=days)


def score(item: dict) -> tuple[int, int]:
    text = f"{item.get('title', '')} {item.get('type', '')}".lower()
    value = 0
    for keyword, weight in {
        "revenue": 8,
        "earnings": 8,
        "results": 8,
        "guidance": 7,
        "annual report": 6,
        "20-f": 6,
        "partnership": 5,
        "collaboration": 5,
        "manufacturing": 4,
        "infrastructure": 4,
        "ai": 3,
    }.items():
        if keyword in text:
            value += weight
    if "geforce" in text or "gaming" in text:
        value -= 8
    return value, int(item.get("sort_key") or 0)


def load_candidates() -> list[dict]:
    if not CANDIDATES_FILE.exists():
        return []
    payload = json.loads(CANDIDATES_FILE.read_text(encoding="utf-8"))
    items = []
    for company_id, records in (payload.get("companies") or {}).items():
        for item in records:
            summary = [normalize(line) for line in item.get("content_summary", []) if normalize(line)]
            if not summary:
                continue
            items.append(
                {
                    **item,
                    "company_id": company_id,
                    "content_summary": summary,
                }
            )
    return items


def company_name(company_id: str) -> str:
    names = {
        "nvidia": "NVIDIA",
        "tsmc": "TSMC",
        "microsoft": "Microsoft",
        "alibaba": "阿里巴巴",
        "inovance": "汇川技术",
        "luxshare": "立讯精密",
        "gevernova": "GE Vernova",
        "constellation": "Constellation Energy",
    }
    return names.get(company_id, company_id)


def reading_focus(item: dict) -> list[str]:
    title = normalize(item.get("title", ""))
    raw_text = f"{title} {' '.join(item.get('content_summary', []))}"
    text = raw_text.lower()
    company = company_name(item.get("company_id", ""))
    if any(token in text for token in ("partnership", "collaboration", "strategic")) or any(
        token in raw_text for token in ("合作", "客户", "订单", "部署", "产能")
    ):
        return [
            f"这类合作对 {company} 是否重要，取决于它能否带来真实客户绑定、产品默认入口、部署规模或收入路径。",
            "如果原文没有披露金额、期限、产能、订单或客户落地范围，就先把它当作业务线索，而不是直接当作估值变化。",
        ]
    if any(token in text for token in ("revenue", "earnings", "results", "eps")) or any(
        token in raw_text for token in ("营收", "收入", "净利润", "毛利率", "现金流", "股利", "分红", "资本支出")
    ):
        return [
            f"这类内容对 {company} 的价值在于验证经营质量：收入增速、利润率、现金流、资本开支和下一季指引要一起看。",
            "如果只有收入或 EPS 变动，而没有利润率、现金流和管理层口径，就先不要急着更新估值结论。",
        ]
    if "ai" in text or "infrastructure" in text or "agent" in text:
        return [
            f"这类内容更像 {company} 业务边界或平台能力的信号，关键是它能否从技术叙事转成客户采用、收入或粘性。",
            "阅读时不要只看“AI”字样，要看客户是谁、场景是什么、是否进入生产环境、是否有商业化路径。",
        ]
    return [
        f"先把这条内容作为 {company} 的业务变化线索阅读，重点找原文里有没有客户、订单、金额、产能或管理层量化口径。",
        "如果没有可量化信息，就只进入观察池，不直接改变估值或仓位动作。",
    ]


def verification_points(item: dict) -> list[str]:
    title = normalize(item.get("title", "")).lower()
    if "revenue" in title or "earnings" in title or "results" in title:
        return [
            "下一份正式披露里收入和利润率是否延续同方向变化。",
            "现金流、资本开支或库存等质量指标是否支持表面增长。",
        ]
    if "partnership" in title or "collaboration" in title:
        return [
            "合作是否披露金额、期限、产能、客户或部署节奏。",
            "后续财报或电话会是否把合作转成可量化收入路径。",
        ]
    return [
        "是否出现更多客户、订单、部署规模或管理层量化口径。",
        "这条线索是否会反复出现在后续正式披露中，而不是一次性新闻。",
    ]


def render_item(index: int, item: dict) -> str:
    summary = "\n".join(f"- {line}" for line in item["content_summary"][:6])
    focus = "\n".join(f"- {line}" for line in reading_focus(item))
    verification = "\n".join(f"- {line}" for line in verification_points(item))
    source = normalize(item.get("source_url", ""))
    source_line = f"\n\n[打开原文]({source})" if source else ""
    return f"""## {index}. {company_name(item.get("company_id", ""))}｜{normalize(item.get("title", ""))}

**原文摘要**

{summary}

**读这条时重点看**

{focus}

**后续观察点**

{verification}{source_line}
"""


def main() -> None:
    now = datetime.now(ZoneInfo("Asia/Shanghai"))
    today = now.strftime("%Y-%m-%d")
    candidates = [
        item for item in load_candidates()
        if is_recent(item, now, days=2)
    ]
    selected = sorted(candidates, key=score, reverse=True)[:5]
    if not selected:
        print("No enriched same-day/recent candidates; morning brief not updated.")
        return

    body = "\n".join(render_item(index, item) for index, item in enumerate(selected, start=1))
    MORNING_BRIEF_FILE.write_text(
        f"""# 竹鉴晨报 | {today}

今日值得读的内容：

{body}
""",
        encoding="utf-8",
    )
    print(f"Morning brief written to: {MORNING_BRIEF_FILE} ({len(selected)} items)")


if __name__ == "__main__":
    main()
