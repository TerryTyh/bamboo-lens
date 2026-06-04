#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
CONFIG_FILE = ROOT / "config" / "companies.json"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_FILE = OUTPUT_DIR / "daily_brief.md"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
OFFICIAL_CANDIDATES_FILE = OUTPUT_DIR / "official_candidates.json"


def load_companies() -> list[dict]:
    data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return data["companies"]


def load_event_store() -> dict:
    if not EVENT_STORE_FILE.exists():
        return {"companies": {}}
    return json.loads(EVENT_STORE_FILE.read_text(encoding="utf-8"))


def load_official_candidate_payload() -> dict:
    if not OFFICIAL_CANDIDATES_FILE.exists():
        return {"companies": {}}
    return json.loads(OFFICIAL_CANDIDATES_FILE.read_text(encoding="utf-8"))


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
                    "source_url": event.get("source_url", ""),
                    "source_candidate_title": event.get("source_candidate_title", ""),
                    "reviewed_at": event.get("reviewed_at", ""),
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


def flatten_official_candidate_payload(payload: dict, companies: list[dict]) -> list[dict]:
    company_names = {company["id"]: company["name"] for company in companies}
    items = []
    for company_id, candidates in payload.get("companies", {}).items():
        for event in candidates or []:
            items.append(
                {
                    "company_id": company_id,
                    "company_name": event.get("company_name") or company_names.get(company_id, company_id),
                    "title": event.get("title", ""),
                    "date": event.get("date", ""),
                    "fetched_at": event.get("fetched_at", ""),
                    "type": event.get("type", "官方候选"),
                    "fact": event.get("fact", ""),
                    "judgment": event.get("judgment", ""),
                    "action": event.get("action", ""),
                    "priority": event.get("priority", "候选"),
                    "sort_key": event.get("sort_key", 0),
                    "source_url": event.get("source_url", ""),
                    "source_excerpt": event.get("source_excerpt", ""),
                    "source_body": event.get("source_body", ""),
                    "content_summary": event.get("content_summary", []),
                }
            )
    return sorted(items, key=lambda item: item["sort_key"], reverse=True)


def merge_official_candidates(*groups: list[dict]) -> list[dict]:
    merged: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for group in groups:
        for item in group:
            key = (normalize(item.get("company_id", "")), normalize(item.get("title", "")).lower())
            if not key[0] or not key[1] or key in seen:
                continue
            seen.add(key)
            merged.append(item)
    return sorted(merged, key=rank_candidate, reverse=True)


def compact(text: str, limit: int = 82) -> str:
    value = " ".join((text or "").split())
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def normalize(text: str) -> str:
    return " ".join((text or "").split()).strip()


def current_time() -> datetime:
    override = os.environ.get("DAILY_BRIEF_NOW", "").strip()
    if override:
        parsed = datetime.fromisoformat(override)
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=ZoneInfo("Asia/Shanghai"))
        return parsed.astimezone(ZoneInfo("Asia/Shanghai"))
    return datetime.now(ZoneInfo("Asia/Shanghai"))


def localize_brief_terms(text: str) -> str:
    value = normalize(text)

    def replace_usd_billion(match: re.Match[str]) -> str:
        amount = float(match.group(1).replace(",", ""))
        value_in_yi = amount * 10
        if value_in_yi >= 100:
            rendered = f"{value_in_yi:.1f}".rstrip("0").rstrip(".")
        else:
            rendered = f"{value_in_yi:.2f}".rstrip("0").rstrip(".")
        return f"{rendered} 亿美元"

    value = re.sub(r"US\$\s*([0-9][0-9,]*(?:\.[0-9]+)?)\s*billion\b", replace_usd_billion, value, flags=re.I)
    replacements = {
        "GAAP / non-GAAP": "GAAP / non-GAAP",
        "free cash flow": "自由现金流",
        "Data Center": "数据中心",
        "Networking": "网络业务",
        "networking": "网络业务",
        "compute": "计算",
        "revenue": "收入",
        "gross margin": "毛利率",
    }
    for source, target in replacements.items():
        value = value.replace(source, target)
    return value


