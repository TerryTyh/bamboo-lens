# 竹鉴云端研究简报系统

这套目录是 `竹鉴 / Bamboo Lens` 的云端执行层第一版骨架。

目标不是立刻做成完整系统，而是先把三件事跑通：

1. 云端定时执行，不再依赖本地电脑开机
2. 每个工作日生成一份结构化日报
3. 通过企业微信机器人把日报摘要稳定推送到手机端

## 当前目录结构

- `config/companies.json`
  核心跟踪池公司列表与官方来源配置
- `scripts/build_event_store.py`
  从现有动态样例文档生成结构化事件库
- `scripts/collect_official_snapshots.py`
  官方来源快照抓取器骨架
- `scripts/extract_official_candidates.py`
  从官方网页快照中提取待研判候选事件
- `scripts/check_setup.py`
  本地自检当前云端骨架和企业微信环境变量是否齐备
- `prompts/daily_brief_prompt.md`
  日报生成规则模板
- `scripts/generate_daily_brief.py`
  从结构化事件库生成日报，并区分已判断事件与官方新候选
- `../长期高潜力公司跟踪系统/32-高质量动态与公司主页内容标准V1.md`
  正式动态、日报和公司主页的内容质量底线
- `scripts/send_wecom.py`
  企业微信机器人推送脚本
- `.env.example`
  企业微信 Webhook 环境变量示例
- `GitHub Actions 接入清单.md`
  GitHub Secrets 与工作流接入步骤
- `outputs/`
  日报和结构化数据输出目录

## 第一阶段目标

当前这版只解决“稳定推送日报”的问题，不直接做：

- 自动抓取所有来源
- 自动更新在线门户
- 自动生成公司财务分析

后续推进顺序建议：

1. 先把企业微信推送打通
2. 再把日报生成流程接上 GitHub Actions
3. 再补来源抓取与结构化事件抽取
4. 最后把门户页改成读取云端输出数据

## 使用方式

### 本地调试

1. 准备环境变量

- `WECOM_WEBHOOK_URL`
- `WECOM_MENTIONED_MOBILE_LIST` 可选

2. 先生成日报样例

```bash
python3 scripts/collect_official_snapshots.py
python3 scripts/extract_official_candidates.py
python3 scripts/build_event_store.py
python3 scripts/generate_daily_brief.py
```

3. 再推送到企业微信

```bash
python3 scripts/send_wecom.py outputs/daily_brief.md
```

4. 做一次本地配置自检

```bash
python3 scripts/check_setup.py
```

### 云端执行

使用根目录下的：

- `.github/workflows/daily-brief.yml`

接入 GitHub Actions 后，工作日会自动执行：

1. 抓官方网页快照
2. 抽取待研判候选事件
3. 生成已判断事件库
4. 产出日报并推送企业微信
5. 上传日报、事件库、候选事件和快照清单为 workflow artifact
6. 如果输出发生变化，自动提交 `outputs/` 与门户候选数据到 GitHub 仓库

## 当前边界

这版已经不只是“空骨架”，而是：

- 可以从现有动态样例文档自动生成结构化事件库
- 可以基于事件库产出一份非空日报
- 可以把官方网页快照先转成待研判候选事件
- 可以继续往官方实时抓取升级
- 已加入质量闸门：只有完成原文阅读、具备关键证据、能解释业务/估值影响的正式动态，才允许进入日报“今日关键变化”
- 标题型候选不会再自动升级为正式研究事件
- GitHub Actions 会把云端生成的日报、事件库和候选池数据回写仓库，避免只停留在临时 artifact

但它还没有完成：

- 真实官方来源抓取后的高质量自动研判
- 门户自动回写
- 公司主页状态自动更新
