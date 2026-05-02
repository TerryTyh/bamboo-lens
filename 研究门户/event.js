function getLatestEventsForEventPage(sectionData) {
  return sortEventsNewestFirst([
    ...(sectionData.events || []),
    {
      date: "待验证",
      type: "关键验证点",
      title: "下一次关键验证点",
      note: sectionData.nextCheck,
      analysis: sectionData.valuationImpact,
      action: "等待验证",
      priority: "P1",
    },
  ]);
}

function getEventDateValue(record) {
  const matches = String(record?.date || "").match(/\d{4}[-年]?\d{1,2}(?:[-月]?\d{1,2})?/g) || [];
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

function sortEventsNewestFirst(records) {
  return [...records].sort((a, b) => getEventDateValue(b) - getEventDateValue(a));
}

function cleanMarkdownValue(value) {
  return (value || "")
    .replace(/^\s{2,}/gm, "")
    .replace(/`/g, "")
    .trim();
}

function buildFallbackEventRecord(event, sectionData) {
  return {
    ...event,
    title: event.title,
    date: event.date,
    type: event.type,
    fact: event.fact || event.note,
    judgment: event.judgment || event.analysis || sectionData.businessImpact,
    action: event.action || "维持跟踪",
    priority: event.priority || "P2",
  };
}

function normalizeEventStoreRecord(event) {
  return {
    title: event.title,
    date: event.date,
    type: event.type,
    fact: event.fact,
    judgment: event.judgment,
    action: event.action,
    priority: event.priority,
    sourceSummary: event.source_summary,
    evidence: event.evidence,
    businessAnalysis: event.business_analysis,
    valuationAnalysis: event.valuation_analysis,
    verification: event.verification,
    sourceLinks: event.source_url ? [{ label: "官方来源", href: event.source_url }] : [],
    sortKey: event.sort_key,
    note: event.fact,
    analysis: event.judgment,
  };
}

function getEventStoreRecords(company) {
  const events = window.BAMBOO_LENS_EVENT_STORE?.companies?.[company]?.events || [];
  return events.map(normalizeEventStoreRecord);
}

function renderSourceLinks(links) {
  const node = document.getElementById("eventSourceLinks");
  if (!node) return;

  if (!links?.length) {
    node.innerHTML = '<p class="muted">暂无可直接打开的原文链接。</p>';
    return;
  }

  node.innerHTML = links.map((link) => `
    <a class="source-link" href="${link.href}" target="_blank" rel="noreferrer">${link.label}</a>
  `).join("");
}

function renderList(id, items) {
  const node = document.getElementById(id);
  if (!node) return;

  if (!items?.length) {
    node.innerHTML = "<li>暂无</li>";
    return;
  }

  node.innerHTML = items.map((item) => `<li>${item}</li>`).join("");
}

async function parseEventRecordsFromMarkdown(sourceDoc) {
  if (!sourceDoc) return [];

  const response = await fetch(sourceDoc);
  if (!response.ok) {
    throw new Error(`Load failed: HTTP ${response.status}`);
  }

  const markdown = await response.text();
  const blocks = [];
  const blockRegex =
    /### 动态 \d+：([^\n]+)\n\n- 日期：([^\n]+)\n- 事件类型：([^\n]+)\n- 事实：\n([\s\S]*?)\n- 判断：\n([\s\S]*?)\n- 动作：\n\s*`?([^`\n]+)`?\n- 优先级：\n\s*`?([^`\n]+)`?/g;

  let match;
  while ((match = blockRegex.exec(markdown)) !== null) {
    blocks.push({
      title: cleanMarkdownValue(match[1]),
      date: cleanMarkdownValue(match[2]),
      type: cleanMarkdownValue(match[3]),
      fact: cleanMarkdownValue(match[4]),
      judgment: cleanMarkdownValue(match[5]),
      action: cleanMarkdownValue(match[6]),
      priority: cleanMarkdownValue(match[7]),
    });
  }

  return sortEventsNewestFirst(blocks);
}

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value || "暂无";
}

function renderParagraphs(id, paragraphs) {
  const node = document.getElementById(id);
  if (!node) return;

  const items = Array.isArray(paragraphs) ? paragraphs : [paragraphs].filter(Boolean);
  if (!items.length) {
    node.innerHTML = "<p>暂无</p>";
    return;
  }

  node.innerHTML = items.map((item) => `<p>${item}</p>`).join("");
}

async function initEventPage() {
  const titleNode = document.getElementById("eventTitle");
  if (!titleNode || !window.COMPANY_EVENT_META) return;

  const params = new URLSearchParams(window.location.search);
  const company = params.get("company");
  const eventIndex = Number(params.get("event") || "0");
  const page = Number(params.get("page") || "1");
  const sectionData = window.COMPANY_EVENT_META[company];
  const companyData = sectionData;
  if (!companyData || !sectionData) return;

  const storeEvents = getEventStoreRecords(company);
  const events = storeEvents.length ? storeEvents : getLatestEventsForEventPage(sectionData);
  const event = events[eventIndex];
  if (!event) return;

  let parsedEvents = [];
  try {
    parsedEvents = await parseEventRecordsFromMarkdown(sectionData.sourceDoc);
  } catch (error) {
    console.error(error);
  }

  const eventRecord =
    storeEvents[eventIndex] || parsedEvents[eventIndex] || buildFallbackEventRecord(event, sectionData);

  document.title = `${window.getCompanyDisplayName(company)} | ${eventRecord.title}`;
  document.getElementById("eventCompanyTitle").textContent = window.getCompanyDisplayName(company);
  document.getElementById("eventPageSummary").textContent = sectionData.summary;
  setText("eventTitle", eventRecord.title);
  setText("eventDate", eventRecord.date);
  setText("eventType", eventRecord.type);
  setText("eventFact", eventRecord.fact);
  setText("eventJudgment", eventRecord.judgment);
  setText("eventAction", eventRecord.action);
  setText("eventPriority", eventRecord.priority);
  renderParagraphs("eventSourceSummary", eventRecord.sourceSummary || "这条记录还没有补原文摘要，后续不应作为高质量样板。");
  renderSourceLinks(eventRecord.sourceLinks || []);
  renderList("eventEvidenceList", eventRecord.evidence || []);
  renderList("eventVerificationList", eventRecord.verification || []);
  setText("eventSummary", eventRecord.note || event.note);
  setText("eventAnalysis", eventRecord.analysis || eventRecord.judgment);
  setText("eventBusinessImpact", eventRecord.businessAnalysis || sectionData.businessImpact);
  setText("eventValuationImpact", eventRecord.valuationAnalysis || sectionData.valuationImpact);

  const tag = document.getElementById("eventCompanyTag");
  tag.textContent = companyData.tag;
  tag.classList.add(companyData.tagClass);

  const backLink = document.getElementById("backToLatest");
  if (company) {
    backLink.href = `./company.html?company=${encodeURIComponent(company)}&page=${page}&v=20260412-24#companyUpdates`;
    backLink.textContent = "← 返回公司主页";
  } else {
    backLink.href = "./index.html?v=20260412-24";
    backLink.textContent = "← 返回研究门户";
  }

}

initEventPage();
