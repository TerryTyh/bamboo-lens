# 竹鉴晨报 | 2026-05-26

## 1. TSMC｜出售 VIS 约 8.1% 股权：最多处置 1.52 亿股，持股将由约 27.1% 降至约 19%

**原文讲了什么**

- TSMC 公告计划通过大宗交易向金融机构投资者出售最多 1.52 亿股 VIS（Vanguard_International Semiconductor）普通股，约占 VIS 完全稀释后股本的 8.1%。
- 公告强调该出售不影响与 VIS 的战略合作关系，包括：TSMC 继续将 interposer 产能外包给 VIS、并继续向 VIS 授权 GaN 技术；
该交易属于“聚焦核心业务资源”的资本配置安排。

**业务影响**

业务层面，公告明确 interposer 外包与 GaN 技术授权仍将持续，意味着供应链合作关系未发生方向性变化；
同时 TSMC 已在 2024 年 6 月退出 VIS 董事会席位，本次继续降低持股比例可视为治理与资源聚焦的延续。
对 TSMC 的核心竞争力与产能规划并无直接边际信息，但对“如何处理非核心资产、如何在合作与控制之间取舍”的公司理解有增量。

**估值/动作影响**

估值/动作层面，事件的可量化影响取决于出售定价、会计处理与资金用途披露（公告未给出交易价格与预计损益）。
在缺少定价与现金流量化信息的情况下，不把该事件视为仓位动作触发；
后续更多用于更新对资本配置纪律与非核心资产处置节奏的判断。

**后续观察点**

- 跟踪该 block_trade 是否完成、成交价格区间及是否披露一次性损益/现金回笼规模。
- 观察后续公告中对资金用途与资本配置（回购、capex、并购等）的描述是否发生变化。
- 继续跟踪与 VIS 的 interposer 外包与 GaN 授权合作是否保持稳定（供给、质量与交付节奏）。

