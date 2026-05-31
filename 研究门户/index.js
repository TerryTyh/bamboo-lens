function getLatestDateValue(dateText) {
  const normalized = (dateText || "").replace(/\//g, " ");
  const matches = normalized.match(/\d{4}[-年]?\d{1,2}(?:[-月]?\d{1,2})?/g) || [];
  if (!matches.length) return 0;

  const values = matches.map((item) => {
    const parts = item.match(/\d+/g) || [];
    const year = parts[0] || "0";
    const month = (parts[1] || "1").padStart(2, "0");
    const day = (parts[2] || "1").padStart(2, "0");
    return Number(`${year}${month}${day}`);
  });

  return Math.max(...values);
}

function isExternalCompanyCandidate(item) {
  if (!item || item.candidate_status === "promoted") return false;
  if (item.type && item.type !== "官方候选") return false;

  const internalText = `${item.title || ""} ${item.source_excerpt || ""} ${item.source_body || ""}`;
  return !/研究池种子候选|观察卡待建|最小研究包待更新|待建|待更新/.test(internalText);
}

function buildTimelineEvents() {
  const eventStoreCompanies = window.BAMBOO_LENS_EVENT_STORE?.companies || {};
  const metaCompanies = window.COMPANY_EVENT_META || {};
  const candidateCompanies = window.BAMBOO_LENS_CANDIDATES?.companies || {};
  const officialCandidates = Object.entries(candidateCompanies).flatMap(([company, items]) => {
    const meta = metaCompanies[company] || {};
    return (items || [])
      .filter(isExternalCompanyCandidate)
      .map((item, index) => ({
        company,
        companyName: item.company_name || meta.displayName || company,
        tag: meta.tag || "公司新闻",
        tagClass: meta.tagClass || "",
        index,
        date: item.date,
        type: "公司新闻候选",
        title: item.title,
        note: item.content_summary || item.source_excerpt || "来自公司官方来源的候选新闻，尚未完成正式研判。",
        sortKey: Number(item.sort_key) || getLatestDateValue(item.date),
        link: item.source_url || "./candidates.html",
        linkLabel: item.source_url ? "查看官方来源" : "查看候选台",
        external: Boolean(item.source_url),
      }));
  });

  if (Object.keys(eventStoreCompanies).length) {
    const formalEvents = Object.entries(eventStoreCompanies).flatMap(([company, companyData]) => {
      const meta = metaCompanies[company] || {};
      const events = companyData?.events || [];
      return events.map((event, index) => ({
        company,
        companyName: meta.displayName || companyData.name || company,
        tag: meta.tag || companyData.market || "公司",
        tagClass: meta.tagClass || "",
        index,
        date: event.date,
        type: event.type,
        title: event.title,
        note: event.fact || event.judgment || "",
        sortKey: Number(event.sort_key) || getLatestDateValue(event.date),
        link: `./event.html?company=${encodeURIComponent(company)}&event=${index}&return=company&v=20260412-24`,
        linkLabel: "查看原文详情",
        external: false,
      }));
    });
    return [...formalEvents, ...officialCandidates].sort((a, b) => b.sortKey - a.sortKey);
  }

  const fallbackEvents = Object.entries(metaCompanies).flatMap(([company, latest]) => {
    if (!latest?.events) return [];
    return [...latest.events]
      .sort((a, b) => getLatestDateValue(b.date) - getLatestDateValue(a.date))
      .map((event, index) => ({
      company,
      companyName: window.getCompanyDisplayName(company),
      tag: latest.tag,
      tagClass: latest.tagClass,
      index,
      date: event.date,
      type: event.type,
      title: event.title,
      note: event.note,
      sortKey: getLatestDateValue(event.date),
      link: `./event.html?company=${encodeURIComponent(company)}&event=${index}&return=company&v=20260412-24`,
      linkLabel: "查看原文详情",
      external: false,
    }));
  });
  return [...fallbackEvents, ...officialCandidates].sort((a, b) => b.sortKey - a.sortKey);
}

function isChineseCompanyEvent(event) {
  const tagText = `${event.tag || ""} ${event.tagClass || ""} ${event.companyName || ""}`;
  return /A 股|港股|中概|\bcn\b|\bhk\b/.test(tagText);
}

function selectDiverseTimelineEvents(events, limit = 12, perCompanyLimit = 2, chineseShareTarget = 0.4) {
  const selected = [];
  const selectedKeys = new Set();
  const companyCounts = {};
  const chineseTarget = Math.min(
    Math.ceil(limit * chineseShareTarget),
    events.filter(isChineseCompanyEvent).length,
  );

  const makeKey = (event) => `${event.company || event.companyName || ""}-${event.index}-${event.title}`;
  const canSelect = (event) => {
    const company = event.company || event.companyName || "";
    return !selectedKeys.has(makeKey(event)) && (companyCounts[company] || 0) < perCompanyLimit;
  };
  const addEvent = (event) => {
    const company = event.company || event.companyName || "";
    selected.push(event);
    selectedKeys.add(makeKey(event));
    companyCounts[company] = (companyCounts[company] || 0) + 1;
  };

  events.forEach((event) => {
    if (selected.length >= limit) return;
    if (!isChineseCompanyEvent(event)) return;
    if (selected.filter(isChineseCompanyEvent).length >= chineseTarget) return;
    if (!canSelect(event)) return;
    addEvent(event);
  });

  events.forEach((event) => {
    if (selected.length >= limit) return;
    if (!canSelect(event)) return;
    addEvent(event);
  });

  return selected.sort((a, b) => b.sortKey - a.sortKey);
}

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

const COCKPIT_VALUATION_WATCH = {
  alibaba: {
    name: "阿里巴巴",
    symbol: "9988.HK",
    range: { low: 137.6, mid: 155.5, high: 173.5 },
    currency: "HK$",
    fundamentalState: "云 AI 强化，但即时零售投入、自由现金流和回购质量仍要验证。",
    action: {
      low: "复核机会，但不能只因便宜行动；先看云 EBITA、自由现金流和回购是否继续支撑估值中枢。",
      belowMid: "低于中枢，适合复核机会；动作前确认云增长没有被即时零售投入抵消。",
      nearMid: "接近中枢，继续观察，等下一季云收入、云 EBITA、自由现金流和回购执行。",
      nearHigh: "接近上沿，控制追价；除非云 AI 商业化和现金流同步改善。",
      expensive: "偏贵，等待验证；只有估值中枢被云 AI 和现金流共同上修后再提高动作。",
    },
  },
  luxshare: {
    name: "立讯精密",
    symbol: "002475.SZ",
    range: { low: 54.9, mid: 59.7, high: 64.5 },
    currency: "¥",
    fundamentalState: "复杂制造平台逻辑仍在，但现金流、存货、应收和新业务利润质量处于强验证期。",
    action: {
      low: "复核机会，但先确认客户、现金流和新业务质量没有恶化。",
      belowMid: "低于中枢，可优先复核；必须等应付、存货、应收三项没有同步恶化。",
      nearMid: "接近中枢，继续观察；重点等下一季现金流质量和汽车/数据中心业务盈利质量。",
      nearHigh: "接近上沿，不要因为上涨追价；若 Q1 没证明现金流修复，以等待验证为主。",
      expensive: "偏贵，控制追价；除非现金流明显修复、新业务利润率清晰、客户集中风险没有扩大。",
    },
  },
};

function getMarketSnapshotCompany(companyId) {
  return window.BAMBOO_LENS_MARKET_SNAPSHOT?.companies?.[companyId] || null;
}

function getPrimaryPrice(companyId) {
  const company = getMarketSnapshotCompany(companyId);
  const primary = company?.primary || null;
  if (!primary || typeof primary.price !== "number") return null;
  return {
    price: primary.price,
    displayPrice: primary.display?.price || `${primary.currency || ""}${primary.price}`,
    changePercent: primary.display?.changePercent || "",
    marketTime: primary.marketTime,
  };
}

function classifyPricePosition(price, range) {
  if (typeof price !== "number" || !range) {
    return { status: "待更新", key: "nearMid", severity: 0 };
  }
  if (price < range.low) return { status: "低于合理区间", key: "low", severity: 2 };
  if (price < range.mid) return { status: "低于中枢", key: "belowMid", severity: 1 };
  if (price <= range.high) {
    const progress = (price - range.mid) / (range.high - range.mid || 1);
    return progress >= 0.6
      ? { status: "接近上沿", key: "nearHigh", severity: 3 }
      : { status: "接近中枢", key: "nearMid", severity: 1 };
  }
  return { status: "偏贵", key: "expensive", severity: 4 };
}

function formatRange(range, currency) {
  return `${currency}${range.low}-${range.high}，中枢 ${currency}${range.mid}`;
}

function buildCockpitActionItems() {
  return Object.entries(COCKPIT_VALUATION_WATCH).map(([companyId, config]) => {
    const quote = getPrimaryPrice(companyId);
    const position = classifyPricePosition(quote?.price, config.range);
    return {
      companyId,
      ...config,
      quote,
      position,
      actionText: config.action[position.key] || config.action.nearMid,
    };
  }).sort((a, b) => b.position.severity - a.position.severity);
}

function renderDecisionCockpit() {
  const latestTarget = document.getElementById("cockpitLatestChange");
  const focusTarget = document.getElementById("cockpitFocusCompany");
  const actionTarget = document.getElementById("cockpitActionTrigger");

  if (latestTarget) {
    const latest = buildTimelineEvents()[0];
    if (latest) {
      latestTarget.innerHTML = `
        <span class="status-label">最近发生了什么</span>
        <div class="event-meta">
          <span>${escapeHtml(latest.date || "日期待确认")}</span>
          <span>${escapeHtml(latest.companyName)}</span>
        </div>
        <h3>${escapeHtml(latest.title)}</h3>
        <p>${escapeHtml(latest.note || "这条事件已进入正式事件库，建议打开详情看原文摘要和分析。")}</p>
        <a class="event-link" href="${escapeHtml(latest.link || `./event.html?company=${encodeURIComponent(latest.company)}&event=${latest.index}&return=company&v=20260516-1`)}"${latest.external ? ' target="_blank" rel="noreferrer"' : ""}>${escapeHtml(latest.linkLabel || "查看事件详情")}</a>
      `;
    }
  }

  if (focusTarget) {
    const queueItems = window.BAMBOO_LENS_DECISION_QUEUE?.items || [];
    const formalItem = queueItems.find((item) => item.source_type === "formal_event") || queueItems[0];
    if (formalItem) {
      const link = getDecisionLink(formalItem);
      const externalAttrs = formalItem.source_type === "official_candidate" && formalItem.source_url
        ? ' target="_blank" rel="noreferrer"'
        : "";
      focusTarget.innerHTML = `
        <span class="status-label">当前最该看谁</span>
        <div class="event-meta">
          <span>${escapeHtml(formalItem.date || "日期待确认")}</span>
          <span>${escapeHtml(formalItem.company_name || formalItem.company)}</span>
        </div>
        <h3>${escapeHtml(formalItem.title)}</h3>
        <p><strong>${escapeHtml(formalItem.decision_action || "先读原文")}</strong>：${escapeHtml(formalItem.why || "这条内容在当前决策队列里优先级较高。")}</p>
        <a class="event-link" href="${escapeHtml(link)}"${externalAttrs}>${getDecisionLinkLabel(formalItem)}</a>
      `;
    }
  }

  if (actionTarget) {
    const items = buildCockpitActionItems();
    const primary = items[0];
    if (primary) {
      actionTarget.innerHTML = `
        <span class="status-label">有没有动作触发</span>
        <h3>${escapeHtml(primary.name)}：${escapeHtml(primary.position.status)}</h3>
        <p>${escapeHtml(primary.quote?.displayPrice || "暂无最新价格")}；第一版合理区间约 ${escapeHtml(formatRange(primary.range, primary.currency))}。</p>
        <p><strong>动作提示：</strong>${escapeHtml(primary.actionText)}</p>
        <div class="cockpit-price-row">
          ${items.map((item) => `
            <div>
              <small>${escapeHtml(item.name)}</small>
              <b>${escapeHtml(item.position.status)}</b>
              <span>${escapeHtml(item.quote?.displayPrice || "暂无价格")}</span>
            </div>
          `).join("")}
        </div>
        <a class="event-link" href="./company.html?company=${encodeURIComponent(primary.companyId)}&v=20260516-1#companyValuationModelSection">查看估值动作</a>
      `;
    }
  }
}

function compactMarkdown(markdown, maxLines = 9) {
  const lines = String(markdown || "")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .filter((line) => !/^[-*_]{3,}$/.test(line))
    .slice(0, maxLines);

  if (!lines.length) return "<p>暂无可展示内容。等云端同步完成后，这里会自动出现最新摘要。</p>";

  return lines.map((line) => {
    const cleaned = escapeHtml(line.replace(/^#{1,6}\s*/, "").replace(/^\-\s*/, ""));
    if (/^竹鉴日报|^周末同步|^#/.test(line)) return `<h4>${cleaned}</h4>`;
    if (/^一句话结论|^明日重点|^本周新增|^候选池|^建议阅读顺序|^最新日报/.test(line)) return `<strong>${cleaned}</strong>`;
    return `<p>${cleaned}</p>`;
  }).join("");
}

async function fetchText(path) {
  const response = await fetch(path, { cache: "no-store" });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.text();
}

async function renderMarkdownPreview(targetId, path, maxLines) {
  const target = document.getElementById(targetId);
  if (!target) return;

  try {
    const markdown = await fetchText(path);
    target.classList.remove("loading");
    target.innerHTML = compactMarkdown(markdown, maxLines);
  } catch (error) {
    target.classList.remove("loading");
    target.innerHTML = `
      <p>暂时没有读取到这份云端产物。</p>
      <p class="muted">如果刚打开电脑，可以先运行「同步并启动竹鉴.command」，它会拉取云端输出并生成周末复盘。</p>
    `;
  }
}

function renderCandidateStats() {
  const target = document.getElementById("candidateStats");
  const payload = window.BAMBOO_LENS_CANDIDATES;
  if (!target || !payload?.companies) return;

  const companies = Object.entries(payload.companies);
  const candidates = companies.flatMap(([, items]) => Array.isArray(items) ? items : []);
  const pendingCount = candidates.filter((item) => item.candidate_status === "pending").length;
  const promotedCount = candidates.filter((item) => item.candidate_status === "promoted").length;

  target.innerHTML = `
    <div class="cloud-stat-box">
      <span>待研判</span>
      <strong>${pendingCount} 条</strong>
    </div>
    <div class="cloud-stat-box">
      <span>已入库</span>
      <strong>${promotedCount} 条</strong>
    </div>
    <div class="cloud-stat-box wide">
      <span>覆盖公司</span>
      <strong>${companies.length} 家</strong>
    </div>
  `;
}

function renderCloudSync() {
  renderMarkdownPreview("dailyBriefPreview", "./docs/briefs/daily_brief.md", 10);
  renderMarkdownPreview("weekendSyncPreview", "./docs/briefs/weekend_sync_summary.md", 9);
  renderCandidateStats();
}

function getDecisionLink(item) {
  if (item.source_type === "formal_event" && Number.isInteger(item.event_index)) {
    return `./event.html?company=${encodeURIComponent(item.company)}&event=${item.event_index}&return=company&v=20260412-24`;
  }
  if (item.source_url) return item.source_url;
  return "./candidates.html";
}

function getDecisionLinkLabel(item) {
  if (item.source_type === "formal_event") return "查看事件详情";
  if (item.source_url) return "打开官方原文";
  return "进入候选池";
}

function renderDecisionQueue() {
  const feed = document.getElementById("decisionQueueFeed");
  const stats = document.getElementById("decisionStats");
  const payload = window.BAMBOO_LENS_DECISION_QUEUE;
  if (!feed || !stats) return;

  if (!payload?.items?.length) {
    stats.innerHTML = "<span>暂无待处理</span>";
    feed.innerHTML = '<p class="muted">当前没有进入决策队列的事件或候选。</p>';
    return;
  }

  const items = payload.items.slice(0, 8);
  const summary = payload.summary || {};
  stats.innerHTML = `
    <span>队列 ${summary.total || payload.items.length} 条</span>
    <span>正式事件 ${summary.formal_events || 0}</span>
    <span>候选 ${summary.official_candidates || 0}</span>
  `;

  feed.innerHTML = items.map((item) => {
    const isCandidate = item.source_type === "official_candidate";
    const link = getDecisionLink(item);
    const externalAttrs = isCandidate && item.source_url ? ' target="_blank" rel="noreferrer"' : "";
    return `
      <article class="decision-card ${isCandidate ? "candidate" : "formal"}">
        <div class="decision-card-top">
          <span class="decision-stage">${escapeHtml(item.stage)}</span>
          <span class="decision-score">Score ${item.score}</span>
        </div>
        <div class="event-meta">
          <span>${escapeHtml(item.date || "日期待确认")}</span>
          <span>${escapeHtml(item.company_name)}</span>
        </div>
        <h3>${escapeHtml(item.title)}</h3>
        <div class="decision-action-row">
          <span>${escapeHtml(item.priority || "待定")}</span>
          <strong>${escapeHtml(item.decision_action)}</strong>
        </div>
        <p>${escapeHtml(item.why)}</p>
        <div class="decision-next">
          <strong>下一步</strong>
          <p>${escapeHtml(item.read_next)}</p>
        </div>
        <a class="event-link" href="${link}"${externalAttrs}>${getDecisionLinkLabel(item)}</a>
      </article>
    `;
  }).join("");
}

function renderDecisionImpact() {
  const feed = document.getElementById("decisionImpactFeed");
  const stats = document.getElementById("decisionImpactStats");
  const payload = window.BAMBOO_LENS_DECISION_IMPACT;
  if (!feed || !stats) return;

  if (!payload?.items?.length) {
    stats.innerHTML = "<span>暂无影响记录</span>";
    feed.innerHTML = '<p class="muted">正式事件研判后，这里会显示业务、估值和动作影响。</p>';
    return;
  }

  const summary = payload.summary || {};
  stats.innerHTML = `
    <span>影响 ${summary.total || payload.items.length} 条</span>
    <span>需估值更新 ${summary.valuation_update_needed || 0}</span>
    <span>正向强化 ${summary.positive || 0}</span>
  `;

  feed.innerHTML = payload.items.slice(0, 6).map((item) => `
    <article class="decision-impact-card">
      <div class="decision-card-top">
        <span class="decision-stage">${escapeHtml(item.direction)}</span>
        <span class="decision-score">${escapeHtml(item.trigger_type)}</span>
      </div>
      <div class="event-meta">
        <span>${escapeHtml(item.event_date || "日期待确认")}</span>
        <span>${escapeHtml(item.company_name)}</span>
      </div>
      <h3>${escapeHtml(item.event_title)}</h3>
      <div class="impact-chip-row">
        ${(item.dimensions || []).map((dimension) => `<span>${escapeHtml(dimension)}</span>`).join("")}
        ${item.valuation_update_needed ? "<strong>需看估值</strong>" : ""}
      </div>
      <div class="decision-output-box">
        <strong>${escapeHtml(item.decision_output?.confidence_change || "维持确信度")}</strong>
        <p>${escapeHtml(item.decision_output?.portfolio_hint || "维持观察，等待下一次验证。")}</p>
        <small>应更新：${escapeHtml((item.decision_output?.update_targets || []).join(" / ") || "当前结论")}</small>
      </div>
      <p><strong>判断变化：</strong>${escapeHtml(item.decision_change)}</p>
      <p><strong>估值/动作：</strong>${escapeHtml(item.valuation_impact)}</p>
      <div class="decision-next">
        <strong>下一次验证</strong>
        <p>${escapeHtml((item.next_verification || []).join("；") || "等待下一次正式披露。")}</p>
      </div>
      <a class="event-link" href="${escapeHtml(item.detail_link)}">查看事件详情</a>
    </article>
  `).join("");
}

function renderDecisionDeposition() {
  const feed = document.getElementById("decisionDepositionFeed");
  const stats = document.getElementById("decisionDepositionStats");
  const payload = window.BAMBOO_LENS_DECISION_DEPOSITION;
  if (!feed || !stats) return;

  if (!payload?.items?.length) {
    stats.innerHTML = "<span>暂无回写计划</span>";
    feed.innerHTML = '<p class="muted">正式事件通过研判后，这里会显示公司主页应更新的板块。</p>';
    return;
  }

  const summary = payload.summary || {};
  stats.innerHTML = `
    <span>计划 ${summary.total || payload.items.length} 条</span>
    <span>可回写 ${summary.ready || 0}</span>
    <span>需估值/财务更新 ${summary.needs_model_update || 0}</span>
    <span>仅事件流 ${summary.watch_only || 0}</span>
  `;

  feed.innerHTML = payload.items.slice(0, 6).map((item) => {
    const updates = item.recommended_updates || [];
    const blockers = item.writeback_blockers || [];
    return `
      <article class="decision-deposition-card ${escapeHtml(item.status)}">
        <div class="decision-card-top">
          <span class="decision-stage">${escapeHtml(item.quality || "待确认")}</span>
          <span class="decision-score">${escapeHtml(item.status_label || item.status || "ready")}${item.writeback_quality_score ? ` · ${escapeHtml(item.writeback_quality_score)}` : ""}</span>
        </div>
        <div class="event-meta">
          <span>${escapeHtml(item.event_date || "日期待确认")}</span>
          <span>${escapeHtml(item.company_name)}</span>
        </div>
        <h3>${escapeHtml(item.event_title)}</h3>
        <div class="impact-chip-row">
          ${(item.update_targets || []).map((target) => `<span>${escapeHtml(target)}</span>`).join("")}
        </div>
        <p><strong>为什么要沉淀：</strong>${escapeHtml(item.reason || "这条事件改变了公司当前判断。")}</p>
        <div class="deposition-update-list">
          ${updates.map((update) => `
            <div class="deposition-update-item">
              <strong>${escapeHtml(update.target)}</strong>
              <small>${escapeHtml((update.fields || []).join(" / "))}</small>
              <p>${escapeHtml(update.suggestion)}</p>
            </div>
          `).join("")}
        </div>
        ${blockers.length ? `<p><strong>暂不回写原因：</strong>${escapeHtml(blockers.join("；"))}</p>` : ""}
        <a class="event-link" href="${escapeHtml(item.detail_link)}">查看事件详情</a>
      </article>
    `;
  }).join("");
}

function renderResearchPool() {
  const summaryTarget = document.getElementById("researchPoolSummary");
  const companyTarget = document.getElementById("researchPoolCompanies");
  const cadenceTarget = document.getElementById("researchPoolCadence");
  const discoveryTarget = document.getElementById("weeklyDiscoveryList");
  const payload = window.BAMBOO_LENS_RESEARCH_POOL;
  if (!summaryTarget || !companyTarget || !cadenceTarget || !payload) return;

  const summary = payload.summary || {};
  summaryTarget.innerHTML = `
    <article class="research-pool-card">
      <span>A 层核心</span>
      <strong>${escapeHtml(summary.a_core ?? "-")} 家</strong>
      <p>已有公司主页、估值模型和动态回写机制；但不享有永久资格。</p>
    </article>
    <article class="research-pool-card">
      <span>B 层观察</span>
      <strong>${escapeHtml(summary.b_watch ?? "-")} 家</strong>
      <p>先做最小研究包，等关键验证点兑现后再决定是否建主页。</p>
    </article>
    <article class="research-pool-card">
      <span>下一步</span>
      <strong>复评 + 发现</strong>
      <p>${escapeHtml(summary.next_focus || "先稳定 V2 闭环，再扩展新公司。")}</p>
    </article>
  `;

  companyTarget.innerHTML = (payload.companies || []).map((company) => `
    <article class="pool-company-row level-${escapeHtml(String(company.level || "").toLowerCase())}">
      <div>
        <strong>${escapeHtml(company.name)}</strong>
        <span>${escapeHtml(company.thesis || "")}</span>
      </div>
      <div>
        <b>${escapeHtml(company.level_label || company.level || "待评估")}</b>
        <small>下次复评：${escapeHtml(company.next_review || "待定")}</small>
      </div>
      <p>${escapeHtml(company.review_result ? `本轮复评：${company.review_result}。${company.review_note || ""}` : company.review_focus || "")}</p>
    </article>
  `).join("");

  cadenceTarget.innerHTML = (payload.cadence || []).map((item) => `
    <article class="pool-cadence-row">
      <strong>${escapeHtml(item.name)}</strong>
      <p>${escapeHtml(item.target)}</p>
      <small>${escapeHtml(item.output)}</small>
    </article>
  `).join("");

  if (discoveryTarget) {
    discoveryTarget.innerHTML = (payload.weekly_discovery || []).map((item) => `
      <article class="weekly-discovery-row level-${escapeHtml(String(item.initial_level || "").toLowerCase())}">
        <div>
          <strong>${escapeHtml(item.company)}</strong>
          <span>${escapeHtml(item.theme)}</span>
        </div>
        <p>${escapeHtml(item.trigger)}</p>
        <div>
          <b>${escapeHtml(item.initial_level_label || item.initial_level || "初筛")}</b>
          <small>${escapeHtml(item.next_step || "等待下一步材料")}</small>
        </div>
      </article>
    `).join("");
  }
}

function renderTimelineFeed() {
  const feed = document.getElementById("timelineFeed");
  const count = document.getElementById("timelineCount");
  if (!feed || !count) return;

  const events = buildTimelineEvents();
  const visibleEvents = selectDiverseTimelineEvents(events, 12, 2);
  const visibleCompanies = new Set(visibleEvents.map((event) => event.company || event.companyName)).size;
  const chineseCompanies = new Set(
    visibleEvents.filter(isChineseCompanyEvent).map((event) => event.company || event.companyName),
  ).size;
  count.textContent = `最新 ${visibleEvents.length} 条关键动态 · 覆盖 ${visibleCompanies} 家 · 中企 ${chineseCompanies} 家`;

  feed.innerHTML = visibleEvents.map((event) => `
    <article class="event-card rich-card timeline-card-item">
      <div class="event-meta">
        <span>${event.date}</span>
        <span>${event.type}</span>
      </div>
      <span class="company-tag ${event.tagClass}">${event.tag}</span>
      <h4>${event.companyName} | ${event.title}</h4>
      <p class="event-summary">${event.note}</p>
      <a class="event-link" href="${escapeHtml(event.link || `./event.html?company=${encodeURIComponent(event.company)}&event=${event.index}&return=company&v=20260412-24`)}"${event.external ? ' target="_blank" rel="noreferrer"' : ""}>${escapeHtml(event.linkLabel || "查看原文详情")}</a>
    </article>
  `).join("");
}

renderDecisionCockpit();
renderCloudSync();
renderDecisionQueue();
renderDecisionImpact();
renderDecisionDeposition();
renderResearchPool();
renderTimelineFeed();
