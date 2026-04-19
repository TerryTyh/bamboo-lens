function getLatestEventsForEventPage(sectionData) {
  return [
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
  ];
}

function cleanMarkdownValue(value) {
  return (value || "")
    .replace(/^\s{2,}/gm, "")
    .replace(/`/g, "")
    .trim();
}

function buildFallbackEventRecord(event, sectionData) {
  return {
    title: event.title,
    date: event.date,
    type: event.type,
    fact: event.note,
    judgment: event.analysis || sectionData.businessImpact,
    action: event.action || "维持跟踪",
    priority: event.priority || "P2",
  };
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

  return blocks;
}

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value || "暂无";
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

  const events = getLatestEventsForEventPage(sectionData);
  const event = events[eventIndex];
  if (!event) return;

  let parsedEvents = [];
  try {
    parsedEvents = await parseEventRecordsFromMarkdown(sectionData.sourceDoc);
  } catch (error) {
    console.error(error);
  }

  const eventRecord =
    parsedEvents[eventIndex] || buildFallbackEventRecord(event, sectionData);

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
  setText("eventSummary", event.note);
  setText("eventAnalysis", event.analysis || eventRecord.judgment);
  setText("eventBusinessImpact", sectionData.businessImpact);
  setText("eventValuationImpact", sectionData.valuationImpact);

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
