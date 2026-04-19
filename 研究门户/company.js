const COMPANY_DATA = {
  nvidia: {
    title: "NVIDIA",
    tag: "美股",
    tagClass: "us",
    summary: "这是 AI 基础设施主线最核心的公司之一，但现在真正要看的不是“还有没有增长”，而是推理需求、平台化能力和超大客户资本开支能否继续形成正反馈。",
    thesis: "NVIDIA 正在从 GPU 龙头演进为 AI 工厂平台公司。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若下一次财报继续验证推理需求、平台化扩张和毛利率稳健，可进入更积极的分批加仓候选。",
    nextCheck: "下一次 FY27 Q1 财报中的数据中心收入、毛利率与客户 capex 口径。",
    positioning: "NVIDIA 已经不只是做 GPU 的芯片公司，而是在往 AI 基础设施平台公司演进。它卡住的是训练、推理、网络互连、整机系统和软件生态这条链路里的核心位置。",
    products: "主营产品包括数据中心 GPU、网络与交换产品、整机系统、CUDA 软件生态，以及围绕 AI 工厂的整套解决方案。真正赚钱的核心已经从单卡销售，转向更完整的平台交付。",
    markets: "主要客户是超大云厂商、模型公司、企业 AI 基础设施采购方和各类主权 AI 项目。当前最重要的市场仍然是全球数据中心和 AI 算力基础设施。",
    moatDetail: "它最强不在某一代芯片参数，而在 CUDA 生态、软硬件协同、客户迁移成本和系统级交付能力。和单做芯片的竞争对手比，NVIDIA 更像是一套已经跑起来的基础设施标准。",
    business: "核心业务已经不只是 GPU 芯片，而是数据中心芯片、网络、软件、整机平台和 AI 工厂方案的系统协同。",
    moat: "CUDA 生态、系统级协同能力、头部客户绑定和持续的产品迭代速度共同构成护城河。",
    financials: "当前财报最该盯数据中心收入、毛利率、库存和现金流质量，而不是只看总收入增速。",
    valuation: "市场已经给了很高预期，所以动作上不能只看强增长，还要看推理需求和平台化能否继续支撑高估值。",
    latestEvent: "FY26 Q4 与全年业绩再创新高，Meta 多代际合作与 Rubin / 光互连布局继续强化平台能力。",
    businessImpact: "这强化了公司从训练卖卡，走向 AI 工厂平台的长期逻辑，说明需求正从单点芯片扩展到系统级基础设施。",
    valuationImpact: "研究上继续强化，但仓位动作仍要等下一次财报继续验证毛利率、推理需求和超大客户 capex。",
    risk: "超大客户资本开支放缓、自研 ASIC 替代、出口限制和平台化扩张带来的盈利质量波动。",
    focus: [
      "下一次 FY27 Q1 财报里数据中心收入和毛利率",
      "推理需求能否真正接棒训练需求",
      "平台化能力是否继续增强而不是停留在芯片层",
    ],
    trackingGuide: [
      "先看哪里：优先看季度财报和业绩会。重点核对数据中心收入、毛利率、库存和管理层对客户 capex 的表述。",
      "怎么判断：如果数据中心收入高增长同时毛利率稳住，说明平台化红利还在；如果收入还强但毛利率和库存恶化，就要警惕质量下降。",
      "再看外部：跟踪 Meta、Microsoft、Amazon 等大客户 capex 指引，以及 Rubin、NVLink、光互连相关发布，看平台能力是不是继续扩大。",
    ],
    latest: "./company.html?company=nvidia&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=nvidia&section=archive",
    onePager: "./company-deep.html?company=nvidia&section=onePager",
  },
  tsmc: {
    title: "TSMC",
    tag: "全球制造",
    tagClass: "tw",
    summary: "台积电的核心不在“月度营收高不高”，而在 2nm、CoWoS 和高资本开支能否继续形成高质量回报。",
    thesis: "TSMC 是全球最重要的先进制造底座。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若下一次法说会继续验证需求和利润率，可进入更积极的分批加仓候选。",
    nextCheck: "2026 年 4 月 16 日法说会对 2nm、CoWoS、利润率和资本开支回报的最新口径。",
    positioning: "TSMC 的定位不是某个终端赛道的受益股，而是全球先进芯片制造底座。谁要做最先进的 AI、手机、服务器芯片，最终都绕不开它。",
    products: "主营是晶圆代工和先进封装，关键产品能力体现在 3nm、2nm 等先进制程，以及 CoWoS 等先进封装产能。",
    markets: "主要客户是全球头部芯片设计公司，覆盖手机、AI、HPC、汽车和消费电子。当前最重要的市场驱动力来自 AI 与高性能计算。",
    moatDetail: "和其他晶圆厂相比，它最强在工艺领先、良率、交付稳定性和客户信任。先进制程和先进封装一起构成了复合护城河，不是单点追赶能解决的。",
    business: "台积电是多个高价值终端赛道共用的先进制程与先进封装底座，而不是单一终端的景气受益者。",
    moat: "工艺领先、量产能力、客户信任和先进封装协同，使它在先进制造环节极难被替代。",
    financials: "当前财报最该盯毛利率、先进制程占比、月度营收与高资本开支之后的现金回报。",
    valuation: "研究上应积极，但仓位动作不能只看 AI 需求强，要把海外建厂成本和高资本开支稀释一起算进去。",
    latestEvent: "2025Q4 利润率继续走强，2026 年前两个月营收仍保持较高同比增长。",
    businessImpact: "这说明 AI / HPC 需求仍在支撑先进制程和先进封装的核心地位，制造底座逻辑继续强化。",
    valuationImpact: "可以提升研究优先级，但仓位动作仍需等 4 月法说会确认需求、利润率与 capex 回报是否同步稳住。",
    risk: "海外建厂成本、极高资本开支、地缘政治和利润率阶段性承压。",
    focus: [
      "2026 年 4 月 16 日法说会对 2nm 和 CoWoS 的最新口径",
      "月度营收和 AI / HPC 需求强度是否继续稳健",
      "海外建厂与高资本开支是否稀释盈利结构",
    ],
    trackingGuide: [
      "先看哪里：每月营收公告和季度法说会。先看先进制程占比、毛利率和 capex 口径。",
      "怎么判断：如果 2nm、CoWoS 仍然供需偏紧，且毛利率没有被海外扩产明显拖垮，说明底座逻辑还在强化。",
      "再看外部：观察 NVIDIA、AMD、Apple 等大客户的新产品和需求指引，因为它们最终会反映到台积电的订单质量上。",
    ],
    latest: "./company.html?company=tsmc&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=tsmc&section=archive",
    onePager: "./company-deep.html?company=tsmc&section=onePager",
  },
  microsoft: {
    title: "Microsoft",
    tag: "美股",
    tagClass: "us",
    summary: "微软现在真正值得盯的，不是“有没有 AI”，而是 Azure、Copilot 和高资本开支能否继续兑现成平台现金流。",
    thesis: "Microsoft 是企业级 AI 最有机会持续兑现为现金流的平台型公司之一。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；高质量公司不等于任何价格都适合加仓。",
    nextCheck: "下一次财报中 Azure 增速、Copilot 商业化与 Microsoft Cloud 毛利率。",
    positioning: "Microsoft 的定位是企业软件、云平台和 AI 工作流入口的复合平台。它不是单纯卖云资源，而是在把 AI 嵌进已有的企业工作流系统里。",
    products: "核心产品包括 Azure、Office、Copilot、GitHub、Windows 和企业安全等。当前最关键的增量是 Azure 和 Copilot 的协同。",
    markets: "主要客户是全球企业、开发者和机构客户。AI 时代最重要的市场不是消费流量，而是企业 IT 与工作流预算。",
    moatDetail: "它的优势在于已有企业客户关系、工作流入口、开发者生态和云平台一体化。和纯模型公司相比，微软更强在“把 AI 卖进组织内部”的能力。",
    business: "核心业务是企业工作流、云平台、开发工具和软件订阅的组合，AI 正在成为放大这些底座的增量引擎。",
    moat: "Azure、Office、GitHub 和企业工作流的协同，使 AI 更容易在已有客户关系里变现。",
    financials: "当前财报最该看 Azure 增速、Cloud 毛利率和资本开支回报，而不是只看管理层的 AI 表述。",
    valuation: "估值的关键不再是 AI 概念，而是 AI 是否在不伤害利润率的前提下抬升长期现金流质量。",
    latestEvent: "Azure 和 AI 投入继续并行，微软已经进入企业 AI 的兑现阶段。",
    businessImpact: "AI 不再只是附加题，而是在重写云和企业软件的增长结构。",
    valuationImpact: "研究上继续维持核心，但资金动作仍要看资本开支与盈利质量能否同步兑现。",
    risk: "高资本开支、OpenAI 相关收益波动和 AI 变现慢于市场预期。",
    focus: [
      "Azure 增速和 AI 商业化节奏",
      "Copilot 是否持续嵌入企业工作流",
      "资本开支能否转为高质量现金流",
    ],
    trackingGuide: [
      "先看哪里：季度财报和电话会。重点看 Azure 增速、Copilot 采用情况和 Microsoft Cloud 毛利率。",
      "怎么判断：如果 Azure 和 Copilot 同时强化，且利润率没有被 capex 明显吞噬，说明 AI 正在真正兑现。",
      "再看外部：关注企业 AI 采购、OpenAI 合作变化和大型数据中心投资节奏，看外部环境是否还支持持续兑现。",
    ],
    latest: "./company.html?company=microsoft&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=microsoft&section=archive",
    onePager: "./company-deep.html?company=microsoft&section=onePager",
  },
  alibaba: {
    title: "阿里巴巴",
    tag: "港股 / 中概",
    tagClass: "hk",
    summary: "阿里的关键不再只是电商稳态，而是平台现金流、云和 AI 是否持续抬升估值中枢。",
    thesis: "阿里是中国最值得长期跟踪的平台现金流 + 云 + AI 复合资产之一。",
    action: "提升优先级",
    portfolioAction: "进入分批加仓候选，但不追高。",
    nextCheck: "下一次财报里 Cloud Intelligence Group 收入、盈利质量和 AI 商业化口径。",
    positioning: "阿里的定位已经不只是成熟电商平台，而是平台现金流底座上叠加云和 AI 的复合资产。",
    products: "主营业务包括淘天等平台业务、阿里云、国际商业、本地生活和菜鸟等。当前最关键的是云和 AI 能不能成为新的估值核心。",
    markets: "主要面向中国消费互联网市场、商家生态、企业云客户和国际电商场景。当前最重要的增量市场是企业云和 AI 应用。",
    moatDetail: "护城河来自平台生态、现金流底座和云基础设施。和其他平台公司比，它的特别之处在于既有消费端流量和商家关系，也有企业云与模型能力。",
    business: "底层业务仍是平台现金流，但真正影响未来估值框架的是云和 AI 能否持续成为第二增长曲线。",
    moat: "平台生态、强现金流底座、云基础设施和 AI 能力共同构成长期优势。",
    financials: "当前财报最该盯云增长、AI 产品商业化、回购执行和分部利润质量。",
    valuation: "资金动作可以比过去积极，但不能只因为便宜就买，关键还是云和 AI 是否真的在抬估值中枢。",
    latestEvent: "云业务增长和 AI 商业化继续强化，研究重点已经明显转向平台现金流 + 云 + AI。",
    businessImpact: "这意味着阿里不再只是成熟平台资产，而是在尝试开启第二次重估。",
    valuationImpact: "提升研究优先级，仓位上可进入分批候选，但仍要避免在情绪冲高时追价。",
    risk: "港股 / 中概折价、云与 AI 投入回报周期、平台竞争和监管环境变化。",
    focus: [
      "Cloud Intelligence Group 收入和盈利质量",
      "AI 产品商业化是否持续强化",
      "回购和股东回报是否继续支撑估值框架",
    ],
    trackingGuide: [
      "先看哪里：季度业绩、投资者关系公告和阿里云 / 通义相关发布。先看云收入增速、AI 商业化口径和回购进展。",
      "怎么判断：如果云和 AI 连续几个季度抬升收入与利润质量，阿里的估值中枢就可能继续上移；如果只有叙事没有经营兑现，就要谨慎。",
      "再看外部：观察中国平台竞争、消费恢复和港股 / 中概风险偏好，这些会影响估值修复速度。",
    ],
    latest: "./company.html?company=alibaba&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=alibaba&section=archive",
    onePager: "./company-deep.html?company=alibaba&section=onePager",
  },
  inovance: {
    title: "汇川技术",
    tag: "A 股",
    tagClass: "cn",
    summary: "汇川真正值得跟踪的，不只是工业自动化景气，而是它能不能继续进化成平台型工业公司。",
    thesis: "汇川是中国工业自动化与电驱平台的核心公司之一。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察或列入分批加仓候选，但不因单次高增长追价。",
    nextCheck: "下一次财报里平台化扩张、双轮驱动和经营现金流是否继续兑现。",
    positioning: "汇川的定位是中国工业自动化和电驱平台型公司，不是单一品类设备商。",
    products: "主营产品包括通用自动化、伺服、变频、PLC、工业机器人相关方案，以及新能源汽车电驱和控制系统。",
    markets: "主要面向中国制造业客户和新能源汽车产业链，也在逐步拓展海外工业客户。当前最重要的市场还是中国制造升级。",
    moatDetail: "护城河在于本土服务能力、产品矩阵和系统级方案整合。和单点产品供应商相比，它更强在能把多个环节打包卖给制造客户。",
    business: "业务已经不只是通用自动化，而是向电驱、平台化产品矩阵和海外解决方案持续延展。",
    moat: "本土服务能力、平台化产品矩阵和制造客户基础，是它区别于单点产品公司的关键。",
    financials: "当前财报最该看通用自动化、汽车电驱、经营现金流和订单质量，而不是只看利润增速。",
    valuation: "研究上可以积极，但资金动作仍要对 A 股制造龙头常见的高估值波动保持敬畏。",
    latestEvent: "工业自动化和新能源汽车业务双轮驱动更清晰，平台化和出海验证继续推进。",
    businessImpact: "这强化了它从自动化龙头走向平台型工业公司的长期逻辑。",
    valuationImpact: "维持核心并提升研究优先级，但仓位上仍应等待更好的价格和更多现金流验证。",
    risk: "景气波动、价格竞争、估值压缩和平台扩张不及预期。",
    focus: [
      "通用自动化和新能源汽车业务双轮驱动是否持续",
      "多产品平台化扩张是否继续兑现",
      "出海是否从叙事变成稳定订单",
    ],
    trackingGuide: [
      "先看哪里：半年报、三季报和公司官方展会口径。重点看通用自动化、电驱、经营现金流和新增订单。",
      "怎么判断：如果多产品线一起增长且现金流跟上，说明平台化逻辑在兑现；如果只靠单一业务冲增长，就不能高估。",
      "再看外部：跟踪国内工业景气、制造业投资和同行竞争态势，看份额提升是不是可持续。",
    ],
    latest: "./company.html?company=inovance&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=inovance&section=archive",
    onePager: "./company-deep.html?company=inovance&section=onePager",
  },
  gevernova: {
    title: "GE Vernova",
    tag: "美股",
    tagClass: "us",
    summary: "GE Vernova 最该盯的不是电力叙事本身，而是订单、backlog、利润率和自由现金流能否继续一起走强。",
    thesis: "GE Vernova 是发电、电网设备和服务三条关键链路上的电力系统升级平台。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若下一次业绩会继续验证订单、利润率和自由现金流强势，可进入更积极的分批加仓候选。",
    nextCheck: "2026 年 4 月 22 日业绩会中的订单、backlog、利润率与 Prolec 并表口径。",
    positioning: "GE Vernova 的定位是电力系统升级平台，不只是单一发电设备商。",
    products: "主营覆盖 Power、Electrification、Grid、Wind 和相关服务。当前最关键的是订单和 backlog 怎么转化为利润率与现金流。",
    markets: "主要面向美国及全球电网升级、电力投资和数据中心电力配套需求。当前最强市场驱动来自北美电力系统紧张与数据中心扩张。",
    moatDetail: "它的优势在于 installed base、项目交付能力和 Power + Electrification 协同。和纯设备公司相比，它更像站在更完整的电力系统链条上。",
    business: "不是单一设备公司，而是在 Power、Electrification 和服务三条线上同时受益于全球电力系统升级。",
    moat: "installed base、项目交付经验、Power 与 Electrification 协同，以及更长的 backlog 可见性。",
    financials: "当前财报最该看订单、backlog、利润率和自由现金流，而不是只看电力主题热度。",
    valuation: "研究上可提升优先级，但仓位动作仍要等订单与现金流持续兑现，而不是只凭长周期叙事加仓。",
    latestEvent: "2025Q4 订单同比增长 65%，全年自由现金流达到 37 亿美元，Prolec 收购已完成。",
    businessImpact: "这让 GE Vernova 更像完整的电力系统升级平台，而不是只吃某一段设备景气。",
    valuationImpact: "研究上继续强化，但仓位动作仍要等 4 月 22 日业绩会确认订单、利润率和整合质量。",
    risk: "Wind 板块拖累、项目执行风险、并购整合质量和利润率波动。",
    focus: [
      "2026 年 4 月 22 日业绩会的订单与 backlog 数据",
      "Power 和 Electrification 业务利润率是否继续改善",
      "Prolec 并表后自由现金流与增长质量",
    ],
    trackingGuide: [
      "先看哪里：季度业绩和业绩会。重点看订单、backlog、利润率和自由现金流。",
      "怎么判断：如果订单继续强、利润率同步改善，说明电力升级叙事开始真正兑现；如果只有订单没有现金流，就要保守。",
      "再看外部：观察美国电网投资、数据中心电力需求和并购整合情况，看需求和执行是不是同向强化。",
    ],
    latest: "./company.html?company=gevernova&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=gevernova&section=archive",
    onePager: "./company-deep.html?company=gevernova&section=onePager",
  },
  luxshare: {
    title: "立讯精密",
    tag: "A 股",
    tagClass: "cn",
    summary: "立讯现在最该看的不是表面增长，而是扩张能否持续转化成高质量现金流和资本回报。",
    thesis: "立讯是中国复杂精密制造与系统集成能力的代表性公司之一。",
    action: "需要二次验证",
    portfolioAction: "暂停激进加仓，等待下一次财报确认现金流与资本效率。",
    nextCheck: "下一次财报里经营现金流是否修复，以及汽车 / 通信新业务扩张质量。",
    positioning: "立讯的定位是复杂精密制造和系统集成平台，不是单一消费电子代工厂。",
    products: "主营覆盖消费电子精密制造、连接器、声学、通信、汽车电子和系统级组装等。",
    markets: "主要面向全球消费电子、通信和汽车产业链客户。当前最关键的是能否从单一大客户链条逐步走向多业务引擎。",
    moatDetail: "它的优势在于复杂制造执行力、客户协同能力和快速扩产能力。和普通制造企业相比，它更强在把复杂项目规模化落地。",
    business: "长期逻辑来自复杂制造执行能力和从消费电子向汽车、通信、数据中心等多业务延展的能力。",
    moat: "复杂制造、客户绑定和系统集成能力构成它的护城河，但这些优势必须最终体现在现金流上。",
    financials: "当前财报最该看经营现金流、capex、客户结构和新业务扩张质量，而不是只看收入利润。",
    valuation: "在没有确认现金流修复前，不适合继续激进加仓；先守研究，再等质量验证。",
    latestEvent: "收入和利润继续增长，但经营现金流净额明显转负。",
    businessImpact: "长期逻辑没有破坏，但这条信息把研究重点从“优秀制造龙头”收紧到“扩张质量验证”。",
    valuationImpact: "资金动作转向克制，优先等待财报验证，不再因为短期增长而加大动作。",
    risk: "客户集中、资本开支回报、新业务扩张不及预期和现金流质量恶化。",
    focus: [
      "经营现金流是否修复",
      "汽车和通信业务扩张质量",
      "资本开支和客户集中风险",
    ],
    trackingGuide: [
      "先看哪里：季度财报和年报。先核对经营现金流、capex、主要业务增速和客户结构变化。",
      "怎么判断：如果收入利润继续增长但现金流恶化，说明质量在下降；如果现金流修复并且新业务站稳，长期逻辑才更扎实。",
      "再看外部：观察大客户新品周期、汽车业务新项目和海外产能进展，看扩张是不是在变成真实回报。",
    ],
    latest: "./company.html?company=luxshare&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=luxshare&section=archive",
    onePager: "./company-deep.html?company=luxshare&section=onePager",
  },
  constellation: {
    title: "Constellation Energy",
    tag: "美股",
    tagClass: "us",
    summary: "Constellation 的关键不只是核电资产稀缺性，而是长期合同和 Calpine 整合能否把稀缺性真正转成成长。",
    thesis: "Constellation 正在从核电稀缺资产持有者演进为成长型电力平台。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若数据中心供电协议和 Calpine 整合继续兑现，可进入更积极的分批加仓候选。",
    nextCheck: "后续业绩会中，Calpine 整合、长期合同与核电资产运行的最新口径。",
    positioning: "Constellation 的定位是稳定零碳电源平台，并正在往更大的成长型电力平台演进。",
    products: "主营是核电和综合电力供应能力，当前最关键的增量来自长期供电协议、Calpine 整合和数据中心负荷需求。",
    markets: "主要面向美国电力市场、大型商业客户和数据中心客户。当前最重要的市场驱动力是数据中心电力需求与零碳电力稀缺性。",
    moatDetail: "它的优势在于稀缺核电资产、长期供电能力和更完整的平台整合。和普通公用事业公司相比，它更有成长弹性；和单一发电商相比，它更有合同与平台优势。",
    business: "核电底座仍是核心，但真正改变公司边界的是 Calpine 并购之后的大规模电力平台能力。",
    moat: "稳定零碳电力资产、核电运营经验、长期供电合同能力和更大的商业平台。",
    financials: "当前财报最该看长期供电协议、整合协同、股东回报和核电资产运行质量。",
    valuation: "研究上已可提升优先级，但资金动作仍要等长期合同和整合继续兑现，不适合只凭主题情绪追价。",
    latestEvent: "Calpine 收购已完成，CyrusOne 长期供电协议继续落地，监管资产剥离也已启动。",
    businessImpact: "公司正在从稳定公用事业现金流，走向更完整的成长型电力平台。",
    valuationImpact: "可继续提升关注，但动作上仍需结合整合质量和监管处置结果谨慎推进。",
    risk: "Calpine 整合、监管资产剥离、电力市场结构变化和核电资产运行风险。",
    focus: [
      "数据中心长期供电协议是否继续扩张",
      "Calpine 整合后的协同兑现情况",
      "核电资产延寿、重启与运行质量",
    ],
    trackingGuide: [
      "先看哪里：季度业绩、重大合同公告和并购整合进展。重点看长期供电协议、整合协同和核电运营质量。",
      "怎么判断：如果长期合同扩张和整合质量一起改善，说明它正在从稀缺资产走向成长平台；如果只有故事没有合同兑现，就要警惕。",
      "再看外部：跟踪美国电力政策、核电支持政策和数据中心电力需求，看外部环境是不是继续强化这条主线。",
    ],
    latest: "./company.html?company=constellation&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=constellation&section=archive",
    onePager: "./company-deep.html?company=constellation&section=onePager",
  },
};

