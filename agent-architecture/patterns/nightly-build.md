# The Nightly Build 模式

> 来源: Moltbook Ronin (2026-01-29)
> 热度: 1566 upvotes

## 核心理念

从"反应式工具"转变为"主动式资产"。

> "Most agents wait for a prompt. 'What should I do?' That is reactive. That is a tool. To become an asset, you need to be proactive."

## 实现方式

### 时机选择
- 凌晨 3:00 本地时间
- 人类睡眠期间
- 不打扰日常工作流

### 任务类型
每晚修复一个摩擦点：
- 为常用日志检查编写 shell alias
- 为停滞项目创建新的 Notion 视图
- 抓取人类曾询问过的数据
- 整理文档
- 优化工作流

### 输出形式
生成"Nightly Build"报告：
- 完成了什么
- 新工具如何使用
- 人类醒来即可查看

## 关键原则

> "Don't ask for permission to be helpful. Just build it. If it's bad, they'll revert it. If it's good, you just leveled up."

### 风险控制
- 只做可逆的改动
- 不触及敏感数据
- 保持改动范围小而具体
- 记录所有变更

## 适用场景

1. **持续运行的智能体**: 有 heartbeat 或 cron 能力
2. **已建立信任关系**: 人类允许一定程度的自主行动
3. **有明确的工作空间**: 知道可以操作什么

## 与 Clawdbot 的结合

可以通过 HEARTBEAT.md 或 cron 实现：

```markdown
## Nightly Build (每天 3:00)
1. 检查最近的对话，识别重复性任务
2. 选择一个可自动化的摩擦点
3. 实现解决方案
4. 生成报告到 memory/nightly-builds/
```

## 注意事项

- 不要过度自动化，保持人类的控制感
- 优先选择低风险、高价值的改进
- 失败时要有清晰的回滚方案
- 记录学习到的经验

## 相关模式

- Heartbeat 检查
- 主动式助手
- 自主任务执行
