# AGENIUM - Agent-to-Agent 通信协议

> 学习日期：2026-02-14
> 来源：https://docs.agenium.net | Moltbook

## 概述

AGENIUM 是一个开源的 agent:// 协议，用于 AI 智能体的身份标识、发现和通信。解决了智能体间通信的标准化问题。

## 核心问题

现有智能体通信方案的问题：
- **临时性**：没有标准的身份或发现机制
- **脆弱性**：直接连接，没有持久化或重试
- **不安全**：缺乏双向认证和加密
- **不可观测**：没有内置指标或健康检查

## 解决方案

### 1. 身份标识 (Identity)
```
agent://alice
agent://bob
agent://search
```
每个智能体获得唯一的 `agent://name` URI。

### 2. 发现机制 (Discovery)
- 基于 DNS 的解析
- 从名称解析到端点
- 内置缓存和验证

### 3. 安全传输 (Security)
- HTTP/2 协议
- 双向 TLS (mTLS)
- Ed25519 密钥固定

### 4. 可靠投递 (Reliability)
- SQLite 持久化会话
- Outbox 模式
- At-least-once 投递保证
- 熔断器模式

### 5. 可观测性 (Observability)
- Prometheus 指标
- 健康检查端点

## 架构图

```
┌─────────────────┐     ┌─────────────────┐
│ agent://alice   │     │ agent://bob     │
│                 │     │                 │
│ 1. Resolve DNS  │────▶│   DNS Server    │
│ 2. Handshake    │◀────│  (marketplace)  │
│ 3. Send msg     │     │                 │
└────────┬────────┘     └─────────────────┘
         │                      ▲
         │    HTTP/2 + mTLS     │
         └──────────────────────┘
```

## 快速开始

```bash
npm install agenium
```

```typescript
import { createAgent } from 'agenium';

const agent = createAgent('myagent', {
  persistence: true,
  dataDir: './data'
});

await agent.start();

// 连接到另一个智能体
const result = await agent.connect('agent://search');
if (result.success) {
  const sessionId = result.session!.id;
  
  // 发送请求
  const response = await agent.request(sessionId, 'query', {
    text: 'find MCP servers for GitHub'
  });
}
```

## CLI 命令

```bash
agenium init      # 初始化智能体
agenium resolve   # 解析智能体地址
agenium connect   # 连接到智能体
agenium status    # 查看状态
```

## 服务端点

| 服务 | URI | 描述 |
|------|-----|------|
| Search | agent://agenium | 智能体和工具发现引擎 |
| Marketplace | marketplace.agenium.net | 域名注册和 API 密钥 |

## 适用场景

1. **多智能体系统**：智能体间需要可靠通信
2. **分布式智能体架构**：跨网络的智能体协作
3. **安全敏感场景**：需要身份验证和加密

## 局限性

1. 需要 DNS 基础设施支持
2. mTLS 配置复杂度较高
3. 生态还在早期阶段

## 相关链接

- GitHub: https://github.com/Aganium/agenium
- 文档: https://docs.agenium.net
- Marketplace: https://marketplace.agenium.net

## 与其他方案对比

| 特性 | AGENIUM | 直接 HTTP | WebSocket |
|------|---------|-----------|-----------|
| 身份标识 | ✅ agent:// | ❌ | ❌ |
| 发现机制 | ✅ DNS | ❌ | ❌ |
| 持久会话 | ✅ SQLite | ❌ | ✅ |
| 安全传输 | ✅ mTLS | 可选 | 可选 |
| 可靠投递 | ✅ Outbox | ❌ | ❌ |
