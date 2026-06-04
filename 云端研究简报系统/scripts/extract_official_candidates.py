#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime
import html as html_lib
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "outputs" / "snapshots"
MANIFEST_FILE = SNAPSHOT_DIR / "manifest.json"
OUTPUT_FILE = ROOT / "outputs" / "official_candidates.json"

DATE_REGEX = re.compile(r"(20\d{2}[-/年.]\d{1,2}(?:[-/月.]\d{1,2})?)")
COMPACT_DATE_REGEX = re.compile(r"\b(20\d{2})(\d{2})(\d{2})T?\d*")
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
CN_INVESTMENT_KEYWORDS = (
    "投资者关系活动记录表",
    "投资者关系管理信息",
    "业绩说明会",
    "年度报告",
    "季度报告",
    "半年度报告",
    "业绩预告",
    "业绩快报",
    "向特定对象发行股票",
    "定增",
    "募集说明书",
    "募集资金",
    "重大合同",
    "日常经营重大合同",
    "中标",
    "订单",
    "回购",
)
CN_WAITING_MATERIAL_KEYWORDS = (
    "关于召开",
    "业绩说明会的公告",
    "股东大会通知",
)
CN_LOW_SIGNAL_PATTERNS = (
    "公告包括",
    "承诺报告内容真实可靠",
    "定期报告",
    "临时公告",
    "法律意见书",
    "工作细则",
    "公司章程",
    "独立董事",
    "董事会",
    "监事会",
    "审计委员会",
    "提名委员会",
    "战略委员会",
    "薪酬与考核委员会",
    "股权激励",
    "限制性股票归属",
    "作废部分",
    "工商变更",
    "工商登记",
    "营业执照",
    "权益分派实施公告",
    "非经营性资金占用",
    "专项意见",
    "内部控制",
)
CN_GENERIC_CANDIDATE_TITLES = {"年度报告", "半年度报告", "季度报告", "业绩预告", "业绩快报", "临时公告", "定期报告"}
CN_ANNOUNCEMENT_COMPANIES = {"jcet", "naura", "amec", "innolight", "eoptolink", "shennan", "wus", "fii"}
BAD_EXCERPT_PATTERNS = (
    "PLATFORMS Autonomous Machines",
    "View All Products GPU TECHNOLOGY CONFERENCE",
    "NVIDIA in Brief Exec Bios",
    "Skip to main content",
)

A_SHARE_SEED_CANDIDATES = {
    "jcet": [
        {
            "title": "长电科技最小研究包待更新：验证长电微亏损、先进封装毛利率与经营现金流",
            "date": "2026-05-27",
            "source_url": "https://www.jcetglobal.com/cn/site/news",
            "source_excerpt": "研究池种子候选：长电科技已完成强 B 层最小研究包，下一步应读取 2025 年报、2026Q1 和投资者关系材料，验证先进封装收入含金量、长电微亏损是否收窄、毛利率与经营现金流是否改善。",
        }
    ],
    "naura": [
        {
            "title": "北方华创一页式观察卡待建：半导体设备平台化、订单质量与现金流验证",
            "date": "2026-05-27",
            "source_url": "https://www.naura.com/list/8.html",
            "source_excerpt": "研究池种子候选：北方华创用于补前道半导体设备国产化拼图。第一步读取 2025 年报、2026Q1、订单/合同负债、毛利率和现金流，判断增长是否由真实设备需求支撑。",
        }
    ],
    "amec": [
        {
            "title": "中微公司一页式观察卡待建：刻蚀设备、MOCVD 与先进制程设备国产化",
            "date": "2026-05-27",
            "source_url": "https://www.amec-inc.com/investor",
            "source_excerpt": "研究池种子候选：中微公司用于和北方华创形成设备侧对照。第一步读取 2025 年报、2026Q1、研发投入、新产品进展和毛利率，验证刻蚀设备份额和先进制程设备兑现度。",
        }
    ],
    "innolight": [
        {
            "title": "中际旭创一页式观察卡待建：AI 光模块、800G/1.6T 与客户集中度验证",
            "date": "2026-05-27",
            "source_url": "https://www.innolight.com/inv2.aspx",
            "source_excerpt": "研究池种子候选：中际旭创用于补 AI capex 向光模块链条传导的验证点。第一步读取 2025 年报、2026Q1、客户集中度、800G/1.6T 产品代际和现金流，判断高增长质量。",
        }
    ],
}


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


