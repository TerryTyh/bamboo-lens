const STATUS_ORDER = ["all", "pending", "waiting_material", "promoted", "skipped", "archived"];

const STATUS_LABELS = {
  all: "全部",
  pending: "待研判",
  waiting_material: "待材料",
  promoted: "已入库",
  skipped: "暂不研判",
  archived: "先存档",
};

let activeStatus = "all";

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function getCandidateDateValue(item) {
  if (Number.isFinite(item?.sort_key)) return item.sort_key;

  const text = item?.date || item?.fetched_at || "";
  const matches = String(text).match(/\d{4}[-年]?\d{1,2}(?:[-月]?\d{1,2})?/g) || [];
  if (!matches.length) return 0;

  const values = matches.map((dateText) => {
    const parts = dateText.match(/\d+/g) || [];
    const year = parts[0] || "0";
    const month = (parts[1] || "1").padStart(2, "0");
    const day = (parts[2] || "1").padStart(2, "0");
    return Number(`${year}${month}${day}`);
  });

  return Math.max(...values);
}

function flattenCandidates() {
  const payload = window.BAMBOO_LENS_CANDIDATES || { companies: {} };
  return Object.entries(payload.companies || {}).flatMap(([company, items]) =>
    (items || []).map((item) => ({
      ...item,
      company: item.company || company,
      candidate_status: item.candidate_status || "pending",
      status_label: item.status_label || "待研判",
      review_score: item.review_score || 0,
    }))
  ).sort((a, b) => {
    const statusDelta = (b.candidate_status === "pending") - (a.candidate_status === "pending");
    if (statusDelta) return statusDelta;
    const scoreDelta = (b.review_score || 0) - (a.review_score || 0);
    if (scoreDelta) return scoreDelta;
    return getCandidateDateValue(b) - getCandidateDateValue(a);
  });
}

function getStatusCounts(candidates) {
  return candidates.reduce((counts, item) => {
    counts[item.candidate_status] = (counts[item.candidate_status] || 0) + 1;
    counts.all += 1;
    return counts;
  }, { all: 0 });
}

function renderStats(candidates) {
  const total = document.getElementById("candidateTotal");
  const companyCount = document.getElementById("candidateCompanyCount");
  const pending = document.getElementById("candidatePendingCount");
  const promoted = document.getElementById("candidatePromotedCount");
  if (!total || !companyCount || !pending || !promoted) return;

  const companies = new Set(candidates.map((item) => item.company));
  const counts = getStatusCounts(candidates);
  total.textContent = String(candidates.length);
  companyCount.textContent = String(companies.size);
  pending.textContent = String(counts.pending || 0);
  promoted.textContent = String(counts.promoted || 0);
}

function renderFilters(candidates) {
  const node = document.getElementById("candidateFilters");
  if (!node) return;

  const counts = getStatusCounts(candidates);
  node.innerHTML = STATUS_ORDER
    .filter((status) => status === "all" || counts[status])
    .map((status) => `
      <button class="candidate-filter ${activeStatus === status ? "active" : ""}" data-status="${status}">
        <span>${STATUS_LABELS[status]}</span>
        <strong>${counts[status] || 0}</strong>
      </button>
    `).join("");

  node.querySelectorAll("[data-status]").forEach((button) => {
    button.addEventListener("click", () => {
      activeStatus = button.dataset.status;
      renderCandidates();
    });
  });
}

function buildTargetLink(item) {
  if (item.candidate_status === "promoted") {
    return `./company.html?company=${encodeURIComponent(item.company)}&v=20260505-1#companyUpdates`;
  }
  return item.source_url || "";
}

function buildTargetLabel(item) {
  if (item.candidate_status === "promoted") return "查看公司主页沉淀";
  if (item.source_url) return "打开官方来源";
  return "";
}

function renderCandidateCard(item) {
  const targetLink = buildTargetLink(item);
  const targetLabel = buildTargetLabel(item);
  return `
    <article class="candidate-review-card status-${escapeHtml(item.candidate_status)}">
      <div class="candidate-card-top">
        <span class="candidate-status-pill">${escapeHtml(item.status_label)}</span>
        <span class="candidate-score">Score ${escapeHtml(item.review_score || 0)}</span>
      </div>
      <div class="event-meta">
        <span>${escapeHtml(item.date || item.fetched_at || "日期待确认")}</span>
        <span>${escapeHtml(item.company_name || item.company)}</span>
      </div>
      <h3>${escapeHtml(item.title)}</h3>
      <p class="candidate-fact">${escapeHtml(item.fact || item.judgment || "待研判候选。")}</p>
      <div class="candidate-review-block">
        <strong>${escapeHtml(item.review_lane || "研判建议")}</strong>
        <p>${escapeHtml(item.review_reason || "尚未完成研判。")}</p>
      </div>
      <div class="candidate-review-block">
        <strong>下一步</strong>
        <p>${escapeHtml(item.read_next || "打开来源，确认是否具备正式事件质量。")}</p>
      </div>
      ${targetLink ? `<a class="event-link" href="${escapeHtml(targetLink)}" ${item.candidate_status === "promoted" ? "" : "target=\"_blank\" rel=\"noreferrer\""}>${escapeHtml(targetLabel)}</a>` : ""}
    </article>
  `;
}

function renderCandidates() {
  const feed = document.getElementById("candidateFeed");
  if (!feed) return;

  const candidates = flattenCandidates();
  renderStats(candidates);
  renderFilters(candidates);

  const visibleCandidates = activeStatus === "all"
    ? candidates
    : candidates.filter((item) => item.candidate_status === activeStatus);

  if (!visibleCandidates.length) {
    feed.innerHTML = '<p class="muted">当前筛选下没有候选线索。</p>';
    return;
  }

  feed.innerHTML = visibleCandidates.slice(0, 80).map(renderCandidateCard).join("");
}

renderCandidates();
