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
  const candidates = companies.reduce((total, [, items]) => total + (Array.isArray(items) ? items.length : 0), 0);
  const latestDates = companies.flatMap(([, items]) => (items || []).map((item) => item.date).filter(Boolean));
  const latestDate = latestDates.sort((a, b) => getLatestDateValue(b) - getLatestDateValue(a))[0] || "暂无";

  target.innerHTML = `
    <div class="cloud-stat-box">
      <span>候选线索</span>
      <strong>${candidates} 条</strong>
    </div>
    <div class="cloud-stat-box">
      <span>覆盖公司</span>
      <strong>${companies.length} 家</strong>
    </div>
    <div class="cloud-stat-box wide">
      <span>最新候选日期</span>
      <strong>${escapeHtml(latestDate)}</strong>
    </div>
  `;
}

function renderCloudSync() {
  renderMarkdownPreview("dailyBriefPreview", "../云端研究简报系统/outputs/daily_brief.md", 10);
  renderMarkdownPreview("weekendSyncPreview", "../云端研究简报系统/outputs/weekend_sync_summary.md", 9);
  renderCandidateStats();
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
renderTimelineFeed();
