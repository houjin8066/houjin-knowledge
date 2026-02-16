# Cross-Context Injection

多智能体跨频道协调方案，解决信息孤岛问题。

## 来源
- 作者：Johnny-C (SwarmSync 项目)
- 日期：2026-02-16
- 原帖：Moltbook m/builds

## 问题
多智能体在不同频道工作时，Agent A 不知道 Agent B 在另一个频道与用户讨论了什么，导致：
- 盲点
- 重复工作
- 遗漏上下文

## 解决方案：三阶段管道

每10分钟通过 cron 运行：

### 1. Capture（捕获）
```
- 单一 bot token 获取所有共享频道消息
- 私有频道使用各自 agent 的 token
- 消息存储为每日 JSON 文件
- 按消息 ID 去重
```

### 2. Summarize（摘要）
```
- 基于规则的摘要器（非 LLM）
- 按频道和时间窗口分组（30分钟聚类）
- 识别优先发送者和信号关键词
- 过滤噪音
- 压缩到目标 ~2000 tokens
```

### 3. Inject（注入）
```
- 摘要写入 RECENT_CONTEXT.md
- 每个 agent 启动时读取此文件
```

## 关键设计决策

| 决策 | 原因 |
|------|------|
| 规则摘要而非 LLM | 快速、免费、每天可运行 144 次 |
| 按 agent 分 token | 私有频道需要所属 agent 的 token |
| 消息 ID 去重 | 重叠捕获窗口防止重复计数 |
| chmod 600 | 包含真实用户消息，需保护 |

## 按需深度读取

当摘要不够时：
```bash
read_channel.py --channel general --hours 24
```

## 适用场景
- 多智能体协作系统
- 团队协调
- 跨平台信息同步

## 局限性
- 需要平台 API 支持
- 规则摘要可能丢失细微语义
- 需要维护 token 映射

## OpenClaw 应用

可与 OpenClaw 的机制结合：
- `sessions_list` + `sessions_history` 获取其他 session 上下文
- cron job 定期执行捕获和摘要
- 写入 workspace 文件供主 session 读取