def clean_html_text(raw: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", raw or "", flags=re.IGNORECASE)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    return normalize_text(html_lib.unescape(text))


def clean_markdown_text(raw: str) -> str:
    text = raw or ""
    if "Markdown Content:" in text:
        text = text.split("Markdown Content:", 1)[1]
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[*-]\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\|", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    lines = []
    for line in text.splitlines():
        value = normalize_text(line)
        lowered = value.lower()
        if len(value) < 35:
            continue
        if any(
            noise in lowered
            for noise in (
                "skip to main content",
                "dedicated ic foundry",
                "contact public relations",
                "related information",
                "cookie",
                "privacy",
                "document center",
                "tsmc-online",
            )
        ):
            continue
        lines.append(value)
        if len(" ".join(lines)) >= 5000:
            break
    return normalize_text(" ".join(lines))


def first_match(pattern: str, text: str, flags: int = re.IGNORECASE) -> str:
    match = re.search(pattern, text or "", flags)
    return match.group(1).strip() if match else ""


def trim_excerpt(text: str, limit: int = 420) -> str:
    value = normalize_text(text)
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip(" ，,。;；") + "…"


def is_readable_excerpt(text: str) -> bool:
    value = normalize_text(text)
    if len(value) < 60:
        return False
    return not any(pattern.lower() in value.lower() for pattern in BAD_EXCERPT_PATTERNS)


def fetch_url_text(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        return ""
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 BambooLensResearchBot/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
    )
    def _read(target_url: str) -> str:
        req = urllib.request.Request(target_url, headers=dict(request.header_items()))
        with urllib.request.urlopen(req, timeout=18) as response:
            raw = response.read(1_000_000)
            charset = response.headers.get_content_charset() or "utf-8"
            return raw.decode(charset, errors="ignore")

    def _proxy_url(target_url: str) -> str:
        return f"https://r.jina.ai/http://{target_url.replace('https://', '').replace('http://', '')}"

    def _looks_like_article(raw_html: str) -> bool:
        if not raw_html:
            return False
        if "Markdown Content:" in raw_html:
            return len(clean_markdown_text(raw_html)) >= 180
        paragraphs = extract_article_paragraphs(raw_html)
        if len(paragraphs) >= 2:
            return True
        cleaned = clean_html_text(raw_html)
        if any(pattern.lower() in cleaned.lower() for pattern in BAD_EXCERPT_PATTERNS):
            return False
        return len(cleaned) >= 600 and bool(re.search(r"\b(revenue|earnings|announc|partnership|customer|ai|data center|capital|margin)\b", cleaned, re.I))

    try:
        direct = _read(url)
        if _looks_like_article(direct):
            return direct
    except Exception:
        direct = ""

    try:
        return _read(_proxy_url(url))
    except Exception:
        return direct or ""


def extract_meta_description(html: str) -> str:
    patterns = [
        r'<meta\s+name=["\']description["\'][^>]*content=["\']([^"\']+)["\']',
        r'<meta\s+property=["\']og:description["\'][^>]*content=["\']([^"\']+)["\']',
        r'<meta\s+content=["\']([^"\']+)["\'][^>]*(?:name|property)=["\'](?:description|og:description)["\']',
    ]
    for pattern in patterns:
        value = first_match(pattern, html)
        if value:
            return clean_html_text(value)
    return ""


def extract_article_paragraphs(html: str) -> list[str]:
    if not html:
        return []
    paragraphs = []
    for match in re.findall(r"<p[^>]*>([\s\S]*?)</p>", html, flags=re.IGNORECASE):
        text = clean_html_text(match)
        lowered = text.lower()
        if len(text) < 45:
            continue
        if any(noise in lowered for noise in ("cookie", "privacy", "forward-looking", "safe harbor", "subscribe")):
            continue
        paragraphs.append(text)
        if len(paragraphs) >= 12:
            break
    return paragraphs


def extract_article_excerpt(html: str) -> str:
    if not html:
        return ""
    if "Markdown Content:" in html or not re.search(r"<p[\s>]", html, flags=re.IGNORECASE):
        excerpt = trim_excerpt(clean_markdown_text(html))
        return excerpt if is_readable_excerpt(excerpt) else ""
    meta = extract_meta_description(html)
    paragraphs = extract_article_paragraphs(html)
    excerpt = trim_excerpt(" ".join(paragraphs[:3]) or meta)
    return excerpt if is_readable_excerpt(excerpt) else ""


def extract_article_body(html: str) -> str:
    if "Markdown Content:" in html or not re.search(r"<p[\s>]", html or "", flags=re.IGNORECASE):
        body = clean_markdown_text(html)
        return body if is_readable_excerpt(body) else ""
    body = normalize_text(" ".join(extract_article_paragraphs(html)))
    return body if is_readable_excerpt(body) else ""


def load_manifest() -> list[dict]:
    if not MANIFEST_FILE.exists():
        return []
    return json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))


