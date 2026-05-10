#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

from promote_reviewed_event import (
    REVIEWED_EVENTS_FILE,
    load_json,
    load_reviewed_events,
    normalize_event,
    resolve_draft_path,
    run_refresh_chain,
    upsert_event,
    validate_draft,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Promote multiple completed review drafts into reviewed_events.json, then refresh outputs once."
    )
    parser.add_argument(
        "--draft-ids",
        required=True,
        help="One or more draft ids. Supports comma, whitespace or newline separated values.",
    )
    parser.add_argument("--allow-todo", action="store_true", help="Allow placeholder text. Not recommended.")
    parser.add_argument("--no-refresh", action="store_true", help="Do not regenerate event store / portal outputs.")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on the first invalid draft.")
    return parser.parse_args()


def split_draft_ids(raw: str) -> list[str]:
    return [item.strip().removesuffix(".json") for item in re.split(r"[\s,]+", raw or "") if item.strip()]


def main() -> None:
    args = parse_args()
    draft_ids = split_draft_ids(args.draft_ids)
    if not draft_ids:
        print("No draft ids provided.", file=sys.stderr)
        sys.exit(1)

    payload = load_reviewed_events()
    payload["generated_at"] = datetime.now().isoformat(timespec="seconds")
    promoted: list[dict] = []
    skipped: list[dict] = []

    for draft_id in draft_ids:
        try:
            draft_path = resolve_draft_path(SimpleNamespace(draft=None, draft_id=draft_id))
            draft = load_json(draft_path)
            errors = validate_draft(draft, args.allow_todo)
            if errors:
                skipped.append({"draft_id": draft_id, "reason": "; ".join(errors)})
                if args.fail_fast:
                    break
                continue

            event = normalize_event(draft)
            upsert_event(payload, draft["company"].strip(), event)
            promoted.append({"draft_id": draft_id, "company": draft["company"], "title": event["title"]})
        except Exception as exc:  # noqa: BLE001 - batch report should keep going unless fail-fast.
            skipped.append({"draft_id": draft_id, "reason": str(exc)})
            if args.fail_fast:
                break

    if not promoted:
        print("No drafts were promoted.", file=sys.stderr)
        print(json.dumps({"skipped": skipped}, ensure_ascii=False, indent=2), file=sys.stderr)
        sys.exit(1)

    REVIEWED_EVENTS_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print("Promoted drafts:")
    for item in promoted:
        print(f"- {item['company']}｜{item['title']}｜{item['draft_id']}")

    if skipped:
        print("\nSkipped drafts:")
        for item in skipped:
            print(f"- {item['draft_id']}: {item['reason']}")

    if not args.no_refresh:
        run_refresh_chain()
        print("\nRefreshed event store, company state, decision queue and portal data once after batch promotion.")


if __name__ == "__main__":
    main()
