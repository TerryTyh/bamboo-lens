window.BAMBOO_LENS_AUTOMATION_HEALTH = {
  "generated_at": "2026-08-11T05:08:58+08:00",
  "status": "healthy",
  "status_label": "健康",
  "summary_notes": [
    "工作流文件：4/4 已存在。",
    "关键云端产物：12/12 已存在。",
    "门户数据文件：10/10 已存在。",
    "日报保护状态：healthy。",
    "公司页审计状态：healthy。",
    "行情覆盖状态：healthy。"
  ],
  "file_groups": [
    {
      "label": "GitHub Actions",
      "status": "healthy",
      "missing": [],
      "total": 4,
      "present": 4
    },
    {
      "label": "云端 outputs",
      "status": "healthy",
      "missing": [],
      "total": 12,
      "present": 12
    },
    {
      "label": "门户数据文件",
      "status": "healthy",
      "missing": [],
      "total": 10,
      "present": 10
    }
  ],
  "workflow_coverage": {
    "status": "healthy",
    "missing": {}
  },
  "freshness": {
    "status": "healthy",
    "thresholdHours": 42,
    "items": [
      {
        "name": "official_candidates",
        "path": "云端研究简报系统/outputs/official_candidates.json",
        "timestamp": "2026-08-10T12:44:33+08:00",
        "ageHours": 16.4,
        "status": "healthy"
      },
      {
        "name": "event_store",
        "path": "云端研究简报系统/outputs/event_store.json",
        "timestamp": "2026-08-11T05:08:58+08:00",
        "ageHours": 0.0,
        "status": "healthy"
      },
      {
        "name": "decision_queue",
        "path": "云端研究简报系统/outputs/decision_queue.json",
        "timestamp": "2026-08-11T05:08:58+08:00",
        "ageHours": 0.0,
        "status": "healthy"
      },
      {
        "name": "company_page_overrides",
        "path": "云端研究简报系统/outputs/company_page_overrides.json",
        "timestamp": "2026-08-11T05:08:58+08:00",
        "ageHours": 0.0,
        "status": "healthy"
      },
      {
        "name": "readability_audit",
        "path": "云端研究简报系统/outputs/company_page_readability_audit.json",
        "timestamp": "2026-08-11T05:08:58+08:00",
        "ageHours": 0.0,
        "status": "healthy"
      },
      {
        "name": "mainline_audit",
        "path": "云端研究简报系统/outputs/company_page_mainline_audit.json",
        "timestamp": "2026-08-11T05:08:58+08:00",
        "ageHours": 0.0,
        "status": "healthy"
      },
      {
        "name": "market_snapshot",
        "path": "云端研究简报系统/outputs/market_snapshot.json",
        "timestamp": "2026-08-10T20:44:40+08:00",
        "ageHours": 8.4,
        "status": "healthy"
      },
      {
        "name": "daily_brief",
        "path": "云端研究简报系统/outputs/daily_brief.md",
        "timestamp": "2026-08-10T00:00:00+08:00",
        "ageHours": 29.1,
        "status": "healthy"
      },
      {
        "name": "morning_brief",
        "path": "云端研究简报系统/outputs/morning_brief.md",
        "timestamp": "2026-08-11T00:00:00+08:00",
        "ageHours": 5.1,
        "status": "healthy"
      }
    ],
    "stale": [],
    "missingTimestamp": []
  },
  "brief_guard": {
    "status": "healthy",
    "today": "2026-08-11",
    "expectedMorningDate": "2026-08-11",
    "morningSameDay": true,
    "morningMeaningful": false,
    "dailySameDay": false,
    "dailyEmpty": false,
    "notes": [
      "当天晨报存在但正文不足，发送逻辑会回退到 fallback 日报。"
    ]
  },
  "audits": {
    "status": "healthy",
    "readability": {
      "companies": 6,
      "healthy": 6,
      "review": 0,
      "at_risk": 0
    },
    "mainline": {
      "companies": 6,
      "healthy": 6,
      "review": 0,
      "weak": 0
    }
  },
  "market_snapshot_quality": {
    "status": "healthy",
    "expected": 16,
    "covered": 16,
    "issues": [],
    "warnings": [
      "Yahoo quote fetch failed, falling back to chart API: HTTP Error 401: Unauthorized"
    ],
    "errors": []
  }
};