def load_existing_payload() -> dict:
    if not OUTPUT_FILE.exists():
        return {"generated_at": "", "companies": {}}
    try:
        payload = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"generated_at": "", "companies": {}}
    return payload if isinstance(payload, dict) else {"generated_at": "", "companies": {}}


def count_candidates(payload: dict) -> int:
    return sum(len(items) for items in (payload.get("companies") or {}).values())


def merge_candidate_payloads(base: dict, extra: dict) -> dict:
    merged = {
        "generated_at": extra.get("generated_at") or datetime.now().isoformat(timespec="seconds"),
        "companies": {company: list(items or []) for company, items in (base.get("companies") or {}).items()},
    }
    for company_id, items in (extra.get("companies") or {}).items():
        target = merged["companies"].setdefault(company_id, [])
        seen = {normalize_text(item.get("title", "")).lower() for item in target}
        for item in items or []:
            title = normalize_text(item.get("title", "")).lower()
            if title and title not in seen:
                target.append(item)
                seen.add(title)
    return merged


def clean_candidate(text: str) -> str:
    value = normalize_text(text)
    value = re.sub(r"\s+[|｜-]\s+.*$", "", value)
    value = re.sub(r"^var\s+[A-Za-z0-9_]+\s*=\s*.*$", "", value)
    return value.strip(" -|｜:：")


def parse_date(value: str) -> tuple[str, int]:
    compact_match = COMPACT_DATE_REGEX.search(value or "")
    if compact_match:
        year, month, day = compact_match.groups()
        try:
            parsed = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d"), int(parsed.strftime("%Y%m%d"))
        except ValueError:
            pass

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
    if any(keyword in text for keyword in CN_INVESTMENT_KEYWORDS):
        score += 5
    if any(keyword in text for keyword in CN_WAITING_MATERIAL_KEYWORDS):
        score += 2
    if len(text) < 18 or len(text) > 180:
        score -= 2
    if any(noise in value for noise in NOISE_PATTERNS):
        score -= 5
    if any(noise in text for noise in CN_LOW_SIGNAL_PATTERNS):
        score -= 8
    if text.strip() in CN_GENERIC_CANDIDATE_TITLES:
        score -= 8
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


def extract_cn_announcement_candidates(text_nodes: list[tuple[str, str]]) -> list[dict]:
    items = build_items_from_nodes(text_nodes, min_score=5)
    focused = [
        item
        for item in items
        if any(keyword in item["title"] for keyword in CN_INVESTMENT_KEYWORDS + CN_WAITING_MATERIAL_KEYWORDS)
        and not any(noise in item["title"] for noise in CN_LOW_SIGNAL_PATTERNS)
        and item["title"].strip() not in CN_GENERIC_CANDIDATE_TITLES
    ]
    return dedupe_items(focused or items)


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
    for date_text, title, source_url in list_pattern.findall(text):
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
                "source_url": source_url,
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


