#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
RESEARCH_ROOT = PROJECT_ROOT / "长期高潜力公司跟踪系统"
CONFIG_FILE = ROOT / "config" / "companies.json"
OUTPUT_DIR = ROOT / "outputs"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
OFFICIAL_CANDIDATES_FILE = OUTPUT_DIR / "official_candidates.json"

SOURCE_DOC_MAP = {
    "nvidia": "28-NVIDIA动态更新样例V1.md",
    "tsmc": "25-TSMC动态更新样例V1.md",
    "microsoft": "24-Microsoft动态更新样例V1.md",
    "alibaba": "20-阿里巴巴动态更新样例V1.md",
    "inovance": "23-汇川技术动态更新样例V1.md",
    "gevernova": "26-GE Vernova动态更新样例V1.md",
    "luxshare": "18-立讯精密动态更新样例V1.md",
    "constellation": "27-Constellation Energy动态更新样例V1.md",
}

BLOCK_REGEX = re.compile(
    r"### 动态 \d+：([^\n]+)\n\n"
    r"- 日期：([^\n]+)\n"
    r"- 事件类型：([^\n]+)\n"
    r"- 事实：\n([\s\S]*?)\n"
    r"- 判断：\n([\s\S]*?)\n"
    r"- 动作：\n\s*`?([^`\n]+)`?\n"
    r"- 优先级：\n\s*`?([^`\n]+)`?",
    re.MULTILINE,
)


def load_companies() -> list[dict]:
    return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))["companies"]


def load_official_candidates() -> dict:
    if not OFFICIAL_CANDIDATES_FILE.exists():
        return {"companies": {}}
    return json.loads(OFFICIAL_CANDIDATES_FILE.read_text(encoding="utf-8"))


def clean(text: str) -> str:
    return (text or "").replace("`", "").replace("\r", "").strip()


def parse_sort_key(date_text: str) -> int:
    matches = re.findall(r"\d{4}-\d{2}(?:-\d{2})?", date_text or "")
    if not matches:
        return 0

    values = []
    for item in matches:
        if len(item) == 7:
            item = f"{item}-01"
        try:
            values.append(int(datetime.strptime(item, "%Y-%m-%d").strftime("%Y%m%d")))
        except ValueError:
            continue
    return max(values) if values else 0


def parse_company_events(company_id: str) -> list[dict]:
    doc_name = SOURCE_DOC_MAP.get(company_id)
    if not doc_name:
        return []

    source_path = RESEARCH_ROOT / doc_name
    if not source_path.exists():
        return []

    markdown = source_path.read_text(encoding="utf-8")
    events = []
    for match in BLOCK_REGEX.finditer(markdown):
        title, date_text, event_type, fact, judgment, action, priority = match.groups()
        events.append(
            {
                "title": clean(title),
                "date": clean(date_text),
                "fetched_at": "",
                "type": clean(event_type),
                "fact": clean(fact),
                "judgment": clean(judgment),
                "action": clean(action),
                "priority": clean(priority),
                "sort_key": parse_sort_key(date_text),
                "source_doc": str(source_path),
            }
        )
    return events


def promote_tsmc_candidates(candidates: list[dict]) -> list[dict]:
    promoted: list[dict] = []
    for item in candidates:
        title = clean(item.get("title", ""))
        date_text = clean(item.get("date", ""))
        source_url = item.get("source_url", "")
        source_file = item.get("source_file", "")
        lower = title.lower()

        event_type = ""
        fact = ""
        judgment = ""
        action = ""
        priority = ""

        if "reports first quarter eps" in lower:
            event_type = "财报"
            fact = f"TSMC 在 {date_text} 发布 2026 年第一季度业绩，标题显示第一季度 EPS 为 NT$22.08。来源：{source_url}"
            judgment = "这是 TSMC 最关键的季度经营更新之一，通常会直接影响市场对先进制程需求、盈利能力和资本开支回报的判断。"
            action = "提升优先级"
            priority = "P1"
        elif "revenue report" in lower:
            month_label = title.replace("TSMC ", "").replace(" Revenue Report", "")
            event_type = "月度营收"
            fact = f"TSMC 在 {date_text} 发布《{month_label} Revenue Report》，说明月度营收已有新增官方披露。来源：{source_url}"
            judgment = "月度营收报告能帮助我们更快验证 AI、HPC 与先进制程需求是否仍在延续，是季度财报之间最有价值的高频跟踪点之一。"
            action = "继续跟踪"
            priority = "P2"
        elif "board of directors meeting resolutions" in lower:
            event_type = "资本配置"
            fact = f"TSMC 在 {date_text} 披露董事会决议相关更新。来源：{source_url}"
            judgment = "董事会决议往往涉及资本开支、股东回报或重要治理动作，对评估资本配置质量很有参考意义。"
            action = "继续跟踪"
            priority = "P2"
        elif "annual report" in lower or "form 20-f" in lower:
            event_type = "年报"
            fact = f"TSMC 在 {date_text} 提交 2025 年 Form 20-F 年报文件。来源：{source_url}"
            judgment = "年报文件更适合沉淀长期研究底稿，短期交易价值次于季度业绩和月度营收，但对补全风险、治理和资本配置细节很重要。"
            action = "维持原判断"
            priority = "P3"

        if not event_type:
            continue

        promoted.append(
            {
                "title": title,
                "date": date_text,
                "fetched_at": "",
                "type": event_type,
                "fact": fact,
                "judgment": judgment,
                "action": action,
                "priority": priority,
                "sort_key": parse_sort_key(date_text) or item.get("sort_key", 0),
                "source_doc": source_file or source_url,
            }
        )

    return promoted


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    official_candidates = load_official_candidates()
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "companies": {},
    }

    for company in load_companies():
        company_id = company["id"]
        company_candidates = official_candidates.get("companies", {}).get(company_id, [])
        events = parse_company_events(company_id)
        if company_id == "tsmc":
            events.extend(promote_tsmc_candidates(company_candidates))
            events = sorted(events, key=lambda row: row.get("sort_key", 0), reverse=True)
        payload["companies"][company_id] = {
            "name": company["name"],
            "market": company["market"],
            "tier": company["tier"],
            "theme": company["theme"],
            "events": events,
            "official_candidates": company_candidates,
        }

    EVENT_STORE_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Event store written to: {EVENT_STORE_FILE}")


if __name__ == "__main__":
    main()
