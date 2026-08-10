# 竹鉴晨报 | 2026-08-11

## 1. NVIDIA｜NVIDIA把GPUDirect Storage推向开源与行业标准，AI工厂数据路径从存储侧开始重新定价

**原文讲了什么**

NVIDIA在2026年8月4日围绕Future of Memory and Storage会议发布文章，核心不是简单宣传更多存储容量，而是说明AI工厂的数据瓶颈正在从GPU算力扩展到内存、存储、加密、压缩、校验和数据重构。文章称智能体会消耗大量数据，GPU现在可以直接发起存储请求，带来数千个并发操作，传统由CPU承担的数据服务会成为新瓶颈。

原文披露两条具体技术推进：第一，NVIDIA宣布开源cuFile API以及其下方的垂直存储软件栈，让GPU而不只是CPU可以直接从存储读写数据；cuFile作为GPUDirect Storage组件，可以利用大量GPU线程和高带宽内存，在微秒级安全访问存储数据。第二，NVIDIA推动Storage-Next倡议，联合超过40家存储和闪存厂商，包括DDN、KIOXIA和Micron，围绕GPU驱动存储形成可互操作的开放行业标准。

文章还把Vera CPU和BlueField-4 STX放进存储数据路径：NVIDIA引用技术benchmark称，Vera CPU在两阶段压缩和加密流水线中的吞吐最高达到x86 CPU的3.21倍。NVIDIA同时提出SCADA框架，让大规模并行GPU只把应用需要的数据从存储直接拉入自身高速内存，并举例称DDN正在把SCADA集成到Infinia平台。

**业务影响**

业务影响主要在AI工厂系统栈和数据中心平台化。大模型训练、长上下文推理、RAG、企业智能体和科学计算都在扩大数据读取与上下文窗口，存储不再只是低成本容量，而会影响GPU利用率、推理延迟、数据安全和单位算力产出。NVIDIA如果把GPUDirect Storage、BlueField/Vera数据服务、Spectrum-X网络和CUDA软件生态串起来，就能把服务器之外的存储、控制器和数据服务厂商也纳入其平台标准。对业务理解的增量是：NVIDIA的AI基础设施护城河不只来自GPU性能，还来自让GPU、网络、DPU/CPU和存储软件共同决定AI工厂吞吐的系统级协同。

**估值/动作影响**

估值/动作上，这条事件支持NVIDIA的平台溢价和长期配套附加率想象，但权重低于Blackwell/Rubin出货、云厂资本开支、网络收入、软件收入和明确客户部署。当前不因这篇文章提高估值区间或仓位动作；更合理的处理是维持核心跟踪，把GPU直连存储和Storage-Next作为AI工厂架构标准化观察点。若后续主流存储厂商把SCADA/cuFile做成正式产品、云厂在AI集群中默认部署GPUDirect Storage/Vera/BlueField数据路径，或NVIDIA在财报中披露相关网络/DPU/软件收入贡献，才可能提高它在估值分部中的权重。

**后续观察点**

- 跟踪Storage-Next是否发布具体标准、参考架构、认证清单或主流存储产品支持，而不是停留在会议文章和厂商名单。
- 观察DDN、KIOXIA、Micron及更多存储/闪存厂商是否把SCADA、cuFile或GPUDirect Storage支持写入正式产品规格和客户案例。
- 在NVIDIA后续财报中验证网络、DPU、CPU、软件和系统级解决方案收入是否加速，避免把架构趋势误读成已兑现收入。
- 检查云厂和AI云客户的集群配置，确认GPU直连存储是否成为Blackwell/Rubin AI工厂的默认数据路径。
- 继续对比Vera/BlueField数据服务与x86 CPU方案在加密、压缩、校验和存储访问上的实际部署成本与吞吐优势。

[原文](https://blogs.nvidia.com/blog/ai-storage-fms/)
