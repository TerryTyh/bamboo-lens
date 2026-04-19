function escapeHtml(value) {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

const DOC_SEQUENCE = [
  { title: "投资范围建议", doc: "../长期高潜力公司跟踪系统/10-投资范围建议V1.md" },
  { title: "第一批种子跟踪池名单", doc: "../长期高潜力公司跟踪系统/11-第一批种子跟踪池名单V1.md" },
  { title: "八家核心公司一页式研究卡", doc: "../长期高潜力公司跟踪系统/12-八家核心公司一页式研究卡V1.md" },
  { title: "跨市场分析框架适配说明", doc: "../长期高潜力公司跟踪系统/13-跨市场分析框架适配说明.md" },
  { title: "八家核心公司完整版档案", doc: "../长期高潜力公司跟踪系统/14-八家核心公司完整版档案V1.md" },
  { title: "核心跟踪池动态更新面板", doc: "../长期高潜力公司跟踪系统/15-核心跟踪池动态更新面板V1.md" },
  { title: "八家核心公司首次跟踪任务清单", doc: "../长期高潜力公司跟踪系统/16-八家核心公司首次跟踪任务清单V1.md" },
  { title: "核心跟踪池周报样例", doc: "../长期高潜力公司跟踪系统/17-核心跟踪池周报样例V1.md" },
  { title: "立讯精密动态更新样例", doc: "../长期高潜力公司跟踪系统/18-立讯精密动态更新样例V1.md" },
  { title: "手机友好简报格式", doc: "../长期高潜力公司跟踪系统/19-手机友好简报格式V1.md" },
  { title: "阿里巴巴动态更新样例", doc: "../长期高潜力公司跟踪系统/20-阿里巴巴动态更新样例V1.md" },
  { title: "研究结论到投资决策的落地规则", doc: "../长期高潜力公司跟踪系统/21-研究结论到投资决策的落地规则V1.md" },
  { title: "移动端推送接入指南", doc: "../长期高潜力公司跟踪系统/22-移动端推送接入指南V1.md" },
  { title: "汇川技术动态更新样例", doc: "../长期高潜力公司跟踪系统/23-汇川技术动态更新样例V1.md" },
];

function normalizeDocPath(path) {
  return decodeURIComponent(path || "")
    .replace(/\\/g, "/")
    .replace(/^\.\//, "")
    .replace(/\/+/g, "/")
    .trim();
}

function slugify(text) {
  return text
    .toLowerCase()
    .trim()
    .replace(/[^\w\u4e00-\u9fa5]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function renderInline(text) {
  let output = escapeHtml(text);
  output = output.replace(/`([^`]+)`/g, "<code>$1</code>");
  output = output.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  output = output.replace(/\*([^*]+)\*/g, "<em>$1</em>");
  output = output.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  return output;
}

function renderMarkdown(markdown) {
  const lines = markdown.replace(/\r\n/g, "\n").split("\n");
  const html = [];
  const headings = [];
  let inCodeBlock = false;
  let codeBuffer = [];
  let listType = null;
  let tableMode = false;
  let tableHeader = null;
  let tableRows = [];

  function flushList() {
    if (listType) {
      html.push(`</${listType}>`);
      listType = null;
    }
  }

  function flushTable() {
    if (!tableMode) return;
    const headerCells = tableHeader
      .map((cell) => `<th>${renderInline(cell.trim())}</th>`)
      .join("");
    const rowHtml = tableRows
      .map((row) => {
        const cells = row
          .map((cell) => `<td>${renderInline(cell.trim())}</td>`)
          .join("");
        return `<tr>${cells}</tr>`;
      })
      .join("");
    html.push(
      `<div class="table-wrap"><table><thead><tr>${headerCells}</tr></thead><tbody>${rowHtml}</tbody></table></div>`
    );
    tableMode = false;
    tableHeader = null;
    tableRows = [];
  }

  lines.forEach((line, index) => {
    const nextLine = lines[index + 1] || "";

    if (line.trim().startsWith("```")) {
      flushList();
      flushTable();
      if (inCodeBlock) {
        html.push(`<pre><code>${escapeHtml(codeBuffer.join("\n"))}</code></pre>`);
        inCodeBlock = false;
        codeBuffer = [];
      } else {
        inCodeBlock = true;
      }
      return;
    }

    if (inCodeBlock) {
      codeBuffer.push(line);
      return;
    }

    const headingMatch = line.match(/^(#{1,6})\s+(.*)$/);
    if (headingMatch) {
      flushList();
      flushTable();
      const level = headingMatch[1].length;
      const text = headingMatch[2].trim();
      const id = slugify(text);
      headings.push({ level, text, id });
      html.push(`<h${level} id="${id}">${renderInline(text)}</h${level}>`);
      return;
    }

    if (/^\|.*\|$/.test(line) && /^\|?[\s:-]+\|[\s|:-]+$/.test(nextLine.trim())) {
      flushList();
      flushTable();
      tableMode = true;
      tableHeader = line.split("|").slice(1, -1);
      return;
    }

    if (tableMode && /^\|.*\|$/.test(line)) {
      if (!/^\|?[\s:-]+\|[\s|:-]+$/.test(line.trim())) {
        tableRows.push(line.split("|").slice(1, -1));
      }
      return;
    }

    if (tableMode && line.trim() === "") {
      flushTable();
      return;
    }

    const unorderedMatch = line.match(/^\s*-\s+(.*)$/);
    if (unorderedMatch) {
      flushTable();
      if (listType !== "ul") {
        flushList();
        html.push("<ul>");
        listType = "ul";
      }
      html.push(`<li>${renderInline(unorderedMatch[1])}</li>`);
      return;
    }

    const orderedMatch = line.match(/^\s*\d+\.\s+(.*)$/);
    if (orderedMatch) {
      flushTable();
      if (listType !== "ol") {
        flushList();
        html.push("<ol>");
        listType = "ol";
      }
      html.push(`<li>${renderInline(orderedMatch[1])}</li>`);
      return;
    }

    if (line.trim() === "") {
      flushList();
      flushTable();
      return;
    }

    flushList();
    flushTable();
    if (/^>\s?/.test(line)) {
      html.push(`<blockquote>${renderInline(line.replace(/^>\s?/, ""))}</blockquote>`);
      return;
    }

    if (/^---+$/.test(line.trim())) {
      html.push("<hr />");
      return;
    }

    html.push(`<p>${renderInline(line)}</p>`);
  });

  flushList();
  flushTable();

  return { html: html.join(""), headings };
}

function renderToc(headings) {
  const toc = document.getElementById("toc");
  if (!headings.length) {
    toc.innerHTML = "<p class='toc-empty'>当前文档没有可用标题。</p>";
    return;
  }

  const filtered = headings.filter((item) => item.level <= 2);
  toc.innerHTML = filtered
    .map(
      (item) =>
        `<a class="toc-link level-${item.level}" href="#${item.id}">${item.text}</a>`
    )
    .join("");
}

function renderPager(doc) {
  const pager = document.getElementById("docPager");
  const normalizedDoc = normalizeDocPath(doc);
  const currentIndex = DOC_SEQUENCE.findIndex(
    (item) => normalizeDocPath(item.doc) === normalizedDoc
  );
  if (currentIndex === -1) {
    pager.innerHTML = `<div class="pager-note">当前文档未纳入顺序导航。</div>`;
    return;
  }

  const previous = DOC_SEQUENCE[currentIndex - 1];
  const next = DOC_SEQUENCE[currentIndex + 1];
  const makeLink = (item, label) =>
    item
      ? `<a class="pager-link" href="./reader.html?doc=${encodeURIComponent(item.doc)}&title=${encodeURIComponent(item.title)}">
           <span class="pager-label">${label}</span>
           <strong>${item.title}</strong>
         </a>`
      : `<div class="pager-link disabled"><span class="pager-label">${label}</span><strong>没有更多了</strong></div>`;

  pager.innerHTML = `${makeLink(previous, "上一篇")}${makeLink(next, "下一篇")}`;
}

function activateTocOnScroll() {
  const links = Array.from(document.querySelectorAll(".toc-link"));
  const sections = links
    .map((link) => {
      const id = decodeURIComponent(link.getAttribute("href").slice(1));
      const element = document.getElementById(id);
      return element ? { link, element } : null;
    })
    .filter(Boolean);

  if (!sections.length) return;

  const setActive = (id) => {
    links.forEach((link) => link.classList.remove("active"));
    const target = links.find(
      (link) => decodeURIComponent(link.getAttribute("href").slice(1)) === id
    );
    if (target) target.classList.add("active");
  };

  setActive(sections[0].element.id);

  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.target.offsetTop - b.target.offsetTop);
      if (visible.length) {
        setActive(visible[0].target.id);
      }
    },
    {
      rootMargin: "-12% 0px -72% 0px",
      threshold: 0,
    }
  );

  sections.forEach(({ element }) => observer.observe(element));
}

