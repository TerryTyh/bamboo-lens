#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
DECISION_QUEUE_FILE = OUTPUT_DIR / "decision_queue.json"
EVENT_STORE_FILE = OUTPUT_DIR / "event_store.json"
REVIEWED_EVENTS_FILE = OUTPUT_DIR / "reviewed_events.json"
DRAFT_DIR = OUTPUT_DIR / "review_drafts"
INDEX_FILE = OUTPUT_DIR / "review_draft_index.json"
BATCH_PLAN_FILE = OUTPUT_DIR / "review_batch_plan.json"
PORTAL_DOC_DIR = PROJECT_ROOT / "研究门户" / "docs" / "review-drafts"
PORTAL_DATA_FILE = PROJECT_ROOT / "研究门户" / "review-draft-data.js"

MAX_DRAFTS = 16
MIN_SCORE = 6
SOURCE_PREVIEW_CHARS = 2600
CURRENT_DATE_KEY = int(datetime.now().strftime("%Y%m%d"))
MONTH_NAMES = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

LOW_SIGNAL_KEYWORDS = [
    "geforce now",
    "games hit the cloud",
    "gaijin",
    "gaming",
    "protecting the planet",
    "national robotics week",
    "rainforests",
    "recycling plants",
]


def load_json(path: Path, fallback: dict) -> dict:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def clean(text: object) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip()


def slugify(text: str) -> str:
    slug = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]+", "-", text).strip("-").lower()
    return slug[:96] or "review-draft"


def candidate_key(company: str, title: str) -> str:
    normalized = re.sub(r"\s+", " ", title).strip().lower()
    return f"{company}::{normalized}"


def normalize_url(url: str) -> str:
    normalized = re.sub(r"#.*$", "", clean(url)).rstrip("/")
    normalized = re.sub(r"^https?://", "", normalized, flags=re.I)
    return normalized.lower()


