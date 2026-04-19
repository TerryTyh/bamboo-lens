# GitHub Actions 接入清单

这份清单的目标很简单：

- 让 `竹鉴 / Bamboo Lens` 的工作日日报在云端稳定运行
- 让日报通过企业微信群机器人推送到你的手机

## 1. 准备企业微信群机器人 Webhook

1. 打开你的企业微信群
2. 添加一个群机器人
3. 复制机器人 Webhook 地址

你最终会得到一条类似这样的地址：

```text
https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

## 2. 在 GitHub 仓库中配置 Secret

进入你的 GitHub 仓库：

`Settings -> Secrets and variables -> Actions -> New repository secret`

新增以下 Secret：

- `WECOM_WEBHOOK_URL`

值就是上一步复制的企业微信机器人 Webhook。

## 3. 检查工作流文件

当前工作流文件已经准备好：

- [daily-brief.yml](/Users/tianyuehua/Documents/项目/一个财务投资应用/.github/workflows/daily-brief.yml)

它会在工作日定时执行：

1. 抓官方网页快照
2. 提取官方候选事件
3. 合并现有研究事件库
4. 生成日报
5. 发到企业微信

## 4. 先做一次本地自检

在项目根目录运行：

```bash
cd "/Users/tianyuehua/Documents/项目/一个财务投资应用/云端研究简报系统"
python3 scripts/check_setup.py
```

如果你想连企业微信一起本地测试，可以临时带上环境变量：

```bash
cd "/Users/tianyuehua/Documents/项目/一个财务投资应用/云端研究简报系统"
WECOM_WEBHOOK_URL="你的 webhook" python3 scripts/check_setup.py
```

## 5. 手动触发一次 GitHub Actions

进入 GitHub Actions 页面，找到：

- `Daily Brief`

然后手动执行一次 `Run workflow`。

这样我们就能先验证三件事：

1. 云端能否正常抓取
2. 日报能否正常生成
3. 企业微信能否收到消息

## 6. 当前需要你提供的唯一关键值

当前只差：

- 企业微信群机器人 Webhook

没有这个值，我可以继续把代码和流程都铺好，但无法替你完成真正的发送验证。

## 7. 下一步最值得做什么

在第一条正式云端日报跑通后，下一步建议是：

1. 优先增强 `TSMC` 和 `NVIDIA` 的官方事件抽取质量
2. 再把云端事件结果回写到门户数据层

