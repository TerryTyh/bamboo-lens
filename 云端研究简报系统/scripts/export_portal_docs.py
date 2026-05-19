#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PORTAL_DOCS = PROJECT_ROOT / "研究门户" / "docs"

DOCS = [
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "31-研究池与真实组合衔接改造计划V1.md",
        PORTAL_DOCS / "research" / "31-研究池与真实组合衔接改造计划V1.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "01-筛选规则.md",
        PORTAL_DOCS / "rules" / "01-筛选规则.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "02-公司分析框架.md",
        PORTAL_DOCS / "rules" / "02-公司分析框架.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "21-研究结论到投资决策的落地规则V1.md",
        PORTAL_DOCS / "rules" / "21-研究结论到投资决策的落地规则V1.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "37-新增公司准入标准V1.md",
        PORTAL_DOCS / "rules" / "37-新增公司准入标准V1.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "38-长电科技新增公司准入评估V1.md",
        PORTAL_DOCS / "research" / "38-长电科技新增公司准入评估V1.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "39-长电科技最小研究包V1.md",
        PORTAL_DOCS / "research" / "39-长电科技最小研究包V1.md",
    ),
    (
        ROOT / "outputs" / "daily_brief.md",
        PORTAL_DOCS / "briefs" / "daily_brief.md",
    ),
    (
        ROOT / "outputs" / "weekend_sync_summary.md",
        PORTAL_DOCS / "briefs" / "weekend_sync_summary.md",
    ),
    (
        ROOT / "outputs" / "company_page_readability_audit.md",
        PORTAL_DOCS / "research" / "company_page_readability_audit.md",
    ),
    (
        ROOT / "outputs" / "company_page_mainline_audit.md",
        PORTAL_DOCS / "research" / "company_page_mainline_audit.md",
    ),
    (
        ROOT / "outputs" / "automation_health.md",
        PORTAL_DOCS / "research" / "automation_health.md",
    ),
]


def copy_doc(source: Path, target: Path) -> bool:
    if not source.exists():
        print(f"Skip missing doc: {source}")
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    print(f"Exported: {target}")
    return True


def main() -> None:
    exported = sum(1 for source, target in DOCS if copy_doc(source, target))
    print(f"Portal docs exported: {exported}")


if __name__ == "__main__":
    main()
