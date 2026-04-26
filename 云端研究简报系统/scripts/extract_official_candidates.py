#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import urllib.parse
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "outputs" / "snapshots"
MANIFEST_FILE = SNAPSHOT_DIR / "manifest.json"
OUTPUT_FILE = ROOT / "outputs" / "official_candidates.json"

DATE_REGEX = re.compile(r"(20\d{2}[-/年.]\d{1,2}(?:[-/月.]\d{1,2})?)")
EN_DATE_REGEX = re.compile(r"((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s+20\d{2})", re.IGNORECASE)
NOISE_PATTERNS = (
    "cookie",
    "privacy",
    "investor relations",
    "javascript",
    "learn more",
    "read more",
    "default.aspx",
    "skip to main content",
    "financial statements",
    "segment revenue",
    "segment results",
    "earnings and financials",
    "acquisition history",
    "support for ai marketplace apps",
    "educator training and development",
    "reports",
    "news and resources",
    "corporate governance",
    "culture and values",
    "esg ",
    "esg reports hub",
    "esg ratings and awards",
    "esg news and views",
    "modern slavery act",
    "transparency in coverage",
    "sustainability report",
    "supply chain management",
    "nuclear preservation",
    "nuclear license renewal",
)


class CandidateHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.stack: list[str] = []
        self.text_nodes: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
            return
        if tag in self.stack:
            self.stack.reverse()
            self.stack.remove(tag)
            self.stack.reverse()

    def handle_data(self, data: str) -> None:
        text = normalize_text(data)
        if not text:
            return
        tag = self.stack[-1] if self.stack else "text"
        self.text_nodes.append((tag, text))


def normalize_text(text: str) -> str:
    return " ".join((text or "").replace("\xa0", " ").split()).strip()


def load_manifest() -> list[dict]:
    if not MANIFEST_FILE.exists():
        return []
    return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))


def clean_candidate(text: str) -> str:
    value = normalize_text(text)
    value = re.sub(r"\s+[|｜-]\s+.*$", "", value)
    value = re.sub(r"^var\s+[A-Za-z0-9_]+\s*=\s*.*$", "", value)
    return value.strip(" -|｜:：")


def parse_date(value: str) -> tuple[str, int]:
    match = DATE_REGEX.search(value or "")
    if match:
        raw = match.group(1)
        normalized = (
            raw.replace("年", "-")
            .replace("月", "-")
            .replace("日", "")
            .replace("/", "-")
            .replace(".", "-")
        )
        parts = [part for part in normalized.split("-") if part]
        if len(parts) == 2:
            parts.append("01")
        if len(parts) == 3:
            try:
                sort_key = int(datetime.strptime("-".join(parts), "%Y-%m-%d").strftime("%Y%m%d"))
                return "-".join(parts), sort_key
            except ValueError:
                pass

    en_match = EN_DATE_REGEX.search(value or "")
    if en_match:
        raw = en_match.group(1)
        normalized = raw.replace("Sept", "Sep")
        try:
            parsed = datetime.strptime(normalized, "%b %d, %Y")
            return parsed.strftime("%Y-%m-%d"), int(parsed.strftime("%Y%m%d"))
        except ValueError:
            try:
                parsed = datetime.strptime(normalized, "%B %d, %Y")
                return parsed.strftime("%Y-%m-%d"), int(parsed.strftime("%Y%m%d"))
            except ValueError:
                return raw, 0

    return "", 0


def score_candidate(tag: str, text: str) -> int:
    value = text.lower()
    score = 0
    if tag in {"title", "h1", "h2", "h3", "a"}:
        score += 4
    if DATE_REGEX.search(text):
        score += 4
    if any(keyword in value for keyword in ("results", "earnings", "reports", "announces", "revenue", "quarter", "financial", "guidance")):
        score += 3
    if any(keyword in value for keyword in ("ai", "cloud", "data center", "acquisition", "partnership", "conference")):
        score += 2
    if len(text) < 18 or len(text) > 180:
        score -= 2
    if any(noise in value for noise in NOISE_PATTERNS):
        score -= 5
    return score


def parse_text_nodes(html: str) -> list[tuple[str, str]]:
    if "<html" not in html.lower() and "Markdown Content:" in html:
        text_nodes = []
        for line in html.splitlines():
            text = normalize_text(line)
            if not text:
                continue
            text_nodes.append(("text", text))
        return text_nodes

    parser = CandidateHTMLParser()
    parser.feed(html)
    return parser.text_nodes


