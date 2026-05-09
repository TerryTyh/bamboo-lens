const COMPANY_DATA = {
  nvidia: {
    title: "NVIDIA",
    tag: "美股",
    tagClass: "us",
    summary: "这是 AI 基础设施主线最核心的公司之一。最新要看的不是单颗 GPU 还有多强，而是 NVIDIA 能否把算力、网络、协议、软件运行时和企业智能体需求连成 AI 工厂平台。",
    thesis: "NVIDIA 正在从 GPU 龙头演进为 AI 工厂平台公司，并开始把网络层和企业智能体运行环境纳入护城河。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若下一次财报继续验证推理需求、平台化扩张和毛利率稳健，可进入更积极的分批加仓候选。",
    nextCheck: "下一次 FY27 Q1 财报中的数据中心收入、毛利率、Networking / Spectrum-X 采用情况，以及客户 capex 是否继续支持 AI 工厂扩张。",
    positioning: "NVIDIA 已经不只是做 GPU 的芯片公司，而是在往 AI 基础设施平台公司演进。它卡住的是训练、推理、网络互连、整机系统、软件生态和安全运行时这条链路里的核心位置。",
    products: "主营产品包括数据中心 GPU、网络与交换产品、SuperNIC、整机系统、CUDA 软件生态、Spectrum-X Ethernet、OpenShell 等运行时能力，以及围绕 AI 工厂的整套解决方案。真正赚钱的核心已经从单卡销售，转向更完整的平台交付。",
    markets: "主要客户是超大云厂商、模型公司、企业 AI 基础设施采购方、主权 AI 项目和企业软件平台。当前最重要的市场仍然是全球数据中心和 AI 算力基础设施，下一阶段要看推理和企业智能体是否形成持续需求。",
    moatDetail: "它最强不在某一代芯片参数，而在 CUDA 生态、软硬件协同、客户迁移成本、网络互连、协议标准和系统级交付能力。和单做芯片的竞争对手比，NVIDIA 更像是一套已经跑起来的 AI 工厂基础设施标准。",
    business: "核心业务已经不只是 GPU 芯片，而是数据中心芯片、网络、软件、整机平台、协议和 AI 工厂方案的系统协同。",
    moat: "CUDA 生态、Spectrum-X / NVLink 等网络互连、系统级协同能力、头部客户绑定和持续的产品迭代速度共同构成护城河。",
    financials: "当前财报最该盯数据中心收入、毛利率、库存和现金流质量，而不是只看总收入增速。",
    valuation: "市场已经给了很高预期，所以动作上不能只看强增长，还要看推理需求和平台化能否继续支撑高估值。",
    latestEvent: "Spectrum-X / MRC 和 ServiceNow 自主智能体合作，继续强化 NVIDIA 从 GPU 芯片走向 AI 工厂系统平台的逻辑。",
    businessImpact: "Spectrum-X 与 MRC 说明 NVIDIA 正在把网络层、协议层和硬件层纳入 AI 工厂效率；ServiceNow 合作说明推理需求和企业智能体运行环境也可能成为下一阶段增长入口。",
    valuationImpact: "研究上继续强化平台化判断，但仓位动作仍要等 FY27 Q1 验证数据中心收入、毛利率、Networking 收入、推理需求和超大客户 capex。",
    risk: "超大客户资本开支放缓、自研 ASIC 替代、出口限制和平台化扩张带来的盈利质量波动。",
    focus: [
      "下一次 FY27 Q1 财报里数据中心收入和毛利率",
      "Spectrum-X、MRC、SuperNIC、Networking 收入和客户采用是否继续增强",
      "推理需求能否真正接棒训练需求",
      "平台化能力是否继续增强而不是停留在芯片层",
    ],
    trackingGuide: [
      "先看哪里：优先看季度财报和业绩会。重点核对数据中心收入、毛利率、库存和管理层对客户 capex 的表述。",
      "怎么判断：如果数据中心收入高增长同时毛利率稳住，说明平台化红利还在；如果收入还强但毛利率和库存恶化，就要警惕质量下降。",
      "再看外部：跟踪 Meta、Microsoft、OpenAI、Oracle、Amazon 等大客户 capex 指引，以及 Rubin、NVLink、Spectrum-X、MRC、光互连和企业智能体相关发布，看平台能力是不是继续扩大。",
    ],
    financeMap: {
      intro: "NVIDIA 的财务地图不能只看总收入增速。真正要拆的是：Data Center 是否继续主导、毛利率是否守住、下一季指引是否兑现，以及平台化扩张是否开始侵蚀盈利质量。",
      rows: [
        {
          metric: "FY26 Q4 收入",
          value: "681.27 亿美元",
          change: "同比 +73%，环比 +20%",
          read: "总收入仍在高基数上快速增长，但关键是增长几乎全部由数据中心主导。",
        },
        {
          metric: "Data Center 收入",
          value: "623.14 亿美元",
          change: "同比 +75%，环比 +22%",
          read: "约占季度收入 91%，说明 NVIDIA 的核心已经高度集中在 AI 基础设施。",
        },
        {
          metric: "FY26 全年收入",
          value: "2159.38 亿美元",
          change: "同比 +65%",
          read: "全年维度确认这不是单季度冲高，而是公司收入结构已经完成迁移。",
        },
        {
          metric: "Data Center 全年收入",
          value: "1937.37 亿美元",
          change: "同比 +68%",
          read: "全年数据中心收入几乎就是公司的主体，后续估值主要看这条线的持续性。",
        },
        {
          metric: "Q4 non-GAAP 毛利率",
          value: "75.2%",
          change: "GAAP 毛利率 75.0%",
          read: "高增长没有明显牺牲毛利率，说明定价能力和平台价值仍强。",
        },
        {
          metric: "Q4 GAAP 净利润",
          value: "429.60 亿美元",
          change: "同比 +94%",
          read: "净利润增速高于收入增速，说明本季度盈利弹性仍强。",
        },
        {
          metric: "FY27 Q1 收入指引",
          value: "780 亿美元",
          change: "上下浮动 2%",
          read: "在不假设中国数据中心计算收入的情况下仍然给出高指引，是强需求信号。",
        },
        {
          metric: "FY27 Q1 毛利率指引",
          value: "约 75%",
          change: "GAAP 74.9%，non-GAAP 75.0%",
          read: "如果下一季兑现，说明 Blackwell / 平台化扩张没有明显压低盈利质量。",
        },
      ],
      bridge: [
        {
          label: "第一层：不是所有收入都一样",
          text: "总收入 681.27 亿美元很强，但更重要的是 Data Center 收入 623.14 亿美元，说明增长主线非常集中。",
        },
        {
          label: "第二层：数据中心已经压倒性主导",
          text: "Data Center 约占季度收入九成，NVIDIA 的估值锚已经从 GPU 公司转向 AI 基础设施公司。",
        },
        {
          label: "第三层：毛利率验证定价力",
          text: "Q4 non-GAAP 毛利率 75.2%，说明高需求没有被供应链、平台切换或竞争明显侵蚀。",
        },
        {
          label: "第四层：指引验证持续性",
          text: "FY27 Q1 收入指引 780 亿美元，且不假设中国数据中心计算收入，是下一轮最关键验证点。",
        },
        {
          label: "第五层：平台化决定估值韧性",
          text: "如果 Rubin、NVLink、网络、存储和 AI factories 继续扩大系统级平台优势，高估值才更有支撑。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "NVIDIA 的 FY26 Q4 强化了 AI 工厂平台逻辑。它已经不只是 GPU 高景气，而是数据中心、网络、软件和系统平台一起扩张。",
        },
        {
          title: "下一季最该看",
          text: "FY27 Q1 收入是否接近 780 亿美元，Data Center 是否继续环比增长，毛利率是否守在约 75%。",
        },
        {
          title: "真正的风险信号",
          text: "如果超大客户 capex 转弱、毛利率下行、库存或应收异常扩张，或者推理需求不能接棒训练需求，就要下调确信度。",
        },
      ],
    },
    businessMap: {
      intro: "NVIDIA 现在不应只被理解为 GPU 芯片公司。更准确的理解是：它用 GPU、CPU、SuperNIC、Spectrum-X 网络、NVLink、整机系统、CUDA 软件生态和 AI 工厂方案，把自己放在全球 AI 基础设施资本开支的核心位置。",
      segments: [
        {
          title: "Data Center：绝对主线",
          scale: "FY26 Q4 收入 623.14 亿美元，约占季度收入 91%",
          text: "这是公司当前估值和增长的核心。数据中心收入背后包括训练、推理、网络、系统和云厂商/模型公司/企业 AI 基础设施采购。",
        },
        {
          title: "Gaming / Pro Visualization：底盘但非主线",
          scale: "仍有品牌和生态价值",
          text: "这些业务仍能贡献现金流和开发者生态，但不再决定公司估值中枢。它们更像技术生态和品牌底盘，而不是当前主引擎。",
        },
        {
          title: "AI 工厂平台：长期边界",
          scale: "Rubin、NVLink、Spectrum-X、MRC、光互连、系统级合作",
          text: "未来价值不只来自单颗 GPU，而来自 AI 工厂级系统：芯片、网络、协议、光互连、整机、软件和客户多年路线图共同构成平台能力。Spectrum-X 与 MRC 的意义，是把网络吞吐、负载均衡、故障恢复和 GPU 利用率也纳入平台价值。",
        },
        {
          title: "企业智能体与推理：下一阶段需求入口",
          scale: "ServiceNow Project Arc、OpenShell、安全运行时、AI factories",
          text: "如果企业智能体从演示走向真实工作流，长期运行、多步骤执行和治理要求会带来持续推理需求。NVIDIA 通过 OpenShell、模型、domain-specific skills 和 AI factories 试图嵌入企业 agent 从运行时到算力的链条。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在 CUDA 生态、硬件迭代、系统级交付、网络互连、协议控制、客户绑定和开发者迁移成本。竞争对手很难只靠单颗芯片参数追平整套生态。",
        },
        {
          title: "和普通芯片公司差别",
          text: "普通芯片公司卖的是部件，NVIDIA 越来越像卖 AI 基础设施标准。客户买的不只是 GPU，而是训练、推理、网络、协议、运行时和软件协同能力。",
        },
        {
          title: "护城河的弱点",
          text: "高度依赖超大客户 capex、先进制程供应链和出口规则。如果客户自研 ASIC、网络方案替代或 capex 放缓，市场预期会快速重估。",
        },
      ],
    },
    valuationFrame: {
      intro: "NVIDIA 的估值判断不能只看高增长，而要看高增长能否在高预期下继续兑现：Data Center 增长、毛利率、客户 capex、推理需求和平台化能力必须同向强化。",
      cards: [
        {
          title: "估值上行条件",
          text: "FY27 Q1 收入接近或超过 780 亿美元，Data Center 继续环比增长，毛利率维持约 75%，推理需求和 Rubin / NVLink 平台化继续强化。",
        },
        {
          title: "估值压制因素",
          text: "如果客户 capex 放缓、毛利率下降、出口限制扩大，或自研 ASIC 替代预期升温，高估值会比普通公司更敏感。",
        },
        {
          title: "当前动作",
          text: "研究上维持核心并提升优先级；资金动作仍要克制，等待下一季验证，而不是只因财报强就追高。",
        },
        {
          title: "真正触发升级的证据",
          text: "连续几个季度 Data Center、毛利率、推理需求、Networking / Spectrum-X 采用和客户 capex 同向强化，同时库存和应收没有出现过热信号。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 至 2026-04-23 可得市场数据",
      intro: "NVIDIA 的估值模型不能只用“AI 龙头”四个字解释。它现在的市值是在同时买 Data Center 现金流、CUDA / 网络 / 系统级护城河、AI 工厂平台化，以及未来推理需求能否接棒训练需求。",
      conclusion: "合理偏高；只有继续超预期兑现才支撑更积极动作",
      read: "按 2026-04-15 至 2026-04-23 快照，NVIDIA 股价约 US$197.8-199.6、市值约 US$4.81-4.85T、PE 约 40-41x、Forward PE 约 23.6-24.3x、P/FCF 约 49.7x。第一版合理市值区间约 US$4.2-5.2T，中枢约 US$4.7T。当前价格接近合理区间中上部，不是无法解释的泡沫，但已经要求 FY27 Q1 继续验证收入、毛利率、推理需求和客户 capex。",
      snapshot: [
        {
          label: "股价快照",
          value: "约 US$197.8-199.6",
          note: "2026-04-15 至 2026-04-23 可得市场快照，非实时。",
        },
        {
          label: "总市值 / EV",
          value: "约 US$4.81-4.85T / US$4.76T",
          note: "全球市值最高梯队，市场已经把 AI 基础设施核心地位充分定价。",
        },
        {
          label: "估值倍数",
          value: "PE 约 40-41x / Forward PE 约 24x",
          note: "Forward PE 看起来没有离谱，但前提是未来利润继续高速增长。",
        },
        {
          label: "现金流倍数",
          value: "P/FCF 约 49.7x",
          note: "自由现金流质量很强，但市场为每 1 美元 FCF 付了接近 50 美元，容错率不高。",
        },
      ],
      currentBreakdown: [
        {
          title: "Data Center 现金流主引擎",
          text: "约 US$3.0-3.7T。依据是 FY26 Q4 Data Center 收入 623.14 亿美元、约占季度收入 91%，FY26 全年 Data Center 收入 1937.37 亿美元。这部分是当前估值的绝对主体。",
        },
        {
          title: "CUDA / 网络 / 系统级护城河",
          text: "约 US$0.7-1.1T。NVIDIA 的溢价不只是 GPU 芯片，而是 CUDA、NVLink、网络、整机系统和客户迁移成本共同构成的平台标准。",
        },
        {
          title: "推理、Rubin 与 AI 工厂期权",
          text: "约 US$0.6-1.0T。未来估值上行不只靠训练需求，而靠推理、Rubin、光互连、AI factories 和主权 AI 等需求接续。它是高估值能否继续扩张的关键期权。",
        },
        {
          title: "Gaming / Pro Visualization / Auto 底盘",
          text: "约 US$0.2-0.4T。这些业务不是当前估值主线，但提供品牌、开发者生态、边缘 AI 和长期应用场景。",
        },
        {
          title: "客户 capex、出口限制和替代折价",
          text: "扣减约 US$0.5-1.0T。超大客户 capex 放缓、自研 ASIC、出口限制、毛利率回落和供应链限制，都会让市场快速下调估值中枢。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 US$3.2-4.2T",
          text: "FY27 Q1 收入或毛利率低于预期，客户 capex 口径转弱，推理需求接续不清晰，或自研 ASIC / 出口限制带来估值压缩。",
        },
        {
          title: "中性情景：约 US$4.2-5.2T",
          text: "FY27 Q1 收入接近 780 亿美元指引，毛利率维持约 75%，Data Center 继续环比增长，客户 capex 没有明显降温。这是当前主情景。",
        },
        {
          title: "乐观情景：约 US$5.2-6.5T",
          text: "推理需求明确接棒训练需求，Rubin / NVLink / 网络平台继续扩大系统级优势，客户 capex 上修，毛利率和现金流继续维持极高质量。",
        },
      ],
      implied: [
        {
          title: "市场已经把 NVIDIA 当 AI 基础设施标准",
          text: "4.8 万亿美元市值不是在买单颗 GPU，而是在买全球 AI 数据中心、软件生态、网络互连和系统交付标准。",
        },
        {
          title: "Forward PE 低于直觉，但不是安全边际",
          text: "Forward PE 约 24x 看似不高，是因为市场预期利润继续高速增长；如果增长斜率下降，倍数会迅速重估。",
        },
        {
          title: "P/FCF 约 50x 说明容错率有限",
          text: "NVIDIA 现金流质量非常强，但当前价格仍要求 FCF 继续高速扩大。若毛利率或客户 capex 转弱，估值会很敏感。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "FY27 Q1 收入达到或超过 780 亿美元指引，毛利率守在约 75%，Data Center 继续高增长，推理需求和客户 capex 口径同步强化。",
        },
        {
          title: "继续等待的触发",
          text: "收入仍强但股价处于高位，且推理需求、Rubin 平台化或客户 capex 没有给出新增证据。此时公司仍强，但不必追价。",
        },
        {
          title: "下调估值中枢的触发",
          text: "Data Center 增速放缓、毛利率低于预期、库存或应收异常上升、出口限制扩大，或超大客户明确放缓 AI capex。",
        },
      ],
    },
    latest: "./company.html?company=nvidia&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=nvidia&section=archive",
    onePager: "./company-deep.html?company=nvidia&section=onePager",
  },
  tsmc: {
    title: "TSMC",
    tag: "全球制造",
    tagClass: "tw",
    summary: "台积电现在的核心变化，是 HPC / AI 已经明显主导收入结构，同时先进制程和高产能利用率继续把利润率推在高位。",
    thesis: "TSMC 是全球最重要的先进制造底座。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若 2026Q2 继续验证收入、毛利率和 HPC 占比，可进入更积极的分批加仓候选。",
    nextCheck: "2026Q2 实际收入是否落在 US$39.0-40.2 billion 指引区间，毛利率是否维持 65.5%-67.5%。",
    positioning: "TSMC 的定位不是某个终端赛道的受益股，而是全球先进芯片制造底座。谁要做最先进的 AI、手机、服务器芯片，最终都绕不开它。",
    products: "主营是晶圆代工和先进封装，关键产品能力体现在 3nm、2nm 等先进制程，以及 CoWoS 等先进封装产能。",
    markets: "主要客户是全球头部芯片设计公司，覆盖手机、AI、HPC、汽车和消费电子。当前最重要的市场驱动力来自 AI 与高性能计算。",
    moatDetail: "和其他晶圆厂相比，它最强在工艺领先、良率、交付稳定性和客户信任。先进制程和先进封装一起构成了复合护城河，不是单点追赶能解决的。",
    business: "台积电是多个高价值终端赛道共用的先进制程与先进封装底座，而不是单一终端的景气受益者。",
    moat: "工艺领先、量产能力、客户信任和先进封装协同，使它在先进制造环节极难被替代。",
    financials: "当前财报最该盯毛利率、先进制程占比、月度营收与高资本开支之后的现金回报。",
    valuation: "研究上应积极，但仓位动作不能只看 AI 需求强，要把海外建厂成本和高资本开支稀释一起算进去。",
    latestEvent: "2026Q1 显示 HPC 占净收入 61%，毛利率 66.2%，AI / HPC 正在成为最核心收入引擎。",
    businessImpact: "这说明 TSMC 不只是先进制程龙头，而是在全球 AI / HPC 资本开支中承担最核心的制造底座角色。",
    valuationImpact: "可以提升研究优先级，但仓位动作仍要看高 capex、海外扩产和 2nm / CoWoS 投入能否持续转成高质量现金回报。",
    risk: "海外建厂成本、极高资本开支、地缘政治和利润率阶段性承压。",
    focus: [
      "2026Q2 收入是否落在 US$39.0-40.2 billion 指引区间",
      "毛利率是否继续维持 65.5%-67.5% 高位",
      "HPC 占比是否继续在 60% 左右，还是重新回到手机周期主导",
      "海外建厂与高资本开支是否开始稀释自由现金流和资本回报",
    ],
    trackingGuide: [
      "先看哪里：每月营收公告和季度法说会。先看先进制程占比、毛利率和 capex 口径。",
      "怎么判断：如果 2nm、CoWoS 仍然供需偏紧，且毛利率没有被海外扩产明显拖垮，说明底座逻辑还在强化。",
      "再看外部：观察 NVIDIA、AMD、Apple 等大客户的新产品和需求指引，因为它们最终会反映到台积电的订单质量上。",
    ],
    financeMap: {
      intro: "TSMC 的财务地图不能只看收入增速。更关键的是：收入增长来自哪个平台，先进制程占比是否维持高位，毛利率能否覆盖高资本开支和海外扩产成本。",
      rows: [
        {
          metric: "2026Q1 营收",
          value: "NT$1,134.10 billion",
          change: "同比 +35.1%，环比 +8.4%",
          read: "收入不是低基数修复，而是在高基数上继续增长，说明 AI / HPC 需求仍有强支撑。",
        },
        {
          metric: "2026Q1 净利润",
          value: "NT$572.48 billion",
          change: "同比 +58.3%，环比 +13.2%",
          read: "净利润增速高于收入增速，说明本季度增长质量较好，不只是规模扩张。",
        },
        {
          metric: "EPS",
          value: "NT$22.08",
          change: "财报标题指标",
          read: "EPS 是结果，不是原因。真正要拆的是 HPC 占比、先进制程结构和利润率。",
        },
        {
          metric: "毛利率",
          value: "66.2%",
          change: "较 2025Q4 提升 3.9 个百分点",
          read: "这是最强信号之一，说明先进制程结构、产能利用率和成本改善仍然压过扩产成本。",
        },
        {
          metric: "营业利润率",
          value: "58.1%",
          change: "维持极高水平",
          read: "营业利润率没有被高投入立刻吞噬，说明规模效应和定价能力仍强。",
        },
        {
          metric: "先进制程占比",
          value: "7nm 及以下占 74%",
          change: "3nm 25%，5nm 36%，7nm 13%",
          read: "收入质量主要来自高价值先进制程，而不是成熟制程反弹。",
        },
        {
          metric: "HPC 平台占比",
          value: "61%",
          change: "环比 +20%；Smartphone 占 26%，环比 -11%",
          read: "HPC 已经成为主引擎，TSMC 的收入结构正在从手机周期转向 AI / HPC 基础设施周期。",
        },
        {
          metric: "2026Q2 指引",
          value: "收入 US$39.0-40.2B",
          change: "毛利率 65.5%-67.5%，营业利润率 56.5%-58.5%",
          read: "如果 Q2 兑现，说明高毛利不是一次性冲高，而可能成为 AI / HPC 周期下的新常态。",
        },
      ],
      bridge: [
        {
          label: "第一层：不是只看 EPS",
          text: "EPS NT$22.08 是结果，背后真正重要的是收入结构和利润率共同改善。",
        },
        {
          label: "第二层：收入由 HPC 主导",
          text: "HPC 占净收入 61%，环比增长 20%，说明 AI / HPC 已经成为台积电最重要的收入平台。",
        },
        {
          label: "第三层：先进制程支撑定价",
          text: "7nm 及以下先进制程占晶圆收入 74%，高价值制程仍是毛利率和护城河的核心来源。",
        },
        {
          label: "第四层：利润率没有被扩产吞掉",
          text: "毛利率 66.2%，营业利润率 58.1%，说明至少在 2026Q1，高产能利用率和成本改善抵消了高投入压力。",
        },
        {
          label: "第五层：下一步看 Q2 兑现",
          text: "真正验证点是 Q2 收入和毛利率能否落在指引区间，以及高 capex 是否继续换来高质量回报。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "TSMC 的最新财报强化了 AI / HPC 制造底座逻辑，HPC 已经从增长线索变成收入结构里的主引擎。",
        },
        {
          title: "下一季最该看",
          text: "Q2 收入、毛利率、HPC 占比、先进制程占比，以及 2nm / CoWoS 相关投入是否继续供需偏紧。",
        },
        {
          title: "真正的风险信号",
          text: "如果高 capex 和海外扩产开始明显压低毛利率、自由现金流和资本回报，即使收入继续增长，也要下调估值中枢。",
        },
      ],
    },
    businessMap: {
      intro: "TSMC 不是普通芯片公司，也不是单一手机链公司。它更像全球先进算力和高端芯片创新的制造底座：客户做 AI 芯片、手机芯片、服务器芯片、汽车芯片，最终都要回到先进制程、先进封装和稳定量产能力。",
      segments: [
        {
          title: "HPC / AI：当前主引擎",
          scale: "2026Q1 占净收入 61%，环比 +20%",
          text: "这是当前最重要的变化。HPC 已经不只是边际增量，而是台积电收入结构里的主导平台。它把 AI 算力资本开支传导到先进制程、先进封装和高产能利用率。",
        },
        {
          title: "Smartphone：仍是大底盘但不再主导",
          scale: "2026Q1 占净收入 26%，环比 -11%",
          text: "手机仍然是重要收入来源，但本季度不是由手机周期驱动。对台积电来说，手机业务提供稳定底盘，HPC / AI 才是当前决定估值中枢的变量。",
        },
        {
          title: "汽车 / IoT / DCE：长尾平台",
          scale: "汽车 4%，IoT 6%，DCE 1%",
          text: "这些业务短期不是主线，但它们让台积电不只绑定单一终端。真正要看的是这些长尾平台是否使用更先进制程，并在周期波动时提供结构稳定性。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在工艺领先、良率、稳定量产、客户信任和先进封装协同。先进芯片设计公司可以换设计，但很难轻易换掉最可靠的制造底座。",
        },
        {
          title: "和普通晶圆厂差别",
          text: "普通晶圆厂更多受成熟制程价格和周期影响，TSMC 的核心价值在先进制程和先进封装，它参与的是客户最前沿产品的量产，而不是低端产能竞争。",
        },
        {
          title: "护城河的弱点",
          text: "它的护城河很深，但不是无成本的。2nm、CoWoS、海外建厂和高 capex 会不断消耗现金，必须持续证明投入能换来高利润率和高资本回报。",
        },
      ],
    },
    valuationFrame: {
      intro: "TSMC 的估值判断不是“AI 需求强所以买”，而是看 AI / HPC 需求能否持续转化为高毛利、高产能利用率和高资本回报，同时不被高 capex 与海外扩产稀释。",
      cards: [
        {
          title: "估值上行条件",
          text: "Q2 收入落在 US$39.0-40.2B 区间，毛利率维持 65.5%-67.5%，HPC 占比继续高位，同时 2nm 和 CoWoS 需求继续偏紧。",
        },
        {
          title: "估值压制因素",
          text: "如果海外建厂、高折旧和高资本开支开始压低毛利率或自由现金流，市场会重新评估“先进制造底座”能否维持高估值。",
        },
        {
          title: "当前动作",
          text: "研究上提升优先级，但资金动作仍应等待下一轮验证。高质量公司不等于任何价格都值得追，尤其在 AI 链预期充分时。",
        },
        {
          title: "真正触发升级的证据",
          text: "HPC 占比持续高位、先进制程占比稳定、毛利率没有被扩产拖垮、capex 后自由现金流仍健康。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 至 2026-04-24 可得市场数据",
      intro: "TSMC 估值的核心不是单纯给半导体公司一个 PE，而是判断市场给出的高市值，究竟是在买先进制程垄断、HPC / AI 需求、CoWoS / 2nm 期权，还是已经过度预支了高毛利和高资本回报。",
      conclusion: "合理略偏高，但仍属于高质量公司可解释的估值",
      read: "按 2026-04-15 台股快照，TSMC 股价约 NT$2,080、市值约 NT$53.29T、PE 约 31x、Forward PE 约 22.4x；4 月下旬股价一度冲至 NT$2,185，市值进一步上移。第一版合理市值区间约 NT$48-60T，中枢约 NT$54T。也就是说，4 月中旬价格大致贴近合理中枢，4 月下旬新高附近已经偏向区间上半部，需要后续 Q2 毛利率、HPC 占比和 capex 回报继续兑现。",
      snapshot: [
        {
          label: "台股股价",
          value: "约 NT$2,080",
          note: "2026-04-15 可得快照；4 月下旬曾到约 NT$2,185 的新高附近。",
        },
        {
          label: "总市值",
          value: "约 NT$53.29T",
          note: "按 2026-04-15 台股口径；ADR 口径约 US$1.7T，口径和日期不同会有差异。",
        },
        {
          label: "估值倍数",
          value: "PE 约 31x / Forward PE 约 22.4x",
          note: "Forward PE 看起来不夸张，但前提是 AI / HPC 高增长和高毛利可以继续兑现。",
        },
        {
          label: "本轮估值锚",
          value: "HPC 61% + 毛利率 66.2%",
          note: "TSMC 当前估值不是由手机周期主导，而是由 AI / HPC、先进制程和先进封装共同支撑。",
        },
      ],
      currentBreakdown: [
        {
          title: "HPC / AI 先进制程主价值",
          text: "约 NT$32-40T。依据是 2026Q1 HPC 占净收入 61%、环比 +20%，7nm 及以下先进制程占晶圆收入 74%。这部分是当前估值的主体，因为它同时决定收入增速、产能利用率和定价权。",
        },
        {
          title: "Smartphone 高端芯片底盘",
          text: "约 NT$7-10T。2026Q1 Smartphone 占净收入 26%，环比 -11%。它不再是本轮主引擎，但仍提供稳定的大客户底盘和先进制程规模效应。",
        },
        {
          title: "汽车 / IoT / DCE 与成熟平台",
          text: "约 NT$3-5T。汽车 4%、IoT 6%、DCE 1%，短期不是估值主线，但它们让 TSMC 不完全依赖单一终端周期。",
        },
        {
          title: "2nm / CoWoS / 先进封装期权",
          text: "约 NT$6-10T。这部分不是单独利润表项目，而是市场对下一代工艺、先进封装紧缺和 AI 客户长期产能绑定的溢价。它能抬高估值中枢，但必须靠 Q2 以后 capex 回报继续证明。",
        },
        {
          title: "高 capex、海外扩产和地缘折价",
          text: "扣减约 NT$4-7T。TSMC 护城河很深，但代价是极高资本开支、海外建厂成本、折旧压力和地缘政治风险；如果毛利率从 66% 区间明显下滑，这个折价会扩大。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 NT$40-48T",
          text: "HPC 仍增长但毛利率回落，高 capex 与海外扩产开始稀释自由现金流，市场把 TSMC 从 AI 稀缺资产重新往周期制造龙头定价。",
        },
        {
          title: "中性情景：约 NT$48-60T",
          text: "Q2 收入落在 US$39.0-40.2B 指引附近，毛利率维持 65.5%-67.5%，HPC 占比继续在高位，capex 仍能换来高质量回报。这是当前主情景。",
        },
        {
          title: "乐观情景：约 NT$60-72T",
          text: "2nm、CoWoS 和先进封装继续供需偏紧，HPC 占比进一步提升，毛利率维持高位，海外扩产成本没有明显吞噬资本回报。此时市场会继续给全球先进制造底座稀缺溢价。",
        },
      ],
      implied: [
        {
          title: "当前价格已经承认 TSMC 是 AI 制造底座",
          text: "NT$53T 以上市值不是在买普通晶圆厂，而是在买先进制程、HPC 客户需求、良率、先进封装和长期产能绑定。",
        },
        {
          title: "市场隐含毛利率不能明显掉队",
          text: "如果毛利率不能维持在 65% 左右，或者营业利润率明显低于指引区间，当前估值会快速变得偏贵。",
        },
        {
          title: "4 月下旬新高附近容错率下降",
          text: "股价上到 NT$2,185 附近后，市场已经把 Q2 兑现和 AI 链持续强势纳入预期，后续更需要看数据而不是只看叙事。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "Q2 收入和毛利率均落在指引上沿附近，HPC 占比继续高位，2nm / CoWoS 需求继续偏紧，同时自由现金流没有被 capex 明显拖垮。",
        },
        {
          title: "继续等待的触发",
          text: "股价处在新高附近，但 Q2 只兑现收入、没有兑现毛利率或现金流质量。高质量公司也需要价格给安全边际。",
        },
        {
          title: "下调估值中枢的触发",
          text: "毛利率明显低于 65%、海外扩产成本持续侵蚀利润、HPC 占比回落，或大客户 capex / AI 芯片需求出现明确放缓。",
        },
      ],
    },
    latest: "./company.html?company=tsmc&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=tsmc&section=archive",
    onePager: "./company-deep.html?company=tsmc&section=onePager",
  },
  microsoft: {
    title: "Microsoft",
    tag: "美股",
    tagClass: "us",
    summary: "微软现在真正值得盯的，不是“有没有 AI”，而是 Microsoft Cloud、Azure、RPO、AI 收入和高资本开支能否继续兑现成平台现金流。",
    thesis: "Microsoft 是企业级 AI 最有机会持续兑现为现金流的平台型公司之一，但已经进入 capex 回报验证期。",
    action: "维持 A 池核心，并提升财务回报验证优先级",
    portfolioAction: "继续观察；如果 Azure / AI 收入继续增长且 Cloud 毛利率企稳，再考虑更积极的分批候选。",
    nextCheck: "下一次重点看 Azure 增速、Microsoft Cloud 毛利率、AI run-rate、RPO 转化与资本开支回报。",
    positioning: "Microsoft 的定位不是单一软件公司，也不是单纯云厂商，而是企业工作流、云基础设施、开发者生态和 AI 应用入口的复合平台。它的关键优势是能把 AI 嵌入企业已经每天使用的系统里。",
    products: "核心产品包括 Azure、Microsoft 365 / Office、Copilot、GitHub、Windows、Security、Dynamics 和 Power Platform。当前最关键的增量是 Azure AI 基础设施、Copilot 工作流和 GitHub 开发者生产力。",
    markets: "主要客户是全球企业、开发者、政府和机构客户。AI 时代最重要的市场不是纯消费流量，而是企业 IT 预算、云迁移预算、软件订阅预算和 AI 自动化预算。",
    moatDetail: "它的护城河来自企业客户关系、Office 工作流入口、Azure 云基础设施、GitHub 开发者生态、安全与身份体系，以及跨产品打包销售能力。和纯模型公司相比，微软更强在商业分发和企业落地；和单一云厂商相比，它更强在软件入口和工作流黏性。",
    business: "核心业务是企业工作流、云平台、开发工具和软件订阅的组合，AI 正在成为放大这些底座的增量引擎。",
    moat: "Azure、Microsoft 365、GitHub、安全体系和企业客户关系的协同，使 AI 更容易在已有客户关系里变现。",
    financials: "当前财报最该看 Microsoft Cloud 收入、Azure 增速、Cloud 毛利率、RPO、AI run-rate 和资本开支回报，而不是只看管理层的 AI 表述。",
    valuation: "估值的关键不再是 AI 概念，而是 AI 是否在重资本投入下继续抬升长期现金流质量。",
    latestEvent: "FY26 Q3 Microsoft Cloud 达 545 亿美元，Azure 增长 40%，AI 年化收入 run-rate 超 370 亿美元，但 Cloud 毛利率降至 66%。",
    businessImpact: "云、AI 收入、RPO 与企业工作流同时强化，说明微软的企业 AI 平台逻辑正在进入更硬的数据验证阶段。",
    valuationImpact: "研究上继续维持核心，但资金动作要更关注 AI capex 是否持续换来高质量收入、利润率和自由现金流。",
    risk: "高资本开支、Cloud 毛利率下行、OpenAI 相关收益波动、AI 变现慢于市场预期，以及企业客户 AI 预算扩张放缓。",
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
    financeMap: {
      intro: "Microsoft 的财务地图不能只看总收入和 EPS。真正要拆的是：Microsoft Cloud 与 Azure 是否继续高增长，RPO 是否提供未来收入可见性，AI run-rate 是否转成真实收入，以及 AI 基建投入是否开始压低毛利率和自由现金流。",
      rows: [
        {
          metric: "FY26 Q3 收入",
          value: "828.86 亿美元",
          change: "同比 +18%",
          read: "收入仍在高基数上快速增长，说明云、软件和 AI 不是单点拉动，而是平台整体扩张。",
        },
        {
          metric: "营业利润",
          value: "383.98 亿美元",
          change: "同比 +20%",
          read: "营业利润增速高于收入增速，说明核心经营杠杆还在，不是只靠收入堆规模。",
        },
        {
          metric: "净利润 / EPS",
          value: "317.78 亿美元 / 4.27 美元",
          change: "均同比 +23%",
          read: "利润端继续强，给高估值提供基本面支撑，但要和资本开支一起看。",
        },
        {
          metric: "Microsoft Cloud 收入",
          value: "545 亿美元",
          change: "同比 +29%",
          read: "这是微软 AI 与云平台化的核心收入底座，比单个产品发布更重要。",
        },
        {
          metric: "Microsoft Cloud 毛利率",
          value: "66%",
          change: "同比下降",
          read: "AI 基础设施投资和 AI 产品使用增长正在压低云毛利率，是当前最重要的质量验证点。",
        },
        {
          metric: "Intelligent Cloud 收入",
          value: "346.81 亿美元",
          change: "同比 +30%",
          read: "Azure 所在板块仍是增长主引擎，直接决定 AI 基础设施投入是否有收入承接。",
        },
        {
          metric: "Azure and other cloud services",
          value: "增长 40%",
          change: "constant currency +39%",
          read: "Azure 仍保持很高增速，说明企业和 AI 基础设施需求继续强。",
        },
        {
          metric: "Commercial RPO",
          value: "6270 亿美元",
          change: "同比 +99%",
          read: "未来收入可见性大幅增强，关键是后续能否转成高毛利云和软件收入。",
        },
        {
          metric: "AI business annual revenue run rate",
          value: "超过 370 亿美元",
          change: "同比 +123%",
          read: "AI 已经进入可量化收入阶段，但还要继续看它是不是高质量收入。",
        },
        {
          metric: "FY26 Q3 新增 property and equipment",
          value: "308.76 亿美元",
          change: "FY26 前三季度 801.46 亿美元",
          read: "AI 基建投入极重，后续估值的核心问题是这些 capex 能否换来更高质量现金流。",
        },
      ],
      bridge: [
        {
          label: "第一层：平台收入仍在扩张",
          text: "FY26 Q3 收入 828.86 亿美元、营业利润 383.98 亿美元，说明微软不是只有 AI 概念，核心经营仍强。",
        },
        {
          label: "第二层：云是 AI 兑现主通道",
          text: "Microsoft Cloud 收入 545 亿美元、Azure 增长 40%，说明 AI 需求正在通过云基础设施和企业软件兑现。",
        },
        {
          label: "第三层：RPO 提供未来可见性",
          text: "Commercial RPO 达 6270 亿美元，同比增长 99%，这是未来合同收入的蓄水池。",
        },
        {
          label: "第四层：毛利率是质量闸门",
          text: "Microsoft Cloud 毛利率降至 66%，说明 AI 增长不是免费的，必须看效率改善能否抵消基建投入。",
        },
        {
          label: "第五层：capex 决定估值韧性",
          text: "FY26 Q3 新增 property and equipment 308.76 亿美元，后续真正要验证的是 capex 回报率，而不是只看收入增速。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "Microsoft 的 FY26 Q3 强化了企业 AI 平台逻辑：云、AI 收入和 RPO 同时走强，但资本开支和 Cloud 毛利率压力也更清楚。",
        },
        {
          title: "下一季最该看",
          text: "Azure 增速、Microsoft Cloud 毛利率、AI run-rate、RPO 转化、经营现金流与 property and equipment 支出之间的差距。",
        },
        {
          title: "真正的风险信号",
          text: "如果 Azure 增速放缓、Cloud 毛利率继续下行、AI 收入没有持续转化，或者 capex 继续大幅吞噬自由现金流，就要下调估值中枢。",
        },
      ],
    },
    businessMap: {
      intro: "Microsoft 不能只被理解为 Office + Windows，也不能只被理解为 Azure 云厂商。更准确的理解是：它用云基础设施、企业工作流、开发者生态、安全体系和 AI 助手，把自己放在企业数字化和 AI 预算的核心入口。",
      segments: [
        {
          title: "Azure / Intelligent Cloud：AI 基础设施主通道",
          scale: "FY26 Q3 Intelligent Cloud 收入 346.81 亿美元，Azure and other cloud services 增长 40%",
          text: "这是当前最关键的增长引擎。Azure 承接企业云迁移、AI 训练/推理、数据服务和大模型应用部署，是 AI 收入真正落地的基础设施入口。",
        },
        {
          title: "Microsoft 365 / Copilot：企业工作流入口",
          scale: "把 AI 嵌入办公、协作、会议、邮件和知识管理",
          text: "Copilot 的价值不在单个聊天机器人，而在把 AI 嵌进企业日常工作流。只要企业继续用 Microsoft 365，微软就有机会通过席位、ARPU 和高级功能包持续变现。",
        },
        {
          title: "GitHub / Developer / Security：开发与治理入口",
          scale: "连接开发者生产力、安全、身份和企业 IT 管控",
          text: "GitHub Copilot、Azure DevOps、安全和身份体系让微软不只卖办公软件，还参与软件开发、代码生成、安全治理和企业系统管理。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在企业客户关系、工作流入口、Azure 云基础设施、GitHub 开发者生态、安全和身份体系，以及跨产品打包销售能力。这些能力组合起来，比单一模型或单一软件更难被替代。",
        },
        {
          title: "和纯 AI / 模型公司差别",
          text: "纯模型公司更强在模型能力，微软更强在分发、计费、企业落地和工作流嵌入。企业真正付钱时，往往不是只买模型，而是买能接入权限、数据、流程和安全体系的生产工具。",
        },
        {
          title: "护城河的弱点",
          text: "AI 基建投入很重，OpenAI 生态关系也有复杂性。如果客户 AI 付费意愿低于预期、Google / AWS / Anthropic 等竞争加剧，或者 capex 回报周期拉长，微软的高估值会承压。",
        },
      ],
    },
    valuationFrame: {
      intro: "Microsoft 的估值判断不是“AI 很强所以买”，而是看 AI 是否持续转成高质量云收入、软件订阅、RPO 和现金流，同时不被过重的 AI 基建投入拖垮毛利率。",
      cards: [
        {
          title: "估值上行条件",
          text: "Azure 保持高增速，AI run-rate 继续扩大，RPO 逐步转成高质量收入，Microsoft Cloud 毛利率稳定或恢复。",
        },
        {
          title: "估值压制因素",
          text: "AI capex 继续高速扩张，但 Cloud 毛利率和自由现金流没有改善；或者 Copilot / AI 收入不够透明，市场会下调回报率预期。",
        },
        {
          title: "当前动作",
          text: "维持 A 池核心和高优先级跟踪，但资金动作不因单季强财报追价。下一步更适合等 capex 回报与毛利率验证。",
        },
        {
          title: "真正触发升级的证据",
          text: "Azure 高增速延续、Microsoft Cloud 毛利率企稳、AI run-rate 增长且披露更清晰、RPO 转化为收入、自由现金流质量恢复。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 至 2026-04-24 可得市场数据",
      intro: "Microsoft 的估值模型要同时看两件事：一边是 Office / Azure / RPO / AI run-rate 这套企业平台现金流，另一边是 AI 数据中心投入对自由现金流和 Cloud 毛利率的压力。",
      conclusion: "合理偏低，但不是无脑低估；关键取决于 AI capex 回报能否兑现",
      read: "按 2026-04-15 快照，Microsoft 股价约 US$407.7、市值约 US$3.03T、PE 约 24.6x、Forward PE 约 22.4x；4 月下旬市值约 US$3.13T，PE 约 26x、Forward PE 约 23.7x。第一版合理市值区间约 US$3.1-3.8T，中枢约 US$3.45T。当前价格低于中枢，但 P/FCF 约 40x，说明市场仍在等待 AI capex 转成更高质量现金流。",
      snapshot: [
        {
          label: "股价快照",
          value: "约 US$407.7-421.2",
          note: "2026-04-15 至 2026-04-24 可得快照，非实时。",
        },
        {
          label: "总市值",
          value: "约 US$3.03-3.13T",
          note: "全球最大的软件/云平台资产之一，市值已经包含相当多的 AI 平台预期。",
        },
        {
          label: "估值倍数",
          value: "PE 约 24.6-26.0x / Forward PE 约 22.4-23.7x",
          note: "相对微软自身历史高点不算贵，但仍要求 Azure、AI 和 Office 现金流持续兑现。",
        },
        {
          label: "现金流压力",
          value: "P/FCF 约 40x",
          note: "这说明 AI 数据中心投入正在让自由现金流估值显得更贵，capex 回报是关键。",
        },
      ],
      currentBreakdown: [
        {
          title: "Microsoft 365 / Office 企业工作流现金流",
          text: "约 US$1.15-1.45T。依据是 Office、Teams、Security、Dynamics 与企业订阅形成高黏性现金流。这里是微软估值最稳的底盘，也是 Copilot 未来提价和 ARPU 扩张的入口。",
        },
        {
          title: "Azure / Intelligent Cloud",
          text: "约 US$1.25-1.75T。依据是 FY26 Q3 Intelligent Cloud 收入 346.81 亿美元，Azure and other cloud services 增长 40%。这部分决定微软能否真正吃到 AI 基础设施预算。",
        },
        {
          title: "AI / Copilot / GitHub / Security 增量期权",
          text: "约 US$0.35-0.70T。AI business annual revenue run rate 已超过 370 亿美元、同比 +123%，但 Copilot、GitHub 与安全产品的利润率和留存仍需要更多披露。",
        },
        {
          title: "Windows / Gaming / LinkedIn / 其他平台资产",
          text: "约 US$0.45-0.70T。这些业务不是当前 AI 估值主线，但提供分发入口、消费者触点、广告和游戏现金流，降低单一云业务波动。",
        },
        {
          title: "AI capex、Cloud 毛利率和开放生态折价",
          text: "扣减约 US$0.35-0.70T。FY26 Q3 新增 property and equipment 308.76 亿美元，Cloud 毛利率降至 66%；如果投入回报周期拉长，这个折价会扩大。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 US$2.6-3.1T",
          text: "Azure 仍增长但增速放缓，AI 收入披露不够清晰，Cloud 毛利率继续下行，capex 长期压制自由现金流。这个情景下，当前市值只能算接近合理。",
        },
        {
          title: "中性情景：约 US$3.1-3.8T",
          text: "Azure 保持 30%+ 增长，AI run-rate 继续扩大，RPO 转化为高质量收入，Cloud 毛利率不再明显恶化。这是当前“合理偏低”的主情景。",
        },
        {
          title: "乐观情景：约 US$3.8-4.6T",
          text: "Copilot 和 Azure AI 变成清晰第二增长曲线，AI capex 开始体现规模效率，Cloud 毛利率企稳回升，RPO 和企业软件订阅继续强化。",
        },
      ],
      implied: [
        {
          title: "市场已经承认微软是企业 AI 平台",
          text: "3 万亿美元以上市值不是在买传统 Office，而是在买企业工作流、Azure、GitHub、安全和 AI 入口的组合。",
        },
        {
          title: "市场没有完全相信 capex 回报",
          text: "Forward PE 看起来不贵，但 P/FCF 约 40x，说明市场仍担心 AI 数据中心投入会拖慢自由现金流释放。",
        },
        {
          title: "RPO 是估值支撑，但不是终点",
          text: "Commercial RPO 达 6270 亿美元、同比 +99%，提供未来收入可见性；但真正决定估值的是它能否转成高毛利收入和现金流。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "Azure 继续高增长，AI run-rate 持续扩大，Cloud 毛利率企稳或回升，property and equipment 支出增速放缓且自由现金流恢复。",
        },
        {
          title: "继续等待的触发",
          text: "收入和 RPO 继续强，但 Cloud 毛利率下行、capex 继续高增，自由现金流没有改善。此时公司仍好，但价格需要更大安全边际。",
        },
        {
          title: "下调估值中枢的触发",
          text: "Azure 增速明显放缓，Copilot / AI 商业化低于预期，OpenAI 相关关系或成本结构恶化，且 AI capex 持续吞噬自由现金流。",
        },
      ],
    },
    latest: "./company.html?company=microsoft&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=microsoft&section=archive",
    onePager: "./company-deep.html?company=microsoft&section=onePager",
  },
  alibaba: {
    title: "阿里巴巴",
    tag: "港股 / 中概",
    tagClass: "hk",
    summary: "阿里的关键不再只是电商稳态，而是云和 AI 能否成为第二增长曲线，同时核心电商现金流能否承受即时零售和技术投入。",
    thesis: "阿里是中国最值得长期跟踪的平台现金流 + 云 + AI 复合资产之一，但已经进入投入回报验证期。",
    action: "维持 A 池核心，并提升现金流与投入回报验证优先级",
    portfolioAction: "继续观察；若云和 AI 继续高增且自由现金流修复，可进入更积极的分批候选。",
    nextCheck: "下一次重点看 Cloud Intelligence 收入和 EBITA、AI 产品收入、Qwen 用户留存、即时零售亏损收窄和自由现金流。",
    positioning: "阿里的定位已经不只是成熟电商平台，而是平台现金流底座上叠加云、AI 模型、MaaS、自研芯片和多场景应用入口的复合资产。",
    products: "主营业务包括淘天等中国电商、阿里云、Qwen / 通义模型、国际商业、本地生活、菜鸟和数字媒体等。当前最关键的是云和 AI 能否成为新估值核心，同时即时零售投入能否改善单位经济。",
    markets: "主要面向中国消费互联网、商家生态、企业云客户、AI 开发者、国际电商和本地生活场景。当前最重要的增量市场是企业云、AI 应用和即时零售带来的消费场景重构。",
    moatDetail: "护城河来自电商平台生态、商家与消费者关系、支付和物流协同、云基础设施、Qwen 模型生态、开发者使用和强资产负债表。和单纯模型公司比，阿里更强在场景和商业化；和传统平台公司比，它多了一条云和 AI 基础设施曲线。",
    business: "底层业务仍是平台现金流，但真正影响未来估值框架的是云和 AI 能否持续成为第二增长曲线，同时不伤害现金流纪律。",
    moat: "平台生态、强现金流底座、云基础设施、Qwen 模型生态、开发者和消费场景共同构成长期优势。",
    financials: "当前财报最该盯云收入与 EBITA、AI 产品收入、即时零售投入、集团 EBITA、自由现金流和回购，而不是只看收入增速。",
    valuation: "估值修复的前提是云和 AI 真正抬升长期增长，同时核心电商现金流和股东回报没有被新投入过度吞噬。",
    latestEvent: "2025 年 12 月季度云收入增长 36%、Qwen 月活超 3 亿，但集团 adjusted EBITA 和自由现金流被高投入明显压低。",
    businessImpact: "阿里正在把云、Qwen、MaaS、自研芯片和电商场景连成全栈 AI 平台，但即时零售和技术投入也在明显吞噬利润。",
    valuationImpact: "估值上有第二增长曲线重估可能，但不能只看云和 AI，高投入导致的 EBITA、自由现金流压力必须同步验证。",
    risk: "港股 / 中概折价、云与 AI 投入回报周期、即时零售亏损、电商竞争、监管环境和自由现金流波动。",
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
    financeMap: {
      intro: "阿里的财务地图要同时看两件事：云和 AI 是否足够强，能不能成为第二增长曲线；核心电商和现金流是否稳得住，能不能支撑即时零售、技术投入和回购。",
      rows: [
        {
          metric: "集团收入",
          value: "2848.43 亿元",
          change: "同比 +2%；剔除已处置业务后 +9%",
          read: "表面收入增速不高，但同口径更能反映真实经营；仍要看增长来自哪里。",
        },
        {
          metric: "Cloud Intelligence 收入",
          value: "432.84 亿元",
          change: "同比 +36%",
          read: "这是阿里最关键的第二增长曲线，本季度增速明显高于集团整体。",
        },
        {
          metric: "云分部 adjusted EBITA",
          value: "39.11 亿元",
          change: "同比 +25%",
          read: "云不是只增长不赚钱，至少本季度仍在贡献利润，但利润率和投入强度要继续盯。",
        },
        {
          metric: "AI 相关产品收入",
          value: "连续第 10 个季度三位数增长",
          change: "官方披露",
          read: "说明 AI 已经进入商业化收入，但还缺更细分的客户、毛利率和留存数据。",
        },
        {
          metric: "Qwen 月活 / 开源下载",
          value: "月活超 3 亿；下载超 10 亿",
          change: "截至 2026-02 / 2026-01-21",
          read: "这是生态指标，不等于收入，但能说明消费端和开发者侧都在扩张。",
        },
        {
          metric: "中国电商 adjusted EBITA",
          value: "346.13 亿元",
          change: "同比 -43%",
          read: "即时零售、用户体验和技术投入正在压低现金流底座，是本季度最大压力之一。",
        },
        {
          metric: "集团 adjusted EBITA",
          value: "233.97 亿元",
          change: "同比 -57%",
          read: "新投入对利润影响很大，不能只看云 AI 高增长而忽略利润质量。",
        },
        {
          metric: "经营现金流 / 自由现金流",
          value: "360.32 亿元 / 113.46 亿元",
          change: "同比 -49% / -71%",
          read: "这是最需要警惕的数据。第二增长曲线必须最终修复现金流，而不是长期吞噬现金流。",
        },
        {
          metric: "现金及其他流动投资",
          value: "5601.75 亿元",
          change: "资产负债表仍强",
          read: "阿里有资源继续投入和回购，但强资产负债表不是无限容忍亏损的理由。",
        },
      ],
      bridge: [
        {
          label: "第一层：集团收入不是核心答案",
          text: "集团收入 2848.43 亿元，同比增长 2%，同口径增长 9%；真正要看增长结构，而不是只看总增速。",
        },
        {
          label: "第二层：云和 AI 是第二增长曲线",
          text: "云收入增长 36%，AI 产品连续十个季度三位数增长，这是估值中枢能否上移的核心。",
        },
        {
          label: "第三层：生态指标要转成商业指标",
          text: "Qwen 月活超 3 亿、开源下载超 10 亿很强，但下一步要看留存、付费、MaaS 收入和企业客户。",
        },
        {
          label: "第四层：即时零售和技术投入在吞利润",
          text: "中国电商 adjusted EBITA 同比下降 43%，集团 adjusted EBITA 同比下降 57%，说明投入压力非常真实。",
        },
        {
          label: "第五层：现金流决定估值修复质量",
          text: "自由现金流同比下降 71%。如果后续不能恢复，市场不会只因为 AI 叙事给高估值。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "阿里的云和 AI 逻辑明显强化，但这家公司当前不能简单归为利好。它正在用核心平台现金流和资产负债表支持新一轮投入，后续必须验证回报。",
        },
        {
          title: "下一季最该看",
          text: "云收入和 EBITA、AI 产品收入、Qwen 用户和开发者生态、即时零售亏损收窄、中国电商 EBITA 和自由现金流恢复。",
        },
        {
          title: "真正的风险信号",
          text: "如果云 AI 高增长不能带来利润，且即时零售继续拖累电商 EBITA 和自由现金流，阿里的估值修复会被压制。",
        },
      ],
    },
    businessMap: {
      intro: "阿里不是单纯电商公司，也不是单纯 AI 公司。更准确的理解是：它用中国电商现金流、云基础设施、Qwen 模型、MaaS、自研芯片和多场景应用，试图把平台公司升级成 AI 时代的基础设施与应用平台。",
      segments: [
        {
          title: "中国电商：现金流底座",
          scale: "2025 年 12 月季度收入 1593.47 亿元，同比增长 6%",
          text: "淘天等业务仍是现金流和商家生态底座。但即时零售和用户体验投入正在压低 EBITA，说明底座虽强，也在进入再投入阶段。",
        },
        {
          title: "Cloud Intelligence：第二增长曲线",
          scale: "收入 432.84 亿元，同比增长 36%；adjusted EBITA 39.11 亿元",
          text: "这是估值重估最关键的业务。云承接企业 AI、MaaS、模型服务和算力需求，决定阿里能否从平台公司变成 AI 基础设施公司。",
        },
        {
          title: "Qwen / AI 生态：模型与场景入口",
          scale: "Qwen 月活超 3 亿，开源下载超 10 亿",
          text: "Qwen 的意义不只是模型能力，而是能进入淘宝、天猫、高德、飞猪、支付宝和企业云场景。如果生态指标转为商业化，估值逻辑会更强。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在商家和消费者生态、支付与物流协同、阿里云基础设施、Qwen 模型生态、自研芯片、MaaS 能力和强资产负债表。这些组合起来，给阿里提供了从消费到企业的 AI 落地场景。",
        },
        {
          title: "和 Microsoft 的差别",
          text: "Microsoft 更强在全球企业软件和工作流，阿里更强在中国消费、电商场景和本土云/AI 生态。阿里的估值还要额外承受港股/中概折价和国内消费竞争。",
        },
        {
          title: "护城河的弱点",
          text: "电商竞争和即时零售投入会吞噬利润；云和 AI 需要长期 capex；港股/中概风险偏好会压制估值。阿里有强底座，但不是没有代价。",
        },
      ],
    },
    valuationFrame: {
      intro: "阿里的估值判断不能只看“便宜”，也不能只看“AI 很强”。真正要看云和 AI 能否抬升长期增长，同时核心电商现金流、回购和自由现金流能否托住底部。",
      cards: [
        {
          title: "估值上行条件",
          text: "云收入继续 30%+ 增长，云 EBITA 保持改善，AI 产品收入持续高增，Qwen 生态转为商业化，核心电商 EBITA 和自由现金流恢复。",
        },
        {
          title: "估值压制因素",
          text: "即时零售和技术投入继续压低集团 EBITA，自由现金流长期下滑，AI 用户和下载指标不能转为收入，港股/中概折价持续。",
        },
        {
          title: "当前动作",
          text: "维持 A 池核心，但不因单季云 AI 高增就追价。更合理的是等下一季验证利润、现金流和 AI 商业化质量。",
        },
        {
          title: "真正触发升级的证据",
          text: "Cloud Intelligence 高增长且 EBITA 改善、AI 收入披露更清晰、即时零售亏损收窄、自由现金流恢复、回购继续执行。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 可得市场数据",
      intro: "这是第一版估值模型样板，目标不是给一个精确目标价，而是把当前市场估值、合理估值区间和分部贡献拆开看清楚。",
      conclusion: "合理偏低，但不是无脑低估",
      read: "按 9988.HK 约 HK$128.6、BABA 约 US$132.6、总市值约 US$297B / HK$2.30T 的快照看，折合人民币约 2.15 万亿元。第一版分部估值给出的合理市值区间约 RMB 2.3-2.9 万亿元，中枢约 RMB 2.6 万亿元。当前市值低于中枢但没有低到保守区间以下，所以更像“合理偏低”，不是“明显低估到闭眼买”。",
      snapshot: [
        {
          label: "9988.HK 股价",
          value: "约 HK$128.6",
          note: "港股口径，非实时，来自 2026-04-15 可得市场快照。",
        },
        {
          label: "BABA ADR 股价",
          value: "约 US$132.6",
          note: "ADR 口径，1 ADR 通常对应 8 股普通股。",
        },
        {
          label: "总市值",
          value: "约 US$297B / HK$2.30T",
          note: "市场对全部业务、净现金和未来增长期权的合计定价。",
        },
        {
          label: "估值倍数",
          value: "PE 约 22x，Forward PE 约 19x",
          note: "不是极端便宜，但考虑净现金和云 AI 期权后，可进一步拆分判断。",
        },
      ],
      parts: [
        {
          title: "1. 先定当前市场估值",
          text: "当前市场给阿里全部业务、净现金/投资资产和未来增长期权的合计价格约 RMB 2.15 万亿元。",
        },
        {
          title: "2. 再定合理估值区间",
          text: "第一版分部估值给出的合理市值区间约 RMB 2.3-2.9 万亿元，中枢约 RMB 2.6 万亿元。",
        },
        {
          title: "3. 拆每个板块贡献",
          text: "核心电商、云、AI、净现金和其他业务性质不同，所以用分部估值 SOTP，而不是只用一个 PE 粗暴估。",
        },
        {
          title: "4. 最后得出结论",
          text: "当前 RMB 2.15 万亿元低于合理区间中枢约 RMB 2.6 万亿元，但没有明显低于保守区间 RMB 2.3 万亿元，因此是合理偏低，而不是无脑低估。",
        },
      ],
      currentBreakdown: [
        {
          title: "核心电商现金流",
          text: "约 RMB 1.20-1.45 万亿元，占合理价值约 50%-55%。依据是中国电商仍是现金流底座，但即时零售和用户体验投入压低 EBITA，所以给折价后的现金流估值。",
        },
        {
          title: "Cloud Intelligence",
          text: "约 RMB 0.35-0.55 万亿元，占比约 15%-20%。依据是季度云收入 432.84 亿元、同比 +36%，年化收入约 1700+ 亿元，用 2-3 倍收入并结合 EBITA 改善给区间。",
        },
        {
          title: "净现金与投资资产",
          text: "约 RMB 0.40-0.55 万亿元，占比约 15%-20%。依据是现金及其他流动投资 5601.75 亿元，但考虑债务、投入消耗和资本配置折价，不按 100% 计入。",
        },
        {
          title: "AI / Qwen 期权",
          text: "约 RMB 0.10-0.25 万亿元，占比约 5%-10%。依据是 Qwen 月活超 3 亿、开源下载超 10 亿、AI 产品收入连续三位数增长，但商业化和利润率还不够清晰。",
        },
        {
          title: "国际、本地生活、菜鸟等其他业务",
          text: "约 RMB 0.15-0.30 万亿元，占比约 5%-10%。依据是这些业务有规模和战略价值，但盈利质量、竞争格局和资本消耗差异较大，所以给较低权重。",
        },
        {
          title: "折价与投入拖累",
          text: "扣减约 RMB 0.25-0.45 万亿元。依据是港股/中概折价、即时零售投入、自由现金流同比 -71%、集团 adjusted EBITA 同比 -57%。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 RMB 2.0-2.3 万亿元",
          text: "即时零售继续压低利润，自由现金流恢复慢，云和 AI 高增长但利润贡献有限。若落在这个情景，当前市值并不便宜，只能算接近合理。",
        },
        {
          title: "中性情景：约 RMB 2.4-2.8 万亿元",
          text: "云保持 30%+ 增长，云 EBITA 改善，核心电商利润逐步修复，自由现金流恢复。这是当前“合理偏低”判断的主情景。",
        },
        {
          title: "乐观情景：约 RMB 2.9-3.4 万亿元",
          text: "云和 AI 成为清晰第二增长曲线，Qwen / MaaS 商业化改善，即时零售亏损收窄，回购继续执行。此时当前价格对云和 AI 的价值给得不够。",
        },
      ],
      implied: [
        {
          title: "市场承认阿里仍有现金流",
          text: "当前估值没有把阿里当成衰退资产，但也没有给出高成长平台溢价。",
        },
        {
          title: "市场对云和 AI 给了部分价值",
          text: "云 36% 增长和 AI 高增已被部分反映，但 Qwen / MaaS 的长期期权还没有充分定价。",
        },
        {
          title: "市场在惩罚投入不确定性",
          text: "集团 adjusted EBITA -57%、自由现金流 -71%，让市场担心新投入吞噬老现金流。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "云继续 30%+ 增长且 EBITA 改善，自由现金流明显修复，即时零售亏损收窄，回购持续。",
        },
        {
          title: "继续等待的触发",
          text: "云增长强但集团利润和自由现金流继续大幅下滑，说明第二增长曲线还不足以覆盖投入。",
        },
        {
          title: "下调估值中枢的触发",
          text: "云增速明显放缓、AI 商业化不清晰、核心电商利润继续被侵蚀，且回购力度下降。",
        },
      ],
    },
    latest: "./company.html?company=alibaba&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=alibaba&section=archive",
    onePager: "./company-deep.html?company=alibaba&section=onePager",
  },
  inovance: {
    title: "汇川技术",
    tag: "A 股",
    tagClass: "cn",
    summary: "汇川真正值得跟踪的，不只是工业自动化景气，而是它能不能在通用自动化、新能源汽车和产品矩阵上继续进化成平台型工业公司。",
    thesis: "汇川是中国工业自动化与电驱平台的核心公司之一，但估值动作必须服从现金流、库存和周期验证。",
    action: "维持 A 池核心，但提升现金流和存货质量验证优先级",
    portfolioAction: "继续观察或列入分批候选；不因单次高增长追价，等待估值和现金流质量更匹配。",
    nextCheck: "下一次重点看通用自动化增速、新能源汽车业务利润质量、经营现金流、存货和研发投入回报。",
    positioning: "汇川的定位是中国工业自动化和电驱平台型公司，不是单一品类设备商。它试图用伺服、变频、PLC、机器人、视觉、传感器、电驱等产品组合，为制造客户提供系统级方案。",
    products: "主营产品包括通用自动化、伺服系统、低压变频器、PLC、工业机器人、视觉、传感器、丝杠导轨，以及新能源汽车电驱和控制系统。",
    markets: "主要面向中国制造业客户、新能源汽车产业链、轨道交通、电梯和海外工业客户。当前最重要的市场仍是中国制造升级和新能源汽车供应链，同时出海开始进入验证期。",
    moatDetail: "护城河在于本土服务能力、产品矩阵、系统级方案、制造客户基础和快速响应能力。和单点产品供应商相比，它更强在多产品组合销售；和海外巨头相比，它更强在中国本土客户理解和成本服务效率。",
    business: "业务已经不只是通用自动化，而是向电驱、平台化产品矩阵、系统解决方案和海外市场持续延展。",
    moat: "本土服务能力、平台化产品矩阵、制造客户基础、快速迭代和系统级方案能力，是它区别于单点产品公司的关键。",
    financials: "当前财报最该看通用自动化、新能源汽车和轨交、经营现金流、研发费用、存货和资产减值，而不是只看收入利润增速。",
    valuation: "研究上可以积极，但资金动作要对 A 股制造龙头常见的高估值、周期波动和库存压力保持敬畏。",
    latestEvent: "2025 前三季度收入 316.63 亿元、归母净利润 42.54 亿元，双轮增长继续兑现，但研发投入和存货减值压力上升。",
    businessImpact: "通用自动化和新能源汽车/轨交双轮继续兑现，平台型工业公司逻辑更清晰，但研发、存货和减值压力也要同步看。",
    valuationImpact: "研究上维持核心，但 A 股工业龙头不能只因高增长追价，后续要看现金流、存货和利润率是否继续匹配。",
    risk: "制造业景气波动、价格竞争、新能源汽车链利润率、存货减值、研发投入回报不及预期和 A 股估值压缩。",
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
    financeMap: {
      intro: "汇川的财务地图要同时看增长和质量。收入利润双位数增长是第一层，真正决定估值的是通用自动化和新能源汽车/轨交是否双轮兑现，经营现金流是否跟上，研发和存货是否在可控范围内。",
      rows: [
        {
          metric: "前三季度收入",
          value: "316.63 亿元",
          change: "同比 +24.67%",
          read: "收入仍保持较快增长，说明主航道景气和份额能力仍在。",
        },
        {
          metric: "归母净利润",
          value: "42.54 亿元",
          change: "同比 +26.84%",
          read: "利润增速略高于收入增速，说明本期盈利弹性仍不错。",
        },
        {
          metric: "扣非净利润",
          value: "38.88 亿元",
          change: "同比 +24.03%",
          read: "扣非利润与收入同步增长，说明不是靠非经常项目撑利润。",
        },
        {
          metric: "经营现金流净额",
          value: "39.31 亿元",
          change: "同比 +1.92%",
          read: "现金流仍为正，但增速明显低于利润增速，后续要看应收和存货是否拖累。",
        },
        {
          metric: "通用自动化收入",
          value: "约 131 亿元",
          change: "同比约 +20%",
          read: "这是制造业自动化底座，增长说明核心主业仍稳。",
        },
        {
          metric: "新能源汽车和轨交收入",
          value: "约 148 亿元",
          change: "同比约 +38%",
          read: "这是当前更高弹性的增长来源，但也要看利润率和客户结构。",
        },
        {
          metric: "智慧电梯收入",
          value: "约 36 亿元",
          change: "同比基本持平",
          read: "这条线更像稳定业务，不是当前增长主引擎。",
        },
        {
          metric: "研发费用",
          value: "29.94 亿元",
          change: "同比 +35.74%",
          read: "平台化需要研发投入，但研发增速高于收入增速，必须看新产品和份额回报。",
        },
        {
          metric: "资产减值损失",
          value: "2.32 亿元",
          change: "同比 +175.97%",
          read: "存货和设备减值压力抬升，是本期需要持续盯的质量信号。",
        },
      ],
      bridge: [
        {
          label: "第一层：增长还在",
          text: "收入 316.63 亿元、归母净利润 42.54 亿元，均保持 20%+ 增长，说明主航道仍强。",
        },
        {
          label: "第二层：不是单业务驱动",
          text: "通用自动化约 131 亿元、新能源汽车和轨交约 148 亿元，双轮结构比单一产品更稳。",
        },
        {
          label: "第三层：现金流没有掉队但要警惕",
          text: "经营现金流 39.31 亿元仍为正，但增速只有 1.92%，低于利润增速。",
        },
        {
          label: "第四层：研发投入是平台化成本",
          text: "研发费用增长 35.74%，说明公司在为产品矩阵和系统方案投入，但后续要看回报。",
        },
        {
          label: "第五层：存货和减值是风险闸门",
          text: "资产减值损失同比扩大 175.97%，提醒我们高增长背后不能忽略库存和设备利用质量。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "汇川的 2025Q3 强化了平台型工业公司逻辑，但也提醒我们：A 股制造龙头不能只看利润表，现金流、存货和研发回报同样重要。",
        },
        {
          title: "下一季最该看",
          text: "通用自动化是否维持增长、新能源汽车业务利润率、经营现金流是否追上利润、存货和资产减值是否继续扩大。",
        },
        {
          title: "真正的风险信号",
          text: "如果现金流持续弱于利润，存货和减值继续抬升，同时新能源汽车链价格竞争加剧，就要下调估值中枢。",
        },
      ],
    },
    businessMap: {
      intro: "汇川不是单一变频器或伺服公司。更准确的理解是：它用通用自动化产品矩阵、新能源汽车电驱、工业机器人和系统方案，试图成为中国制造业升级中的平台型工业公司。",
      segments: [
        {
          title: "通用自动化：工业底座",
          scale: "前三季度收入约 131 亿元，同比增长约 20%",
          text: "这是公司的基本盘，覆盖伺服、变频、PLC、运动控制、机器人等产品。制造业自动化需求和国产替代是这条线的核心逻辑。",
        },
        {
          title: "新能源汽车和轨交：增长弹性",
          scale: "前三季度收入约 148 亿元，同比增长约 38%",
          text: "这条线提供更高增长，但也更受客户结构、价格竞争和行业周期影响。不能只看收入高增，还要看利润率和现金流。",
        },
        {
          title: "平台化新产品：长期边界",
          scale: "视觉、传感器、丝杠导轨、气动元件、协作机器人等",
          text: "这些新产品决定汇川能否从强产品公司变成系统级方案公司。平台化成功，客户价值和单客户收入都会提升；失败则可能带来研发和库存压力。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在本土服务、快速响应、产品矩阵、客户粘性和系统方案能力。国内制造客户需要的不只是单个硬件，而是能解决现场问题的组合方案。",
        },
        {
          title: "和海外工业巨头差别",
          text: "海外巨头技术和品牌强，但汇川在中国市场更贴近客户、成本效率更高、响应更快。这是它持续提升份额的核心。",
        },
        {
          title: "护城河的弱点",
          text: "工业产品不是软件平台，库存、设备、价格竞争和周期波动都很真实。如果景气下行或客户压价，利润率和估值会一起受压。",
        },
      ],
    },
    valuationFrame: {
      intro: "汇川的估值判断不能只看高增长和国产替代。A 股工业龙头最容易在景气好时估值过高，所以必须用利润增长、现金流质量、库存风险和周期位置一起判断。",
      cards: [
        {
          title: "估值上行条件",
          text: "通用自动化和新能源汽车双轮继续增长，经营现金流追上利润，存货和减值不再扩大，新产品和出海开始贡献可见订单。",
        },
        {
          title: "估值压制因素",
          text: "制造业景气走弱、新能源汽车价格竞争、现金流弱于利润、存货减值扩大，都会让市场下调高质量制造龙头的 PE。",
        },
        {
          title: "当前动作",
          text: "维持 A 池核心，但资金动作克制。不要因为单期 20%+ 增长追价，要等现金流和存货质量继续验证。",
        },
        {
          title: "真正触发升级的证据",
          text: "经营现金流连续改善、双轮业务利润率稳定、研发投入转成新产品收入、出海订单持续、库存和减值压力缓解。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-30 可得市场数据",
      intro: "汇川的估值模型不能只按 A 股工业龙头给一个高 PE。它要同时看通用自动化周期、新能源汽车电驱利润质量、平台化产品矩阵、现金流、存货和资产减值。",
      conclusion: "合理略偏高；好公司但需要现金流和库存继续验证",
      read: "按 2026-04-30 快照，汇川股价约 68.6 元、市值约 1857 亿元、PE 约 39.6x、Forward PE 约 28.3x。第一版合理市值区间约 1550-1950 亿元，中枢约 1750 亿元。当前市值接近区间上半部，不算离谱，但已经要求通用自动化、新能源汽车和现金流质量继续兑现。",
      snapshot: [
        {
          label: "股价快照",
          value: "约 68.6 元",
          note: "2026-04-30 可得市场快照，非实时。",
        },
        {
          label: "总市值",
          value: "约 1857 亿元",
          note: "A 股工业龙头估值已经包含平台化和国产替代预期。",
        },
        {
          label: "估值倍数",
          value: "PE 约 39.6x / Forward PE 约 28.3x",
          note: "Forward PE 不算极端，但对制造业公司来说，需要现金流和库存质量配合。",
        },
        {
          label: "当前关键分歧",
          value: "增长质量",
          note: "前三季度利润增速不错，但经营现金流增速只有 1.92%，资产减值损失同比 +175.97%。",
        },
      ],
      currentBreakdown: [
        {
          title: "通用自动化工业底盘",
          text: "约 700-900 亿元。依据是前三季度通用自动化收入约 131 亿元、同比约 +20%。这是汇川最核心的工业底座，决定它是不是能持续享受国产替代和制造升级红利。",
        },
        {
          title: "新能源汽车与轨交增长弹性",
          text: "约 550-750 亿元。依据是前三季度该板块收入约 148 亿元、同比约 +38%。这部分提供成长弹性，但受价格竞争、客户结构和利润率波动影响更大。",
        },
        {
          title: "平台化新产品与出海期权",
          text: "约 250-450 亿元。视觉、传感器、丝杠导轨、气动、机器人和海外市场，是从产品公司走向系统方案公司的期权，但目前仍需要订单和利润率验证。",
        },
        {
          title: "智慧电梯与稳定业务",
          text: "约 120-180 亿元。收入约 36 亿元、同比基本持平，更像稳定现金流业务，不是估值弹性主来源。",
        },
        {
          title: "现金流、库存和减值折价",
          text: "扣减约 120-250 亿元。经营现金流增速明显低于利润，资产减值损失同比扩大，说明高增长背后需要给库存和设备利用质量留折价。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 1200-1550 亿元",
          text: "制造业景气走弱，新能源汽车链价格竞争加剧，现金流持续弱于利润，存货和资产减值继续扩大。这个情景下当前价格偏贵。",
        },
        {
          title: "中性情景：约 1550-1950 亿元",
          text: "通用自动化维持增长，新能源汽车和轨交利润率稳定，经营现金流逐步追上利润，存货和减值压力没有继续扩大。这是当前主情景。",
        },
        {
          title: "乐观情景：约 1950-2400 亿元",
          text: "通用自动化景气回升，新产品平台化和出海开始贡献可见订单，新能源汽车业务利润率改善，现金流质量明显修复。此时当前价格才更有上行空间。",
        },
      ],
      implied: [
        {
          title: "市场仍把汇川当高质量工业龙头",
          text: "近 40x PE 说明市场没有按普通制造公司定价，而是在买国产替代、平台化产品矩阵和双轮增长。",
        },
        {
          title: "Forward PE 约 28x 要求增长继续兑现",
          text: "这个倍数可以接受，但前提是 2026 年利润继续增长，且现金流和库存质量不能恶化。",
        },
        {
          title: "现金流和减值是估值闸门",
          text: "如果经营现金流继续明显弱于利润，或资产减值继续扩大，市场会降低对平台型工业公司的估值溢价。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "通用自动化继续增长，新能源汽车业务利润率稳定，经营现金流增速追上利润，存货和减值压力缓解，新产品/出海订单更清晰。",
        },
        {
          title: "继续等待的触发",
          text: "收入和利润继续增长，但经营现金流、存货和减值没有同步改善。此时研究可以积极，资金动作仍要克制。",
        },
        {
          title: "下调估值中枢的触发",
          text: "制造业景气下行、通用自动化增速放缓、新能源车业务利润率被压缩，经营现金流持续弱于利润，或资产减值继续扩大。",
        },
      ],
    },
    latest: "./company.html?company=inovance&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=inovance&section=archive",
    onePager: "./company-deep.html?company=inovance&section=onePager",
  },
  gevernova: {
    title: "GE Vernova",
    tag: "美股",
    tagClass: "us",
    summary: "GE Vernova 最该盯的不是电力叙事本身，而是订单、backlog、利润率、自由现金流和全年指引能否一起兑现。",
    thesis: "GE Vernova 是发电、电网设备和服务三条关键链路上的电力系统升级平台。",
    action: "维持 A 池核心，并适度提升研究优先级",
    portfolioAction: "继续观察；若 Q2/Q3 继续验证订单、利润率和自由现金流强势，可进入更积极的分批加仓候选。",
    nextCheck: "2026Q2 订单、backlog、Power / Electrification 利润率、自由现金流和 Prolec 并表质量。",
    positioning: "GE Vernova 的定位是电力系统升级平台，不只是单一发电设备商。",
    products: "主营覆盖 Power、Electrification、Grid、Wind 和相关服务。当前最关键的是订单和 backlog 怎么转化为利润率与现金流。",
    markets: "主要面向美国及全球电网升级、电力投资和数据中心电力配套需求。当前最强市场驱动来自北美电力系统紧张与数据中心扩张。",
    moatDetail: "它的优势在于 installed base、项目交付能力和 Power + Electrification 协同。和纯设备公司相比，它更像站在更完整的电力系统链条上。",
    business: "不是单一设备公司，而是在 Power、Electrification 和服务三条线上同时受益于全球电力系统升级。",
    moat: "installed base、项目交付经验、Power 与 Electrification 协同，以及更长的 backlog 可见性。",
    financials: "当前财报最该看订单、backlog、利润率和自由现金流，而不是只看电力主题热度。",
    valuation: "研究上可提升优先级，但仓位动作仍要等订单与现金流持续兑现，而不是只凭长周期叙事加仓。",
    latestEvent: "2026Q1 订单同比增长 71%，backlog 顺增 130 亿美元，自由现金流 48 亿美元，全年指引上修。",
    businessImpact: "这让 GE Vernova 更像完整的电力系统升级平台，而不是只吃某一段设备景气；电力周期正在转化为订单和现金流。",
    valuationImpact: "研究上继续强化，但仓位动作仍要等 Q2/Q3 验证订单、利润率、自由现金流和 Prolec 整合是否持续兑现。",
    risk: "Wind 板块拖累、项目执行风险、并购整合质量和利润率波动。",
    focus: [
      "2026Q2 订单与 backlog 是否继续高位",
      "Power 和 Electrification 业务利润率是否继续改善",
      "Prolec 并表后 Electrification 增长质量",
      "自由现金流是否继续向 50-60 亿美元全年指引靠拢",
    ],
    trackingGuide: [
      "先看哪里：季度业绩和业绩会。重点看订单、backlog、利润率和自由现金流。",
      "怎么判断：如果订单继续强、利润率同步改善，说明电力升级叙事开始真正兑现；如果只有订单没有现金流，就要保守。",
      "再看外部：观察美国电网投资、数据中心电力需求和并购整合情况，看需求和执行是不是同向强化。",
    ],
    financeMap: {
      intro: "GE Vernova 的财务地图要先看需求可见性，再看兑现质量。订单和 backlog 决定未来收入可见性，利润率和自由现金流决定这个周期是不是能变成股东价值。",
      rows: [
        {
          metric: "2026Q1 订单",
          value: "124 亿美元",
          change: "同比 +71%",
          read: "这是最关键的领先指标，说明电力设备和服务需求仍然很强，不只是存量 backlog 消化。",
        },
        {
          metric: "Backlog",
          value: "1630 亿美元",
          change: "季度顺增 130 亿美元",
          read: "backlog 是未来收入和交付的蓄水池，顺增说明订单可见性继续增强。",
        },
        {
          metric: "Gas Power 排产",
          value: "100GW",
          change: "设备 backlog + slot reservation agreements",
          read: "这说明核心发电设备不是短期需求，而是已经进入更长排产周期。",
        },
        {
          metric: "2026Q1 收入",
          value: "82 亿美元",
          change: "同比 +11%",
          read: "收入增长低于订单增速，说明一部分需求还在 backlog 中，后续要看交付节奏。",
        },
        {
          metric: "Adjusted EBITDA",
          value: "11 亿美元",
          change: "Margin 13.9%",
          read: "利润率明显高于此前年度水平，说明订单兑现质量在改善。",
        },
        {
          metric: "自由现金流",
          value: "48 亿美元",
          change: "经营现金流 52 亿美元",
          read: "对工业公司很关键，说明本季度不是只有订单和利润，现金流也同步兑现。",
        },
        {
          metric: "2026 收入指引",
          value: "370-380 亿美元",
          change: "上调全年指引",
          read: "管理层把一季度强势部分外推到全年，后续要看是否兑现。",
        },
        {
          metric: "2026 FCF 指引",
          value: "50-60 亿美元",
          change: "上调全年自由现金流指引",
          read: "如果全年兑现，GE Vernova 的估值逻辑会从主题股更靠近高质量工业现金流平台。",
        },
      ],
      bridge: [
        {
          label: "第一层：订单是领先指标",
          text: "订单同比 +71%，说明需求仍在进入公司，而不是只靠过去积累的 backlog。",
        },
        {
          label: "第二层：backlog 给可见性",
          text: "backlog 到 1630 亿美元，并且单季顺增 130 亿美元，提供未来收入和产能排布可见性。",
        },
        {
          label: "第三层：利润率验证质量",
          text: "Adjusted EBITDA margin 13.9%，说明订单开始转化为更好的经营质量。",
        },
        {
          label: "第四层：自由现金流验证兑现",
          text: "自由现金流 48 亿美元，说明本季度不是只增加订单，而是已经有现金流产出。",
        },
        {
          label: "第五层：指引上修决定持续性",
          text: "全年收入、利润率和自由现金流指引上调，后续要看 Q2/Q3 是否继续兑现，而不是 Q1 一次性高点。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "GE Vernova 的电力周期逻辑继续强化，且正在从订单和 backlog 进一步兑现到利润率与自由现金流。",
        },
        {
          title: "下一季最该看",
          text: "Q2 订单、backlog、Power / Electrification 利润率、Prolec 并表贡献和自由现金流节奏。",
        },
        {
          title: "真正的风险信号",
          text: "如果订单高但利润率回落、自由现金流无法延续，或 Wind / 项目执行拖累扩大，就要下调确信度。",
        },
      ],
    },
    businessMap: {
      intro: "GE Vernova 不是单一电力设备商，而是站在发电、电网设备、电气化和服务几条链路上的电力系统升级平台。它的价值来自电力需求增长、设备供给紧张、服务 installed base 和电网投资共振。",
      segments: [
        {
          title: "Power：发电设备和服务底座",
          scale: "Gas Power backlog / slot reservation agreements 100GW",
          text: "Power 是公司最核心的周期兑现抓手之一。燃气发电设备、服务和长期排产让公司直接受益于全球电力需求和可靠电源投资。",
        },
        {
          title: "Electrification：电网设备主线",
          scale: "Prolec 并表后更重要",
          text: "这条线对应电网升级、变压器、输配电和数据中心电力连接。Prolec 交易增强了北美电网设备供给能力，是后续利润率和增长质量的关键观察点。",
        },
        {
          title: "Wind：潜在拖累和可选改善",
          scale: "仍需谨慎跟踪",
          text: "Wind 不是当前最强逻辑，但它会影响整体利润率和市场情绪。如果 Wind 拖累收窄，会给估值提供弹性；如果继续恶化，会抵消 Power / Electrification 的强化。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在 installed base、项目交付经验、发电设备服务能力、电网设备布局和越来越长的 backlog 可见性。",
        },
        {
          title: "和普通设备公司差别",
          text: "普通设备公司更容易只吃单一产品周期，GE Vernova 同时站在发电、电网、服务和电气化几条链路上，更接近电力系统升级平台。",
        },
        {
          title: "护城河的弱点",
          text: "它仍然是工业项目公司，项目执行、供应链、并购整合、Wind 拖累和周期节奏都会影响利润率与现金流。",
        },
      ],
    },
    valuationFrame: {
      intro: "GE Vernova 的估值不应只看电力主题热度，而要看订单和 backlog 能否持续转化为利润率、自由现金流和更高质量的全年指引。",
      cards: [
        {
          title: "估值上行条件",
          text: "订单继续高位，backlog 继续增长，Power / Electrification 利润率改善，自由现金流向 50-60 亿美元全年指引靠拢。",
        },
        {
          title: "估值压制因素",
          text: "如果订单强但利润率回落，或自由现金流不能延续，市场会把它重新看成周期设备股，而不是电力系统升级平台。",
        },
        {
          title: "当前动作",
          text: "研究上提升优先级；资金动作仍要克制，等待 Q2/Q3 验证订单、利润率、现金流和 Prolec 整合持续性。",
        },
        {
          title: "真正触发升级的证据",
          text: "连续几个季度订单、backlog、利润率和自由现金流同向改善，同时 Wind 拖累没有扩大。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 至 2026-04-30 可得市场数据",
      intro: "GE Vernova 的估值模型要把“电力系统升级叙事”翻译成订单、backlog、利润率和自由现金流。它现在已经不是便宜的周期设备股，市场在提前买电网升级、燃气发电排产、数据中心电力需求和 Prolec 并表后的平台价值。",
      conclusion: "偏高但有基本面支撑；不适合只因电力主题追价",
      read: "按 2026-04-15 快照，GEV 股价约 US$975-980、市值约 US$262-263B、PE 约 55.8x、Forward PE 约 69.0x、P/FCF 约 71.8x；4 月 30 日收盘约 US$1,083.5，市值粗略上移到约 US$291B。第一版合理市值区间约 US$220-280B，中枢约 US$250B。当前价格已经在区间上沿甚至略上方，需要 Q2/Q3 连续证明订单、利润率和自由现金流，而不是只靠电力景气叙事。",
      snapshot: [
        {
          label: "股价快照",
          value: "约 US$975-1,083",
          note: "2026-04-15 至 2026-04-30 可得市场快照；4 月 30 日收盘约 US$1,083.5。",
        },
        {
          label: "总市值",
          value: "约 US$262B-291B",
          note: "4 月中旬约 US$262B；按 4 月 30 日价格粗略约 US$291B。",
        },
        {
          label: "估值倍数",
          value: "PE 约 55.8x / P/FCF 约 71.8x",
          note: "这不是普通工业设备股估值，市场已经给了电力系统升级平台溢价。",
        },
        {
          label: "全年现金流锚",
          value: "2026 FCF 指引 US$5-6B",
          note: "如果全年兑现，按 4 月底市值仍约 48-58 倍指引自由现金流，不便宜。",
        },
      ],
      currentBreakdown: [
        {
          title: "Power：发电设备与服务底座",
          text: "约 US$90-115B。依据是 Gas Power backlog / slot reservation agreements 达 100GW，发电设备和服务是电力需求增长最直接的兑现通道。",
        },
        {
          title: "Electrification：电网升级和 Prolec 并表",
          text: "约 US$75-105B。电网、变压器和输配电设备是当前最稀缺的链条之一，Prolec 交易强化北美电网设备供给能力，但并表后的利润率和交付质量还要验证。",
        },
        {
          title: "服务、installed base 与 backlog 可见性",
          text: "约 US$45-65B。1630 亿美元 backlog 和大量 installed base 提供未来收入可见性，也让公司比普通一次性设备销售更有韧性。",
        },
        {
          title: "Wind 修复期权",
          text: "约 US$0-15B。Wind 目前不是主要估值支撑，更像潜在修复期权。如果拖累收窄，会带来估值弹性；如果继续恶化，会抵消 Power 和 Electrification 的改善。",
        },
        {
          title: "项目执行、周期和高估值折价",
          text: "扣减约 US$25-55B。P/FCF 高、订单交付周期长、项目执行风险、供应链和 Wind 拖累，都要求估值里保留折价。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 US$170-220B",
          text: "订单仍高但利润率回落，自由现金流不能延续 Q1 强度，Wind 或项目执行拖累扩大。这个情景下，当前市值明显偏贵。",
        },
        {
          title: "中性情景：约 US$220-280B",
          text: "2026 收入落在 370-380 亿美元指引，FCF 接近 50-60 亿美元指引，Power / Electrification 利润率继续改善，Prolec 并表不拖累。这是当前主情景。",
        },
        {
          title: "乐观情景：约 US$280-340B",
          text: "订单和 backlog 继续上行，Electrification 供给紧缺持续，Power 排产更长，Wind 拖累收窄，自由现金流显著超过指引。当前价格需要接近这个情景才能更舒服。",
        },
      ],
      implied: [
        {
          title: "市场已经把它当电力系统升级平台",
          text: "US$260B 以上市值和 70x 左右 P/FCF，说明市场买的是长周期电力设备稀缺，而不是只看当期利润。",
        },
        {
          title: "当前价格隐含 Q2/Q3 必须继续兑现",
          text: "Q1 订单 +71%、backlog 顺增 130 亿美元、FCF 48 亿美元很强，但当前价格需要这些指标不是一次性高点。",
        },
        {
          title: "自由现金流比订单更关键",
          text: "订单和 backlog 再强，如果不能转成利润率和现金流，市场会把它重新定价为周期设备公司。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "Q2/Q3 订单、backlog、Power / Electrification 利润率和自由现金流同向强化，2026 FCF 指引继续上修，Wind 拖累没有扩大。",
        },
        {
          title: "继续等待的触发",
          text: "订单仍强但股价处于高位，且自由现金流和 Prolec 并表质量还没有连续验证。此时更适合等回调或等下一季数据。",
        },
        {
          title: "下调估值中枢的触发",
          text: "订单增速回落、backlog 不再增长、利润率下滑、FCF 低于指引路径，或 Wind / 项目执行风险重新扩大。",
        },
      ],
    },
    latest: "./company.html?company=gevernova&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=gevernova&section=archive",
    onePager: "./company-deep.html?company=gevernova&section=onePager",
  },
  luxshare: {
    title: "立讯精密",
    tag: "A 股",
    tagClass: "cn",
    summary: "立讯现在最该看的不是表面增长，而是营运资本与现金流质量：应付回落、存货占用与应收变化谁在主导。",
    thesis: "立讯是中国复杂精密制造与系统集成能力的代表性公司之一。",
    action: "需要二次验证（现金流质量）",
    portfolioAction: "观望为主，不追加；等待 2026Q1 季报验证现金流与营运资本，若验证失败再考虑减仓/降级。",
    nextCheck: "预计 2026-04-25 前后披露的 2026Q1 季报：经营性应付/存货/经营性应收三项是否同步改善。",
    positioning: "立讯的定位是复杂精密制造和系统集成平台，不是单一消费电子代工厂。",
    products: "主营覆盖消费电子精密制造、连接器、声学、通信、汽车电子和系统级组装等。",
    markets: "主要面向全球消费电子、通信和汽车产业链客户。当前最关键的是能否从单一大客户链条逐步走向多业务引擎。",
    moatDetail: "它的优势在于复杂制造执行力、客户协同能力和快速扩产能力。和普通制造企业相比，它更强在把复杂项目规模化落地。",
    business: "长期逻辑来自复杂制造执行能力和从消费电子向汽车、通信、数据中心等多业务延展的能力。",
    moat: "复杂制造、客户绑定和系统集成能力构成它的护城河，但这些优势必须最终体现在现金流上。",
    financials: "把“利润”拆成“现金”：优先盯经营性应付/存货/经营性应收三项，其次再看 capex 与并表整合对现金流的影响。",
    valuation: "估值能否站得住，核心取决于增长能否持续转化为自由现金流与资本回报；在验证前不适合激进加仓。",
    latestEvent: "年报拆解显示：现金流压力更像应付回落+存货占用，而非全公司回款崩坏；2026Q1 是关键验证点。",
    businessImpact: "业务扩张仍在推进（消费电子基座 + 汽车/通讯及数据中心增量），但“扩张质量”进入强验证阶段。",
    valuationImpact: "资金动作以观望为主：在 2026Q1 验证前不追加；若应收转为拖累且存货继续堆、应付继续回落，则需下调确信度并收敛仓位。",
    risk: "客户集中、资本开支回报、新业务扩张不及预期和现金流质量恶化。",
    focus: [
      "经营性应付是否继续回落（付款/结算节奏）",
      "存货占用是否继续扩大（爬坡与去化效率）",
      "经营性应收是否由贡献转为拖累（回款/账期）",
      "资本开支和客户集中风险",
    ],
    trackingGuide: [
      "先看哪里：年报/季报里的现金流补充资料与资产负债表变动原因。把 CFO 拆到“应付/存货/应收”三项。",
      "怎么判断：若 CFO 转差主要由应付回落与存货占用驱动，仍可视为扩张期波动；若应收开始显著拖累，则要把它升级为回款风险。",
      "再看外部：跟踪大客户周期与汽车/通讯爬坡的量产节奏，看“增量业务”是否在拉高毛利/现金回报而非只拉高规模。",
    ],
    financeMap: {
      intro: "先不急着看估值倍数，先把利润、现金流和营运资本的关系看清楚。立讯 2025 年的关键问题不是“有没有增长”，而是增长过程里现金被哪些科目占用了。",
      rows: [
        {
          metric: "经营现金流净额",
          value: "+173.25 亿元",
          change: "同比下降 36.11%",
          read: "全年仍为正，说明不是现金流崩坏；但同比明显下降，说明增长质量需要复核。",
        },
        {
          metric: "2025H1 经营现金流",
          value: "-16.58 亿元",
          change: "Q1 -66.92 亿元拖累，Q2 起转正",
          read: "压力集中在上半年，尤其 Q1；更像结算节奏问题，而不是全年线性恶化。",
        },
        {
          metric: "经营性应付项目",
          value: "-135.16 亿元",
          change: "现金流调节表最大拖累项",
          read: "对应“向供应商付款/应付减少”。这是本轮现金流下降的主因，说明公司把过去欠供应商的钱支付出去了。",
        },
        {
          metric: "存货",
          value: "-33.83 亿元",
          change: "存货增加导致现金占用",
          read: "对应备货、爬坡、并表或交付节奏。它不是坏账风险，但会占用现金，后续要看能否转化为收入和回款。",
        },
        {
          metric: "经营性应收项目",
          value: "+60.06 亿元",
          change: "对经营现金流为正贡献",
          read: "这点很关键：它反证 2025 年现金流压力不能简单归因为客户回款崩坏。",
        },
        {
          metric: "消费电子收入",
          value: "2642.66 亿元",
          change: "占总收入 79.52%",
          read: "仍是公司现金流波动的最大底盘，大客户周期和供应链结算节奏会显著影响现金流。",
        },
        {
          metric: "汽车电子收入",
          value: "392.55 亿元",
          change: "同比增长 185.34%",
          read: "是重要增量，但高增长和并表整合也可能带来存货、在制品和营运资本占用。",
        },
      ],
      bridge: [
        {
          label: "第一层：全年现金流没有崩",
          text: "经营现金流净额 +173.25 亿元，仍然是正数，所以不能把它直接定性为现金流危机。",
        },
        {
          label: "第二层：同比下降需要警惕",
          text: "同比下降 36.11%，说明利润增长没有同等质量地转化成现金，需要拆科目。",
        },
        {
          label: "第三层：主因是应付回落",
          text: "经营性应付项目减少 -135.16 亿元，是最大拖累。通俗说，就是公司支付了更多供应商到期货款。",
        },
        {
          label: "第四层：存货是次要占用",
          text: "存货增加 -33.83 亿元，占用了现金。它可能来自备货、项目爬坡或并表整合，后面要看能否释放。",
        },
        {
          label: "第五层：应收没有证明回款崩坏",
          text: "经营性应收项目贡献 +60.06 亿元，所以现有证据不支持“客户收不回钱”这个最坏解释。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "立讯不是被这一组现金流数据直接否定，而是进入“现金流质量验证期”。看多或看空都要等下一期数据验证。",
        },
        {
          title: "下一季最该看",
          text: "2026Q1 要继续拆三项：应付是否继续大幅减少、存货是否继续增加、应收是否从正贡献转为拖累。",
        },
        {
          title: "真正的风险信号",
          text: "如果应付继续回落、存货继续堆、应收也开始拖累，同时经营现金流再次大幅转负，那才是需要下调确信度的组合信号。",
        },
      ],
    },
    businessMap: {
      intro: "立讯不是简单的“苹果链代工厂”。更准确的理解是：它以消费电子大客户体系为现金和能力底座，再把复杂制造、连接、模组、线束和系统组装能力迁移到汽车、通信及数据中心。",
      segments: [
        {
          title: "消费电子：现金流和规模底盘",
          scale: "2025 收入 2642.66 亿元，占比 79.52%",
          text: "这是公司绝对体量最大的业务，也是供应链结算、客户账期和现金流波动的主来源。它的好处是规模、效率和客户协同强；风险是客户集中度高，议价和排产变化会迅速反映到营运资本。",
        },
        {
          title: "汽车电子：第二增长曲线",
          scale: "2025 收入 392.55 亿元，同比增长 185.34%",
          text: "这条线的价值在于把连接器、线束、模组和系统集成能力迁移到汽车产业链。但高增长阶段通常伴随并表、备货、项目爬坡和现金占用，所以不能只看增速，要看利润率、存货周转和回款质量。",
        },
        {
          title: "通讯及数据中心：潜在增量",
          scale: "2025 收入 245.68 亿元，占比 7.39%",
          text: "这个板块还不是最大收入来源，但如果数据中心连接、散热、线缆和系统级交付能力持续增强，可能成为估值重估的一个来源。当前需要证据，而不是先把它当成 AI 概念股。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在复杂项目的制造执行力、快速扩产、客户协同和供应链管理。它不是靠单一专利赢，而是靠把复杂产品稳定、低成本、大规模交付出来。",
        },
        {
          title: "和普通制造公司差别",
          text: "普通制造企业往往只能做单点零件或单一工序，立讯更接近“复杂制造平台”：能从连接器、模组延伸到系统组装，并围绕大客户需求持续扩品类。",
        },
        {
          title: "护城河的弱点",
          text: "制造平台的护城河最终必须体现在现金流和资本回报。如果收入扩张依赖更多存货、更多应付波动和更重资本投入，护城河就会被财务质量稀释。",
        },
      ],
    },
    valuationFrame: {
      intro: "立讯的估值不能只用“收入利润增长”来判断。更合适的方式是先判断它处在什么质量状态：高质量制造平台、扩张但现金流承压的平台，还是增长质量恶化的制造公司。",
      cards: [
        {
          title: "估值上行条件",
          text: "如果 2026Q1 之后经营现金流修复，存货和应付压力缓解，同时汽车电子、通信及数据中心继续增长，市场才有理由把它看成多业务制造平台，而不是单一消费电子链公司。",
        },
        {
          title: "估值压制因素",
          text: "如果增长伴随持续现金流转弱、存货堆积、应收开始拖累，估值中枢会被压低。制造公司最怕“利润表好看，但现金流和周转质量变差”。",
        },
        {
          title: "当前动作",
          text: "现阶段不是因为单条年报现金流就否定公司，也不是因为收入利润增长就加大动作。更合理的是维持跟踪，等待 2026Q1 把应付、存货、应收三项验证清楚。",
        },
        {
          title: "真正触发升级的证据",
          text: "经营现金流连续修复、存货周转稳定、应收不恶化，新业务增长没有吞噬现金流，同时客户集中风险没有进一步扩大。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 可得市场数据；另参考你提到的近期约 68 元价格",
      intro: "立讯这一版估值模型不再只问“公司好不好”，而是问：当前价格已经预支了多少新业务和现金流修复？如果没有现金流验证，哪些价格属于合理、偏贵或值得等待。",
      conclusion: "58-60 元附近接近合理中枢；68 元附近偏向乐观区间，不适合无验证追价",
      read: "按 2026-04-15 可得快照，立讯股价约 58.78 元、市值约 4283 亿元、TTM PE 约 26 倍、Forward PE 约 20.8 倍。若按你观察到的 68 元附近估算，市值约 4950 亿元，已经接近第一版乐观区间下沿。第一版合理市值区间约 4000-4700 亿元，中枢约 4350 亿元；因此现阶段更像“好公司，但价格已经要求 2026Q1 现金流和新业务继续兑现”。",
      snapshot: [
        {
          label: "股价快照",
          value: "约 58.78 元",
          note: "2026-04-15 可得市场快照，非实时；近期你观察到约 68 元，说明价格已经明显上移。",
        },
        {
          label: "总市值",
          value: "约 4283 亿元",
          note: "按 58.78 元快照；若按 68 元附近，粗略对应约 4950 亿元。",
        },
        {
          label: "估值倍数",
          value: "TTM PE 约 26x / Forward PE 约 20.8x",
          note: "这个倍数本身不离谱，但制造平台要看现金流质量，不能只看利润增速。",
        },
        {
          label: "当前关键分歧",
          value: "现金流验证",
          note: "市场正在给汽车电子、通信/数据中心和平台化一部分估值，但 2025 经营现金流同比下降 36.11%，所以需要下一季验证。",
        },
      ],
      currentBreakdown: [
        {
          title: "消费电子复杂制造底盘",
          text: "约 2800-3300 亿元。依据是 2025 年消费电子收入 2642.66 亿元、占总收入 79.52%，仍是利润和现金流底盘；但客户集中、议价压力和营运资本波动使它不能按高成长科技股估值。",
        },
        {
          title: "汽车电子第二增长曲线",
          text: "约 900-1400 亿元。依据是 2025 年汽车电子收入 392.55 亿元、同比增长 185.34%。这部分是估值弹性的主要来源，但还要看利润率、并表整合、存货和现金回收。",
        },
        {
          title: "通信及数据中心增量",
          text: "约 400-800 亿元。依据是 2025 年通信及数据中心收入 245.68 亿元、占比 7.39%。它可以给公司带来 AI 基础设施相关的重估想象，但目前证据还不够把它当作主估值锚。",
        },
        {
          title: "其他业务与系统集成协同",
          text: "约 200-400 亿元。包括连接、声学、模组和系统级组装能力在不同客户/产品线之间迁移带来的协同价值。",
        },
        {
          title: "现金流与客户集中折价",
          text: "扣减约 300-700 亿元。原因是 2025 年经营现金流 +173.25 亿元但同比下降 36.11%，且主要受应付回落和存货占用影响；如果 2026Q1 修复，这个折价可以收窄，反之会扩大。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 3300-3900 亿元",
          text: "消费电子仍稳，但汽车电子和数据中心增量没有带来足够利润质量；经营现金流继续弱于利润，存货和应付压力没有缓解。这个情景下，68 元附近明显偏贵。",
        },
        {
          title: "中性情景：约 4000-4700 亿元",
          text: "利润增长延续，2026Q1 经营现金流部分修复，应付/存货/应收没有同时恶化，汽车电子和通信数据中心继续增长。这是当前最适合采用的主情景。",
        },
        {
          title: "乐观情景：约 5000-6000 亿元",
          text: "现金流明显修复，汽车电子和数据中心开始贡献更清晰利润，客户结构改善，市场把立讯从单一消费电子链公司重估为多业务复杂制造平台。",
        },
      ],
      implied: [
        {
          title: "58-60 元附近隐含什么",
          text: "市场大致承认消费电子底盘稳、汽车电子有成长，但还没有完全把现金流修复和数据中心重估打满。",
        },
        {
          title: "68 元附近隐含什么",
          text: "市场已经在预支更强的 2026Q1 验证：经营现金流改善、新业务继续高增、客户集中风险没有恶化。这个价格下容错率变低。",
        },
        {
          title: "真正决定估值方向的不是涨了多少",
          text: "关键是下一季现金流是否跟上利润。如果利润继续增长但现金流、存货、应收变差，估值中枢会被压低。",
        },
      ],
      triggers: [
        {
          title: "可以更积极分批的触发",
          text: "2026Q1 经营现金流明显修复，应付不再大幅回落，存货没有继续堆高，应收没有转为明显拖累，同时汽车电子和通信数据中心继续增长。",
        },
        {
          title: "继续观望的触发",
          text: "股价在 68 元附近或更高，但 Q1 还没有证明现金流修复。此时不需要因为上涨而追价，先让数据说话。",
        },
        {
          title: "下调估值中枢的触发",
          text: "经营现金流再次大幅转弱、存货继续增加、应收开始拖累，或者新业务高增长但利润率/现金回报不清晰。",
        },
      ],
    },
    latest: "./company.html?company=luxshare&v=20260412-24#companyUpdates",
    archive: "./company-deep.html?company=luxshare&section=archive",
    onePager: "./company-deep.html?company=luxshare&section=onePager",
  },
  constellation: {
    title: "Constellation Energy",
    tag: "美股",
    tagClass: "us",
    summary: "Constellation 的关键不只是核电资产稀缺性，而是稳定电力资产、长期合同和 Calpine 整合能否把稀缺性转成 EPS 与现金流成长。",
    thesis: "Constellation 正在从核电稀缺资产持有者演进为面向 AI、电气化和再工业化的成长型电力平台。",
    action: "维持 A 池核心，并提升合同与资本回报验证优先级",
    portfolioAction: "继续观察；若 2026 EPS、长期合同溢价和 Calpine 整合继续兑现，可进入更积极的分批候选。",
    nextCheck: "下一次重点看 2026 EPS 指引兑现、147 million MWh 核电签约溢价、Calpine 整合和自由现金流。",
    positioning: "Constellation 的定位是稳定、清洁、可调度电力平台。它不只是核电资产持有者，而是在用核电、天然气、地热和商业合同能力服务数据中心、电气化和再工业化需求。",
    products: "主营包括核电发电、天然气发电、地热及其他清洁能源、电力零售和大型客户长期供电方案。当前最关键的增量来自长期供电协议、Calpine 整合、核电电量重定价和数据中心负荷需求。",
    markets: "主要面向美国电力市场、大型商业和工业客户、数据中心客户，以及需要稳定低碳电力的企业。当前最重要的市场驱动力是 AI 数据中心、电气化、再工业化和能源安全。",
    moatDetail: "它的优势在于稀缺核电资产、稳定可调度电力、核电运营经验、长期供电合同能力和并购后更大的商业平台。和普通公用事业公司相比，它更有成长弹性；和单一发电商相比，它更能把电力资产组合卖成长期合同。",
    business: "核电底座仍是核心，但真正改变公司边界的是 Calpine 并购之后的大规模电力平台和商业合同能力。",
    moat: "稳定零碳电力资产、核电运营经验、55GW 发电平台、长期供电合同能力和更大的商业客户覆盖。",
    financials: "当前最该看 2026 adjusted operating EPS、Base EPS 增长目标、147 million MWh 核电签约溢价、growth capex 回报、回购和自由现金流。",
    valuation: "估值不应只看核电主题，而要看稀缺电力能否通过长期合同、EPS 增长和现金流回报持续兑现。",
    latestEvent: "2026 Outlook 给出 adjusted operating EPS 11-12 美元，并提出 2026-2029 Base EPS 增长 20%+，但 growth capex 和合同溢价仍需验证。",
    businessImpact: "公司正在从核电稀缺资产，升级为核电、天然气、地热和商业合同能力结合的成长型电力平台。",
    valuationImpact: "长期逻辑强化，但 2026 指引与市场预期、growth capex 回报和 Calpine 整合质量必须一起看。",
    risk: "Calpine 整合、监管资产剥离、growth capex 回报不及预期、电力价格波动、核电资产运行和政策风险。",
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
    financeMap: {
      intro: "Constellation 的财务地图不能只看公用事业式稳定利润。真正要拆的是：2026 EPS 指引能否兑现、长期 Base EPS 增长目标是否有合同支撑、核电电量能否重定价、Calpine 整合是否增厚现金流，以及 growth capex 是否获得足够回报。",
      rows: [
        {
          metric: "2026 adjusted operating EPS 指引",
          value: "11.00-12.00 美元",
          change: "管理层 2026 Outlook",
          read: "这是短期兑现锚点。后续要看实际业绩能否落在区间内，甚至是否有上修空间。",
        },
        {
          metric: "2026-2029 Base EPS 增长目标",
          value: "20%+",
          change: "管理层长期目标",
          read: "这是成长型平台重估的核心，但需要合同溢价、Calpine 协同和资本配置共同兑现。",
        },
        {
          metric: "长期滚动三年 Base EPS 增长",
          value: "10%+",
          change: "长期目标",
          read: "如果能持续做到，Constellation 就不只是稳定电力股，而是稀缺电力成长股。",
        },
        {
          metric: "年度可用核电电量",
          value: "147 million MWh",
          change: "未纳入增长展望的潜在上行",
          read: "这是最关键的隐藏杠杆：如果能签出高溢价长期合同，会直接影响 EPS 和估值中枢。",
        },
        {
          metric: "发电组合规模",
          value: "约 55GW",
          change: "Calpine 合并后",
          read: "规模从核电稀缺资产扩展为核电、天然气、地热和商业平台组合。",
        },
        {
          metric: "总回购授权",
          value: "50 亿美元",
          change: "授权提升",
          read: "说明管理层仍重视股东回报，但要与 growth capex 和资产负债表一起看。",
        },
        {
          metric: "Growth capital",
          value: "39 亿美元",
          change: "计划投入增长项目",
          read: "这不是普通维护性投入，而是为了捕捉电力需求增长。关键是回报率能否兑现。",
        },
        {
          metric: "潜在上行来源",
          value: "核电溢价、额外天然气合同、增厚型资本配置",
          change: "未纳入基础增长目标",
          read: "这决定公司能否从“有稳定资产”升级为“有成长选项”。",
        },
      ],
      bridge: [
        {
          label: "第一层：短期看 EPS 指引",
          text: "2026 adjusted operating EPS 11.00-12.00 美元，是判断管理层兑现能力的第一道门槛。",
        },
        {
          label: "第二层：中期看 Base EPS 增长",
          text: "2026-2029 Base EPS 增长 20%+ 是重估核心，但需要合同、协同和资本配置共同支撑。",
        },
        {
          label: "第三层：核电电量是隐藏杠杆",
          text: "147 million MWh 年度可用核电电量若能签出溢价长期合同，会把核电稀缺性直接转成收入和利润。",
        },
        {
          label: "第四层：Calpine 改变公司边界",
          text: "55GW 发电组合让公司从核电资产持有人变成更完整的电力平台，但整合质量要持续验证。",
        },
        {
          label: "第五层：资本回报决定估值",
          text: "39 亿美元 growth capital 和 50 亿美元回购必须平衡好，不能为了成长牺牲现金流质量。",
        },
      ],
      notes: [
        {
          title: "当前结论",
          text: "Constellation 的 2026 Outlook 强化了成长型电力平台逻辑，但判断重点已经从主题热度转向 EPS、合同溢价、growth capex 回报和整合质量。",
        },
        {
          title: "下一季最该看",
          text: "2026 EPS 指引是否维持或上修、长期合同是否新增、Calpine 协同是否开始体现、自由现金流是否支撑回购和 growth capex。",
        },
        {
          title: "真正的风险信号",
          text: "如果合同溢价迟迟不落地、Calpine 整合拖累利润、growth capex 回报不及预期，或者电力价格下行，估值中枢会承压。",
        },
      ],
    },
    businessMap: {
      intro: "Constellation 不是普通公用事业公司。它的核心价值来自稳定、清洁、可调度电力资产，尤其是核电；Calpine 并入后，公司又补上天然气、地热和更大商业平台，使它更能服务 AI 数据中心、电气化和再工业化带来的大负荷需求。",
      segments: [
        {
          title: "核电：最稀缺的底座",
          scale: "147 million MWh 年度可用核电电量是未来签约和溢价的关键",
          text: "核电的价值在于稳定、清洁、可调度。对数据中心和工业客户来说，持续供电比单纯低价电更重要，这给核电长期合同提供溢价空间。",
        },
        {
          title: "Calpine：扩大发电组合和灵活性",
          scale: "合并后约 55GW 发电组合",
          text: "Calpine 带来天然气、地热和更大的商业平台，使 Constellation 不再只依赖核电单一资产，而能用更完整的发电组合服务客户。",
        },
        {
          title: "商业合同：把资产稀缺性变成利润",
          scale: "面向数据中心、大型商业和工业客户",
          text: "真正的价值不是“有电”，而是能把稳定电力签成长期、高质量、可定价的合同。CyrusOne 这类数据中心协议就是验证方向。",
        },
      ],
      moat: [
        {
          title: "强在哪里",
          text: "强在核电稀缺性、稳定可调度电力、运营经验、客户合同能力和 55GW 组合规模。AI 数据中心需要的是长期、稳定、可用电力，这正是公司资产最稀缺的地方。",
        },
        {
          title: "和普通公用事业差别",
          text: "普通公用事业更偏监管回报和稳定分红；Constellation 的弹性来自核电重定价、数据中心长期合同、Calpine 整合和更主动的资本配置。",
        },
        {
          title: "护城河的弱点",
          text: "核电资产虽稀缺，但受监管、安全、检修和政策影响；Calpine 整合复杂；如果电力价格或大客户需求低于预期，成长叙事会被重新定价。",
        },
      ],
    },
    valuationFrame: {
      intro: "Constellation 的估值判断不能只看核电热门，也不能只看稳定分红。核心是稀缺电力能否签成长期合同，并持续转化为 EPS、自由现金流和股东回报。",
      cards: [
        {
          title: "估值上行条件",
          text: "2026 EPS 落在或高于 11-12 美元指引，147 million MWh 核电电量签出溢价，Calpine 协同兑现，growth capex 获得双位数回报。",
        },
        {
          title: "估值压制因素",
          text: "长期合同推进慢、Calpine 整合不顺、监管资产处置影响组合质量、growth capex 回报不足，或电力价格回落。",
        },
        {
          title: "当前动作",
          text: "维持 A 池核心并提升研究优先级，但不因 AI 用电主题追价。更合理的是跟踪合同落地、EPS 和现金流质量。",
        },
        {
          title: "真正触发升级的证据",
          text: "新长期供电合同持续出现、核电溢价明确进入财务预期、Calpine 协同增厚 EPS、自由现金流足以同时支撑 growth capex 和回购。",
        },
      ],
    },
    valuationModel: {
      snapshotDate: "估值快照：2026-04-15 至 2026-04-29 可得市场数据",
      intro: "Constellation 的估值不能按普通公用事业看。市场现在买的不是单纯发电资产，而是核电稀缺性、AI 数据中心用电、长期合同溢价、Calpine 整合和未来 EPS 增长能否一起兑现。",
      conclusion: "合理偏高；必须靠合同、EPS 和自由现金流继续兑现",
      read: "按 2026-04-15 快照，CEG 股价约 US$294.6、市值约 US$106.7B、EV 约 US$114.0B、PE 约 39.8x、Forward PE 约 25.4x；4 月 29 日收盘约 US$297.0，仍低于 52 周高点 US$412.7。第一版合理市值区间约 US$90-120B，中枢约 US$105B。当前价格大致贴近中枢偏上，但 P/FCF 接近 85x，说明市场已经预支了核电重定价和数据中心电力需求，后续必须看现金流兑现。",
      snapshot: [
        {
          label: "股价快照",
          value: "约 US$294.6-297.0",
          note: "2026-04-15 至 2026-04-29 可得市场快照，非实时。",
        },
        {
          label: "总市值 / EV",
          value: "约 US$106.7B / US$114.0B",
          note: "市值已经明显高于传统公用事业估值框架，反映核电和 AI 用电溢价。",
        },
        {
          label: "估值倍数",
          value: "PE 约 39.8x / Forward PE 约 25.4x",
          note: "Forward PE 比 TTM PE 低很多，说明市场在看未来 EPS 增长，而不是当前利润。",
        },
        {
          label: "现金流倍数",
          value: "P/FCF 约 85x",
          note: "这是最大警示：如果长期合同和 Calpine 整合不能改善自由现金流，当前估值会偏贵。",
        },
      ],
      currentBreakdown: [
        {
          title: "核电可调度电力底座",
          text: "约 US$55-70B。依据是 147 million MWh 年度可用核电电量、核电稀缺性和稳定低碳电力价值。这部分是公司估值最核心的底盘，但它必须通过长期合同把稀缺性转成溢价收入。",
        },
        {
          title: "数据中心与大型客户长期合同溢价",
          text: "约 US$15-30B。依据是 AI 数据中心需要稳定、可调度、低碳电力，CyrusOne 等长期供电协议验证了方向。它是估值弹性来源，但不能只靠主题，必须持续看到新合同和价格。",
        },
        {
          title: "Calpine 与 55GW 发电平台",
          text: "约 US$15-25B。Calpine 带来天然气、地热和更大的商业平台，使公司从核电资产持有人扩展为更完整的电力平台；但整合风险和监管资产处置需要折价。",
        },
        {
          title: "回购、growth capital 与资本配置",
          text: "约 US$5-10B。50 亿美元回购授权和 39 亿美元 growth capital 都能提升长期价值，但前提是 EPS 增长和项目回报足够覆盖资本消耗。",
        },
        {
          title: "监管、整合和自由现金流折价",
          text: "扣减约 US$10-20B。核电监管、安全检修、Calpine 整合、资产剥离和 P/FCF 偏高都是估值折价来源。若自由现金流不能改善，这个折价会扩大。",
        },
      ],
      scenarios: [
        {
          title: "保守情景：约 US$70-90B",
          text: "长期合同推进慢，电力价格回落，Calpine 整合贡献低于预期，自由现金流继续偏弱。这个情景下，当前 1000 亿美元以上市值明显偏贵。",
        },
        {
          title: "中性情景：约 US$90-120B",
          text: "2026 adjusted operating EPS 落在 11-12 美元指引，长期合同持续推进，Calpine 整合不拖累，回购和 growth capex 能同时维持。这是当前主情景。",
        },
        {
          title: "乐观情景：约 US$120-150B",
          text: "核电电量签出明显溢价，数据中心合同持续扩张，Calpine 协同增厚 EPS，2026-2029 Base EPS 20%+ 增长目标更可信，市场继续给稀缺电力成长溢价。",
        },
      ],
      implied: [
        {
          title: "市场已经把它当成长型电力平台",
          text: "Forward PE 约 25x 对传统公用事业不低，说明市场已经在买核电稀缺、电力紧张和 AI 数据中心长期需求。",
        },
        {
          title: "当前价格要求 EPS 快速兑现",
          text: "2026 adjusted operating EPS 11-12 美元必须落地，2026-2029 Base EPS 20%+ 增长目标也要有合同和协同支撑。",
        },
        {
          title: "现金流是最大分歧",
          text: "P/FCF 接近 85x 表明自由现金流还没有完全跟上估值。如果 growth capex、整合和回购一起消耗现金，估值会被压缩。",
        },
      ],
      triggers: [
        {
          title: "更积极分批的触发",
          text: "新增数据中心或大型商业长期供电合同，核电溢价进入管理层 EPS 预期，Calpine 协同提前兑现，自由现金流改善并能支撑回购。",
        },
        {
          title: "继续等待的触发",
          text: "EPS 指引仍强，但合同细节、自由现金流和 Calpine 整合证据不足。此时公司逻辑好，但估值已经不便宜。",
        },
        {
          title: "下调估值中枢的触发",
          text: "长期合同落地慢，电力价格或政策环境转弱，Calpine 整合拖累利润，growth capex 回报不足，或自由现金流继续明显弱于 EPS。",
        },
      ],
    },
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

function getEventDateValue(record) {
  if (Number.isFinite(record?.sortKey)) return record.sortKey;

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

function buildFallbackEventRecords(company) {
  const latest = window.COMPANY_EVENT_META?.[company];
  return (latest?.events || []).map((event) => ({
    ...event,
    title: event.title,
    date: event.date,
    type: event.type,
    fact: event.fact || event.note,
    judgment: event.judgment || event.analysis || latest.businessImpact,
    action: event.action || "维持跟踪",
    priority: event.priority || "P2",
  }));
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
    qualityLabel: event.review_status === "reviewed" ? "已研判正式事件" : "",
  };
}

function getEventStoreRecords(company) {
  const events = window.BAMBOO_LENS_EVENT_STORE?.companies?.[company]?.events || [];
  return events.map(normalizeEventStoreRecord);
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

  const sortedRecords = sortEventsNewestFirst(records);
  const pageSize = 4;
  const totalPages = Math.max(1, Math.ceil(sortedRecords.length / pageSize));
  const safePage = Math.min(Math.max(page, 1), totalPages);
  const startIndex = (safePage - 1) * pageSize;
  const visibleRecords = sortedRecords.slice(startIndex, startIndex + pageSize);

  feed.innerHTML = visibleRecords.map((event, index) => `
    <article class="event-card rich-card compact-event">
      <div class="event-meta">
        <span>${event.date}</span>
        <span>${event.type}</span>
      </div>
      <h4>${event.title}</h4>
      <p class="event-summary">${event.fact}</p>
      <p class="event-analysis">判断：${event.judgment}</p>
      ${event.qualityLabel ? `<span class="quality-pill">${event.qualityLabel}</span>` : ""}
      <a class="event-link" href="./event.html?company=${encodeURIComponent(company)}&event=${startIndex + index}&return=company&page=${safePage}&v=20260412-24">查看原文详情</a>
    </article>
  `).join("");

  renderCompanyEventPager(company, safePage, totalPages);
}

function renderCompanyDecisionImpact(company) {
  const section = document.getElementById("companyDecisionImpactSection");
  const feed = document.getElementById("companyDecisionImpactFeed");
  if (!section || !feed) return;

  const impacts = window.BAMBOO_LENS_DECISION_IMPACT?.companies?.[company] || [];
  if (!impacts.length) {
    section.hidden = true;
    return;
  }

  section.hidden = false;
  feed.innerHTML = impacts.slice(0, 5).map((item) => `
    <article class="company-impact-card">
      <div class="decision-card-top">
        <span class="decision-stage">${item.direction}</span>
        <span class="decision-score">${item.trigger_type}</span>
      </div>
      <div class="event-meta">
        <span>${item.event_date}</span>
        <span>${item.event_type}</span>
      </div>
      <h3>${item.event_title}</h3>
      <div class="impact-chip-row">
        ${(item.dimensions || []).map((dimension) => `<span>${dimension}</span>`).join("")}
        ${item.valuation_update_needed ? "<strong>需更新估值视角</strong>" : ""}
      </div>
      <div class="decision-output-box">
        <strong>${item.decision_output?.confidence_change || "维持确信度"}</strong>
        <p>${item.decision_output?.portfolio_hint || "维持观察，等待下一次验证。"}</p>
        <small>应更新：${(item.decision_output?.update_targets || ["当前结论"]).join(" / ")}</small>
      </div>
      <p><strong>判断变化：</strong>${item.decision_change}</p>
      <p><strong>业务影响：</strong>${item.business_impact}</p>
      <p><strong>估值 / 动作：</strong>${item.valuation_impact}</p>
      <div class="decision-next">
        <strong>下一次验证</strong>
        <p>${(item.next_verification || []).join("；") || "等待下一次正式披露。"}</p>
      </div>
      <a class="event-link" href="${item.detail_link}">查看事件详情</a>
    </article>
  `).join("");
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

function renderFinanceMap(financeMap) {
  const section = document.getElementById("companyFinanceSection");
  if (!section) return;

  if (!financeMap) {
    section.hidden = true;
    return;
  }

  section.hidden = false;
  setText("companyFinanceIntro", financeMap.intro);

  const rows = document.getElementById("companyFinanceRows");
  if (rows) {
    rows.innerHTML = (financeMap.rows || []).map((row) => `
      <tr>
        <th scope="row">${row.metric}</th>
        <td>${row.value}</td>
        <td>${row.change}</td>
        <td>${row.read}</td>
      </tr>
    `).join("");
  }

  const bridge = document.getElementById("companyFinanceBridge");
  if (bridge) {
    bridge.innerHTML = (financeMap.bridge || []).map((item, index) => `
      <article class="finance-bridge-item">
        <span>${String(index + 1).padStart(2, "0")}</span>
        <div>
          <h4>${item.label}</h4>
          <p>${item.text}</p>
        </div>
      </article>
    `).join("");
  }

  const notes = document.getElementById("companyFinanceNotes");
  if (notes) {
    notes.innerHTML = (financeMap.notes || []).map((note) => `
      <article class="card finance-note">
        <h3>${note.title}</h3>
        <p>${note.text}</p>
      </article>
    `).join("");
  }
}

function renderBusinessMap(businessMap) {
  const container = document.getElementById("companyBusinessMap");
  if (!container) return;

  if (!businessMap) {
    container.innerHTML = "";
    return;
  }

  container.innerHTML = `
    <article class="business-map-intro">
      <h3>怎么理解这家公司</h3>
      <p>${businessMap.intro}</p>
    </article>
    <div class="business-segment-grid">
      ${(businessMap.segments || []).map((segment) => `
        <article class="card business-segment-card">
          <p class="segment-scale">${segment.scale}</p>
          <h3>${segment.title}</h3>
          <p>${segment.text}</p>
        </article>
      `).join("")}
    </div>
    <div class="business-moat-grid">
      ${(businessMap.moat || []).map((item) => `
        <article class="card">
          <h3>${item.title}</h3>
          <p>${item.text}</p>
        </article>
      `).join("")}
    </div>
  `;
}

function renderValuationFrame(valuationFrame) {
  const section = document.getElementById("companyValuationSection");
  const grid = document.getElementById("companyValuationGrid");
  if (!section || !grid) return;

  if (!valuationFrame) {
    section.hidden = true;
    return;
  }

  section.hidden = false;
  setText("companyValuationIntro", valuationFrame.intro);
  grid.innerHTML = (valuationFrame.cards || []).map((card) => `
    <article class="card valuation-card">
      <h3>${card.title}</h3>
      <p>${card.text}</p>
    </article>
  `).join("");
}

function renderValuationModel(model) {
  const section = document.getElementById("companyValuationModelSection");
  if (!section) return;

  if (!model) {
    section.hidden = true;
    return;
  }

  section.hidden = false;
  setText("companyValuationModelIntro", model.intro);
  setText("companyValuationModelDate", model.snapshotDate);
  setText("companyValuationModelConclusion", model.conclusion);
  setText("companyValuationModelRead", model.read);

  const snapshot = document.getElementById("companyValuationSnapshot");
  if (snapshot) {
    snapshot.innerHTML = (model.snapshot || []).map((item) => `
      <article class="valuation-snapshot-item">
        <span>${item.label}</span>
        <strong>${item.value}</strong>
        <p>${item.note}</p>
      </article>
    `).join("");
  }

  const renderList = (id, items) => {
    const node = document.getElementById(id);
    if (!node) return;
    node.innerHTML = (items || []).map((item) => `
      <article class="valuation-list-item">
        <span>${item.title}</span>
        <p>${item.text}</p>
      </article>
    `).join("");
  };

  renderList("companyValuationCurrentBreakdown", model.currentBreakdown);
  renderList("companyValuationScenarios", model.scenarios);
  renderList("companyValuationImplied", model.implied);
  renderList("companyValuationTriggers", model.triggers);
}

function appendItems(baseItems, extraItems) {
  return [
    ...(Array.isArray(baseItems) ? baseItems : []),
    ...(Array.isArray(extraItems) ? extraItems : []),
  ];
}

function applySectionDeposits(data, override) {
  const deposits = override?.sectionDeposits;
  if (!deposits) return data;

  return {
    ...data,
    financeMap: data.financeMap || deposits.financeMap ? {
      ...(data.financeMap || {}),
      rows: appendItems(data.financeMap?.rows, deposits.financeMap?.rows),
      bridge: appendItems(data.financeMap?.bridge, deposits.financeMap?.bridge),
      notes: appendItems(data.financeMap?.notes, deposits.financeMap?.notes),
    } : data.financeMap,
    businessMap: data.businessMap || deposits.businessMap ? {
      ...(data.businessMap || {}),
      segments: appendItems(data.businessMap?.segments, deposits.businessMap?.segments),
      moat: appendItems(data.businessMap?.moat, deposits.businessMap?.moat),
    } : data.businessMap,
    valuationModel: data.valuationModel || deposits.valuationModel ? {
      ...(data.valuationModel || {}),
      snapshot: appendItems(data.valuationModel?.snapshot, deposits.valuationModel?.snapshot),
      currentBreakdown: appendItems(data.valuationModel?.currentBreakdown, deposits.valuationModel?.currentBreakdown),
      scenarios: appendItems(data.valuationModel?.scenarios, deposits.valuationModel?.scenarios),
      implied: appendItems(data.valuationModel?.implied, deposits.valuationModel?.implied),
      triggers: appendItems(data.valuationModel?.triggers, deposits.valuationModel?.triggers),
    } : data.valuationModel,
  };
}

function applyCompanyStateOverlay(company, data) {
  const state = window.BAMBOO_LENS_COMPANY_STATE?.companies?.[company];
  const override = window.BAMBOO_LENS_COMPANY_PAGE_OVERRIDES?.companies?.[company];
  if (!state && !override) return data;

  const overlaid = {
    ...data,
    action: override?.action || state?.action || data.action,
    nextCheck: override?.nextCheck || state?.nextCheck || data.nextCheck,
    latestEvent: override?.latestEvent || state?.latestEvent || data.latestEvent,
    businessImpact: override?.businessImpact || state?.businessImpact || data.businessImpact,
    valuationImpact: override?.valuationImpact || state?.valuationImpact || data.valuationImpact,
  };
  return applySectionDeposits(overlaid, override);
}

async function initCompanyPage() {
  const params = new URLSearchParams(window.location.search);
  const company = params.get("company");
  const page = Number(params.get("page") || "1");
  const baseData = COMPANY_DATA[company];
  if (!baseData) return;
  const data = applyCompanyStateOverlay(company, baseData);

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
  renderFinanceMap(data.financeMap);
  renderBusinessMap(data.businessMap);
  renderValuationModel(data.valuationModel);

  let records = [];
  try {
    records = await parseEventRecordsFromMarkdown(company);
  } catch (error) {
    console.error(error);
  }

  const storeRecords = getEventStoreRecords(company);
  const safeRecords = storeRecords.length ? storeRecords : (records.length ? records : buildFallbackEventRecords(company));
  renderCompanyEventFeed(company, safeRecords, page);
  renderCompanyDecisionImpact(company);
}

initCompanyPage();