来源：[TSMC](http://pr.tsmc.com/english/news/3314) / [原文](http://pr.tsmc.com/english/news/3314)

## 2. NVIDIA｜Vera CPU 开始交付：首批送达 Anthropic/OpenAI/SpaceXAI/OCI

**原文讲了什么**

- NVIDIA 宣布其首款面向智能体 AI 的独立数据中心 CPU「Vera」开始向客户交付：首批送达 Anthropic（旧金山）、OpenAI（Mission_Bay）、SpaceXAI（帕洛阿尔托），随后交付 Oracle_Cloud Infrastructure（圣克拉拉）。
- 黄仁勋在 2026 年 3 月 GTC_San Jose 上把 Vera 定位为面向智能体 AI 的新一代 CPU，并称其将成为 NVIDIA 下一条“数十亿美元级”业务线。
- 文中给出 Vera 的关键规格与口径：88 个自研 Olympus 核心、1.2TB/s 内存带宽，并宣称在持续高负载下单核性能提升约 50%，用于支撑智能体沙箱、工具调用、编译与数据处理等 CPU 侧瓶颈工作。
- 文章引用 Anthropic 计算负责人观点，强调扩展算力对模型迭代的重要性，并把 Vera 视为解决智能体工作负载的新硬件方向之一。

**业务影响**

业务层面，Vera 是 NVIDIA 把智能体 AI 的关键瓶颈（沙箱、工具调用、编排、长上下文检索、数据处理等 CPU 侧工作）纳入自家平台的关键一步：当客户购买的不再只是 GPU，而是包含 CPU、互联与系统的整套 AI 工厂，平台粘性与系统级 ASP/份额通常更强。
首批进入 Anthropic/OpenAI/SpaceXAI/OCI 的意义更多是“标杆客户与生态背书”，用来推动后续在云与企业 AI 工厂中的规模化部署与软件栈适配。

**估值/动作影响**

估值/动作层面，这条消息更偏中期平台化验证：它支持“从 GPU 供应商走向系统平台”的叙事，但短期财务贡献取决于 Vera 的量产节奏、在整机/机架方案中的装机率、以及客户是否把更多 CPU 侧预算迁移到 NVIDIA 体系。
当前不把单次交付新闻视为加仓触发，而是把 Vera 的实际出货与客户采用（尤其是云厂商与企业系统）作为后续验证点。

**后续观察点**

- 跟踪 Vera 进入哪些量产系统（例如是否成为机架级平台的标准配置）以及公开的出货节奏/客户名单扩展。
- 观察后续财报或产品沟通中，管理层是否给出 Vera 相关收入归类、ASP/毛利结构或更明确的量化目标。
- 持续跟踪客户侧真实工作负载反馈：智能体沙箱、编排与数据处理等 CPU 密集型环节是否成为推动采购的主因，还是更多停留在宣传口径。

来源：[NVIDIA](https://blogs.nvidia.com/blog/vera-cpu-delivery/) / [原文](https://blogs.nvidia.com/blog/vera-cpu-delivery/)

## 3. NVIDIA｜Dell 大会：企业 AI 工厂上新（Rubin/Vera 服务器与网络）

**原文讲了什么**

- NVIDIA 在 Dell_Technologies World 强调企业侧 AI 正从试点走向智能体 AI 与推理部署规模化，主打方案是「Dell_AI Factory_with NVIDIA」，把算力、网络与系统一体化交付给企业客户。
- 文章给出 Dell 的宏观口径：到 2030 年全球 AI 基础设施支出可能达到 3-4 万亿美元，并引用“token 消耗增长 3,400%”的预测，作为企业算力需求扩张的背景。
- 产品侧更新包括：基于 NVIDIA_Vera Rubin NVL72 的 Dell_PowerEdge XE9812（宣称在大规模智能体推理场景可实现“每 token 成本最多降低 10 倍”）；
以及基于 HGX_Rubin NVL8 的 XE9880L/XE9885L/XE9882L（文中提及单机架最多 144 GPUs、100% 直冷节点，并宣称相对 HGX B200 性能最多提升 10 倍）。
- 网络与系统侧更新包括：NVIDIA_Quantum-X800 InfiniBand 与 Spectrum-6 Ethernet 相关的 Dell_PowerSwitch 产品组合，以及集成式系统 Dell_PowerRack；
同时提到采用 Vera_CPU 的 PowerEdge M9822/R9822（文中给出 1.2TB/s 内存带宽与“智能体工作负载较 x86 约快 50%”的口径）。

**业务影响**

业务层面，Dell 是企业 IT 的关键分销与集成渠道。
若「AI_Factory」形态（机架/系统级交付 + 网络/存储/软件一体化）能在企业侧规模化，将有利于 NVIDIA 把需求从“单卡/单节点采购”升级为“系统级采购”，提高平台绑定与生态渗透。
文中多处强调智能体推理与企业内网部署，意味着推理侧与企业数据治理/安全需求可能成为下一阶段增量来源；
但需要警惕会议稿件把“性能口径”与“真实可获得供给/价格”混在一起，导致市场对短期兑现过度乐观。

**估值/动作影响**

估值/动作层面，这类会议型事件对短期业绩的直接增量有限，更多是对高估值叙事（企业 AI 进入规模部署、Rubin/Vera 平台化）的支撑材料。
对仓位动作不应由单篇会议稿触发，重点回到：后续几个季度的 Data_Center 收入结构、推理需求口径、以及企业侧系统订单/交付是否体现“从试点到规模化”的斜率变化。

**后续观察点**

- 跟踪 Dell_AI Factory 相关系统在后续季度的实际出货与客户案例（尤其是企业侧、非云厂商），判断是否从发布走向规模采购。
- 对文中“10 倍成本/性能”等口径，后续关注是否有更可比的基准、配置与价格披露，避免把营销口径当成可直接映射到财务模型的变量。
- 观察 Rubin/Vera 平台供给与交付节奏（以及企业客户可获得性），验证企业侧需求是否受供给约束。

来源：[NVIDIA](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/) / [原文](https://blogs.nvidia.com/blog/dell-technologies-agent-enterprise-ai/)

## 4. NVIDIA｜Google Cloud 合作把 Rubin、Blackwell、Nemotron 与物理 AI 推向云端生产平台

**原文讲了什么**

- NVIDIA 官方博客披露，NVIDIA 与 Google_Cloud 在 Google_Cloud Next 期间扩大合作，重点不是单一 GPU 上云，而是把 AI_Hypercomputer、Vera_Rubin A5X、Blackwell 机密计算、Gemini_Enterprise、Nemotron、NeMo、Omniverse、Isaac_Sim 和 Cosmos 等组件打包成面向 agentic_AI 与 physical_AI 的全栈云端平台。
- 基础设施层面，Google_Cloud 将推出由 NVIDIA_Vera Rubin NVL72 机架级系统驱动的 A5X bare-metal_instances。
原文称 A5X 在每 token 推理成本和每兆瓦 token 吞吐上，较前代可实现最高 10 倍改善，并可在单站点扩展到 8 万颗 Rubin_GPU、多站点扩展到 96 万颗 Rubin_GPU。
- 安全与主权 AI 层面，Gemini 模型将在 Google_Distributed Cloud 上以 NVIDIA_Blackwell 与 Blackwell_Ultra GPU 预览运行；
同时 Google_Cloud 还预览 Confidential G4 VMs_with NVIDIA_RTX PRO 6000 Blackwell_GPUs，使敏感 prompt、模型与数据在多租户云环境中获得机密计算保护。
- 模型与开发平台层面，NVIDIA_Nemotron 3 Super 会进入 Gemini_Enterprise Agent_Platform，NeMo_RL 支撑新的 managed_reinforcement learning_API，让企业和开发者更容易训练、定制和部署 agentic_AI 系统。
- 物理 AI 层面，NVIDIA_Omniverse libraries、Isaac_Sim、Cosmos_Reason 2 NIM_microservices 等进入 Google_Cloud Marketplace、Vertex_AI 和 GKE，用于工业数字孪生、机器人仿真、视觉 AI_agent、自动化数据标注和机器人规划推理。

**业务影响**

对业务层面，这条合作强化了 NVIDIA_Data Center 的系统级粘性。
Rubin / Blackwell 是算力底座，ConnectX / NVLink / Virgo_networking 是集群扩展路径，Nemotron / NeMo / Gemini_Enterprise 是 agentic_AI 的开发入口，Omniverse / Isaac / Cosmos 是物理 AI 和工业场景入口。
Google_Cloud 作为超大云平台，把这些能力产品化后，企业客户买到的不只是单颗 GPU，而是一套从训练、推理、机密计算、强化学习、数字孪生到机器人仿真的云端 AI 工厂。
这会提高 NVIDIA 在云厂商资本开支、企业 AI 生产部署和 physical_AI 生态中的嵌入深度。

**估值/动作影响**

估值上，这条事件支持 NVIDIA 高估值中的“平台溢价”部分，但不应该被当成短期追买触发。
正面是：Rubin A5X 给出 10 倍成本/能效指标、最大 96 万 GPU 多站点扩展、OpenAI 与 Thinking_Machines 等真实工作负载案例，说明 NVIDIA 的平台价值正在从训练延伸到推理、agentic_AI 和 physical_AI。
限制是：这些多数是平台发布、预览或合作扩展，短期收入兑现仍要回到 Google_Cloud 与其他云厂商 capex、Rubin 量产节奏、Blackwell / GB300 供给、推理需求和毛利率。
当前动作是维持 A 池核心并上调研究优先级，而不是因为合作新闻单独加仓。

**后续观察点**

- 下一次 NVIDIA 财报继续看 Data_Center 收入、毛利率、推理需求口径，以及 Rubin / Blackwell / GB300 供给节奏是否支撑平台化兑现。
- 跟踪 Google_Cloud A5X 的实际推出时间、客户采用、定价和可用区域，验证 80,000 / 960,000 GPU 扩展能力是否从发布口径走向真实部署。
- 跟踪 OpenAI、Thinking_Machines、CrowdStrike、Siemens/Cadence 等客户案例是否带来可重复的高价值工作负载，而不只是发布会引用。
- 观察 Nemotron、NeMo_RL、Omniverse、Isaac_Sim、Cosmos_NIM 在 Google_Cloud 上的开发者使用和企业采购情况，判断软件/物理 AI 生态是否能增强 NVIDIA 平台溢价。
- 警惕 Google、OpenAI 等大客户自研 ASIC 与多供应商策略对 NVIDIA 单位经济和议价能力的长期压制。

来源：[NVIDIA](https://blogs.nvidia.com/blog/google-cloud-agentic-physical-ai-factories/) / [原文](https://blogs.nvidia.com/blog/google-cloud-agentic-physical-ai-factories/)