def parse_json_payload(raw: str) -> dict | None:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return None
    return payload if isinstance(payload, dict) else None


def nearest_date(text_nodes: list[tuple[str, str]], index: int, window: int = 6) -> tuple[str, int]:
    left = max(0, index - window)
    right = min(len(text_nodes), index + window + 1)
    for cursor in range(index, left - 1, -1):
        date_text, sort_key = parse_date(text_nodes[cursor][1])
        if sort_key:
            return date_text, sort_key
    for cursor in range(index + 1, right):
        date_text, sort_key = parse_date(text_nodes[cursor][1])
        if sort_key:
            return date_text, sort_key
    return "", 0


def build_items_from_nodes(text_nodes: list[tuple[str, str]], min_score: int = 4) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    for index, (tag, text) in enumerate(text_nodes):
        title = clean_candidate(text)
        if not title:
            continue
        if "@" in title or title.count("/") > 3:
            continue
        key = title.lower()
        if key in seen:
            continue
        seen.add(key)

        score = score_candidate(tag, title)
        if score < min_score:
            continue

        date_text, sort_key = parse_date(title)
        if not sort_key:
            date_text, sort_key = nearest_date(text_nodes, index)
        items.append(
            {
                "title": title,
                "date": date_text,
                "sort_key": sort_key,
                "tag": tag,
                "score": score,
            }
        )
    return items


def dedupe_items(items: list[dict], limit: int = 8) -> list[dict]:
    picked: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for item in sorted(items, key=lambda row: (row["sort_key"], row["score"]), reverse=True):
        key = (item["title"].lower(), item["date"])
        if key in seen:
            continue
        seen.add(key)
        picked.append(item)
        if len(picked) >= limit:
            break
    return picked


def extract_tsmc_candidates(text_nodes: list[tuple[str, str]], url: str) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if any(keyword in item["title"].lower() for keyword in ("revenue", "eps", "board", "quarter", "results"))
    ]
    if "quarterly-results" in url:
        focused = [
            item
            for item in items
            if any(keyword in item["title"].lower() for keyword in ("results", "eps", "conference", "quarter"))
        ]
    return dedupe_items(focused or items)


def extract_tsmc_candidates_from_markdown(text: str) -> list[dict]:
    items: list[dict] = []

    list_pattern = re.compile(r"\*\s+\[(20\d{2}/\d{2}/\d{2})\s+##\s+([^\]]+)\]\(([^)]+)\)")
    for date_text, title, _url in list_pattern.findall(text):
        parsed_date, sort_key = parse_date(date_text)
        if not sort_key:
            continue
        items.append(
            {
                "title": clean_candidate(title),
                "date": parsed_date,
                "sort_key": sort_key,
                "tag": "markdown",
                "score": 9,
            }
        )

    heading_pattern = re.compile(r"^#\s+(TSMC .*?)$", re.MULTILINE)
    for title in heading_pattern.findall(text):
        if any(keyword in title.lower() for keyword in ("latest news", "monthly revenue")):
            continue
        items.append(
            {
                "title": clean_candidate(title),
                "date": "",
                "sort_key": 0,
                "tag": "markdown",
                "score": 5,
            }
        )

    return dedupe_items(items)


def extract_nvidia_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if any(keyword in item["title"].lower() for keyword in ("financial", "results", "nvidia", "ai", "platform", "partner", "expands", "fusion"))
    ]
    return dedupe_items(focused or items)


def extract_microsoft_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in ("microsoft", "azure", "ai", "copilot", "cloud", "earnings", "results", "announces")
        )
    ]
    return dedupe_items(focused)


def extract_alibaba_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in ("alibaba", "cloud", "ai", "results", "earnings", "quarter", "repurchase", "qwen")
        )
    ]
    return dedupe_items(focused)


def extract_gevernova_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in ("ge vernova", "orders", "results", "earnings", "grid", "power", "acquisition")
        )
    ]
    return dedupe_items(focused)


def extract_constellation_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in ("constellation", "results", "earnings", "nuclear", "power", "calpine", "agreement")
        )
    ]
    return dedupe_items(focused)


def extract_constellation_investor_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=2)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in (
                "earnings release",
                "earnings webcast",
                "earnings call",
                "conference call",
                "annual meeting",
                "business and earnings outlook",
                "results",
                "quarter",
                "financial",
                "presentation",
            )
        )
    ]
    return dedupe_items(focused)