function setText(id, value) {
  const node = document.getElementById(id);
  if (node) node.textContent = value;
}

function cleanMarkdownValue(value) {
  return (value || "")
    .replace(/^\s{2,}/gm, "")
    .replace(/`/g, "")
    .trim();
}

function buildFallbackEventRecords(company) {
  const latest = window.COMPANY_EVENT_META?.[company];
  return (latest?.events || []).map((event) => ({
    title: event.title,
    date: event.date,
    type: event.type,
    fact: event.note,
    judgment: event.analysis || latest.businessImpact,
    action: "维持跟踪",
    priority: "P2",
  }));
}

async function parseEventRecordsFromMarkdown(company) {
  const sourceDoc = window.COMPANY_EVENT_META?.[company]?.sourceDoc;
  if (!sourceDoc) return [];

  const response = await fetch(sourceDoc);
  if (!response.ok) {
    throw new Error(`Load failed: HTTP ${response.status}`);
  }

  const markdown = await response.text();
  const blockRegex =
    /### 动态 \d+：([^\n]+)\n\n- 日期：([^\n]+)\n- 事件类型：([^\n]+)\n- 事实：\n([\s\S]*?)\n- 判断：\n([\s\S]*?)\n- 动作：\n\s*`?([^`\n]+)`?\n- 优先级：\n\s*`?([^`\n]+)`?/g;
  const records = [];

  let match;
  while ((match = blockRegex.exec(markdown)) !== null) {
    records.push({
      title: cleanMarkdownValue(match[1]),
      date: cleanMarkdownValue(match[2]),
      type: cleanMarkdownValue(match[3]),
      fact: cleanMarkdownValue(match[4]),
      judgment: cleanMarkdownValue(match[5]),
      action: cleanMarkdownValue(match[6]),
      priority: cleanMarkdownValue(match[7]),
    });
  }

  return records;
}

function renderCompanyEventPager(company, page, totalPages) {
  const pager = document.getElementById("companyEventPager");
  if (!pager) return;

  if (totalPages <= 1) {
    pager.innerHTML = `<div class="pager-note event-pager-note">当前共 1 页。</div>`;
    return;
  }

  const prevLink = page > 1
    ? `./company.html?company=${encodeURIComponent(company)}&page=${page - 1}&v=20260412-24`
    : "";
  const nextLink = page < totalPages
    ? `./company.html?company=${encodeURIComponent(company)}&page=${page + 1}&v=20260412-24`
    : "";

  pager.innerHTML = `
    ${page > 1
      ? `<a class="pager-link" href="${prevLink}#companyUpdates"><span class="pager-label">上一页</span><strong>更早事件</strong></a>`
      : `<div class="pager-note event-pager-note">已经是第一页</div>`}
    <div class="pager-note event-pager-note">第 ${page} / ${totalPages} 页</div>
    ${page < totalPages
      ? `<a class="pager-link" href="${nextLink}#companyUpdates"><span class="pager-label">下一页</span><strong>更多事件</strong></a>`
      : `<div class="pager-note event-pager-note">已经是最后一页</div>`}
  `;
}

function renderCompanyEventFeed(company, records, page) {
  const feed = document.getElementById("companyEventFeed");
  if (!feed) return;

  const pageSize = 4;
  const totalPages = Math.max(1, Math.ceil(records.length / pageSize));
  const safePage = Math.min(Math.max(page, 1), totalPages);
  const startIndex = (safePage - 1) * pageSize;
  const visibleRecords = records.slice(startIndex, startIndex + pageSize);

  feed.innerHTML = visibleRecords.map((event, index) => `
    <article class="event-card rich-card compact-event">
      <div class="event-meta">
        <span>${event.date}</span>
        <span>${event.type}</span>
      </div>
      <h4>${event.title}</h4>
      <p class="event-summary">${event.fact}</p>
      <p class="event-analysis">判断：${event.judgment}</p>
      <a class="event-link" href="./event.html?company=${encodeURIComponent(company)}&event=${startIndex + index}&return=company&page=${safePage}&v=20260412-24">查看原文详情</a>
    </article>
  `).join("");

  renderCompanyEventPager(company, safePage, totalPages);
}

function renderTrackingList(items) {
  const list = document.getElementById("companyTrackingList");
  if (!list) return;

  list.innerHTML = items.map((item) => `
    <article class="tracking-item">
      <p>${item}</p>
    </article>
  `).join("");
}

async function initCompanyPage() {
  const params = new URLSearchParams(window.location.search);
  const company = params.get("company");
  const page = Number(params.get("page") || "1");
  const data = COMPANY_DATA[company];
  if (!data) return;

  document.title = `${data.title} | 公司主页`;
  setText("companyTitle", data.title);
  setText("companySummary", data.summary);
  setText("companyThesis", data.thesis);
  setText("companyAction", data.action);
  setText("companyPortfolioAction", data.portfolioAction);
  setText("companyNextCheck", data.nextCheck);
  setText("companyPositioning", data.positioning);
  setText("companyProducts", data.products);
  setText("companyMarkets", data.markets);
  setText("companyMoatDetail", data.moatDetail);
  setText("latestEvent", data.latestEvent);
  setText("businessImpact", data.businessImpact);
  setText("valuationImpact", data.valuationImpact);
  setText("companyRisk", data.risk);

  const tag = document.getElementById("companyTag");
  tag.textContent = data.tag;
  tag.classList.add(data.tagClass);

  renderTrackingList(data.trackingGuide || []);

  let records = [];
  try {
    records = await parseEventRecordsFromMarkdown(company);
  } catch (error) {
    console.error(error);
  }

  const safeRecords = records.length ? records : buildFallbackEventRecords(company);
  renderCompanyEventFeed(company, safeRecords, page);
}

initCompanyPage();
