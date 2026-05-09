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

function buildTimelineEvents() {
  return Object.entries(window.COMPANY_EVENT_META || {}).flatMap(([company, latest]) => {
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
    }));
  }).sort((a, b) => b.sortKey - a.sortKey);
}

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
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
  renderMarkdownPreview("dailyBriefPreview", "../云端研究简报系统/outputs/daily_brief.md", 10);
  renderMarkdownPreview("weekendSyncPreview", "../云端研究简报系统/outputs/weekend_sync_summary.md", 9);
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
  `;

  feed.innerHTML = payload.items.slice(0, 6).map((item) => {
    const updates = item.recommended_updates || [];
    return `
      <article class="decision-deposition-card ${escapeHtml(item.status)}">
        <div class="decision-card-top">
          <span class="decision-stage">${escapeHtml(item.quality || "待确认")}</span>
          <span class="decision-score">${escapeHtml(item.status || "ready")}</span>
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
        <a class="event-link" href="${escapeHtml(item.detail_link)}">查看事件详情</a>
      </article>
    `;
  }).join("");
}

function renderTimelineFeed() {
  const feed = document.getElementById("timelineFeed");
  const count = document.getElementById("timelineCount");
  if (!feed || !count || !window.COMPANY_EVENT_META) return;

  const events = buildTimelineEvents();
  const visibleEvents = events.slice(0, 12);
  count.textContent = `最新 ${visibleEvents.length} 条关键动态`;

  feed.innerHTML = visibleEvents.map((event) => `
    <article class="event-card rich-card timeline-card-item">
      <div class="event-meta">
        <span>${event.date}</span>
        <span>${event.type}</span>
      </div>
      <span class="company-tag ${event.tagClass}">${event.tag}</span>
      <h4>${event.companyName} | ${event.title}</h4>
      <p class="event-summary">${event.note}</p>
      <a class="event-link" href="./event.html?company=${encodeURIComponent(event.company)}&event=${event.index}&return=company&v=20260412-24">查看原文详情</a>
    </article>
  `).join("");
}

renderCloudSync();
renderDecisionQueue();
renderDecisionImpact();
renderDecisionDeposition();
renderTimelineFeed();
