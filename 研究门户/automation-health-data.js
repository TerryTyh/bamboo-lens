window.BAMBOO_LENS_AUTOMATION_HEALTH = {
  "generated_at": "2026-05-17T20:00:02+08:00",
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
    "thresholdHours": 90,
    "items": [
      {
        "name": "official_candidates",
        "path": "云端研究简报系统/outputs/official_candidates.json",
        "timestamp": "2026-05-14T15:39:12+08:00",
        "ageHours": 76.3,
        "status": "healthy"
      },
      {
        "name": "event_store",
        "path": "云端研究简报系统/outputs/event_store.json",
        "timestamp": "2026-05-16T00:25:04+08:00",
        "ageHours": 43.6,
        "status": "healthy"
      },
      {
        "name": "decision_queue",
        "path": "云端研究简报系统/outputs/decision_queue.json",
        "timestamp": "2026-05-16T00:25:12+08:00",
        "ageHours": 43.6,
        "status": "healthy"
      },
      {
        "name": "company_page_overrides",
        "path": "云端研究简报系统/outputs/company_page_overrides.json",
        "timestamp": "2026-05-17T12:11:43+08:00",
        "ageHours": 7.8,
        "status": "healthy"
      },
      {
        "name": "readability_audit",
        "path": "云端研究简报系统/outputs/company_page_readability_audit.json",
        "timestamp": "2026-05-17T12:12:41+08:00",
        "ageHours": 7.8,
        "status": "healthy"
      },
      {
        "name": "mainline_audit",
        "path": "云端研究简报系统/outputs/company_page_mainline_audit.json",
        "timestamp": "2026-05-17T12:12:41+08:00",
        "ageHours": 7.8,
        "status": "healthy"
      },
      {
        "name": "market_snapshot",
        "path": "云端研究简报系统/outputs/market_snapshot.json",
        "timestamp": "2026-05-15T21:35:01+08:00",
        "ageHours": 46.4,
        "status": "healthy"
      },
      {
        "name": "daily_brief",
        "path": "云端研究简报系统/outputs/daily_brief.md",
        "timestamp": "2026-05-15T00:00:00+08:00",
        "ageHours": 68.0,
        "status": "healthy"
      },
      {
        "name": "morning_brief",
        "path": "云端研究简报系统/outputs/morning_brief.md",
        "timestamp": "2026-05-16T00:00:00+08:00",
        "ageHours": 44.0,
        "status": "healthy"
      }
    ],
    "stale": [],
    "missingTimestamp": []
  },
  "brief_guard": {
    "status": "healthy",
    "today": "2026-05-17",
    "morningSameDay": false,
    "dailySameDay": false,
    "dailyEmpty": true,
    "notes": [
      "今天是周末，晨报默认非发送日；没有当天标题不视为异常。",
      "fallback 日报为空，但周末不发送，暂不视为异常。"
    ]
  },
  "audits": {
    "status": "healthy",
    "readability": {
      "companies": 3,
      "healthy": 3,
      "review": 0,
      "at_risk": 0
    },
    "mainline": {
      "companies": 3,
      "healthy": 3,
      "review": 0,
      "weak": 0
    }
  },
  "market_snapshot_quality": {
    "status": "healthy",
    "expected": 8,
    "covered": 8,
    "issues": [],
    "warnings": [
      "Yahoo quote fetch failed, falling back to chart API: HTTP Error 401: Unauthorized"
    ],
    "errors": []
  }
};
