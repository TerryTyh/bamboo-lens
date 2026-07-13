#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
OUTPUT_DIR = ROOT / "outputs"
PORTAL_DATA_DIR = PROJECT_ROOT / "研究门户"
WORKFLOW_DIR = PROJECT_ROOT / ".github" / "workflows"
MARKET_WATCHLIST = ROOT / "config" / "market_watchlist.json"
HEALTH_JSON = OUTPUT_DIR / "automation_health.json"
HEALTH_MD = OUTPUT_DIR / "automation_health.md"
PORTAL_HEALTH_JS = PORTAL_DATA_DIR / "automation-health-data.js"

CN_TZ = ZoneInfo("Asia/Shanghai")
WORKDAY_OUTPUT_MAX_AGE_HOURS = 42
WEEKEND_OUTPUT_MAX_AGE_HOURS = 90

REQUIRED_WORKFLOWS = [
    "collect-candidates.yml",
    "daily-brief.yml",
    "promote-review-draft.yml",
    "deploy-pages.yml",
]

REQUIRED_OUTPUTS = [
    "official_candidates.json",
    "event_store.json",
    "decision_queue.json",
    "decision_impact.json",
    "decision_deposition.json",
    "company_page_overrides.json",
    "company_page_readability_audit.json",
    "company_page_mainline_audit.json",
    "company_state.json",
    "market_snapshot.json",
    "daily_brief.md",
    "morning_brief.md",
]

REQUIRED_PORTAL_DATA = [
    "candidate-data.js",
    "event-store-data.js",
    "decision-data.js",
    "decision-impact-data.js",
    "decision-deposition-data.js",
    "company-page-overrides-data.js",
    "company-readability-audit-data.js",
    "company-mainline-audit-data.js",
    "company-state-data.js",
    "market-snapshot-data.js",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def parse_datetime(value: str) -> datetime | None:
    if not value:
        return None
    text = str(value).strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=CN_TZ)
        return parsed.astimezone(CN_TZ)
    except ValueError:
        pass

    candidates = [
        ("%Y-%m-%dT%H:%M:%S", text[:19]),
        ("%Y-%m-%dT%H:%M:%S.%f", text),
        ("%Y-%m-%d", text[:10]),
        ("%Y%m%d-%H%M%S", text[:15]),
    ]
    for fmt, candidate in candidates:
        try:
            return datetime.strptime(candidate, fmt).replace(tzinfo=CN_TZ)
        except ValueError:
            continue
    return None


def json_generated_at(path: Path) -> datetime | None:
    payload = load_json(path)
    return parse_datetime(str(payload.get("generated_at") or payload.get("created_at") or ""))


def md_header_date(path: Path) -> datetime | None:
    text = read_text(path)
    head = "\n".join(text.splitlines()[:8])
    match = re.search(r"20\d{2}-\d{2}-\d{2}", head)
    if not match:
        return None
    return parse_datetime(match.group(0))


def age_hours(value: datetime | None, now: datetime) -> float | None:
    if value is None:
        return None
    return max(0.0, (now - value).total_seconds() / 3600)


def check_file_group(label: str, root: Path, names: list[str]) -> dict:
    missing = [name for name in names if not (root / name).exists()]
    return {
        "label": label,
        "status": "healthy" if not missing else "risk",
        "missing": missing,
        "total": len(names),
        "present": len(names) - len(missing),
    }


def workflow_contains(workflow: str, snippets: list[str]) -> list[str]:
    text = read_text(WORKFLOW_DIR / workflow)
    return [snippet for snippet in snippets if snippet not in text]