def extract_constellation_investor_markdown(raw: str) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    raw = raw.replace("\r\n", "\n")

    event_pattern = re.compile(
        r"\n([A-Z][^\n]{8,140}?(?:Earnings Conference Call|Annual Meeting of Shareholders|Business and Earnings Outlook Conference Call))\n\s*\n\s*([A-Z][a-z]{2,8}\s+\d{1,2},\s+20\d{2})",
        re.MULTILINE,
    )
    for title, date_source in event_pattern.findall(raw):
        title = clean_candidate(title)
        lowered = title.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        date_text, sort_key = parse_date(date_source)
        items.append(
            {
                "title": title,
                "date": date_text,
                "sort_key": sort_key,
                "tag": "markdown",
                "score": 9,
            }
        )

    calendar_pattern = re.compile(r"https://www\.google\.com/calendar/render\?([^\s)]+)")
    for query_string in calendar_pattern.findall(raw):
        params = urllib.parse.parse_qs(query_string)
        title = clean_candidate(urllib.parse.unquote(params.get("text", [""])[0]))
        dates = urllib.parse.unquote(params.get("dates", [""])[0])
        lowered = title.lower()
        if lowered in seen or not title:
            continue
        if not any(
            keyword in lowered
            for keyword in (
                "earnings conference call",
                "annual meeting of shareholders",
                "business and earnings outlook conference",
            )
        ):
            continue
        seen.add(lowered)
        date_text, sort_key = parse_date(dates)
        items.append(
            {
                "title": title.replace("Constellation Energy Corporation - ", "").strip(),
                "date": date_text,
                "sort_key": sort_key,
                "tag": "markdown",
                "score": 8,
            }
        )

    link_pattern = re.compile(r"\*\s+\[([^\]]+)\]\((https?://[^)]+)\)")
    for title, url in link_pattern.findall(raw):
        title = clean_candidate(title)
        lowered = title.lower()
        if lowered in seen:
            continue
        if not any(
            keyword in lowered
            for keyword in (
                "earnings release and tables",
                "business and earnings outlook presentation",
                "proxy statement",
                "10k annual report",
                "announcement presentation",
                "investor presentation",
            )
        ):
            continue
        seen.add(lowered)
        date_text, sort_key = parse_date(title)
        items.append(
            {
                "title": title,
                "date": date_text,
                "sort_key": sort_key,
                "tag": "markdown",
                "score": 8,
                "source_url": url,
            }
        )

    return dedupe_items(items)


def extract_luxshare_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=3)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in ("report", "annual", "quarter", "financial", "results", "summary")
        )
    ]
    return dedupe_items(focused)


def extract_inovance_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=3)
    focused = [
        item
        for item in items
        if item["sort_key"]
        and any(
            keyword in item["title"].lower()
            for keyword in ("inovance", "automation", "launch", "solution", "exhibition", "report", "results")
        )
    ]
    return dedupe_items(focused)


def extract_inovance_candidates_from_json(payload: dict, url: str) -> list[dict]:
    items: list[dict] = []

    if "/api/product/launch/listPage" in url:
        for row in payload.get("rows", []) or []:
            title = clean_candidate(row.get("name", ""))
            date_text, sort_key = parse_date(str(row.get("launchDate", "")))
            if not title or not sort_key:
                continue
            items.append(
                {
                    "title": title,
                    "date": date_text,
                    "sort_key": sort_key,
                    "tag": "json",
                    "score": 8,
                }
            )

    if "/api/home/search" in url:
        for row in ((payload.get("data") or {}).get("news") or []):
            title = clean_candidate(row.get("newsTitle", ""))
            if not title:
                continue
            lowered = title.lower()
            if any(noise in lowered for noise in ("招标公示", "项目招标", "集采项目", "普通家具")):
                continue
            if not any(
                keyword in title
                for keyword in ("新品", "发布会", "机器人", "价格调整", "自动化", "央视", "战略合作")
            ):
                continue
            date_text, sort_key = parse_date(str(row.get("createTime") or row.get("beginDate") or ""))
            if not sort_key:
                continue
            items.append(
                {
                    "title": title,
                    "date": date_text,
                    "sort_key": sort_key,
                    "tag": "json",
                    "score": 7,
                }
            )

    return dedupe_items(items)


def extract_luxshare_candidates_from_html(html: str) -> list[dict]:
    items: list[dict] = []
    patterns = [
        re.compile(
            r"<p>\s*(20\d{2}-\d{2}-\d{2})\s*</p>[\s\S]{0,300}?<p class=\"mod_tit(?:24|36)\">([^<]+)</p>",
            re.IGNORECASE,
        ),
    ]
    for pattern in patterns:
        for date_text, title in pattern.findall(html):
            parsed_date, sort_key = parse_date(date_text)
            if not sort_key:
                continue
            items.append(
                {
                    "title": clean_candidate(title),
                    "date": parsed_date,
                    "sort_key": sort_key,
                    "tag": "html",
                    "score": 8,
                }
            )
    return dedupe_items(items)


