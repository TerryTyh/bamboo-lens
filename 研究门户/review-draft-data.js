window.BAMBOO_LENS_REVIEW_DRAFTS = {
  "generated_at": "2026-05-18T14:56:45",
  "summary": {
    "total": 3,
    "companies": 2,
    "with_source_body": 2,
    "suppressed_count": 0,
    "readiness_counts": {
      "needs_source": 2,
      "low_investment_signal": 1
    },
    "priority_batch": []
  },
  "by_key": {
    "constellation::q1 2026 constellation energy corporation earnings conference call": {
      "draft_id": "auto-constellation-q1-2026-constellation-energy-corporation-earnings-conference-call",
      "company": "constellation",
      "company_name": "Constellation Energy",
      "title": "Q1 2026 Constellation Energy Corporation Earnings Conference Call",
      "date": "2026-05-11",
      "score": 14,
      "readiness_score": 21,
      "investment_signal_score": 5,
      "readiness_lane": "needs_source",
      "readiness_label": "待补正文",
      "review_batch_reason": "当前主要是标题或短事实，不适合直接进入正式事件。",
      "promotion_blockers": [
        "还没有抓到足够正文",
        "可读内容偏短"
      ],
      "source_url": "https://investors.constellationenergy.com/events-and-presentations/past-events",
      "portal_doc": "./docs/review-drafts/auto-constellation-q1-2026-constellation-energy-corporation-earnings-conference-call.md",
      "has_source_body": false,
      "company_page_writeback": {
        "targets": [
          "最新动态",
          "财务地图",
          "当前结论",
          "估值模型"
        ],
        "guidance": "若原文包含收入、利润率、现金流、指引或管理层口径，正式事件入库后必须同步更新公司主页的财务地图和估值/动作判断。"
      }
    },
    "tsmc::tsmc files annual report on form 20-f for 2025": {
      "draft_id": "auto-tsmc-tsmc-files-annual-report-on-form-20-f-for-2025",
      "company": "tsmc",
      "company_name": "TSMC",
      "title": "TSMC Files Annual Report on Form 20-F for 2025",
      "date": "2026-04-16",
      "score": 10,
      "readiness_score": 20,
      "investment_signal_score": 9,
      "readiness_lane": "needs_source",
      "readiness_label": "待读原文件",
      "review_batch_reason": "当前只读到了年报提交公告，不是年报正文；需要抓取 Form 20-F 或年报 PDF 后再进入深读。",
      "promotion_blockers": [
        "年报公告只说明文件已提交，未抓到年报正文里的经营和财务内容"
      ],
      "source_url": "http://pr.tsmc.com/english/news/3300",
      "portal_doc": "./docs/review-drafts/auto-tsmc-tsmc-files-annual-report-on-form-20-f-for-2025.md",
      "has_source_body": true,
      "company_page_writeback": {
        "targets": [
          "最新动态",
          "财务地图",
          "业务地图",
          "风险与跟踪重点"
        ],
        "guidance": "若读到的是年报正文而非提交公告，应沉淀业务结构、风险、资本开支、现金流和治理信息。"
      }
    },
    "tsmc::tsmc to sell 8.1% of vanguard international semiconductor": {
      "draft_id": "auto-tsmc-tsmc-to-sell-8-1-of-vanguard-international-semiconductor",
      "company": "tsmc",
      "company_name": "TSMC",
      "title": "TSMC to Sell 8.1% of Vanguard International Semiconductor",
      "date": "2026-05-15",
      "score": 8,
      "readiness_score": 12,
      "investment_signal_score": -7,
      "readiness_lane": "low_investment_signal",
      "readiness_label": "低投资信息密度",
      "review_batch_reason": "虽然有较长正文，但内容更偏品牌、演讲或泛宣传，不应排在正式事件深读前列。",
      "promotion_blockers": [],
      "source_url": "http://pr.tsmc.com/english/news/3314",
      "portal_doc": "./docs/review-drafts/auto-tsmc-tsmc-to-sell-8-1-of-vanguard-international-semiconductor.md",
      "has_source_body": true,
      "company_page_writeback": {
        "targets": [
          "最新动态",
          "当前结论",
          "跟踪重点"
        ],
        "guidance": "正式事件入库后，应判断是否改变当前结论、业务地图、财务地图、估值模型或跟踪重点。"
      }
    }
  },
  "companies": {
    "constellation": [
      {
        "draft_id": "auto-constellation-q1-2026-constellation-energy-corporation-earnings-conference-call",
        "company": "constellation",
        "company_name": "Constellation Energy",
        "title": "Q1 2026 Constellation Energy Corporation Earnings Conference Call",
        "date": "2026-05-11",
        "score": 14,
        "readiness_score": 21,
        "investment_signal_score": 5,
        "readiness_lane": "needs_source",
        "readiness_label": "待补正文",
        "review_batch_reason": "当前主要是标题或短事实，不适合直接进入正式事件。",
        "promotion_blockers": [
          "还没有抓到足够正文",
          "可读内容偏短"
        ],
        "source_url": "https://investors.constellationenergy.com/events-and-presentations/past-events",
        "portal_doc": "./docs/review-drafts/auto-constellation-q1-2026-constellation-energy-corporation-earnings-conference-call.md",
        "has_source_body": false,
        "company_page_writeback": {
          "targets": [
            "最新动态",
            "财务地图",
            "当前结论",
            "估值模型"
          ],
          "guidance": "若原文包含收入、利润率、现金流、指引或管理层口径，正式事件入库后必须同步更新公司主页的财务地图和估值/动作判断。"
        }
      }
    ],
    "tsmc": [
      {
        "draft_id": "auto-tsmc-tsmc-files-annual-report-on-form-20-f-for-2025",
        "company": "tsmc",
        "company_name": "TSMC",
        "title": "TSMC Files Annual Report on Form 20-F for 2025",
        "date": "2026-04-16",
        "score": 10,
        "readiness_score": 20,
        "investment_signal_score": 9,
        "readiness_lane": "needs_source",
        "readiness_label": "待读原文件",
        "review_batch_reason": "当前只读到了年报提交公告，不是年报正文；需要抓取 Form 20-F 或年报 PDF 后再进入深读。",
        "promotion_blockers": [
          "年报公告只说明文件已提交，未抓到年报正文里的经营和财务内容"
        ],
        "source_url": "http://pr.tsmc.com/english/news/3300",
        "portal_doc": "./docs/review-drafts/auto-tsmc-tsmc-files-annual-report-on-form-20-f-for-2025.md",
        "has_source_body": true,
        "company_page_writeback": {
          "targets": [
            "最新动态",
            "财务地图",
            "业务地图",
            "风险与跟踪重点"
          ],
          "guidance": "若读到的是年报正文而非提交公告，应沉淀业务结构、风险、资本开支、现金流和治理信息。"
        }
      },
      {
        "draft_id": "auto-tsmc-tsmc-to-sell-8-1-of-vanguard-international-semiconductor",
        "company": "tsmc",
        "company_name": "TSMC",
        "title": "TSMC to Sell 8.1% of Vanguard International Semiconductor",
        "date": "2026-05-15",
        "score": 8,
        "readiness_score": 12,
        "investment_signal_score": -7,
        "readiness_lane": "low_investment_signal",
        "readiness_label": "低投资信息密度",
        "review_batch_reason": "虽然有较长正文，但内容更偏品牌、演讲或泛宣传，不应排在正式事件深读前列。",
        "promotion_blockers": [],
        "source_url": "http://pr.tsmc.com/english/news/3314",
        "portal_doc": "./docs/review-drafts/auto-tsmc-tsmc-to-sell-8-1-of-vanguard-international-semiconductor.md",
        "has_source_body": true,
        "company_page_writeback": {
          "targets": [
            "最新动态",
            "当前结论",
            "跟踪重点"
          ],
          "guidance": "正式事件入库后，应判断是否改变当前结论、业务地图、财务地图、估值模型或跟踪重点。"
        }
      }
    ]
  },
  "items": [
    {
      "draft_id": "auto-constellation-q1-2026-constellation-energy-corporation-earnings-conference-call",
      "company": "constellation",
      "company_name": "Constellation Energy",
      "title": "Q1 2026 Constellation Energy Corporation Earnings Conference Call",
      "date": "2026-05-11",
      "score": 14,
      "readiness_score": 21,
      "investment_signal_score": 5,
      "readiness_lane": "needs_source",
      "readiness_label": "待补正文",
      "review_batch_reason": "当前主要是标题或短事实，不适合直接进入正式事件。",
      "promotion_blockers": [
        "还没有抓到足够正文",
        "可读内容偏短"
      ],
      "source_url": "https://investors.constellationenergy.com/events-and-presentations/past-events",
      "portal_doc": "./docs/review-drafts/auto-constellation-q1-2026-constellation-energy-corporation-earnings-conference-call.md",
      "has_source_body": false,
      "company_page_writeback": {
        "targets": [
          "最新动态",
          "财务地图",
          "当前结论",
          "估值模型"
        ],
        "guidance": "若原文包含收入、利润率、现金流、指引或管理层口径，正式事件入库后必须同步更新公司主页的财务地图和估值/动作判断。"
      }
    },
    {
      "draft_id": "auto-tsmc-tsmc-files-annual-report-on-form-20-f-for-2025",
      "company": "tsmc",
      "company_name": "TSMC",
      "title": "TSMC Files Annual Report on Form 20-F for 2025",
      "date": "2026-04-16",
      "score": 10,
      "readiness_score": 20,
      "investment_signal_score": 9,
      "readiness_lane": "needs_source",
      "readiness_label": "待读原文件",
      "review_batch_reason": "当前只读到了年报提交公告，不是年报正文；需要抓取 Form 20-F 或年报 PDF 后再进入深读。",
      "promotion_blockers": [
        "年报公告只说明文件已提交，未抓到年报正文里的经营和财务内容"
      ],
      "source_url": "http://pr.tsmc.com/english/news/3300",
      "portal_doc": "./docs/review-drafts/auto-tsmc-tsmc-files-annual-report-on-form-20-f-for-2025.md",
      "has_source_body": true,
      "company_page_writeback": {
        "targets": [
          "最新动态",
          "财务地图",
          "业务地图",
          "风险与跟踪重点"
        ],
        "guidance": "若读到的是年报正文而非提交公告，应沉淀业务结构、风险、资本开支、现金流和治理信息。"
      }
    },
    {
      "draft_id": "auto-tsmc-tsmc-to-sell-8-1-of-vanguard-international-semiconductor",
      "company": "tsmc",
      "company_name": "TSMC",
      "title": "TSMC to Sell 8.1% of Vanguard International Semiconductor",
      "date": "2026-05-15",
      "score": 8,
      "readiness_score": 12,
      "investment_signal_score": -7,
      "readiness_lane": "low_investment_signal",
      "readiness_label": "低投资信息密度",
      "review_batch_reason": "虽然有较长正文，但内容更偏品牌、演讲或泛宣传，不应排在正式事件深读前列。",
      "promotion_blockers": [],
      "source_url": "http://pr.tsmc.com/english/news/3314",
      "portal_doc": "./docs/review-drafts/auto-tsmc-tsmc-to-sell-8-1-of-vanguard-international-semiconductor.md",
      "has_source_body": true,
      "company_page_writeback": {
        "targets": [
          "最新动态",
          "当前结论",
          "跟踪重点"
        ],
        "guidance": "正式事件入库后，应判断是否改变当前结论、业务地图、财务地图、估值模型或跟踪重点。"
      }
    }
  ],
  "suppressed": []
};