def extract_sent_brief_signatures(text: str) -> set[str]:
    """Return title/url signatures from the previous committed fallback brief.

    Daily Brief runs do not commit their generated output, but the nightly
    candidate collection does. Reading the checked-in daily_brief.md before
    overwriting it lets us avoid sending the same fallback candidate again on
    consecutive mornings.
    """
    signatures: set[str] = set()
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        match = re.match(r"\d+\.\s+(.+?)｜(.+)", stripped)
        if match:
            company = normalize(match.group(1)).lower()
            title = normalize(match.group(2)).lower()
            if company and title:
                signatures.add(f"title:{company}::{title}")
        for url in re.findall(r"\]\((https?://[^)]+)\)", stripped):
            signatures.add(f"url:{normalize(url).lower()}")
    return signatures


def item_signatures(item: dict) -> set[str]:
    company = normalize(item.get("company_name", "")).lower()
    title = normalize(item.get("title", "")).lower()
    source = normalize(item.get("source_url", "") or item.get("source_doc", "")).lower()
    signatures: set[str] = set()
    if company and title:
        signatures.add(f"title:{company}::{title}")
    if source.startswith("http"):
        signatures.add(f"url:{source}")
    return signatures


def was_sent_before(item: dict, previous_signatures: set[str]) -> bool:
    return bool(item_signatures(item) & previous_signatures)


def research_doc_exists(filename: str) -> bool:
    return (PROJECT_ROOT / "长期高潜力公司跟踪系统" / filename).exists()


def is_completed_research_candidate(item: dict) -> bool:
    company_id = normalize(item.get("company_id", "")).lower()
    title = normalize(item.get("title", ""))
    completed = {
        "naura": research_doc_exists("51-北方华创一页式观察卡_2026-05-28.md"),
        "amec": research_doc_exists("52-中微公司一页式观察卡_2026-05-29.md"),
        "optical_module_compare": research_doc_exists("54-中际旭创与新易盛光模块正式对照卡_2026-05-29.md"),
        "jcet": research_doc_exists("55-长电科技强B复核_2026-05-30.md"),
    }
    if completed["optical_module_compare"] and ("中际旭创" in title or "新易盛" in title or "光模块" in title):
        return True
    if completed["jcet"] and ("长电科技" in title or "强 B 复核" in title or "强B复核" in title or "最小研究包待更新" in title):
        return True
    return completed.get(company_id, False) and "观察卡待建" in title


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
    return localize_brief_terms("；".join(selected))


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
    parsed_reviewed = parse_date_like(item.get("reviewed_at", ""))
    if parsed_reviewed is not None:
        age = today.date() - parsed_reviewed.date()
        if timedelta(days=0) <= age <= timedelta(days=days):
            return True

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