def extract_constellation_candidates_from_html(html: str) -> list[dict]:
    items: list[dict] = []
    pattern = re.compile(
        r"<p class=\"mb-2 ce-label text-disabled\">([^<]+)</p>[\s\S]{0,260}?<p class=\"mb-(?:0|3) [^\"]*?ce-header-1[^\"]*?\">([^<]+)</p>",
        re.IGNORECASE,
    )
    for date_text, title in pattern.findall(html):
        parsed_date, sort_key = parse_date(date_text)
        if not sort_key:
            continue
        items.append(
            {
                "title": clean_candidate(title),
                "date": parsed_date,
                "sort_key": sort_key,
                "tag": "html",
                "score": 7,
            }
        )
    return dedupe_items(items)


def extract_candidates_from_html(html: str, company_id: str, url: str) -> list[dict]:
    payload = parse_json_payload(html)
    if payload and company_id == "inovance":
        return extract_inovance_candidates_from_json(payload, url)

    if company_id == "tsmc" and "Markdown Content:" in html:
        return extract_tsmc_candidates_from_markdown(html)
    if company_id == "constellation" and "Markdown Content:" in html and "investors.constellationenergy.com" in url:
        return extract_constellation_investor_markdown(html)

    text_nodes = parse_text_nodes(html)

    if company_id == "tsmc":
        return extract_tsmc_candidates(text_nodes, url)
    if company_id == "nvidia":
        return extract_nvidia_candidates(text_nodes)
    if company_id == "microsoft":
        return extract_microsoft_candidates(text_nodes)
    if company_id == "alibaba":
        return extract_alibaba_candidates(text_nodes)
    if company_id == "gevernova":
        return extract_gevernova_candidates(text_nodes)
    if company_id == "constellation":
        if "investors.constellationenergy.com" in url:
            return extract_constellation_investor_candidates(text_nodes)
        return extract_constellation_candidates_from_html(html) or extract_constellation_candidates(text_nodes)
    if company_id == "luxshare":
        return extract_luxshare_candidates_from_html(html) or extract_luxshare_candidates(text_nodes)
    if company_id == "inovance":
        return extract_inovance_candidates(text_nodes)

    return dedupe_items(build_items_from_nodes(text_nodes))


def summarize_title(title: str, url: str) -> str:
    value = title.strip()
    if len(value) > 120:
        value = value[:117].rstrip() + "..."
    return f"官方来源抓到候选更新：{value}（来源：{url}）"


def candidate_fact(title: str, date_text: str, url: str) -> str:
    parts = []
    if date_text:
        parts.append(f"日期：{date_text}")
    parts.append(f"标题：{title}")
    parts.append(f"来源：{url}")
    return "；".join(parts)


def build_payload() -> dict:
    manifest = load_manifest()
    grouped: dict[str, list[dict]] = defaultdict(list)

    for row in manifest:
        if row.get("status") != "ok":
            continue
        file_path = row.get("file")
        if not file_path:
            continue
        path = Path(file_path)
        if not path.exists():
            continue

        html = path.read_text(encoding="utf-8", errors="ignore")
        candidates = extract_candidates_from_html(html, row["company_id"], row["url"])
        for item in candidates:
            fallback_key = re.sub(r"\D", "", row.get("fetched_at", "")[:8]) or "0"
            grouped[row["company_id"]].append(
                {
                    "title": item["title"],
                    "date": item["date"] or row.get("fetched_at", "")[:10],
                    "fetched_at": row.get("fetched_at", ""),
                    "type": "官方候选",
                    "fact": candidate_fact(item["title"], item["date"] or row.get("fetched_at", "")[:10], row["url"]),
                    "judgment": "这是云端从官方页面自动抓到的候选更新，需进一步研判后再升级为正式研究事件。",
                    "action": "加入待研判队列",
                    "priority": "候选",
                    "sort_key": item["sort_key"] or int(fallback_key),
                    "source_url": row["url"],
                    "source_file": str(path),
                }
            )

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "companies": grouped,
    }


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(len(items) for items in payload["companies"].values())
    print(f"Official candidates written to: {OUTPUT_FILE} ({total} items)")


if __name__ == "__main__":
    main()