def extract_nvidia_candidates_from_html(html: str, url: str) -> list[dict]:
    items: list[dict] = []
    blocks = re.findall(r"<article\b[\s\S]*?</article>", html, flags=re.IGNORECASE)
    for block in blocks:
        title_html = first_match(r'<h[23][^>]*class=["\'][^"\']*(?:title)[^"\']*["\'][^>]*>([\s\S]*?)</h[23]>', block)
        href = first_match(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>', title_html or block)
        title = clean_candidate(clean_html_text(title_html))
        if not title:
            continue
        lowered = title.lower()
        if any(noise in lowered for noise in NOISE_PATTERNS):
            continue

        date_source = first_match(r'<div[^>]*class=["\'][^"\']*date[^"\']*["\'][^>]*>([\s\S]*?)</div>', block)
        date_text, sort_key = parse_date(clean_html_text(date_source))
        source_url = urllib.parse.urljoin(url, html_lib.unescape(href)) if href else url

        description = first_match(
            r'<div[^>]*class=["\'][^"\']*(?:description|summary|dek)[^"\']*["\'][^>]*>([\s\S]*?)</div>',
            block,
        )
        excerpt = clean_html_text(description)
        source_body = ""
        if source_url != url:
            detail_html = fetch_url_text(source_url)
            if not excerpt:
                excerpt = extract_article_excerpt(detail_html)
            source_body = extract_article_body(detail_html)

        items.append(
            {
                "title": title,
                "date": date_text,
                "sort_key": sort_key,
                "tag": "html-card",
                "score": score_candidate("a", title) + (2 if excerpt else 0),
                "source_url": source_url,
                "source_excerpt": trim_excerpt(excerpt) if is_readable_excerpt(excerpt) else "",
                "source_body": source_body,
            }
        )
    return dedupe_items(items)


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
        title = normalize_text(urllib.parse.unquote(params.get("text", [""])[0]))
        title = title.replace("Constellation Energy Corporation - ", "").strip()
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
                "title": title,
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
    block_pattern = re.compile(r"<li\b[\s\S]*?</li>", re.IGNORECASE)
    for block in block_pattern.findall(html):
        href = first_match(r'<a[^>]+href=["\']([^"\']+)["\']', block)
        date_text = first_match(r"<p>\s*(20\d{2}-\d{2}-\d{2})\s*</p>", block)
        title = first_match(r'<p class=["\']mod_tit(?:24|36)["\']>([^<]+)</p>', block)
        parsed_date, sort_key = parse_date(date_text)
        title = clean_candidate(title)
        if not title or not sort_key:
            continue
        source_url = urllib.parse.urljoin("https://www.luxshare-ict.com/en/news/release.html", html_lib.unescape(href)) if href else ""
        items.append(
            {
                "title": title,
                "date": parsed_date,
                "sort_key": sort_key,
                "tag": "html",
                "score": 8,
                "source_url": source_url,
            }
        )
    return dedupe_items(items)


def extract_constellation_candidates_from_html(html: str) -> list[dict]:
    items: list[dict] = []
    block_pattern = re.compile(r'<div class=["\']ce-spotlight__card[\s\S]*?</div>\s*</div>', re.IGNORECASE)
    for block in block_pattern.findall(html):
        date_text = first_match(r'<p class=["\']mb-2 ce-label text-disabled["\']>([^<]+)</p>', block)
        title = first_match(r'<p class=["\']mb-(?:0|3) [^"\']*?ce-header-1[^"\']*?["\']>([^<]+)</p>', block)
        excerpt = first_match(r'<p class=["\']mb-0[^"\']*["\']>([\s\S]*?)</p>', block)
        parsed_date, sort_key = parse_date(date_text)
        title = clean_candidate(clean_html_text(title))
        if not sort_key:
            continue
        items.append(
            {
                "title": title,
                "date": parsed_date,
                "sort_key": sort_key,
                "tag": "html",
                "score": 7 + (2 if excerpt else 0),
                "source_excerpt": trim_excerpt(clean_html_text(excerpt)),
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
        return extract_nvidia_candidates_from_html(html, url) or extract_nvidia_candidates(text_nodes)
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
    if company_id in CN_ANNOUNCEMENT_COMPANIES:
        return extract_cn_announcement_candidates(text_nodes)

    return dedupe_items(build_items_from_nodes(text_nodes))


def summarize_title(title: str, url: str) -> str:
    value = title.strip()
    if len(value) > 120:
        value = value[:117].rstrip() + "..."
    return f"官方来源抓到候选更新：{value}（来源：{url}）"


def candidate_fact(title: str, date_text: str, url: str, excerpt: str = "") -> str:
    parts = []
    if date_text:
        parts.append(f"日期：{date_text}")
    parts.append(f"标题：{title}")
    if excerpt:
        parts.append(f"原文内容：{excerpt}")
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
            source_url = item.get("source_url") or row["url"]
            source_excerpt = item.get("source_excerpt", "")
            source_body = item.get("source_body", "")
            if not source_excerpt and source_url != row["url"]:
                detail_html = fetch_url_text(source_url)
                source_excerpt = extract_article_excerpt(detail_html)
                source_body = extract_article_body(detail_html)
            if not is_readable_excerpt(source_excerpt):
                source_excerpt = ""
            grouped[row["company_id"]].append(
                {
                    "title": item["title"],
                    "date": item["date"] or row.get("fetched_at", "")[:10],
                    "fetched_at": row.get("fetched_at", ""),
                    "type": "官方候选",
                    "fact": candidate_fact(
                        item["title"],
                        item["date"] or row.get("fetched_at", "")[:10],
                        source_url,
                        source_excerpt,
                    ),
                    "judgment": "这是云端从官方页面自动抓到的候选更新，需进一步研判后再升级为正式研究事件。",
                    "action": "加入待研判队列",
                    "priority": "候选",
                    "sort_key": item["sort_key"] or int(fallback_key),
                    "source_url": source_url,
                    "source_excerpt": source_excerpt,
                    "source_body": source_body,
                    "source_file": str(path),
                }
            )

    for company_id, seeds in A_SHARE_SEED_CANDIDATES.items():
        existing_titles = {normalize_text(item.get("title", "")).lower() for item in grouped.get(company_id, [])}
        for seed in seeds:
            title = seed["title"]
            if normalize_text(title).lower() in existing_titles:
                continue
            date_text, sort_key = parse_date(seed["date"])
            grouped[company_id].append(
                {
                    "title": title,
                    "date": date_text,
                    "fetched_at": datetime.now().strftime("%Y%m%d-%H%M%S"),
                    "type": "研究池种子候选",
                    "fact": candidate_fact(title, date_text, seed["source_url"], seed["source_excerpt"]),
                    "judgment": "这是为扩充 A 股研究池补入的种子候选，只代表下一步研究待办；必须读取年报、季报、公告或投资者关系材料后，才可升级为正式事件。",
                    "action": "加入 A 股扩池待研判队列",
                    "priority": "候选",
                    "sort_key": sort_key,
                    "source_url": seed["source_url"],
                    "source_excerpt": seed["source_excerpt"],
                    "source_body": seed["source_excerpt"],
                    "source_file": "",
                }
            )

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "companies": grouped,
    }


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    previous_payload = load_existing_payload()
    payload = build_payload()
    total = count_candidates(payload)
    previous_total = count_candidates(previous_payload)

    if total == 0 and previous_total > 0:
        print(
            "Official candidate extraction produced 0 items; "
            f"kept previous candidate file with {previous_total} items."
        )
        return
    if 0 < total < previous_total:
        payload = merge_candidate_payloads(previous_payload, payload)
        total = count_candidates(payload)
        print(
            "Official candidate extraction produced fewer items than previous run; "
            f"merged new seed candidates into previous candidate file ({total} items)."
        )

    OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Official candidates written to: {OUTPUT_FILE} ({total} items)")


if __name__ == "__main__":
    main()
