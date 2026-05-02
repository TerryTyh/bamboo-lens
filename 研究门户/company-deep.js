const COMPANY_DEEP_DATA = {
  nvidia: {
    tag: "美股",
    tagClass: "us",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/28-NVIDIA动态更新样例V1.md",
      title: "最近更新记录",
      summary: "这家公司现在最重要的不是“有没有新品”，而是推理需求、平台化能力和超大客户资本开支能否继续正反馈。",
      happened: "FY26 Q4 与全年业绩再创新高，Meta 多代际合作和 Rubin / 光互连布局继续强化平台能力。",
      businessImpact: "NVIDIA 正在继续从芯片龙头走向 AI 工厂平台，增长来源也在从训练延展到推理、网络和系统能力。",
      valuationImpact: "研究上继续维持核心并提升优先级，但仓位动作仍要等下一次财报确认毛利率、推理需求和客户 capex。",
      nextCheck: "下一次 FY27 Q1 财报中的数据中心收入、毛利率与客户 capex 口径。",
      events: [
        { date: "2026-02-25", type: "财报", title: "FY26 Q4 与全年业绩再创新高", note: "数据中心业务继续主导增长，验证 AI 基础设施主线仍处高景气区间。" },
        { date: "2026-02-25", type: "财报指引", title: "FY27 Q1 指引上修至 780 亿美元", note: "即使不假设来自中国的数据中心计算收入，指引依然强劲。" },
        { date: "2026-02-17", type: "客户 / 合作", title: "Meta 多代际合作继续扩大", note: "说明超大客户资本开支已经写进多年路线图，而不是短期采购。" },
        { date: "2026-03", type: "平台 / 供应链", title: "Rubin、NVLink Fusion 与光互连布局继续推进", note: "公司正从 AI 芯片龙头进一步走向 AI 工厂平台。" },
        { date: "2025-11 至 2026-02", type: "风险跟踪", title: "库存、毛利率与客户集中度仍需盯紧", note: "高增长继续，但盈利质量和 capex 波动不能忽视。" },
      ],
      timeline: [
        "2026-02-25：FY26 Q4 / 全年业绩继续创新高，数据中心业务仍是核心增长引擎。",
        "2026-02-17：Meta 多代际合作验证了超大客户多年资本开支路线图。",
        "2026-03：Rubin、NVLink Fusion 与光互连合作继续强化平台化布局。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解这家公司真正该看的主逻辑。",
      content: [
        "一句话逻辑：全球 AI 基础设施最核心的平台公司之一，正在向更完整的 AI 工厂平台演进。",
        "最强护城河：CUDA 生态 + 芯片、网络、软件和系统级协同。",
        "最大风险：大客户自研 ASIC、出口限制、高估值容错率与客户 capex 波动。",
        "长期验证点：推理需求是否持续接棒训练需求，平台化是否继续扩大护城河。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "适合快速回想为什么它值得长期跟踪。",
      content: [
        "主线：全球算力基础设施。",
        "为什么值得跟踪：需求来自训练、推理、企业部署、AI 工厂和主权 AI。",
        "最该盯的 3 件事：数据中心收入、客户 capex、平台化扩张。",
      ],
    },
  },
  tsmc: {
    tag: "全球制造",
    tagClass: "tw",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/25-TSMC动态更新样例V1.md",
      title: "最近更新记录",
      summary: "当前重点不是月度波动，而是先进制程、先进封装和高资本开支是否继续形成高质量回报。",
      happened: "2025Q4 利润率继续走强，2026 年前两个月营收仍保持较高同比增长。",
      businessImpact: "这继续验证台积电作为先进制造底座的地位，AI / HPC 需求仍在支撑先进制程与先进封装的价值。",
      valuationImpact: "研究上可提升优先级，但仓位动作仍要等 4 月法说会确认需求、利润率和 capex 回报是否同步稳住。",
      nextCheck: "2026 年 4 月 16 日法说会对 2nm、CoWoS、利润率和资本开支回报的口径。",
      events: [
        { date: "2026-01-15", type: "财报", title: "2025Q4 收入、利润率和先进制程占比继续走强", note: "说明增长仍由高价值先进制程主导，而不是成熟制程反弹。" },
        { date: "2026-01-15", type: "财报指引", title: "2026Q1 指引维持高位", note: "领先制程需求依然强劲，管理层并未释放明显降温信号。" },
        { date: "2026-02-10 / 2026-03-10", type: "月度营收", title: "前两个月营收继续维持高同比增长", note: "AI / HPC 需求在高基数下仍有韧性。" },
        { date: "2026-02-10", type: "资本配置", title: "董事会继续大额批准资本预算", note: "扩产决心很强，但回报与利润率稀释也要一起看。" },
        { date: "2026-04-16", type: "验证点", title: "下一次法说会成为关键节点", note: "2nm、CoWoS、利润率与 capex 回报将迎来集中验证。" },
      ],
      timeline: [
        "2026-01-15：2025Q4 业绩与 2026Q1 指引继续高位，先进制程占比提升。",
        "2026-02-10 / 2026-03-10：前两个月营收同比继续维持较高增长。",
        "2026-02-10：董事会继续大额批准资本预算与相关融资安排。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解先进制程底座的核心逻辑。",
      content: [
        "一句话逻辑：全球最重要的先进芯片制造底座，而且正在同时受益于先进制程和先进封装需求的持续抬升。",
        "最强护城河：工艺领先、量产能力、客户信任和先进封装协同。",
        "最大风险：地缘政治、海外建厂成本、高资本开支对利润率和资本回报的稀释。",
        "长期验证点：2nm 和 CoWoS 供需是否持续偏紧，且高投入是否继续换来高质量回报。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回看它为什么值得长期跟踪。",
      content: [
        "主线：先进制造与全球科技底座。",
        "为什么值得跟踪：不是单一终端赛道，而是多个高价值赛道共享的底层制造平台。",
        "最该盯的 3 件事：2nm / CoWoS、利润率与 capex 回报、海外产能布局。",
      ],
    },
  },
  microsoft: {
    tag: "美股",
    tagClass: "us",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/24-Microsoft动态更新样例V1.md",
      title: "最近更新记录",
      summary: "微软现在最值得盯的不是“有没有 AI”，而是 AI 变现和利润率能否持续兑现。",
      happened: "Azure 和 AI 投入继续并行，企业级 AI 平台逻辑稳定，微软已经进入兑现阶段。",
      businessImpact: "AI 不再只是附加题，而是在重写云和企业软件的增长结构。",
      valuationImpact: "研究上继续维持核心，但资金动作仍要看资本开支与盈利质量能否同步兑现。",
      nextCheck: "下一次财报中 Azure 增速、Copilot 商业化与 Microsoft Cloud 毛利率。",
      events: [
        { date: "2026-01-28", type: "财报", title: "FY26 Q2 高质量增长，Cloud 单季收入突破 500 亿美元", note: "说明云与 AI 正在继续扩展整个企业平台的收入基础。" },
        { date: "2026-01-28", type: "财报", title: "Intelligent Cloud 继续强势增长", note: "Azure 所在板块仍是最关键的经营抓手。" },
        { date: "2025-10 至 2026-01", type: "经营趋势", title: "Azure 和企业 AI 从概念验证进入兑现验证", note: "后续不只是看增长，而是看增长质量。" },
        { date: "2025-10 至 2026-01", type: "收益质量", title: "OpenAI 相关投资波动需单独看", note: "AI 叙事不能替代对利润表质量的跟踪。" },
        { date: "持续", type: "资本配置", title: "高资本开支仍是估值持续性的关键变量", note: "后续必须把投入与回报一起看。" },
      ],
      timeline: [
        "2025-10-29：FY26 Q1 继续体现 Azure、Copilot 和平台协同扩张。",
        "2026-01-28：FY26 Q2 高质量增长，Microsoft Cloud 单季收入突破 500 亿美元。",
        "持续：AI 投入已经从概念验证进入兑现验证阶段。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解企业 AI 平台为什么重要。",
      content: [
        "一句话逻辑：企业级 AI 最有可能持续兑现为现金流的平台型公司之一。",
        "最强护城河：Azure + Office + GitHub + 企业工作流协同。",
        "最大风险：AI 基础设施开支过快、变现慢于预期。",
        "长期验证点：Azure 和 Copilot 是否持续强化平台闭环。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回想核心研究角度。",
      content: [
        "主线：云与企业 AI 平台。",
        "为什么值得跟踪：云、企业软件和 AI 商业化路径最清晰。",
        "最该盯的 3 件事：Azure 增速、Copilot 商业化、利润率。",
      ],
    },
  },
  alibaba: {
    tag: "港股 / 中概",
    tagClass: "hk",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/20-阿里巴巴动态更新样例V1.md",
      title: "最近更新记录",
      summary: "云和 AI 已经不只是加分项，而是在逐步变成阿里的新估值中枢。",
      happened: "Cloud Intelligence Group 增长加速，AI 产品持续高增，研究重点已明显转向平台现金流 + 云 + AI。",
      businessImpact: "这意味着阿里不再只是成熟平台资产，而是在尝试开启第二次重估。",
      valuationImpact: "研究上提升优先级，仓位上可进入分批候选，但仍要避免在情绪冲高时追价。",
      nextCheck: "下一次财报里云收入、AI 商业化和回购执行情况。",
      events: [
        { date: "2026-03-19", type: "财报", title: "2025 年 12 月季度云业务增速明显加快", note: "云和 AI 继续成为最核心的增长引擎。" },
        { date: "2026-03-19", type: "产品 / 技术", title: "Qwen App 用户增长与开源生态继续强化", note: "消费端和开发者侧的双轮驱动开始更清晰。" },
        { date: "2025-09 至 2026-03", type: "平台化", title: "全栈 AI 叙事从模型、芯片、云到应用持续强化", note: "说明公司在尝试搭更完整的 AI 平台框架。" },
        { date: "2025-04 至 2025-10", type: "资本配置", title: "持续回购支持股东回报", note: "对港股 / 中概估值折价修复有正面作用。" },
        { date: "2025-09-11", type: "融资", title: "可转债融资为云和国际业务扩张提供长期资本", note: "方向合理，但回报仍需后续验证。" },
      ],
      timeline: [
        "2025-12 季度：云业务同比增长明显加快，AI 产品继续高增。",
        "持续：阿里强化“全栈 AI + 云”定位并持续加大投入。",
        "持续：回购和资本配置继续支撑港股 / 中概折价修复逻辑。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解港股平台资产该怎么跟踪。",
      content: [
        "一句话逻辑：中国最值得长期跟踪的平台型资产之一。",
        "最强护城河：平台生态、强现金流、云基础设施与 AI 能力。",
        "最大风险：港股 / 中概折价、AI 投入回报周期、平台竞争。",
        "长期验证点：云和 AI 是否连续几个季度抬升估值中枢。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回想阿里为什么值得跟踪。",
      content: [
        "主线：平台现金流 + 云 + AI。",
        "为什么值得跟踪：现金流底座强，云和 AI 有望改变估值框架。",
        "最该盯的 3 件事：云增长、AI 商业化、回购与资本配置。",
      ],
    },
  },
  inovance: {
    tag: "A 股",
    tagClass: "cn",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/23-汇川技术动态更新样例V1.md",
      title: "最近更新记录",
      summary: "平台化、双轮驱动和出海验证继续加强了长期逻辑，但估值动作仍应克制。",
      happened: "工业自动化和新能源汽车业务双轮驱动更清晰，平台化扩张和海外验证继续推进。",
      businessImpact: "汇川越来越像平台型工业公司，而不只是单一自动化龙头。",
      valuationImpact: "研究上可以积极，但仓位动作仍要等待更好的价格和更多现金流验证。",
      nextCheck: "下一次财报中平台化扩张、双轮驱动和经营现金流是否继续兑现。",
      events: [
        { date: "2025-10-24", type: "财报", title: "前三季度收入和利润继续双位数增长", note: "主航道经营延续强势，平台型工业公司属性继续强化。" },
        { date: "2025-08-26", type: "财报", title: "上半年双轮驱动更清晰", note: "通用自动化和新能源汽车业务形成更稳定的增长结构。" },
        { date: "2025-08-26", type: "业务结构", title: "多产品组合销售和平台化扩张继续推进", note: "新产品与多业务线协同提升长期逻辑质量。" },
        { date: "2025-08 至 2026-01", type: "出海", title: "出海开始从叙事走向订单验证", note: "海外展示与订单验证逐步增强。" },
        { date: "2025-09-29", type: "产品 / 技术", title: "CIIF 强调系统级智能制造与 AI 驱动方案", note: "公司定位继续从自动化龙头向工业平台升级。" },
      ],
      timeline: [
        "2025-08：半年报体现工业自动化和新能源汽车双轮驱动强化。",
        "2025-09：平台化与系统级智能制造定位在展会与官方沟通中继续强化。",
        "2026-01：海外方案展示继续推进出海验证。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解 A 股工业平台公司的研究重点。",
      content: [
        "一句话逻辑：中国工业自动化和电驱平台型公司。",
        "最强护城河：产品矩阵、本土服务能力、平台协同与制造客户基础。",
        "最大风险：景气波动、价格竞争、估值压缩。",
        "长期验证点：平台化扩张是否持续体现在订单质量和现金流上。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回想汇川为什么值得长期跟踪。",
      content: [
        "主线：中国工业自动化与高端制造。",
        "为什么值得跟踪：平台化能力和制造升级长期主线共振。",
        "最该盯的 3 件事：通用自动化、汽车电驱、海外扩张。",
      ],
    },
  },
  gevernova: {
    tag: "美股",
    tagClass: "us",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/26-GE Vernova动态更新样例V1.md",
      title: "最近更新记录",
      summary: "现在最该盯的不是电力叙事本身，而是订单、backlog、利润率和自由现金流能否继续一起走强。",
      happened: "2025Q4 订单同比增长 65%，全年自由现金流达到 37 亿美元，Prolec 收购已完成。",
      businessImpact: "GE Vernova 正在从电力设备受益者，进化为更完整的电力系统升级平台。",
      valuationImpact: "研究上继续强化，但仓位动作仍要等 4 月 22 日业绩会确认订单、利润率和整合质量。",
      nextCheck: "2026 年 4 月 22 日业绩会中的订单、backlog、利润率与 Prolec 并表口径。",
      events: [
        { date: "2026-01-28", type: "财报", title: "2025Q4 订单和 backlog 明显跳升", note: "Power 与 Electrification 同时强化，需求可见性显著增强。" },
        { date: "2026-01-28", type: "财报", title: "2025 全年利润率和自由现金流继续改善", note: "订单开始更系统地兑现为经营质量改善。" },
        { date: "2026-02-02", type: "并购", title: "Prolec GE 并购完成", note: "进一步强化北美电网设备与 Electrification 主线。" },
        { date: "2026-01 至 2026-03", type: "管理层口径", title: "electricity supercycle 叙事持续强化", note: "但研究重点已转向兑现质量，而非单纯赛道叙事。" },
        { date: "2026-04-22", type: "验证点", title: "下一次业绩会是关键节点", note: "订单、利润率与并购整合质量将迎来集中验证。" },
      ],
      timeline: [
        "2026-01-28：2025Q4 订单和全年自由现金流显著强化。",
        "2026-02-02：Prolec GE 收购完成，Electrification 主线继续加强。",
        "2026-03：管理层持续强调 electricity supercycle，但研究已转向兑现质量。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解电力系统升级公司该怎么看。",
      content: [
        "一句话逻辑：同时卡在发电、电网设备和服务三条关键链路上的电力系统升级平台。",
        "最强护城河：Power 与 Electrification 协同、installed base、长期客户关系与项目交付能力。",
        "最大风险：Wind 板块拖累、项目执行与并购整合质量。",
        "长期验证点：backlog 能否高质量兑现为收入、利润率和自由现金流。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回看这家公司为什么在核心池里。",
      content: [
        "主线：电力设备与电网升级。",
        "为什么值得跟踪：AI 数据中心、电气化和电网投资都在推高需求，而它同时卡在关键设备与服务节点。",
        "最该盯的 3 件事：订单 / backlog、利润率、自由现金流。",
      ],
    },
  },
  luxshare: {
    tag: "A 股",
    tagClass: "cn",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/18-立讯精密动态更新样例V1.md",
      title: "最近更新记录",
      summary: "现金流问题已从“现象”升级为“机制拆解”：应付回落、存货占用与应收变化谁在主导。",
      happened: "2025 年报明确：2025H1 经营现金流为负主要由 Q1 单点流出驱动；全年现金流为正但同比走弱，拖累来自应付回落与存货占用。",
      businessImpact: "增长与业务边界扩展继续，但进入“增长→现金流→资本回报”的兑现验证期。",
      valuationImpact: "资金动作以观望为主：在 2026Q1 季报验证现金流与营运资本前，不做激进加仓决策。",
      nextCheck: "预计 2026-04-25 前后披露的 2026Q1 季报：经营性应付/存货/经营性应收三项是否同步改善。",
      events: [
        { date: "2025-04-26", type: "财报", title: "2025Q1 收入和利润继续增长，但现金流明显承压", note: "这是当前最重要的新风险信号。" },
        { date: "2025-04-26", type: "财报", title: "2024 全年收入和利润保持双位数增长", note: "长期逻辑仍有韧性，问题在质量而不是增长是否存在。" },
        { date: "2025-07-23", type: "产品 / 技术", title: "汽车业务继续向系统级方案延展", note: "说明新业务边界仍在往上走。" },
        { date: "2026-01 至 2026-02", type: "资本配置", title: "公司启动较大规模回购", note: "管理层在释放积极信号，但不应夸大短期含义。" },
        { date: "2025-04-18", type: "管理 / 可持续", title: "ESG 与全球客户体系继续强化", note: "全球客户链条与治理能力仍在加分。" },
      ],
      timeline: [
        "2026-04-14：2025 年报把现金流压力拆到“应付回落+存货占用”，应收全年并未恶化。",
        "2025H1：经营现金流转负，更像付款与营运资本节奏问题。",
        "持续：汽车与通讯及数据中心爬坡是结构升级来源，但也更易带来资金占用与执行风险。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解复杂制造龙头真正该看什么。",
      content: [
        "一句话逻辑：中国复杂精密制造和系统集成能力的代表性公司之一。",
        "最强护城河：复杂制造执行、客户绑定、系统集成能力。",
        "最大风险：客户集中、资本开支回报、新业务扩张质量。",
        "长期验证点：汽车、通信和数据中心新业务能否抬升整体质量。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回想立讯为什么值得长期跟踪。",
      content: [
        "主线：中国复杂制造与全球供应链重构。",
        "为什么值得跟踪：具备从消费电子延展到汽车和通信的制造执行力。",
        "最该盯的 3 件事：经营性应付/存货/应收（营运资本三件套）、客户结构、资本开支回报。",
      ],
    },
  },
  constellation: {
    tag: "美股",
    tagClass: "us",
    latest: {
      sourceDoc: "../长期高潜力公司跟踪系统/27-Constellation Energy动态更新样例V1.md",
      title: "最近更新记录",
      summary: "现在最该盯的，不只是核电资产稀缺性，而是长期合同和整合能否把稀缺性真正转化成成长。",
      happened: "Calpine 收购已完成，CyrusOne 长期供电协议继续落地，监管资产剥离也已启动。",
      businessImpact: "公司正在从核电稀缺资产，被市场重新理解为成长型电力平台。",
      valuationImpact: "研究上可继续提升，但资金动作仍需结合整合质量和监管处置结果谨慎推进。",
      nextCheck: "后续业绩会中，Calpine 整合、长期合同与核电资产运行的最新口径。",
      events: [
        { date: "2026-02-24", type: "财报", title: "2025 全年业绩继续超指引中枢", note: "经营质量和股东回报能力仍在增强。" },
        { date: "2026-01-07", type: "并购", title: "Calpine 并购完成", note: "公司从核电稀缺资产持有者走向更完整的电力平台。" },
        { date: "2026-02-09", type: "合同 / 数据中心", title: "与 CyrusOne 的长期供电协议继续落地", note: "数据中心长期供电逻辑从概念走向实单。" },
        { date: "2026-03-18", type: "监管 / 资产处置", title: "为满足监管要求出售部分 PJM 资产", note: "并购价值需要与监管成本和资产剥离一起评估。" },
        { date: "2026-03-31", type: "展望", title: "公司重心继续拉向长期成长型电力平台", note: "管理层已明确按电气化、再工业化和 AI 用电需求来定位未来增长。" },
      ],
      timeline: [
      "2026-01-07：Calpine 收购完成，公司边界显著扩大。",
      "2026-02-09：CyrusOne 数据中心长期供电协议落地，长期合同逻辑被验证。",
      "2026-03-18：为满足监管要求启动 PJM 资产剥离，提醒整合与监管要一起看。",
      ],
    },
    archive: {
      title: "完整版档案",
      summary: "系统理解稳定电源资产的长期逻辑。",
      content: [
        "一句话逻辑：美国稳定零碳电力的重要拥有者，并在 Calpine 并购后逐步成长为更完整的电力平台。",
        "最强护城河：核电运营经验、长期供电合同能力、稳定零碳发电资产和更大的商业平台。",
        "最大风险：并购整合、监管变化、资产剥离和电力价格周期。",
        "长期验证点：长期供电协议、核电资产延寿 / 重启和整合协同是否持续强化成长属性。",
      ],
    },
    onePager: {
      title: "一页式研究卡",
      summary: "快速回想为什么它能进入核心池。",
      content: [
        "主线：稳定零碳电力与核电重估。",
        "为什么值得跟踪：数据中心、电力安全和减排三条逻辑共振，并且商业平台能力在增强。",
        "最该盯的 3 件事：长期合同、核电资产运行、并购整合。",
      ],
    },
  },
};

window.COMPANY_DEEP_DATA = COMPANY_DEEP_DATA;

function getDisplayName(company) {
  if (company === "gevernova") return "GE Vernova";
  if (company === "inovance") return "汇川技术";
  if (company === "luxshare") return "立讯精密";
  if (company === "constellation") return "Constellation Energy";
  if (company === "alibaba") return "阿里巴巴";
  if (company === "microsoft") return "Microsoft";
  if (company === "tsmc") return "TSMC";
  return "NVIDIA";
}

function getLatestEvents(sectionData) {
  return [
    ...(sectionData.events || []),
    {
      date: "待验证",
      type: "关键验证点",
      title: "下一次关键验证点",
      note: sectionData.nextCheck,
      analysis: sectionData.valuationImpact,
    },
  ];
}

function renderPagination(company, page, totalPages) {
  if (totalPages <= 1) {
    return `
      <div class="pager-note event-pager-note">
        当前共 ${totalPages} 页。后续新增动态会继续叠加到这里。
      </div>
    `;
  }

  const prevLink = page > 1
    ? `./company.html?company=${encodeURIComponent(company)}&page=${page - 1}&v=20260412-24#companyUpdates`
    : "";
  const nextLink = page < totalPages
    ? `./company.html?company=${encodeURIComponent(company)}&page=${page + 1}&v=20260412-24#companyUpdates`
    : "";

  return `
    <div class="event-pager">
      ${page > 1
        ? `<a class="pager-link" href="${prevLink}"><span class="pager-label">上一页</span><strong>查看更早事件</strong></a>`
        : `<div class="pager-note event-pager-note">已经是第一页</div>`}
      <div class="pager-note event-pager-note">第 ${page} / ${totalPages} 页</div>
      ${page < totalPages
        ? `<a class="pager-link" href="${nextLink}"><span class="pager-label">下一页</span><strong>查看更多事件</strong></a>`
        : `<div class="pager-note event-pager-note">已经是最后一页</div>`}
    </div>
  `;
}

function renderLatestSection(sectionData, company, page) {
  const pageSize = 5;
  const allEvents = getLatestEvents(sectionData);
  const totalPages = Math.max(1, Math.ceil(allEvents.length / pageSize));
  const safePage = Math.min(Math.max(page, 1), totalPages);
  const startIndex = (safePage - 1) * pageSize;
  const visibleEvents = allEvents.slice(startIndex, startIndex + pageSize);

  return `
    <div class="deep-grid compact-grid">
      <article class="card">
        <h3>最近发生了什么</h3>
        <p>${sectionData.happened}</p>
      </article>
      <article class="card">
        <h3>对业务的影响</h3>
        <p>${sectionData.businessImpact}</p>
      </article>
      <article class="card">
        <h3>对估值 / 动作的影响</h3>
        <p>${sectionData.valuationImpact}</p>
      </article>
      <article class="card">
        <h3>下一次验证点</h3>
        <p>${sectionData.nextCheck}</p>
      </article>
    </div>
    <div class="card timeline-card">
      <div class="events-header">
        <div>
          <h3>关键动态事件流</h3>
          <p class="muted">每页 5 条，按时间与重要性保留关键事件。</p>
        </div>
      </div>
      <div class="event-grid masonry-grid">
        ${visibleEvents.map((event, index) => `
          <article class="event-card rich-card">
            <div class="event-meta">
              <span>${event.date}</span>
              <span>${event.type}</span>
            </div>
            <h4>${event.title}</h4>
            <p class="event-summary">${event.note}</p>
            <p class="event-analysis">分析：${event.analysis || sectionData.businessImpact}</p>
            <a class="event-link" href="./event.html?company=${encodeURIComponent(company)}&event=${startIndex + index}">查看完整内容</a>
          </article>
        `).join("")}
      </div>
      ${renderPagination(company, safePage, totalPages)}
    </div>
  `;
}

function renderListSection(sectionData) {
  return `
    <ul>
      ${sectionData.content.map((item) => `<li>${item}</li>`).join("")}
    </ul>
  `;
}

function initDeepPage() {
  const content = document.getElementById("deepContent");
  if (!content) return;

  const params = new URLSearchParams(window.location.search);
  const company = params.get("company");
  const section = params.get("section") || "latest";
  const page = Number(params.get("page") || "1");

  if (company && section === "latest") {
    window.location.replace(`./company.html?company=${encodeURIComponent(company)}&page=${page}&v=20260412-24#companyUpdates`);
    return;
  }

  const data = COMPANY_DEEP_DATA[company];
  const sectionData = data?.[section];
  if (!data || !sectionData) return;

  const title = document.getElementById("deepCompanyTitle");
  const summary = document.getElementById("deepSectionSummary");
  const sectionTitle = document.getElementById("deepSectionTitle");
  const tag = document.getElementById("deepCompanyTag");
  const backLink = document.getElementById("backToCompany");

  document.title = `${getDisplayName(company)} | ${sectionData.title}`;
  title.textContent = getDisplayName(company);
  summary.textContent = sectionData.summary;
  sectionTitle.textContent = sectionData.title;
  tag.textContent = data.tag;
  tag.classList.add(data.tagClass);
  backLink.href = "./index.html";

  content.innerHTML = section === "latest"
    ? renderLatestSection(sectionData, company, page)
    : renderListSection(sectionData);
}

initDeepPage();