def source_lookup(event_store: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for company_id, company in event_store.get("companies", {}).items():
        for candidate in company.get("official_candidates", []):
            title = clean(candidate.get("title"))
            if title:
                lookup[candidate_key(company_id, title)] = candidate
    return lookup


def reviewed_lookup(reviewed_events: dict) -> dict[str, dict[str, set[str]]]:
    lookup: dict[str, dict[str, set[str]]] = {}
    for company_id, events in reviewed_events.get("companies", {}).items():
        company_lookup = {
            "source_titles": set(),
            "titles": set(),
            "source_urls": set(),
        }
        for event in events:
            source_title = clean(event.get("source_candidate_title"))
            title = clean(event.get("title"))
            source_url = normalize_url(event.get("source_url", ""))
            if source_title:
                company_lookup["source_titles"].add(source_title.lower())
            if title:
                company_lookup["titles"].add(title.lower())
            if source_url:
                company_lookup["source_urls"].add(source_url)
        lookup[company_id] = company_lookup
    return lookup


def month_revenue_key(title: str) -> int:
    lowered = clean(title).lower()
    if "revenue report" not in lowered:
        return 0
    year_match = re.search(r"\b(20\d{2})\b", lowered)
    if not year_match:
        return 0
    month = 0
    for month_name, month_num in MONTH_NAMES.items():
        if month_name in lowered:
            month = month_num
            break
    if not month:
        return 0
    return int(year_match.group(1)) * 100 + month


def formal_coverage_lookup(queue: dict, reviewed_events: dict) -> dict[str, dict[str, object]]:
    lookup: dict[str, dict[str, object]] = {}

    def ensure_company(company_id: str) -> dict[str, object]:
        return lookup.setdefault(
            company_id,
            {
                "formal_dates": {},
                "latest_month_revenue": 0,
            },
        )

    for item in queue.get("items", []):
        if item.get("source_type") != "formal_event":
            continue
        company = item.get("company", "")
        date = clean(item.get("date"))
        event_type = clean(item.get("type") or item.get("title"))
        if not company or not date:
            continue
        company_lookup = ensure_company(company)
        formal_dates = company_lookup["formal_dates"]
        formal_dates.setdefault(date, []).append(event_type)

    for company, events in reviewed_events.get("companies", {}).items():
        company_lookup = ensure_company(company)
        formal_dates = company_lookup["formal_dates"]
        for event in events:
            date = clean(event.get("date"))
            if date:
                formal_dates.setdefault(date, []).append(clean(event.get("type") or event.get("title")))
            monthly_key = month_revenue_key(event.get("source_candidate_title") or event.get("title") or "")
            if monthly_key:
                company_lookup["latest_month_revenue"] = max(int(company_lookup["latest_month_revenue"]), monthly_key)

    return lookup


def covered_by_existing_event(
    candidate: dict,
    event_candidate: dict,
    reviewed: dict[str, dict[str, set[str]]],
    formal_coverage: dict[str, dict[str, object]],
) -> str:
    company = candidate.get("company", "")
    company_lookup = reviewed.get(company)

    title = clean(candidate.get("title"))
    source_title = clean(event_candidate.get("title") or candidate.get("title"))
    source_url = normalize_url(candidate.get("source_url") or event_candidate.get("source_url", ""))

    if company_lookup:
        if source_title.lower() in company_lookup["source_titles"] or title.lower() in company_lookup["source_titles"]:
            return "同一官方候选标题已经进入正式事件"
        if title.lower() in company_lookup["titles"]:
            return "同一事件标题已经进入正式事件"
        if source_url and source_url in company_lookup["source_urls"]:
            return "同一官方来源链接已经进入正式事件"

    coverage = formal_coverage.get(company, {})
    date = clean(candidate.get("date") or event_candidate.get("date"))
    event_type = infer_event_type(title)
    formal_types = coverage.get("formal_dates", {}).get(date, []) if coverage else []
    if "财报" in event_type and any("财报" in item or "q1" in item.lower() or "q2" in item.lower() for item in formal_types):
        return "同一日期的财报深读已经进入正式事件或公司主页"

    candidate_month = month_revenue_key(title)
    latest_month = int(coverage.get("latest_month_revenue", 0) or 0) if coverage else 0
    if candidate_month and latest_month and candidate_month < latest_month:
        return "较早月份营收已被更新月份营收事件覆盖"
    return ""


def select_candidates(queue: dict) -> list[dict]:
    items = [
        item
        for item in queue.get("items", [])
        if item.get("source_type") == "official_candidate" and int(item.get("score") or 0) >= MIN_SCORE
    ]
    return sorted(items, key=lambda row: (int(row.get("score") or 0), int(row.get("sort_key") or 0)), reverse=True)[
        :MAX_DRAFTS
    ]


def should_build_draft(candidate: dict, event_candidate: dict) -> bool:
    title = clean(candidate.get("title"))
    lowered = title.lower()
    if any(keyword in lowered for keyword in LOW_SIGNAL_KEYWORDS):
        return False

    score = int(candidate.get("score") or 0)
    sort_key = int(candidate.get("sort_key") or 0)
    has_body = bool(clean(event_candidate.get("source_body") or event_candidate.get("source_excerpt")))
    is_meeting = any(word in lowered for word in ["conference call", "annual meeting", "webcast"])

    if is_meeting and not has_body:
        # 日程类候选只保留近端验证点，避免历史会议标题大量挤占草稿台。
        return sort_key >= CURRENT_DATE_KEY - 14

    return score >= MIN_SCORE


def is_low_substance_annual_notice(event_type: str, readable_source: str) -> bool:
    if "年报" not in event_type:
        return False
    lowered = readable_source.lower()
    notice_markers = [
        "filed its 2025 annual report",
        "filed annual report",
        "form 20-f",
        "report is available at",
        "hard copies of the report",
    ]
    if not any(marker in lowered for marker in notice_markers):
        return False
    substantive_markers = [
        "revenue increased",
        "gross margin",
        "operating margin",
        "capital expenditures",
        "cash flow",
        "segment",
    ]
    return not any(marker in lowered for marker in substantive_markers)


def source_text(candidate: dict, event_candidate: dict) -> str:
    body = clean(event_candidate.get("source_body"))
    excerpt = clean(event_candidate.get("source_excerpt"))
    fact = clean(event_candidate.get("fact"))
    if body:
        return body
    if excerpt:
        return excerpt
    if fact:
        return fact
    return clean(candidate.get("why"))


def clip_source(text: str) -> str:
    if len(text) <= SOURCE_PREVIEW_CHARS:
        return text
    return text[:SOURCE_PREVIEW_CHARS].rstrip() + "\n\n（原文较长，草稿只保留前段可读内容；正式研判前必须打开来源阅读全文。）"


def infer_event_type(title: str) -> str:
    lowered = title.lower()
    if any(word in lowered for word in ["earnings", "results", "eps", "revenue", "outlook", "guidance"]):
        return "财报 / 指引"
    if any(word in lowered for word in ["annual report", "20-f", "report"]):
        return "年报 / 深度材料"
    if any(word in lowered for word in ["conference call", "annual meeting", "webcast"]):
        return "会议 / 待材料"
    if any(word in lowered for word in ["partnership", "collaborate", "customer", "contract"]):
        return "合作 / 客户 / 供应链"
    if any(word in lowered for word in ["launch", "technology", "platform", "model", "spectrum", "nvlink"]):
        return "产品 / 技术 / 平台"
    return "官方候选"


def evidence_prompts(event_type: str) -> list[str]:
    if "财报" in event_type:
        return [
            "收入、分部收入、利润率、EPS、现金流或指引中的具体数字",
            "管理层对需求、产能、价格、成本或资本开支的口径",
            "和上一期或市场预期相比，真正变化的指标",
        ]
    if "会议" in event_type:
        return [
            "会议材料或 transcript 是否已经披露",
            "本次会议需要提取的收入、利润率、现金流、订单或指引指标",
            "如果只是日程，必须等材料出来后再升级正式事件",
        ]
    if "合作" in event_type:
        return [
            "合作对象、期限、投入规模、产能或金额",
            "收入路径：一次性收入、长期供应、平台绑定还是生态合作",
            "对客户粘性、供应链地位、成本或毛利率的影响",
        ]
    if "产品" in event_type:
        return [
            "产品或技术到底解决什么问题，面向哪些客户或场景",
            "是否有客户、部署规模、性能指标、成本指标或商业化路径",
            "和竞争对手或替代方案相比，优势是否可持续",
        ]
    return [
        "原文里能支持判断的数字、日期、客户、产品或管理层表述",
        "这件事影响哪条业务线、财务科目或竞争位置",
        "下一次可以验证这件事是否真正有价值的指标",
    ]


def readiness_profile(candidate: dict, event_candidate: dict, event_type: str, readable_source: str) -> dict:
    score = int(candidate.get("score") or 0)
    source_chars = len(readable_source)
    has_body = bool(clean(event_candidate.get("source_body") or event_candidate.get("source_excerpt")))
    title = clean(candidate.get("title"))
    lowered = title.lower()
    blockers: list[str] = []
    low_substance_annual_notice = is_low_substance_annual_notice(event_type, readable_source)

    if not has_body:
        blockers.append("还没有抓到足够正文")
    if source_chars < 600:
        blockers.append("可读内容偏短")
    if "会议" in event_type and not has_body:
        blockers.append("会议类候选需要等材料或 transcript")
    if any(keyword in lowered for keyword in ["board of directors", "appoint", "names "]):
        blockers.append("治理/人事类信息通常不是优先批处理对象")
    if low_substance_annual_notice:
        blockers.append("年报公告只说明文件已提交，未抓到年报正文里的经营和财务内容")

    readiness_score = score
    if has_body:
        readiness_score += 6
    readiness_score += min(source_chars // 500, 6)
    if "财报" in event_type or "合作" in event_type or "产品" in event_type:
        readiness_score += 2
    if "会议" in event_type and not has_body:
        readiness_score -= 4
    if low_substance_annual_notice:
        readiness_score -= 8

    if low_substance_annual_notice:
        lane = "needs_source"
        label = "待读原文件"
        reason = "当前只读到了年报提交公告，不是年报正文；需要抓取 Form 20-F 或年报 PDF 后再进入深读。"
    elif has_body and source_chars >= 1200 and score >= 8:
        lane = "ready_for_deep_review"
        label = "优先深读"
        reason = "已有较长可读正文，候选分数也足够高，适合作为下一批正式事件研判对象。"
    elif has_body and source_chars >= 600:
        lane = "readable_needs_review"
        label = "可读待研判"
        reason = "已经有可读正文，但还需要人工补证据、业务影响和估值/动作影响。"
    elif "会议" in event_type:
        lane = "waiting_material"
        label = "待会议材料"
        reason = "更像会议日程或材料入口，需要等 transcript、presentation 或财报材料出来后再升级。"
    else:
        lane = "needs_source"
        label = "待补正文"
        reason = "当前主要是标题或短事实，不适合直接进入正式事件。"

    return {
        "readiness_lane": lane,
        "readiness_label": label,
        "readiness_score": readiness_score,
        "review_batch_reason": reason,
        "promotion_blockers": blockers,
    }


def build_draft(candidate: dict, event_candidate: dict, generated_at: str) -> dict:
    company = candidate.get("company", "")
    title = clean(candidate.get("title"))
    draft_id = f"auto-{company}-{slugify(title)}"
    event_type = infer_event_type(title)
    readable_source = source_text(candidate, event_candidate)
    has_body = bool(clean(event_candidate.get("source_body") or event_candidate.get("source_excerpt")))
    source_url = clean(candidate.get("source_url") or event_candidate.get("source_url"))
    source_doc = clean(candidate.get("source_doc") or event_candidate.get("source_file"))
    readiness = readiness_profile(candidate, event_candidate, event_type, readable_source)

    return {
        "draft_id": draft_id,
        "draft_status": "auto_draft",
        "generated_at": generated_at,
        "company": company,
        "company_name": candidate.get("company_name", company),
        "source_candidate_title": title,
        "title": title,
        "date": candidate.get("date", "") or event_candidate.get("date", ""),
        "type": event_type,
        "priority": "草稿",
        "action": "等待补证据" if not has_body else "进入人工研判",
        "score": int(candidate.get("score") or 0),
        "sort_key": int(candidate.get("sort_key") or 0),
        "source_url": source_url,
        "source_doc": source_doc,
        **readiness,
        "source_summary": [
            clip_source(readable_source) if readable_source else "当前只抓到了标题或日程，还没有足够正文，不能升级为正式事件。",
        ],
        "fact": clean(event_candidate.get("fact")) or f"{candidate.get('company_name', company)} 出现官方候选：{title}。",
        "evidence": [f"证据缺口：{item}" for item in evidence_prompts(event_type)],
        "evidence_needed": evidence_prompts(event_type),
        "judgment": "这只是正式事件草稿，还不能直接形成投资判断。先读完来源，把事实、数字和管理层口径补齐，再决定是否升级。",
        "business_analysis": "待补：说明它影响哪条业务线、产品、客户、市场、供应链或成本结构。",
        "valuation_analysis": "待补：说明它是否影响收入质量、利润率、现金流、资本开支、估值区间或仓位动作。",
        "verification": [
            "打开原始来源，确认正文是否足够支撑正式事件。",
            "补齐至少三条具体证据，再写业务影响和估值/动作影响。",
            "如果只有标题、日程或营销口号，保留候选，不进入正式事件。",
        ],
        "quality_check": {
            "has_source": bool(source_url or source_doc),
            "has_readable_source": bool(readable_source),
            "has_source_body": has_body,
            "source_chars": len(readable_source),
            "can_promote_now": False,
            "missing_before_promotion": [
                "原文内容总结",
                "三条以上具体证据",
                "业务影响",
                "估值或动作影响",
                "下一次验证点",
            ],
        },
        "portal_doc": f"./docs/review-drafts/{draft_id}.md",
        "draft_file": str(DRAFT_DIR / f"{draft_id}.json"),
    }


def md_link(label: str, url: str) -> str:
    if not url:
        return "暂无"
    return f"[{label}]({url})"


def draft_to_markdown(draft: dict) -> str:
    evidence = "\n".join(f"- {item}" for item in draft["evidence_needed"])
    verification = "\n".join(f"- {item}" for item in draft["verification"])
    source_summary = "\n\n".join(draft["source_summary"])
    quality = draft["quality_check"]
    source_url = md_link("打开官方来源", draft.get("source_url", ""))
    source_doc = draft.get("source_doc") or "暂无"
    blockers = draft.get("promotion_blockers") or []
    blockers_text = "\n".join(f"- {item}" for item in blockers) if blockers else "- 暂无系统识别的硬性阻碍，但仍必须补齐正式事件字段。"

    return f"""# 正式事件草稿｜{draft['company_name']}｜{draft['title']}

## 草稿状态

- 公司：{draft['company_name']}（{draft['company']}）
- 日期：{draft.get('date') or '待确认'}
- 类型：{draft['type']}
- 候选分数：{draft['score']}
- 当前动作：{draft['action']}
- 批处理建议：{draft.get('readiness_label', '待研判')}（readiness {draft.get('readiness_score', draft['score'])}）
- 官方来源：{source_url}
- 来源快照：{source_doc}

## 批处理建议

{draft.get('review_batch_reason', '先确认原文质量，再决定是否进入正式事件。')}

### 当前阻碍

{blockers_text}

## 原文与事实

先看来源到底说了什么，再决定是否形成正式事件。下面是系统已抓到的可读内容或候选事实。

### 原文可读内容

{source_summary}

### 候选事实

{draft['fact']}

## 升级为正式事件前必须补齐

{evidence}

## 初步判断

{draft['judgment']}

## 业务影响待补

{draft['business_analysis']}

## 估值与动作影响待补

{draft['valuation_analysis']}

## 下一步验证

{verification}

## 入库方式

当这份草稿已经补齐原文总结、三条以上证据、业务影响、估值/动作影响和验证点后，可以在 GitHub Actions 里运行 `Promote Review Draft`，输入以下草稿 ID：

`{draft['draft_id']}`

## 质量闸门

- 有来源：{'是' if quality['has_source'] else '否'}
- 有可读正文：{'是' if quality['has_source_body'] else '否'}
- 当前是否可直接入库：否
- 原因：草稿只负责降低整理摩擦，正式事件仍必须补齐原文总结、证据、业务影响、估值/动作影响和验证点。
"""


def write_outputs(drafts: list[dict], generated_at: str, suppressed: list[dict] | None = None) -> None:
    suppressed = suppressed or []
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    PORTAL_DOC_DIR.mkdir(parents=True, exist_ok=True)

    for old in DRAFT_DIR.glob("auto-*.json"):
        old.unlink()
    for old in PORTAL_DOC_DIR.glob("auto-*.md"):
        old.unlink()

    by_key = {}
    by_company: dict[str, list[dict]] = {}
    portal_items = []

    for draft in drafts:
        draft_path = DRAFT_DIR / f"{draft['draft_id']}.json"
        doc_path = PORTAL_DOC_DIR / f"{draft['draft_id']}.md"
        draft_path.write_text(json.dumps(draft, ensure_ascii=False, indent=2), encoding="utf-8")
        doc_path.write_text(draft_to_markdown(draft), encoding="utf-8")

        item = {
            "draft_id": draft["draft_id"],
            "company": draft["company"],
            "company_name": draft["company_name"],
            "title": draft["title"],
            "date": draft.get("date", ""),
            "score": draft["score"],
            "readiness_score": draft.get("readiness_score", draft["score"]),
            "readiness_lane": draft.get("readiness_lane", ""),
            "readiness_label": draft.get("readiness_label", ""),
            "review_batch_reason": draft.get("review_batch_reason", ""),
            "promotion_blockers": draft.get("promotion_blockers", []),
            "source_url": draft.get("source_url", ""),
            "portal_doc": draft["portal_doc"],
            "has_source_body": draft["quality_check"]["has_source_body"],
        }
        key = candidate_key(draft["company"], draft["title"])
        by_key[key] = item
        by_company.setdefault(draft["company"], []).append(item)
        portal_items.append(item)

    portal_items.sort(key=lambda item: (item.get("readiness_score") or 0, item.get("score") or 0), reverse=True)
    for items in by_company.values():
        items.sort(key=lambda item: (item.get("readiness_score") or 0, item.get("score") or 0), reverse=True)

    readiness_counts: dict[str, int] = {}
    for item in portal_items:
        lane = item.get("readiness_lane") or "unknown"
        readiness_counts[lane] = readiness_counts.get(lane, 0) + 1

    index_payload = {
        "generated_at": generated_at,
        "summary": {
            "total": len(drafts),
            "companies": len(by_company),
            "with_source_body": sum(1 for item in portal_items if item["has_source_body"]),
            "suppressed_count": len(suppressed),
            "readiness_counts": readiness_counts,
            "priority_batch": [
                item
                for item in portal_items
                if item.get("readiness_lane") in {"ready_for_deep_review", "readable_needs_review"}
            ][:5],
        },
        "by_key": by_key,
        "companies": by_company,
        "items": portal_items,
        "suppressed": suppressed,
    }
    INDEX_FILE.write_text(json.dumps(index_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    BATCH_PLAN_FILE.write_text(
        json.dumps(
            {
                "generated_at": generated_at,
                "description": "按可读正文、候选分数和事件类型自动生成的草稿批处理优先级。这里只决定先读谁，不代表已经可以入库。",
                "summary": index_payload["summary"],
                "priority_batch": index_payload["summary"]["priority_batch"],
                "items": portal_items,
                "suppressed": suppressed,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    PORTAL_DATA_FILE.write_text(
        "window.BAMBOO_LENS_REVIEW_DRAFTS = "
        + json.dumps(index_payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )


def main() -> None:
    queue = load_json(DECISION_QUEUE_FILE, {"items": []})
    event_store = load_json(EVENT_STORE_FILE, {"companies": {}})
    reviewed_events = load_json(REVIEWED_EVENTS_FILE, {"companies": {}})
    lookup = source_lookup(event_store)
    reviewed = reviewed_lookup(reviewed_events)
    formal_coverage = formal_coverage_lookup(queue, reviewed_events)
    generated_at = datetime.now().isoformat(timespec="seconds")

    drafts = []
    suppressed = []
    for candidate in select_candidates(queue):
        key = candidate_key(candidate.get("company", ""), clean(candidate.get("title")))
        event_candidate = lookup.get(key, {})
        covered_reason = covered_by_existing_event(candidate, event_candidate, reviewed, formal_coverage)
        if covered_reason:
            suppressed.append(
                {
                    "company": candidate.get("company", ""),
                    "company_name": candidate.get("company_name", candidate.get("company", "")),
                    "title": clean(candidate.get("title")),
                    "date": candidate.get("date", "") or event_candidate.get("date", ""),
                    "source_url": clean(candidate.get("source_url") or event_candidate.get("source_url")),
                    "reason": covered_reason,
                }
            )
            continue
        if should_build_draft(candidate, event_candidate):
            drafts.append(build_draft(candidate, event_candidate, generated_at))

    write_outputs(drafts, generated_at, suppressed)
    print(f"Review draft index written to: {INDEX_FILE}")
    print(f"Portal review draft data written to: {PORTAL_DATA_FILE}")
    print(f"Drafts generated: {len(drafts)}")


if __name__ == "__main__":
    main()
