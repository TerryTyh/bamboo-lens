function getCandidateDateValue(item) {
  const text = item?.date || item?.fetched_at || "";
  const match = String(text).match(/\d{4}-?\d{2}-?\d{2}/);
  if (!match) return 0;
  return Number(match[0].replace(/-/g, ""));
}

function flattenCandidates() {
  const payload = window.BAMBOO_LENS_CANDIDATES || { companies: {} };
  return Object.entries(payload.companies || {}).flatMap(([company, items]) =>
    (items || []).map((item) => ({
      ...item,
      company,
    }))
  ).sort((a, b) => getCandidateDateValue(b) - getCandidateDateValue(a));
}

function renderCandidates() {
  const feed = document.getElementById("candidateFeed");
  const total = document.getElementById("candidateTotal");
  const companyCount = document.getElementById("candidateCompanyCount");
  if (!feed || !total || !companyCount) return;

  const candidates = flattenCandidates();
  const companies = new Set(candidates.map((item) => item.company));
  total.textContent = String(candidates.length);
  companyCount.textContent = String(companies.size);

  if (!candidates.length) {
    feed.innerHTML = '<p class="muted">当前还没有官方候选线索。</p>';
    return;
  }

  feed.innerHTML = candidates.slice(0, 40).map((item) => `
    <article class="event-card rich-card timeline-card-item">
      <div class="event-meta">
        <span>${item.date || item.fetched_at || "日期待确认"}</span>
        <span>${item.company_name || item.company}</span>
      </div>
      <h4>${item.title}</h4>
      <p class="event-summary">${item.fact || item.judgment || "待研判候选。"}</p>
      ${item.source_url ? `<a class="event-link" href="${item.source_url}" target="_blank" rel="noreferrer">打开官方来源</a>` : ""}
    </article>
  `).join("");
}

renderCandidates();