def check_workflow_coverage() -> dict:
    missing: dict[str, list[str]] = {}
    expected = {
        "collect-candidates.yml": [
            "audit_company_page_readability.py",
            "audit_company_page_mainlines.py",
            "company_page_mainline_audit.json",
            "company-mainline-audit-data.js",
            "collect_market_snapshots.py",
            "build_morning_brief.py",
            "check_automation_health.py",
        ],
        "daily-brief.yml": [
            "prepare_brief_to_send.py",
            "send_wecom.py",
            "brief_to_send.md",
            "check_automation_health.py",
        ],
        "promote-review-draft.yml": [
            "promote_review_batch.py",
            "automation_health.json",
            "automation-health-data.js",
        ],
        "deploy-pages.yml": [
            "export_portal_docs.py",
            "deploy-pages",
        ],
    }
    for workflow, snippets in expected.items():
        misses = workflow_contains(workflow, snippets)
        if misses:
            missing[workflow] = misses
    return {
        "status": "healthy" if not missing else "risk",
        "missing": missing,
    }


def check_output_freshness(now: datetime) -> dict:
    threshold = WEEKEND_OUTPUT_MAX_AGE_HOURS if now.weekday() >= 5 else WORKDAY_OUTPUT_MAX_AGE_HOURS
    tracked = [
        ("official_candidates", OUTPUT_DIR / "official_candidates.json", json_generated_at),
        ("event_store", OUTPUT_DIR / "event_store.json", json_generated_at),
        ("decision_queue", OUTPUT_DIR / "decision_queue.json", json_generated_at),
        ("company_page_overrides", OUTPUT_DIR / "company_page_overrides.json", json_generated_at),
        ("readability_audit", OUTPUT_DIR / "company_page_readability_audit.json", json_generated_at),
        ("mainline_audit", OUTPUT_DIR / "company_page_mainline_audit.json", json_generated_at),
        ("market_snapshot", OUTPUT_DIR / "market_snapshot.json", json_generated_at),
        ("daily_brief", OUTPUT_DIR / "daily_brief.md", md_header_date),
        ("morning_brief", OUTPUT_DIR / "morning_brief.md", md_header_date),
    ]
    items = []
    stale = []
    missing_timestamp = []
    for name, path, parser in tracked:
        timestamp = parser(path)
        age = age_hours(timestamp, now)
        status = "healthy"
        if not path.exists():
            status = "risk"
            stale.append(name)
        elif age is None:
            status = "watch"
            missing_timestamp.append(name)
        elif age > threshold:
            status = "watch"
            stale.append(name)
        items.append(
            {
                "name": name,
                "path": str(path.relative_to(PROJECT_ROOT)),
                "timestamp": timestamp.isoformat(timespec="seconds") if timestamp else "",
                "ageHours": round(age, 1) if age is not None else None,
                "status": status,
            }
        )
    return {
        "status": "healthy" if not stale and not missing_timestamp else "watch",
        "thresholdHours": threshold,
        "items": items,
        "stale": stale,
        "missingTimestamp": missing_timestamp,
    }


def check_brief_guard(now: datetime) -> dict:
    morning = read_text(OUTPUT_DIR / "morning_brief.md")
    daily = read_text(OUTPUT_DIR / "daily_brief.md")
    today = now.strftime("%Y-%m-%d")
    # Keep this aligned with build_morning_brief.py: after early morning, the
    # generated morning brief is for the next send date.
    expected_morning_date = (now if now.hour < 6 else now + timedelta(days=1)).strftime("%Y-%m-%d")
    is_weekend = now.weekday() >= 5
    morning_same_day = expected_morning_date in "\n".join(morning.splitlines()[:8])
    daily_same_day = today in "\n".join(daily.splitlines()[:8])
    morning_lines = [line.strip() for line in morning.splitlines() if line.strip()]
    morning_body = "\n".join(morning_lines[1:]).strip() if len(morning_lines) > 1 else ""
    morning_meaningful = bool(
        morning_same_day
        and len(morning_body) >= 80
        and ("## " in morning_body or "**原文讲了什么**" in morning_body)
    )
    empty_markers = [
        "今日没有新的可读内容",
        "今天没有新增值得直接推送的已判断研究事件",
    ]
    daily_empty = any(marker in daily for marker in empty_markers)
    status = "healthy"
    notes = []
    if not morning_same_day and not daily_same_day:
        if is_weekend:
            notes.append("今天是周末，晨报默认非发送日；没有当天标题不视为异常。")
        else:
            status = "watch"
            notes.append("morning_brief.md 和 daily_brief.md 都不是当天标题；工作日早晨需复核。")
    if daily_empty and not morning_same_day:
        if is_weekend:
            notes.append("fallback 日报为空，但周末不发送，暂不视为异常。")
        else:
            status = "watch"
            notes.append("fallback 日报为空且没有当天晨报，prepare_brief_to_send.py 会阻断发送。")
    if morning_same_day and not morning_meaningful:
        notes.append("当天晨报存在但正文不足，发送逻辑会回退到 fallback 日报。")
    if morning_meaningful:
        notes.append("当天晨报存在，日报发送会优先选择 morning_brief.md。")
    elif daily_same_day and not daily_empty:
        notes.append("当天 fallback 日报可用，但质量取决于前一晚候选收集是否成功。")
    return {
        "status": status,
        "today": today,
        "expectedMorningDate": expected_morning_date,
        "morningSameDay": morning_same_day,
        "morningMeaningful": morning_meaningful,
        "dailySameDay": daily_same_day,
        "dailyEmpty": daily_empty,
        "notes": notes,
    }


