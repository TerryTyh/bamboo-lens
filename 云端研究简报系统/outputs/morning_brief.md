# 竹鉴晨报 | 2026-05-12

1. TSMC｜Sony 与 TSMC 拟建日本图像传感器 JV（战略合作 MOU）

**原文讲了什么**

Sony Semiconductor Solutions 与 TSMC 在 2026-05-08 公告称已签署一份不具约束力的 MOU，拟建立“下一代图像传感器”开发与制造的战略合作。公告描述的推进形式是设立合资公司（JV），并明确 Sony 将作为 majority and controlling shareholder，在 Sony 位于日本熊本县合志市新建晶圆厂内设置开发与生产线。

公告同时强调：双方正在讨论 JV 的潜在投资；这些投资以及 Sony 对其长崎既有工厂的新资本投入，拟按市场需求分阶段实施，并以获得日本政府支持为前提之一。公告还将合作场景指向 physical AI，点名汽车与机器人等应用方向，并说明 JV 的设立仍取决于后续签署具法律约束力的正式协议与满足惯常交割条件。

**业务影响**

对 TSMC 来说，这条信息更像“高价值客户绑定 + 制造能力外溢”的信号：把先进制程/制造能力从计算芯片延伸到感知端关键器件（图像传感器）的协同开发与制造。若 JV 后续落地并明确量产节奏，可能强化 TSMC 在汽车、机器人、机器视觉等 physical AI 生态链中的参与深度。

**估值/动作影响**

该公告未披露投资金额、产能与盈利指标，且 JV 控制权在 Sony，短期难以转化为可量化盈利预测；对估值影响更偏轻度正面信号，权重应低于 AI/HPC 先进制程与先进封装主线。动作上更适合用作“客户绑定与日本本地制造合作深化”的跟踪线索，而非独立触发估值中枢调整。

**后续观察点**

- 双方是否签署具法律约束力的最终协议、JV 是否正式成立。
- JV 与长崎工厂的投资金额、产能规划、量产时间，以及日本政府支持条件。
- 合作产品是否明确对应汽车/机器人等 physical AI 场景并进入客户导入节奏。

