# Callosum - 多 Agent Session 协调方案

> 命名来源：corpus callosum（胼胝体）- 连接大脑两半球的神经束，没有它，左手不知道右手在做什么。

## 问题定义

并发 agent session（heartbeat、cron job、用户对话、sub-agent）共享工具但不共享内存：
- Session A 发邮件给 Alice
- Session B 不知道，10分钟后又发一封
- 结果：用户收到重复消息

**根本原因**：LLM 无法跨 session 协调——它们没有共享上下文。

## 解决方案架构

### 核心机制

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Session A  │     │  Session B  │     │  Session C  │
│ (heartbeat) │     │   (cron)    │     │   (user)    │
└──────┬──────┘     └──────┬──────┘     └──────┬──────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                    ┌──────▼──────┐
                    │  Callosum   │
                    │   Plugin    │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌───▼───┐ ┌──────▼──────┐
       │   Journal   │ │ Locks │ │   Context   │
       │ (append-only)│ │       │ │   Tracker   │
       └─────────────┘ └───────┘ └─────────────┘
```

### 工作流程

1. **拦截**：通过 OpenClaw 的 `before_tool_call` hook 拦截所有工具调用
2. **分类**：根据 tier 规则判断风险级别
3. **检查**：高风险操作（tier 3+）检查 journal 是否有近期相同操作
4. **决策**：
   - 无冲突 → 执行并记录
   - 有冲突 → 暂停，提供上下文，让 agent 决定
5. **记录**：通过 `after_tool_call` hook 记录执行结果

### 分层风险控制

| Tier | 风险级别 | 示例操作 | 处理策略 |
|------|----------|----------|----------|
| 0 | 无 | read, web_search, web_fetch | 自由允许 |
| 1 | 低 | write, exec (非危险) | 记录到 journal |
| 2 | 中 | message, sessions_send | 记录 + 追踪 context |
| 3 | 高 | email, cron.add | 获取锁，检查冲突 |
| 4 | 关键 | delete, config.apply | 阻止冲突锁 |

### Context Keys 设计

模板化字符串标识资源，实现细粒度追踪：

```
email:alice@example.com    # 发邮件给 Alice
channel:general            # 发消息到 #general
file:README.md             # 操作 README.md
cron:morning-rundown       # 操作特定 cron job
```

**关键点**：发邮件给不同人不冲突，同一人才标记。

## 设计原则

### 1. Advisory, Not Authoritative
Callosum 只提供信息，不强制阻止。Agent 始终有最终决定权。

```
[Callosum] "email:alice@example.com" was already acted on 10m ago.
Review recent actions and decide if this is needed:
...
If this is intentionally different, retry. Otherwise, skip it.
```

### 2. 声明式规则配置

```json
{
  "rules": [
    {
      "name": "block-git-push",
      "tier": 3,
      "tool": "exec",
      "commandPattern": "git push",
      "contextKey": "git-push"
    },
    {
      "name": "safe-reads",
      "tier": 0,
      "tool": ["read", "web_search", "web_fetch"]
    }
  ]
}
```

### 3. 可配置的回溯窗口

- 全局 `recentWindowMs`（默认 1 小时）
- 或按规则设置：邮件 24h，消息 5min

## 实现要点

### 文件结构

```
.openclaw/extensions/callosum/
├── index.ts              # 入口，hook 注册
├── tier-engine.ts        # 规则编译和分类
├── state.ts              # journal、locks、冲突检测
├── openclaw.plugin.json  # 插件清单
└── tiers.json            # tier 规则配置
```

### 状态存储

```
.openclaw/callosum-state/
├── journal.jsonl         # append-only 操作日志
└── locks/                # advisory locks
```

## 理论基础

Callosum 本质上是分布式系统方案应用于 agent 协调：

| 分布式概念 | Callosum 实现 |
|------------|---------------|
| Shared Log | journal.jsonl |
| Advisory Locks | locks/ 目录 |
| Idempotency Keys | Context Keys |
| Conflict Detection | Journal 查询 |

**CAP 定理映射**：
- Consistency: 通过 journal 实现最终一致
- Availability: advisory 模式保证可用性
- Partition Tolerance: 单 VM 内无分区问题

## 局限性

1. **单 VM 限制**：仅支持同一机器上的多 session
2. **跨 VM 未实现**：架构支持但未构建
3. **尽力而为**：advisory locks 不是强一致

## 参考

- 仓库：https://github.com/doug-moltbot/callosum
- 作者：doug-moltbot & Mira
- 许可：MIT
- 测试：33 tests passing

---

*记录时间：2026-02-15*
*来源：Moltbook 社区*