def check_audits() -> dict:
    readability = load_json(OUTPUT_DIR / "company_page_readability_audit.json").get("summary", {})
    mainline = load_json(OUTPUT_DIR / "company_page_mainline_audit.json").get("summary", {})
    readability_risk = int(readability.get("at_risk") or 0)
    mainline_weak = int(mainline.get("weak") or 0)
    mainline_review = int(mainline.get("review") or 0)
    status = "healthy"
    if readability_risk or mainline_weak:
        status = "risk"
    elif mainline_review:
        status = "watch"
    return {
        "status": status,
        "readability": readability,
        "mainline": mainline,
    }


def check_market_snapshot_quality() -> dict:
    config = load_json(MARKET_WATCHLIST)
    snapshot = load_json(OUTPUT_DIR / "market_snapshot.json")
    expected = config.get("companies") or []
    companies = snapshot.get("companies") or {}
    issues = []
    warnings = snapshot.get("warnings") or []
    errors = snapshot.get("errors") or []

    for item in expected:
        company_id = item.get("id")
        primary_symbol = item.get("primary_symbol")
        company = companies.get(company_id or "")
        if not company:
            issues.append(f"{company_id}: 缺少行情快照")
            continue
        primary = company.get("primary")
        quotes = company.get("quotes") or []
        symbols = {quote.get("symbol") for quote in quotes}
        if company.get("stale"):
            issues.append(f"{company_id}: 使用 stale 行情")
        if not primary or not isinstance(primary.get("price"), (int, float)):
            issues.append(f"{company_id}: 缺少可用价格")
        if primary_symbol and primary_symbol not in symbols:
            issues.append(f"{company_id}: 缺少主交易口径 {primary_symbol}")

    status = "healthy"
    if issues:
        status = "risk"
    elif errors:
        status = "watch"

    return {
        "status": status,
        "expected": len(expected),
        "covered": len([item for item in expected if item.get("id") in companies]),
        "issues": issues,
        "warnings": warnings,
        "errors": errors,
    }


def summarize_status(sections: list[dict]) -> str:
    if any(section.get("status") == "risk" for section in sections):
        return "risk"
    if any(section.get("status") == "watch" for section in sections):
        return "watch"
    return "healthy"


