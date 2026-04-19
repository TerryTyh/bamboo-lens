function getLatestDateValue(dateText) {
  const normalized = (dateText || "").replace(/\//g, " ");
  const matches = normalized.match(/\d{4}-\d{2}(?:-\d{2})?/g) || [];
  if (!matches.length) return 0;

  const values = matches.map((item) => {
    const full = item.length === 7 ? `${item}-01` : item;
    return Number(full.replace(/-/g, ""));
  });

  return Math.max(...values);
}

function buildTimelineEvents() {
  return Object.entries(window.COMPANY_EVENT_META || {}).flatMap(([company, latest]) => {
    if (!latest?.events) return [];

    return latest.events.map((event, index) => ({
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

renderTimelineFeed();
