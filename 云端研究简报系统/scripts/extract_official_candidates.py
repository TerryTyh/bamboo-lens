#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "outputs" / "snapshots"
MANIFEST_FILE = SNAPSHOT_DIR / "manifest.json"
OUTPUT_FILE = ROOT / "outputs" / "official_candidates.json"

DATE_REGEX = re.compile(r"(20\d{2}[-/年.]\d{1,2}(?:[-/月.]\d{1,2})?)")
NOISE_PATTERNS = (
    "cookie",
    "privacy",
    "investor relations",
    "javascript",
    "learn more",
    "read more",
    "default.aspx",
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
    return value.strip(" -|｜:：")


def parse_date(value: str) -> tuple[str, int]:
    match = DATE_REGEX.search(value or "")
    if not match:
        return "", 0

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
    if len(parts) != 3:
        return raw, 0

    try:
        sort_key = int(datetime.strptime("-".join(parts), "%Y-%m-%d").strftime("%Y%m%d"))
    except ValueError:
        return raw, 0
    return "-".join(parts), sort_key


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


def extract_candidates_from_html(html: str) -> list[dict]:
    parser = CandidateHTMLParser()
    parser.feed(html)

    items: list[dict] = []
    seen: set[str] = set()
    for tag, text in parser.text_nodes:
        title = clean_candidate(text)
        if not title:
            continue
        key = title.lower()
        if key in seen:
            continue
        seen.add(key)

        score = score_candidate(tag, title)
        if score < 4:
            continue

        date_text, sort_key = parse_date(title)
        items.append(
            {
                "title": title,
                "date": date_text,
                "sort_key": sort_key,
                "tag": tag,
                "score": score,
            }
        )

    items.sort(key=lambda item: (item["sort_key"], item["score"]), reverse=True)
    return items[:8]


def summarize_title(title: str, url: str) -> str:
    value = title.strip()
    if len(value) > 120:
        value = value[:117].rstrip() + "..."
    return f"官方来源抓到候选更新：{value}（来源：{url}）"


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
        candidates = extract_candidates_from_html(html)
        for item in candidates:
            fallback_key = re.sub(r"\D", "", row.get("fetched_at", "")[:8]) or "0"
            grouped[row["company_id"]].append(
                {
                    "title": item["title"],
                    "date": item["date"] or row.get("fetched_at", "")[:10],
                    "type": "官方候选",
                    "fact": summarize_title(item["title"], row["url"]),
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