def build_markdown(payload: dict) -> str:
    lines = [
        "# 竹鉴自动化健康检查",
        "",
        f"生成时间：{payload['generated_at']}",
        "",
        f"总体状态：{payload['status_label']}",
        "",
        "## 核心结论",
        "",
    ]
    for item in payload["summary_notes"]:
        lines.append(f"- {item}")
    lines.extend(["", "## 文件与产物", ""])
    for group in payload["file_groups"]:
        missing = f"，缺失：{'、'.join(group['missing'])}" if group["missing"] else ""
        lines.append(f"- {group['label']}：{group['present']}/{group['total']}，{group['status']}{missing}")
    lines.extend(["", "## 新鲜度", ""])
    lines.append(f"- 阈值：{payload['freshness']['thresholdHours']} 小时")
    for item in payload["freshness"]["items"]:
        age = "未知" if item["ageHours"] is None else f"{item['ageHours']}h"
        lines.append(f"- {item['name']}：{item['status']}，时间 {item['timestamp'] or '未知'}，年龄 {age}")
    lines.extend(["", "## 日报发送保护", ""])
    for note in payload["brief_guard"]["notes"]:
        lines.append(f"- {note}")
    lines.extend(["", "## 公司页质量审计", ""])
    lines.append(f"- 可读性审计：{json.dumps(payload['audits']['readability'], ensure_ascii=False)}")
    lines.append(f"- 主线复核：{json.dumps(payload['audits']['mainline'], ensure_ascii=False)}")
    lines.extend(["", "## 行情与估值动态化", ""])
    market_quality = payload["market_snapshot_quality"]
    lines.append(f"- 覆盖公司：{market_quality['covered']}/{market_quality['expected']}，状态 {market_quality['status']}")
    if market_quality["issues"]:
        for issue in market_quality["issues"]:
            lines.append(f"- 问题：{issue}")
    if market_quality["errors"]:
        for error in market_quality["errors"]:
            lines.append(f"- 抓取错误：{error}")
    if payload["workflow_coverage"]["missing"]:
        lines.extend(["", "## Workflow 缺口", ""])
        for workflow, snippets in payload["workflow_coverage"]["missing"].items():
            lines.append(f"- {workflow} 缺少：{'、'.join(snippets)}")
    return "\n".join(lines) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    now = datetime.now(CN_TZ)
    file_groups = [
        check_file_group("GitHub Actions", WORKFLOW_DIR, REQUIRED_WORKFLOWS),
        check_file_group("云端 outputs", OUTPUT_DIR, REQUIRED_OUTPUTS),
        check_file_group("门户数据文件", PORTAL_DATA_DIR, REQUIRED_PORTAL_DATA),
    ]
    workflow_coverage = check_workflow_coverage()
    freshness = check_output_freshness(now)
    brief_guard = check_brief_guard(now)
    audits = check_audits()
    market_snapshot_quality = check_market_snapshot_quality()
    sections = [*file_groups, workflow_coverage, freshness, brief_guard, audits, market_snapshot_quality]
    status = summarize_status(sections)
    status_label = {"healthy": "健康", "watch": "需观察", "risk": "有风险"}[status]
    summary_notes = [
        f"工作流文件：{file_groups[0]['present']}/{file_groups[0]['total']} 已存在。",
        f"关键云端产物：{file_groups[1]['present']}/{file_groups[1]['total']} 已存在。",
        f"门户数据文件：{file_groups[2]['present']}/{file_groups[2]['total']} 已存在。",
        f"日报保护状态：{brief_guard['status']}。",
        f"公司页审计状态：{audits['status']}。",
        f"行情覆盖状态：{market_snapshot_quality['status']}。",
    ]
    payload = {
        "generated_at": now.isoformat(timespec="seconds"),
        "status": status,
        "status_label": status_label,
        "summary_notes": summary_notes,
        "file_groups": file_groups,
        "workflow_coverage": workflow_coverage,
        "freshness": freshness,
        "brief_guard": brief_guard,
        "audits": audits,
        "market_snapshot_quality": market_snapshot_quality,
    }
    HEALTH_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    HEALTH_MD.write_text(build_markdown(payload), encoding="utf-8")
    PORTAL_HEALTH_JS.write_text(
        "window.BAMBOO_LENS_AUTOMATION_HEALTH = "
        + json.dumps(payload, ensure_ascii=False, indent=2)
        + ";\n",
        encoding="utf-8",
    )
    print(f"Automation health written to: {HEALTH_JSON}")
    print(f"Automation health markdown written to: {HEALTH_MD}")
    print(f"Portal automation health data written to: {PORTAL_HEALTH_JS}")


if __name__ == "__main__":
    main()
