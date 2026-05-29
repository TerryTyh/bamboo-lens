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
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "40-研究池生命周期管理V1.md",
        PORTAL_DOCS / "rules" / "40-研究池生命周期管理V1.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "41-研究池首轮复评_2026-05-24.md",
        PORTAL_DOCS / "research" / "41-研究池首轮复评_2026-05-24.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "42-每周候选发现_2026-05-24.md",
        PORTAL_DOCS / "research" / "42-每周候选发现_2026-05-24.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "43-今日收口与下周启动_2026-05-24.md",
        PORTAL_DOCS / "research" / "43-今日收口与下周启动_2026-05-24.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "44-候选池变化检查_2026-05-25.md",
        PORTAL_DOCS / "research" / "44-候选池变化检查_2026-05-25.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "45-NVIDIA与Google Cloud草稿研判准备_2026-05-25.md",
        PORTAL_DOCS / "research" / "45-NVIDIA与Google Cloud草稿研判准备_2026-05-25.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "46-ASMPT初筛准备_2026-05-25.md",
        PORTAL_DOCS / "research" / "46-ASMPT初筛准备_2026-05-25.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "47-候选池变化复核_2026-05-26.md",
        PORTAL_DOCS / "research" / "47-候选池变化复核_2026-05-26.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "48-NVIDIA FY2027 Q1财报候选研判准备_2026-05-26.md",
        PORTAL_DOCS / "research" / "48-NVIDIA FY2027 Q1财报候选研判准备_2026-05-26.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "49-ASMPT一页式观察卡_2026-05-26.md",
        PORTAL_DOCS / "research" / "49-ASMPT一页式观察卡_2026-05-26.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "50-A股候选扩池_2026-05-27.md",
        PORTAL_DOCS / "research" / "50-A股候选扩池_2026-05-27.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "51-北方华创一页式观察卡_2026-05-28.md",
        PORTAL_DOCS / "research" / "51-北方华创一页式观察卡_2026-05-28.md",
    ),
    (
        PROJECT_ROOT / "长期高潜力公司跟踪系统" / "52-中微公司一页式观察卡_2026-05-29.md",
        PORTAL_DOCS / "research" / "52-中微公司一页式观察卡_2026-05-29.md",
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
