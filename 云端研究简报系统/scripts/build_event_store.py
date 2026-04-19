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


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    official_candidates = load_official_candidates()
    payload = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "companies": {},
    }

    for company in load_companies():
        company_id = company["id"]
        payload["companies"][company_id] = {
            "name": company["name"],
            "market": company["market"],
            "tier": company["tier"],
            "theme": company["theme"],
            "events": parse_company_events(company_id),
            "official_candidates": official_candidates.get("companies", {}).get(company_id, []),
        }

    EVENT_STORE_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Event store written to: {EVENT_STORE_FILE}")


if __name__ == "__main__":
    main()