function scrollToAnchor(anchor) {
  if (!anchor) return;
  const target = document.getElementById(anchor);
  if (!target) return;

  window.location.hash = anchor;
  target.scrollIntoView({ behavior: "auto", block: "start" });

  setTimeout(() => {
    target.scrollIntoView({ behavior: "auto", block: "start" });
  }, 80);
}

async function initReader() {
  const params = new URLSearchParams(window.location.search);
  const doc = normalizeDocPath(params.get("doc"));
  const title = params.get("title") || "研究文档";
  const anchor = params.get("anchor");

  const titleNode = document.getElementById("readerTitle");
  const rawLink = document.getElementById("rawDocLink");
  const metaNode = document.getElementById("docMeta");
  const contentNode = document.getElementById("docContent");

  titleNode.textContent = title;
  rawLink.href = doc || "#";

  if (!doc) {
    contentNode.innerHTML = "<p>缺少文档参数，无法加载内容。</p>";
    return;
  }

  try {
    const resolvedUrl = new URL(doc, window.location.href);
    rawLink.href = resolvedUrl.href;
    renderPager(doc);

    const response = await fetch(resolvedUrl.href);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const markdown = await response.text();
    const { html, headings } = renderMarkdown(markdown);
    const prettyPath = decodeURIComponent(resolvedUrl.pathname);
    const fileName = prettyPath.split("/").pop() || prettyPath;
    metaNode.innerHTML = `<span>来源文档：${fileName}</span>`;
    contentNode.innerHTML = html;
    renderToc(headings);
    activateTocOnScroll();
    requestAnimationFrame(() => scrollToAnchor(anchor));
  } catch (error) {
    contentNode.innerHTML = `
      <div class="error-box">
        <h2>文档加载失败</h2>
        <p>这通常是因为浏览器直接通过 <code>file://</code> 打开页面，导致无法抓取本地 Markdown 文件。</p>
        <p>建议运行 <code>启动研究门户.command</code>，再通过本地服务访问。</p>
        <p>错误信息：${escapeHtml(String(error.message || error))}</p>
      </div>
    `;
    renderToc([]);
  }
}

initReader();
