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
DRAFT_DIR = OUTPUT_DIR / "review_drafts"
INDEX_FILE = OUTPUT_DIR / "review_draft_index.json"
PORTAL_DOC_DIR = PROJECT_ROOT / "研究门户" / "docs" / "review-drafts"
PORTAL_DATA_FILE = PROJECT_ROOT / "研究门户" / "review-draft-data.js"

MAX_DRAFTS = 16
MIN_SCORE = 6
SOURCE_PREVIEW_CHARS = 2600
CURRENT_DATE_KEY = int(datetime.now().strftime("%Y%m%d"))

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


def source_lookup(event_store: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for company_id, company in event_store.get("companies", {}).items():
        for candidate in company.get("official_candidates", []):
            title = clean(candidate.get("title"))
            if title:
                lookup[candidate_key(company_id, title)] = candidate
    return lookup


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


def build_draft(candidate: dict, event_candidate: dict, generated_at: str) -> dict:
    company = candidate.get("company", "")
    title = clean(candidate.get("title"))
    draft_id = f"auto-{company}-{slugify(title)}"
    event_type = infer_event_type(title)
    readable_source = source_text(candidate, event_candidate)
    has_body = bool(clean(event_candidate.get("source_body") or event_candidate.get("source_excerpt")))
    source_url = clean(candidate.get("source_url") or event_candidate.get("source_url"))
    source_doc = clean(candidate.get("source_doc") or event_candidate.get("source_file"))

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
        "source_summary": [
            clip_source(readable_source) if readable_source else "当前只抓到了标题或日程，还没有足够正文，不能升级为正式事件。",
        ],
        "fact": clean(event_candidate.get("fact")) or f"{candidate.get('company_name', company)} 出现官方候选：{title}。",
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

    return f"""# 正式事件草稿｜{draft['company_name']}｜{draft['title']}

## 草稿状态

- 公司：{draft['company_name']}（{draft['company']}）
- 日期：{draft.get('date') or '待确认'}
- 类型：{draft['type']}
- 候选分数：{draft['score']}
- 当前动作：{draft['action']}
- 官方来源：{source_url}
- 来源快照：{source_doc}

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

## 质量闸门

- 有来源：{'是' if quality['has_source'] else '否'}
- 有可读正文：{'是' if quality['has_source_body'] else '否'}
- 当前是否可直接入库：否
- 原因：草稿只负责降低整理摩擦，正式事件仍必须补齐原文总结、证据、业务影响、估值/动作影响和验证点。
"""


def write_outputs(drafts: list[dict], generated_at: str) -> None:
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
            "source_url": draft.get("source_url", ""),
            "portal_doc": draft["portal_doc"],
            "has_source_body": draft["quality_check"]["has_source_body"],
        }
        key = candidate_key(draft["company"], draft["title"])
        by_key[key] = item
        by_company.setdefault(draft["company"], []).append(item)
        portal_items.append(item)

    index_payload = {
        "generated_at": generated_at,
        "summary": {
            "total": len(drafts),
            "companies": len(by_company),
            "with_source_body": sum(1 for item in portal_items if item["has_source_body"]),
        },
        "by_key": by_key,
        "companies": by_company,
        "items": portal_items,
    }
    INDEX_FILE.write_text(json.dumps(index_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    PORTAL_DATA_FILE.write_text(
        "window.BAMBOO_LENS_REVIEW_DRAFTS = "
        + json.dumps(index_payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )


def main() -> None:
    queue = load_json(DECISION_QUEUE_FILE, {"items": []})
    event_store = load_json(EVENT_STORE_FILE, {"companies": {}})
    lookup = source_lookup(event_store)
    generated_at = datetime.now().isoformat(timespec="seconds")

    drafts = []
    for candidate in select_candidates(queue):
        key = candidate_key(candidate.get("company", ""), clean(candidate.get("title")))
        event_candidate = lookup.get(key, {})
        if should_build_draft(candidate, event_candidate):
            drafts.append(build_draft(candidate, event_candidate, generated_at))

    write_outputs(drafts, generated_at)
    print(f"Review draft index written to: {INDEX_FILE}")
    print(f"Portal review draft data written to: {PORTAL_DATA_FILE}")
    print(f"Drafts generated: {len(drafts)}")


if __name__ == "__main__":
    main()