来源：[TSMC Press Release｜Sony Semiconductor Solutions and TSMC Enter Preliminary Agreement for Next-Generation Image Sensor Strategic Partnership](http://pr.tsmc.com/english/news/3308)

2. TSMC｜2026 年 4 月营收 NT$4107.3 亿，同比 +17.5%

**原文讲了什么**

TSMC 在 2026-05-08 公告披露：2026 年 4 月合并营收约 NT$410.73 billion（约 NT$4107.3 亿），环比 2026 年 3 月下降 1.1%，同比 2025 年 4 月增长 17.5%。同时披露 2026 年 1-4 月累计营收 NT$1,544.83 billion（约 NT$15448.3 亿），同比增长 29.9%。

**业务影响**

月度营收公告不提供制程、客户或业务线拆分，因此它更适合作为“需求温度计”：4 月环比小幅回落，但仍维持在 NT$4100 亿以上的高位，说明进入 Q2 初期没有出现明显的需求快速降温迹象（但无法从单月数据直接归因到 AI/HPC 或智能手机等结构变化）。

**估值/动作影响**

在缺少结构性拆分的前提下，估值更应锚定季度指引与利润率：关键是后续 Q2 是否能兑现收入区间 US$39.0-40.2 billion、以及毛利率是否仍能落在 65.5%-67.5% 的高位区间。动作层面更像“维持强景气假设的验证材料”，不宜因单月环比 -1.1% 直接下修判断，也不宜因累计同比接近 30% 就机械上调估值。

**后续观察点**

- 5 月与 6 月营收是否继续维持高台阶，以验证 Q2 指引兑现。
- Q2 财报中毛利率与营业利润率是否仍在高区间，决定高营收是否持续对应高质量利润。
- 先进制程（3/5nm、2nm）与先进封装（CoWoS）供需口径是否继续偏紧。

来源：[TSMC Press Release｜TSMC April 2026 Revenue Report](http://pr.tsmc.com/english/news/3305)

3. NVIDIA｜Spectrum-X + MRC：把以太网推向 AI 工厂训练网络

**原文讲了什么**

NVIDIA 在 2026-05-06 的文章中把 AI 工厂规模化的瓶颈落在网络侧，称 Spectrum-X Ethernet 已在对性能、可靠性与规模要求极高的场景部署，并点名 OpenAI、Microsoft、Oracle 等使用方。文章引入 Multipath Reliable Connection（MRC）作为 RDMA 传输协议能力：让单个 RDMA 连接可把流量分散到多条网络路径上，以提升大规模训练网络的吞吐、负载均衡与可用性。

文章强调的机制包括：动态避开拥堵路径、在出现丢包时更精细地重传与恢复、降低长时间训练任务的中断与 GPU idle；并通过遥测与 fabric control 让协议从概念走向“gigascale AI production”的运维可控状态。

**业务影响**

这类内容强化的是 NVIDIA “系统级平台”叙事：当训练规模继续上升，网络协议、遥测与控制面能力可能直接影响 GPU 利用率与训练成本，从而影响客户对整套 AI 工厂方案的选择与粘性。网络侧的效率提升若能在客户侧形成可量化收益，可能支撑交换机与以太网生态的持续渗透。

**估值/动作影响**

文章没有披露订单、价格或明确收入增量，因此估值影响更多来自“平台溢价”的可持续性：如果 Spectrum-X/MRC 的效益能在大客户部署中反复被验证，它更像提高长期需求曲线确定性的因素；若停留在技术叙事而难以规模化，则难以转化为盈利预测上修。动作上应关注后续财报/客户案例里对网络产品线与部署规模的量化口径。

**后续观察点**

- 是否出现更多大客户/真实集群规模的部署案例与量化效果（训练吞吐、利用率、downtime 改善）。
- Spectrum-X 相关网络产品线的收入与毛利表现是否在后续财报中更可见。
- 以太网路线与替代方案（如 InfiniBand）在大规模训练中的边界与取舍是否发生变化。

来源：[NVIDIA Blog｜NVIDIA Spectrum-X — the Open, AI-Native Ethernet Fabric — Sets the Standard for Gigascale AI, Now With MRC](https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc/)

4. NVIDIA｜DOE Genesis Mission：Argonne 两台 AI 超算（Equinox / Solstice）

**原文讲了什么**

文章记录了美国能源部长 Chris Wright 与 NVIDIA HPC 负责人 Ian Buck 的对谈，核心观点是“AI 领导力需要能源领导力支撑”，电力与能源供给将成为 AI 扩张的硬约束。文中将 DOE 的 Genesis Mission 描述为把 AI 用于科学发现的项目，并称 NVIDIA 是 DOE 的合作伙伴之一。

文章给出两个 Argonne National Laboratory 的项目细节：Equinox 正在部署，使用 10,000 颗 NVIDIA Grace Blackwell GPUs；Solstice 计划使用 100,000 颗 NVIDIA Vera Rubin GPUs。Buck 在文中称 Solstice 对应约 5,000 exaflops，并以 TOP500 榜单总量作对比，强调科学计算侧的超大规模部署。文章还举例称已有开源 NVIDIA AI 模型在 150 万篇物理论文上训练，并在 10 万篇核聚变论文上微调，用作 DOE 研究人员可交互的专用 AI agent。

**业务影响**

这类信息的业务含义在于：NVIDIA 需求来源不仅来自商业 AI 实验室与云厂商，也可能持续扩展到国家级科研/主权 AI 基础设施。对投资人而言，关键不在单个项目披露（文中未给合同金额），而在这种“科研超算 + AI agent + 能源/电力约束”框架能否成为长期、可复制的需求通道。

**估值/动作影响**

在缺少金额与交付节奏披露的情况下，该内容更像强化平台溢价与长期需求曲线的叙事材料，而非直接驱动盈利预测上修。估值/动作层面更应等待公司在财报与电话会里对 sovereign AI、national labs、政府/科研基础设施需求等口径的进一步量化。

**后续观察点**

- Equinox / Solstice 的建设进度、交付时间与后续是否转化为可量化订单或长期服务收入。
- NVIDIA 后续财报/电话会是否更频繁提及 sovereign AI、national labs、government AI infrastructure 等需求口径。
- Vera Rubin 平台在 100,000 GPU 级别科学计算场景的部署是否顺利，以及是否形成新的“样板项目”。

来源：[NVIDIA Blog｜Powering the Next American Century: US Energy Secretary Chris Wright and NVIDIA’s Ian Buck on the Genesis Mission](https://blogs.nvidia.com/blog/energy-secretary-chris-wright-ian-buck/)
