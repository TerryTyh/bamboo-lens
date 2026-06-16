# 正式事件草稿｜NVIDIA｜Fastest, Largest, Strongest: NVIDIA Blackwell Sweeps MLPerf Training 6.0

## 草稿状态

- 公司：NVIDIA（nvidia）
- 日期：2026-06-16
- 类型：财报 / 指引
- 候选分数：10
- 当前动作：进入人工研判
- 批处理建议：优先深读（readiness 32）
- 官方来源：[打开官方来源](https://blogs.nvidia.com/blog/blackwell-mlperf-training-6-0/)
- 来源快照：/home/runner/work/bamboo-lens/bamboo-lens/云端研究简报系统/outputs/snapshots/nvidia__20260616-162319__investor.nvidia.com_news_press-releases_default.aspx.html

## 批处理建议

已有较长可读正文，候选分数也足够高，适合作为下一批正式事件研判对象。

### 当前阻碍

- 暂无系统识别的硬性阻碍，但仍必须补齐正式事件字段。

## 原文与事实

先看来源到底说了什么，再决定是否形成正式事件。下面是系统已抓到的可读内容或候选事实。

### 原文可读内容

Every breakthrough AI model starts the same way: with a training run. The infrastructure running those training jobs shapes everything: how fast teams can iterate, what scale of model they can build and whether those jobs complete reliably. As models grow in size, complexity and intelligence, the demands on training infrastructure are also rising. In MLPerf Training 6.0 — the latest of a series of rigorous, peer-reviewed industry benchmarks for evaluating AI training performance — the NVIDIA Blackwell platform led across every category, demonstrating: NVIDIA brings together performance, scale and reliability in a single platform engineered through extreme codesign to enable AI model builders to launch frontier models faster, minimize training costs and start generating revenue early. MLPerf Training 6.0 added two new mixture-of-experts (MoE) pretraining workloads to the suite: DeepSeek-V3 671B and GPT-OSS-20B, reflecting the growing centrality of MoE architectures. The NVIDIA platform was the only one to be submitted across every benchmark, and delivered the fastest time to train on all seven. This round, NVIDIA submitted results on both NVIDIA GB200 NVL72 and GB300 NVL72 rack-scale systems. Within each rack-scale system, fifth-generation NVIDIA NVLink Switches connect all 72 GPUs with high bandwidth, into a unified pool of compute and memory, enabling them to act as one giant GPU. Large-scale MoE training faces the same all-to-all communication challenge as MoE inference — tokens must be routed across GPUs to reach the right expert subnetwork — and NVLink’s bandwidth advantage is what makes that fast and efficient at scale. NVIDIA also showcased NVFP4 training methods that increase performance while meeting strict accuracy requirements across large- and small-scale pretraining as well as fine-tuning workloads. NVIDIA continues to push low-precision training innovation across different model architectures, most recently using NVFP4 to pretrain the massive 550-billion-parameter NVIDIA Nemotron 3 Ultra model. NVIDIA GB300 NVL72 Delivered up to 1.6x Performance Over GB200 NVL72: In this round, GB300 NVL72 delivered up to 1.6x faster training than GB200 NVL72 at the same scale. Key Blackwell Ultra capabilities such as higher compute density with NVFP4, expanded memory capacity and a higher power ceiling that lets the GPU sustain peak performance drive this improvement. To support distributed training at scale, NVIDIA offers two complementary scale-out networking platforms — NVIDIA Quantum InfiniBand and NVIDIA Spectrum-X Ethernet — giving data centers the fl

（原文较长，草稿只保留前段可读内容；正式研判前必须打开来源阅读全文。）

### 候选事实

日期：2026-06-16；标题：Fastest, Largest, Strongest: NVIDIA Blackwell Sweeps MLPerf Training 6.0；原文内容：Every breakthrough AI model starts the same way: with a training run. The infrastructure running those training jobs shapes everything: how fast teams can iterate, what scale of model they can build and whether those jobs complete reliably. As models grow in size, complexity and intelligence, the demands on training infrastructure are also rising. In MLPerf Training 6.0 — the latest of a series of rigorous, peer-rev…；来源：https://blogs.nvidia.com/blog/blackwell-mlperf-training-6-0/

## 升级为正式事件前必须补齐

- 收入、分部收入、利润率、EPS、现金流或指引中的具体数字
- 管理层对需求、产能、价格、成本或资本开支的口径
- 和上一期或市场预期相比，真正变化的指标

## 初步判断

这只是正式事件草稿，还不能直接形成投资判断。先读完来源，把事实、数字和管理层口径补齐，再决定是否升级。

## 业务影响待补

待补：说明它影响哪条业务线、产品、客户、市场、供应链或成本结构。

## 估值与动作影响待补

待补：说明它是否影响收入质量、利润率、现金流、资本开支、估值区间或仓位动作。

## 下一步验证

- 打开原始来源，确认正文是否足够支撑正式事件。
- 补齐至少三条具体证据，再写业务影响和估值/动作影响。
- 如果只有标题、日程或营销口号，保留候选，不进入正式事件。

## 公司主页回写建议

建议回写位置：

- 最新动态
- 财务地图
- 当前结论
- 估值模型

回写原则：若原文包含收入、利润率、现金流、指引或管理层口径，正式事件入库后必须同步更新公司主页的财务地图和估值/动作判断。

## 入库方式

当这份草稿已经补齐原文总结、三条以上证据、业务影响、估值/动作影响和验证点后，可以在 GitHub Actions 里运行 `Promote Review Draft`，输入以下草稿 ID：

`auto-nvidia-fastest-largest-strongest-nvidia-blackwell-sweeps-mlperf-training-6-0`

## 质量闸门

- 有来源：是
- 有可读正文：是
- 当前是否可直接入库：否
- 原因：草稿只负责降低整理摩擦，正式事件仍必须补齐原文总结、证据、业务影响、估值/动作影响和验证点。
