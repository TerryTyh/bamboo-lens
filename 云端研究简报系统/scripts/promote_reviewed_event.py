#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "outputs"
REVIEWED_EVENTS_FILE = OUTPUT_DIR / "reviewed_events.json"
REVIEW_DRAFT_DIR = OUTPUT_DIR / "review_drafts"

REQUIRED_TEXT_FIELDS = [
    "company",
    "title",
    "date",
    "type",
    "fact",
    "judgment",
    "business_analysis",
    "valuation_analysis",
    "action",
    "priority",
]

REQUIRED_LIST_FIELDS = {
    "source_summary": 1,
    "evidence": 3,
    "verification": 2,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Promote a completed review draft into reviewed_events.json.")
    parser.add_argument("draft", type=Path, nargs="?", help="Path to review draft JSON.")
    parser.add_argument("--draft-id", help="Draft id under outputs/review_drafts, without .json.")
    parser.add_argument("--no-refresh", action="store_true", help="Do not regenerate event store / portal outputs.")
    parser.add_argument("--allow-todo", action="store_true", help="Allow TODO placeholders. Not recommended.")
    return parser.parse_args()


def load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_draft_path(args: argparse.Namespace) -> Path:
    if args.draft and args.draft_id:
        raise ValueError("Use either a draft path or --draft-id, not both.")
    if args.draft:
        return args.draft
    if args.draft_id:
        draft_id = args.draft_id.removesuffix(".json")
        return REVIEW_DRAFT_DIR / f"{draft_id}.json"
    raise ValueError("Missing draft path or --draft-id.")


def contains_todo(value) -> bool:
    if isinstance(value, str):
        placeholders = ["TODO", "待补", "证据缺口", "等待补证据", "这只是正式事件草稿"]
        return any(placeholder in value for placeholder in placeholders)
    if isinstance(value, list):
        return any(contains_todo(item) for item in value)
    if isinstance(value, dict):
        return any(contains_todo(item) for item in value.values())
    return False


def validate_draft(draft: dict, allow_todo: bool) -> list[str]:
    errors = []
    for field in REQUIRED_TEXT_FIELDS:
        if not str(draft.get(field, "")).strip():
            errors.append(f"Missing required field: {field}")

    if not (draft.get("source_url") or draft.get("source_doc")):
        errors.append("Missing source_url or source_doc.")

    for field, min_count in REQUIRED_LIST_FIELDS.items():
        value = draft.get(field)
        if not isinstance(value, list):
            errors.append(f"{field} must be a list.")
            continue
        filled = [item for item in value if str(item).strip()]
        if len(filled) < min_count:
            errors.append(f"{field} needs at least {min_count} filled item(s).")

    if not allow_todo and contains_todo(draft):
        errors.append("Draft still contains placeholder text and is not ready for promotion.")

    return errors


def load_reviewed_events() -> dict:
    if not REVIEWED_EVENTS_FILE.exists():
        return {"generated_at": "", "companies": {}}
    return load_json(REVIEWED_EVENTS_FILE)


def normalize_event(draft: dict) -> dict:
    now = datetime.now().isoformat(timespec="seconds")
    event = {
        "title": draft["title"].strip(),
        "source_candidate_title": str(draft.get("source_candidate_title", "")).strip(),
        "date": draft["date"].strip(),
        "type": draft["type"].strip(),
        "priority": draft["priority"].strip(),
        "action": draft["action"].strip(),
        "sort_key": int(draft.get("sort_key") or 0),
        "source_url": str(draft.get("source_url", "")).strip(),
        "source_doc": str(draft.get("source_doc", "")).strip(),
        "source_summary": draft.get("source_summary", []),
        "fact": draft["fact"].strip(),
        "evidence": draft.get("evidence", []),
        "judgment": draft["judgment"].strip(),
        "business_analysis": draft["business_analysis"].strip(),
        "valuation_analysis": draft["valuation_analysis"].strip(),
        "verification": draft.get("verification", []),
        # Use promotion time as reviewed_at so the morning brief can correctly
        # surface newly promoted items, even if the draft file was authored earlier.
        "reviewed_at": now,
        "draft_reviewed_at": str(draft.get("reviewed_at") or "").strip(),
    }
    if not event["sort_key"]:
        event["sort_key"] = int("".join(ch for ch in event["date"] if ch.isdigit())[:8] or 0)
    return event


def upsert_event(payload: dict, company: str, event: dict) -> None:
    companies = payload.setdefault("companies", {})
    events = companies.setdefault(company, [])
    key = (event["title"], event["date"])
    source_url = str(event.get("source_url") or "").strip().rstrip("/")
    source_candidate_title = str(event.get("source_candidate_title") or "").strip()
    for idx, existing in enumerate(events):
        existing_key = (str(existing.get("title") or ""), str(existing.get("date") or ""))
        if existing_key == key:
            events[idx] = event
            return
        # Allow title refinements by matching on (date + source_url) or
        # (date + source_candidate_title) when title differs.
        existing_url = str(existing.get("source_url") or "").strip().rstrip("/")
        if source_url and existing.get("date") == event["date"] and existing_url == source_url:
            events[idx] = event
            return
        existing_source_title = str(existing.get("source_candidate_title") or "").strip()
        if (
            source_candidate_title
            and existing.get("date") == event["date"]
            and existing_source_title == source_candidate_title
        ):
            events[idx] = event
            return
    events.append(event)
    events.sort(key=lambda item: int(item.get("sort_key") or 0), reverse=True)


def run_refresh_chain() -> None:
    scripts = [
        "build_event_store.py",
        "export_portal_event_store_data.py",
        "build_company_state.py",
        "build_decision_queue.py",
        "build_review_drafts.py",
        "build_decision_impact.py",
        "build_decision_deposition.py",
        "build_company_page_overrides.py",
        "audit_company_page_readability.py",
        "audit_company_page_mainlines.py",
        "export_portal_candidate_data.py",
        "check_automation_health.py",
        "export_portal_docs.py",
    ]
    for script in scripts:
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True)


def main() -> None:
    args = parse_args()
    draft_path = resolve_draft_path(args)
    draft = load_json(draft_path)
    errors = validate_draft(draft, args.allow_todo)
    if errors:
        print("Draft failed quality gate:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        sys.exit(1)

    payload = load_reviewed_events()
    payload["generated_at"] = datetime.now().isoformat(timespec="seconds")
    event = normalize_event(draft)
    upsert_event(payload, draft["company"].strip(), event)
    REVIEWED_EVENTS_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Promoted reviewed event into: {REVIEWED_EVENTS_FILE}")
    print(f"Company: {draft['company']}")
    print(f"Title: {event['title']}")
    print(f"Draft: {draft_path}")

    if not args.no_refresh:
        run_refresh_chain()
        print("Refreshed event store, company state, decision queue and portal data.")


if __name__ == "__main__":
    main()