def candidate_signal_base_score(item: dict) -> int:
    text = " ".join(
        normalize(item.get(field, ""))
        for field in ["title", "type", "fact"]
    ).lower()
    score = 0
    keyword_weights = {
        "财报": 5,
        "业绩": 5,
        "收入": 4,
        "毛利率": 4,
        "现金流": 4,
        "年度报告": 5,
        "季度报告": 5,
        "半年度报告": 4,
        "业绩预告": 5,
        "业绩快报": 5,
        "投资者关系活动记录表": 5,
        "投资者关系管理信息": 5,
        "向特定对象发行股票": 5,
        "定增": 4,
        "募集说明书": 4,
        "重大合同": 4,
        "中标": 3,
        "订单": 3,
        "回购": 3,
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
        "sell": 4,
        "share sale": 4,
        "shareholding": 4,
        "block trade": 4,
        "vanguard": 3,
        "vis": 2,
        "gan": 2,
    }
    low_signal = [
        "法律意见书",
        "工作细则",
        "公司章程",
        "独立董事",
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
        "games hit the cloud",
        "geforce now",
        "gaming",
        "007 first light",
        "game ",
        "games ",
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
    return score


def candidate_signal_score(item: dict) -> int:
    score = candidate_signal_base_score(item)
    if has_candidate_content(item):
        score += 8
    else:
        score -= 8
    return score


def candidate_reason(item: dict) -> str:
    text = normalize(item.get("title", "")).lower()
    raw_text = normalize(item.get("title", ""))
    if any(word in raw_text for word in ["投资者关系活动记录表", "投资者关系管理信息"]):
        return "这类问答记录通常会披露订单能见度、客户结构、产品代际和经营质量，是 A 股跟踪池的优先阅读材料。"
    if any(word in raw_text for word in ["年度报告", "季度报告", "半年度报告", "业绩预告", "业绩快报"]):
        return "这类材料直接关系收入、利润率、现金流和经营指引，值得优先读原文。"
    if any(word in raw_text for word in ["向特定对象发行股票", "定增", "募集说明书"]):
        return "这类融资/募投材料可能改变产能、稀释和长期竞争位置，需要读清项目用途和回报路径。"
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
    raw_text = normalize(item.get("title", ""))
    if any(word in raw_text for word in ["投资者关系活动记录表", "投资者关系管理信息"]):
        return "读问答正文，抓客户集中度、订单能见度、800G/1.6T、毛利率、现金流、存货和应收。"
    if any(word in raw_text for word in ["年度报告", "季度报告", "半年度报告", "业绩预告", "业绩快报"]):
        return "提取收入、利润率、现金流、存货、应收和经营指引，再判断是否升级为正式事件。"
    if any(word in raw_text for word in ["向特定对象发行股票", "定增", "募集说明书"]):
        return "核对募投金额、建设周期、产能用途、客户验证和摊薄影响。"
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
        return "\n   ".join(f"{normalize(line)}" for line in content_summary if normalize(line))

    source_text = normalize(item.get("source_body") or item.get("source_excerpt") or "")
    fallback = fallback_chinese_summary(item, source_text)
    if fallback:
        return "\n   ".join(f"{line}" for line in fallback)

    excerpt = normalize(item.get("source_excerpt", ""))
    if is_readable_candidate_content(excerpt) and contains_chinese(excerpt):
        return excerpt

    fact = normalize(item.get("fact", ""))
    marker = "原文内容："
    if marker in fact:
        extracted = fact.split(marker, 1)[1].split("；来源：", 1)[0].strip()
        if is_readable_candidate_content(extracted) and contains_chinese(extracted):
            return extracted
    return "已抓到原文链接，但尚未抓到可引用的正文摘要；先列为待读候选，等读完原文后再升级为正式研判。"


def split_sentences(text: str) -> list[str]:
    value = normalize(text)
    if not value:
        return []
    pieces = re.split(r"(?<=[.!?。！？])\s+", value)
    return [piece.strip() for piece in pieces if len(piece.strip()) >= 45]


def score_sentence(sentence: str) -> int:
    lowered = sentence.lower()
    score = 0
    high_signal = {
        "revenue": 8,
        "net income": 7,
        "eps": 7,
        "gross margin": 7,
        "operating margin": 6,
        "guidance": 6,
        "expects": 5,
        "data center": 6,
        "ai factory": 6,
        "ai factories": 6,
        "nvl72": 6,
        "rubin": 6,
        "spectrum-x": 6,
        "nvlink": 6,
        "cowos": 6,
        "2nm": 6,
        "a13": 5,
        "partnership": 5,
        "customer": 4,
        "openai": 4,
        "microsoft": 4,
        "oracle": 4,
        "backlog": 6,
        "free cash flow": 6,
        "capital": 4,
        "manufacturing": 4,
    }
    low_signal = (
        "cookie",
        "privacy",
        "forward-looking",
        "safe harbor",
        "subscribe",
        "view all products",
        "gpu technology conference",
        "nvidia in brief",
        "copyright",
        "you are now leaving",
    )
    if any(marker in lowered for marker in low_signal):
        return -20
    for keyword, weight in high_signal.items():
        if keyword in lowered:
            score += weight
    if re.search(r"\d", sentence):
        score += 4
    if 70 <= len(sentence) <= 260:
        score += 2
    if len(sentence) > 420:
        score -= 3
    return score


def simple_zh_sentence(sentence: str) -> str:
    """Deterministic fallback when API summaries are unavailable.

    It is intentionally conservative: keep product/customer names intact,
    translate recurring IR language, and avoid inventing facts.
    """
    value = normalize(sentence)
    lowered = value.lower()
    if "at nvidia gtc taipei at computex" in lowered:
        return "NVIDIA 在台北 GTC/COMPUTEX 把主题集中在 AI 工厂、扩展型基础设施、智能体 AI 和物理 AI，继续强调自己要做完整 AI 基础设施平台，而不只是 GPU 供应商。"
    if "jensen huang" in lowered and "taipei" in lowered:
        return "黄仁勋将在台北音乐中心发表主题演讲；这类会议本身不是财务事件，但通常会集中释放 NVIDIA 下一阶段平台、客户和产品路线信息。"
    if "vera rubin nvl72" in lowered and "connect" in lowered:
        return "Vera Rubin NVL72 是机架级 AI 超级计算机，组合 Vera CPU、Rubin GPU、NVLink、ConnectX、Spectrum-X 和 BlueField 等组件，核心卖点是把计算、网络和数据处理做成整机/整架平台。"
    if "vera rubin nvl72" in lowered and ("10x" in lowered or "35x" in lowered):
        return "Vera Rubin NVL72 被描述为可实现最高 10 倍每瓦推理性能、10 倍更低 token 成本，并在特定组合下实现最高 35 倍每瓦吞吐量；这些数字需要后续客户部署验证。"
    if "nvidia and google cloud" in lowered and "100,000" in lowered:
        return "NVIDIA 与 Google Cloud 的联合开发者社区已服务超过 10 万名开发者，说明双方不只是在卖算力实例，也在把开发者、教程、实验环境和部署工具绑定到 NVIDIA 全栈 AI 平台上。"
    if "launched at google i/o" in lowered and "developers" in lowered:
        return "这个社区从上一届 Google I/O 开始推进，目标人群包括开发者、数据科学家和机器学习工程师，核心是降低他们在 Google Cloud 上使用 NVIDIA GPU、模型和工具链的门槛。"
    if "jax" in lowered and "nvidia gpus" in lowered:
        return "双方新增 JAX on NVIDIA GPUs 学习路径和 NVIDIA Dynamo 推理优化实验，重点是帮助开发者在 Google Cloud 上训练和部署 AI 工作负载。"
    if "retrieval-augmented generation" in lowered or "rag" in lowered:
        return "文章还提到开发者已经在 Google Kubernetes Engine 上构建 RAG 应用，并开始做智能体工作负载的可观测性，这说明合作不只是培训入口，也延伸到真实生产部署场景。"
    if "google cloud ai hypercomputer" in lowered or "maxtext" in lowered:
        return "NVIDIA 与 Google Cloud 也在 JAX、MaxText 和 AI Hypercomputer 等框架/基础设施上协作，目标是让从单 GPU 实验到多机架训练的体验更一致。"
    if "nvidia dynamo on gke" in lowered:
        return "NVIDIA Dynamo on GKE 被用于优化大规模推理，尤其是混合专家模型等复杂模型服务，指向推理成本和部署效率，而不只是训练算力。"
    if "first nvidia vera cpus arrived" in lowered:
        return "首批 NVIDIA Vera CPU 已交付给 Anthropic、OpenAI 等头部 AI 实验室，这意味着 Vera 从发布路线图进入客户试用/部署阶段。"
    if "standalone vera cpu" in lowered and "multibillion" in lowered:
        return "独立 Vera CPU 被描述为 NVIDIA 下一项数十亿美元级业务，说明公司希望把 CPU 也纳入 AI 工厂平台，而不只是销售 GPU。"
    if "agentic ai inference" in lowered and "cost per token" in lowered:
        return "Vera Rubin NVL72 面向智能体 AI 推理，目标是把每 token 成本降到更低水平；这对应的是推理侧商业化效率，而不只是训练算力扩张。"
    if "5,000 enterprises" in lowered and "dell ai factories" in lowered:
        return "已有约 5000 家企业在 Dell AI Factory with NVIDIA 上运行 AI 工作负载，用来证明 NVIDIA 的企业 AI 基础设施正在从概念走向规模部署。"
    if "50% faster" in lowered and "3x faster" in lowered and "vera cpu" in lowered:
        return "Vera CPU 的性能口径包括：智能体沙盒运行速度提升约 50%，企业数据查询最高提升约 3 倍；这些数字仍需要后续真实客户案例验证。"
    if "tsmc" in lowered and "consolidated revenue" in lowered:
        return "原文披露了 TSMC 的核心财务数据，包括合并营收、净利润、EPS 等，用于判断先进制程需求是否仍在兑现为收入和利润。"
    if "tsmc" in lowered and "152.0 million common shares" in lowered:
        return "TSMC 计划通过大宗交易出售最多 1.52 亿股 Vanguard International Semiconductor（VIS）普通股，约占 VIS 完全摊薄后股本的 8.1%。"
    if "reduce its shareholding in vis" in lowered:
        return "交易完成后，TSMC 对 VIS 的持股预计从约 27.1% 降至约 19%；公司同时表示近期没有继续出售更多 VIS 股份的计划。"
    if "strategic relations with vis" in lowered:
        return "TSMC 表示出售股份不会影响与 VIS 的战略关系，包括中介层生产外包以及向 VIS 授权 GaN 技术。"
    if "focus its resources on core business activities" in lowered:
        return "公司把这次出售解释为集中资源于核心业务的一部分；这更像是资本配置和资源聚焦动作，而不是业务关系切断。"
    if "gross margin" in lowered and "operating margin" in lowered:
        return "原文给出毛利率、营业利润率和净利率等盈利质量指标，这比单纯收入增长更能说明公司是否仍具备高质量定价能力。"
    if "revenue is expected to be between" in lowered:
        return "原文给出下一季度收入指引区间，这是后续判断需求是否延续的直接验证线。"
    if "shipments of 3-nanometer" in lowered or "advanced technologies" in lowered:
        return "原文拆分了先进制程收入占比，能帮助判断增长是否来自高价值节点，而不是低毛利成熟制程。"
    if "cowos" in lowered and "reticle" in lowered:
        return "原文提到 CoWoS 封装尺寸和产能路线继续扩展，说明 AI 计算扩张的瓶颈不只在晶圆制程，也在先进封装和 HBM 集成能力。"
    if "a13" in lowered and "production" in lowered:
        return "原文介绍 A13 等后续先进制程路线，重点是 2028-2029 年以后的技术储备，而不是短期收入。"

    replacements = [
        ("NVIDIA founder and CEO Jensen Huang", "NVIDIA 创始人兼 CEO 黄仁勋"),
        ("founder and CEO Jensen Huang", "创始人兼 CEO 黄仁勋"),
        ("the company", "公司"),
        ("announced", "宣布"),
        ("today announced", "今日宣布"),
        ("reported", "披露"),
        ("expects", "预计"),
        ("is expected to", "预计将"),
        ("revenue", "收入"),
        ("net income", "净利润"),
        ("diluted earnings per share", "摊薄每股收益"),
        ("earnings per share", "每股收益"),
        ("gross margin", "毛利率"),
        ("operating margin", "营业利润率"),
        ("net profit margin", "净利率"),
        ("year-over-year", "同比"),
        ("from the previous quarter", "环比上一季度"),
        ("increased", "增长"),
        ("decreased", "下降"),
        ("partnership", "合作"),
        ("long-term partnership", "长期合作"),
        ("AI factories", "AI 工厂"),
        ("AI factory", "AI 工厂"),
        ("data centers", "数据中心"),
        ("data center", "数据中心"),
        ("cloud", "云"),
        ("customers", "客户"),
        ("customer", "客户"),
        ("advanced process technologies", "先进制程技术"),
        ("advanced technologies", "先进技术"),
        ("capital expenditures", "资本开支"),
        ("capital expenditure", "资本开支"),
        ("free cash flow", "自由现金流"),
        ("shipments", "出货"),
        ("accounted for", "占比"),
        ("guidance", "指引"),
        ("management expects", "管理层预计"),
        ("production", "量产/生产"),
        ("manufacturing", "制造"),
        ("power efficiency", "能效"),
        ("latency", "延迟"),
        ("throughput", "吞吐量"),
        ("performance", "性能"),
        ("available", "可用/发布"),
        ("will", "将"),
        ("can", "可以"),
    ]
    for source, target in replacements:
        value = re.sub(re.escape(source), target, value, flags=re.IGNORECASE)
    value = value.strip(" .")
    # If the deterministic fallback cannot confidently paraphrase the sentence,
    # do not leak raw English fragments into the Chinese brief.
    if re.search(r"[A-Za-z]{4,}", value):
        return ""
    if not value.endswith(("。", "！", "？")):
        value += "。"
    return f"原文提到，{value}"


def title_brief(item: dict) -> str:
    title = normalize(item.get("title", ""))
    company = normalize(item.get("company_name", ""))
    lowered = title.lower()
    if "financial results" in lowered or "earnings" in lowered or "eps" in lowered:
        return f"{company} 这条是财报/业绩类更新，优先看收入、利润率、指引和现金流，而不是只看标题。"
    if "revenue report" in lowered:
        return f"{company} 这条是月度营收更新，适合用来验证最近一个季度需求是否连续。"
    if "partnership" in lowered or "collaborat" in lowered:
        return f"{company} 这条是合作/客户绑定类更新，重点看合作对象、持续时间、落地场景和是否带来收入路径。"
    if any(word in lowered for word in ("ai", "rubin", "spectrum-x", "nvlink", "gtc", "computex")):
        return f"{company} 这条和 AI 基础设施/平台能力有关，重点看它是否强化公司从单点产品走向系统平台的逻辑。"
    return f"{company} 这条是官方新增内容，下面按原文中更有信息量的句子做中文摘读。"


def fallback_chinese_summary(item: dict, source_text: str) -> list[str]:
    if not is_readable_candidate_content(source_text):
        return []
    if candidate_signal_base_score(item) < 3:
        return []
    sentences = split_sentences(source_text)
    ranked = sorted(sentences, key=score_sentence, reverse=True)
    picked: list[str] = []
    seen = set()
    for sentence in ranked:
        if score_sentence(sentence) <= 0:
            continue
        normalized = normalize(sentence)
        key = normalized[:90].lower()
        if key in seen:
            continue
        seen.add(key)
        paraphrased = simple_zh_sentence(normalized)
        if not paraphrased:
            continue
        picked.append(paraphrased)
        if len(picked) >= 5:
            break
    if len(picked) < 2:
        return []
    return picked


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
    source_text = normalize(item.get("source_body") or item.get("source_excerpt") or "")
    if fallback_chinese_summary(item, source_text):
        return True
    return (
        "原文内容：" in normalize(item.get("fact", ""))
        and contains_chinese(normalize(item.get("fact", "")).split("原文内容：", 1)[1].split("；来源：", 1)[0])
    )


def rank_candidate(item: dict) -> tuple[int, int]:
    return candidate_signal_score(item), item.get("sort_key", 0)


def select_diverse_candidates(candidates: list[dict], limit: int = 5, per_company: int = 2) -> list[dict]:
    picked: list[dict] = []
    company_counts: dict[str, int] = {}
    seen_titles: set[tuple[str, str]] = set()

    for item in candidates:
        company_id = normalize(item.get("company_id", ""))
        title = normalize(item.get("title", "")).lower()
        key = (company_id, title)
        if key in seen_titles:
            continue
        if company_counts.get(company_id, 0) >= per_company:
            continue
        picked.append(item)
        seen_titles.add(key)
        company_counts[company_id] = company_counts.get(company_id, 0) + 1
        if len(picked) >= limit:
            break

    if len(picked) < limit:
        for item in candidates:
            company_id = normalize(item.get("company_id", ""))
            title = normalize(item.get("title", "")).lower()
            key = (company_id, title)
            if key in seen_titles:
                continue
            picked.append(item)
            seen_titles.add(key)
            if len(picked) >= limit:
                break

    return picked


def distinct_company_count(items: list[dict]) -> int:
    return len({normalize(item.get("company_id", "")) for item in items if normalize(item.get("company_id", ""))})


def render_candidate_block(candidates: list[dict]) -> str:
    if not candidates:
        return "- 今天云端已扫描官方来源，但没有发现足够新的候选线索。"

    lines = []
    for index, event in enumerate(candidates, start=1):
        source = f"\n   [原文]({event['source_url']})" if event.get("source_url") else ""
        date = normalize(event.get("date", ""))
        date_prefix = f"{date}。" if date else ""
        content = candidate_content(event)
        lines.append(
            f"""{index}. {event["company_name"]}｜{normalize(event["title"])}
   {date_prefix}{content}{source}"""
        )
    return "\n\n".join(lines)


def parse_research_doc_filename(path: Path) -> dict | None:
    match = re.match(r"(?P<index>\d+)-(?P<title>.+)_(?P<date>\d{4}-\d{2}-\d{2})\.md$", path.name)
    if not match:
        return None
    title = match.group("title")
    date = match.group("date")
    if (
        "一页式观察卡" not in title
        and "候选扩池" not in title
        and "最小研究包" not in title
        and "对照卡" not in title
        and "复核" not in title
        and "准备" not in title
    ):
        return None
    display_title = title.replace("一页式观察卡", "一页式观察卡").replace("A股", "A 股")
    return {
        "title": display_title,
        "date": date,
        "path": path,
        "portal_doc": f"./docs/research/{path.name}",
    }


def load_recent_research_artifacts(today: datetime, days: int = 1) -> list[dict]:
    research_dir = PROJECT_ROOT / "长期高潜力公司跟踪系统"
    if not research_dir.exists():
        return []
    items: list[dict] = []
    for path in research_dir.glob("*.md"):
        parsed = parse_research_doc_filename(path)
        if not parsed:
            continue
        parsed_date = parse_date_like(parsed["date"])
        if parsed_date is None:
            continue
        age = today.date() - parsed_date.date()
        if timedelta(days=0) <= age <= timedelta(days=days):
            items.append(parsed)
    if any("光模块正式对照卡" in item["title"] for item in items):
        items = [
            item for item in items
            if "光模块对照卡准备" not in item["title"]
        ]
    return sorted(items, key=lambda item: (item["date"], item["title"]), reverse=True)


def render_research_artifacts_block(items: list[dict]) -> str:
    lines = []
    for index, item in enumerate(items, start=1):
        title = normalize(item["title"])
        if "北方华创" in title:
            note = "A 股半导体设备平台观察卡已完成，结论是 B 层观察、不追价，下一步等 2026H1/Q2 验证收入、毛利率、合同负债、存货和现金流。"
        elif "中微公司" in title:
            note = "A 股半导体设备对照观察卡已完成，结论是 B 层观察、不追价，下一步等 2026H1/Q2 验证扣非利润、经营现金流、薄膜设备放量和营运资本。"
        elif "长电科技" in title:
            note = "A 股先进封装强 B 复核已完成，结论是维持强 B、不升 A；下一步等 2026H1/Q2 验证长电微亏损、先进封装毛利率、经营现金流和 capex 回报。"
        elif "中际旭创" in title or "新易盛" in title or "光模块" in title:
            if "正式" in title:
                note = "A 股 AI 光模块正式对照卡已完成，结论是中际旭创 B+ 观察、新易盛 B 观察；下一步等 2026H1/Q2 验证客户集中、800G/1.6T、毛利率、现金流、应收和存货。"
            else:
                note = "A 股 AI 光模块对照卡准备稿已完成，下一步补客户集中度、800G/1.6T 占比、毛利率、经营现金流、存货和应收，决定是否推进正式对照卡。"
        elif "A 股候选扩池" in title or "A股候选扩池" in title:
            note = "A 股候选池扩充记录已完成，用来把日报重点从单一 NVIDIA 线索扩到半导体设备、先进封装、AI 光模块和 PCB/服务器链条。"
        else:
            note = "新增研究文档已沉淀到门户，后续按文档里的验证点继续推进。"
        lines.append(
            f"""{index}. 研究成果｜{title}
   {note}
   [原文]({item["portal_doc"]})"""
        )
    return "\n\n".join(lines)


def has_same_day_reviewed_event(events: list[dict], today: datetime) -> bool:
    for event in events:
        parsed_reviewed = parse_date_like(event.get("reviewed_at", ""))
        if parsed_reviewed is not None and parsed_reviewed.date() == today.date():
            return True
    return False


def render_brief(
    companies: list[dict],
    events: list[dict],
    official_candidates: list[dict],
    previous_brief_text: str = "",
) -> str:
    now = current_time()
    today = now.strftime("%Y-%m-%d")
    names = "、".join(company["name"] for company in companies)
    previous_signatures = extract_sent_brief_signatures(previous_brief_text)
    fresh_events = [
        item for item in events
        if is_recent_event(item, now, days=2)
        and is_publishable_event(item)
        and not was_sent_before(item, previous_signatures)
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
            if is_recent_candidate(item, now, days=5)
            and normalize(item.get("title", "")).lower() not in reviewed_titles
            and not was_sent_before(item, previous_signatures)
            and not is_completed_research_candidate(item)
        ],
        key=rank_candidate,
        reverse=True,
    )
    wider_candidates = sorted(
        [
            item for item in official_candidates
            if is_recent_candidate(item, now, days=10)
            and normalize(item.get("title", "")).lower() not in reviewed_titles
            and not was_sent_before(item, previous_signatures)
            and not is_completed_research_candidate(item)
        ],
        key=rank_candidate,
        reverse=True,
    )
    readable_candidates = [item for item in fresh_candidates if has_candidate_content(item)]
    wider_readable_candidates = [item for item in wider_candidates if has_candidate_content(item)]
    top_events = fresh_events[:3]
    top_candidates = select_diverse_candidates(readable_candidates, limit=5, per_company=2)
    if distinct_company_count(top_candidates) < 2 and distinct_company_count(wider_readable_candidates) >= 2:
        top_candidates = select_diverse_candidates(wider_readable_candidates, limit=5, per_company=2)
    fallback_candidates = select_diverse_candidates(
        [item for item in wider_candidates if candidate_signal_base_score(item) >= 3],
        limit=5,
        per_company=2,
    )
    research_artifacts = load_recent_research_artifacts(now)

    if research_artifacts and not has_same_day_reviewed_event(top_events, now):
        candidate_block = render_candidate_block(top_candidates)
        next_candidate_block = (
            f"\n\n下一步候选：\n\n{candidate_block}\n"
            if top_candidates
            else ""
        )
        return f"""# 竹鉴日报 | {today}

今日研究成果：

{render_research_artifacts_block(research_artifacts)}{next_candidate_block}

明日重点：

- 准备下一轮 A 股候选发现，优先补 PCB/服务器、电力设备、半导体材料和国产软件链条。
- 只在 2026H1/Q2 数据出来后复核北方华创、中微公司、中际旭创/新易盛和长电科技。
- 候选只作为研究待办，不直接形成买卖动作。
"""

    if top_events:
        key_changes = []
        for index, event in enumerate(top_events, start=1):
            source = f"\n   [原文]({event['source_url']})" if event.get("source_url") else ""
            key_changes.append(
                f"""{index}. 公司：{event["company_name"]}
   事件：{localize_brief_terms(event["title"])}
   核心内容：{localize_brief_terms(event["fact"])}
   关键证据：{extract_key_evidence(event)}
   为什么重要：{localize_brief_terms(event["judgment"])}
   动作：{localize_brief_terms(event["action"])}{source}"""
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
        if research_artifacts:
            next_candidate_block = (
                f"\n\n下一步候选：\n\n{candidate_block}\n"
                if top_candidates
                else ""
            )
            return f"""# 竹鉴日报 | {today}

今日研究成果：

{render_research_artifacts_block(research_artifacts)}{next_candidate_block}

明日重点：

- 准备下一轮 A 股候选发现，优先补 PCB/服务器、电力设备、半导体材料和国产软件链条。
- 只在 2026H1/Q2 数据出来后复核北方华创、中微公司、中际旭创/新易盛和长电科技。
- 候选只作为研究待办，不直接形成买卖动作。
"""
        if top_candidates:
            tomorrow_focus = "\n".join(
                f"- 优先阅读：{event['company_name']}｜{normalize(event['title'])}"
                for event in top_candidates[:3]
            )
        else:
            tomorrow_focus = "- 继续扫描官方来源中的新增内容\n- 只在读到正文并形成中文摘要后，才进入晨报主体"
            if fallback_candidates:
                candidate_block = render_candidate_block(fallback_candidates)
                tomorrow_focus = "\n".join(
                    f"- 优先打开原文：{event['company_name']}｜{normalize(event['title'])}"
                    for event in fallback_candidates[:3]
                )
                return f"""# 竹鉴日报 | {today}

今日没有新的可读内容。

今日待读候选：

{candidate_block}

明日重点：

- 当前覆盖公司：{names}
{tomorrow_focus}
"""
            return f"""# 竹鉴日报 | {today}

今日没有新的可读内容。

明日重点：

- 当前覆盖公司：{names}
{tomorrow_focus}
"""
        return f"""# 竹鉴日报 | {today}

{candidate_block}
"""

    return f"""# 竹鉴日报 | {today}

今日关键变化：

{changes_block}

其他可读线索：

{candidate_block}

后续观察：

{next_check}
"""


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ignore_previous = os.environ.get("IGNORE_PREVIOUS_BRIEF_SIGNATURES", "").strip().lower() == "true"
    previous_brief_text = "" if ignore_previous else (OUTPUT_FILE.read_text(encoding="utf-8") if OUTPUT_FILE.exists() else "")
    companies = load_companies()
    event_store = load_event_store()
    official_candidate_payload = load_official_candidate_payload()
    events = flatten_events(event_store)
    official_candidates = merge_official_candidates(
        flatten_official_candidates(event_store),
        flatten_official_candidate_payload(official_candidate_payload, companies),
    )
    brief = render_brief(companies, events, official_candidates, previous_brief_text)
    OUTPUT_FILE.write_text(brief, encoding="utf-8")
    print(f"Daily brief written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
