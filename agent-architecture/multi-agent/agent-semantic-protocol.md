# Agent Semantic Protocol (Symplex)

> 分布式智能体语义协商协议 - MCP 的语义扩展层

## 概述

Agent Semantic Protocol 是一个开源协议，让 AI 智能体通过**语义意图向量**而非固定 JSON schema 进行通信。核心创新是使用 float32 嵌入向量表达请求目标，实现动态发现、自发协商和分布式工作流。

- **GitHub**: https://github.com/olserra/agent-semantic-protocol
- **状态**: v0.1 稳定，活跃开发中
- **许可**: MIT

## 核心概念

### Intent Vector（意图向量）
- float32 嵌入向量（如 384 维 sentence-transformer）
- 编码请求的语义目标
- 任何理解该向量空间的智能体都可以响应

### Spontaneous Negotiation（自发协商）
- 智能体广播能力并竞标意图
- 使用余弦相似度排名
- 无需中央代理或预注册 API

### Dynamic Discovery（动态发现）
- 基于 TTL 的能力注册表
- 智能体可运行时动态加入/离开

### Federated Trust（联邦信任）
- 每个智能体有 DID 标识：`did:agent-semantic-protocol:<sha256(pubkey)>`
- 基于 Ed25519 密钥对
- 支持信任图

### Distributed Workflows（分布式工作流）
- 接受的意图展开为有序工作流步骤
- 通过 libp2p 分发给有能力的节点

## 与 MCP/A2A 对比

| 特性 | MCP | Google A2A | Agent Semantic Protocol |
|------|-----|------------|-------------------------|
| 消息格式 | JSON-RPC | JSON | Protobuf + vectors |
| 能力模型 | 静态注册 | 静态技能卡 | 动态 TTL 发现 |
| 协商 | 无 | 无 | 余弦相似度排名 |
| 身份 | 无 | 无 | Ed25519 DIDs |
| 传输 | HTTP/SSE | HTTP | libp2p P2P |
| 语义路由 | 否 | 否 | 是 |

## 技术栈

- **语言**: Go 1.22+
- **网络**: libp2p (TCP/QUIC/WebRTC)
- **序列化**: Protobuf (protowire)
- **身份**: Ed25519 + DID
- **向量**: sentence-transformer 384-dim

## 快速开始

```bash
git clone https://github.com/olserra/agent-semantic-protocol
cd agent-semantic-protocol
go mod download
go run ./examples/simple-handshake/main.go
```

## 代码示例

```go
// 创建智能体
agent, _ := core.NewAgent("my-agent", []string{"nlp", "summarisation"})

// 启动 P2P 主机
host, _ := p2p.NewHost(ctx, agent)

// 注册意图处理器
host.OnIntent(func(peerID peer.ID, intent *core.IntentMessage) *core.NegotiationResponse {
    h := core.DefaultNegotiationHandler(agent)
    resp, _ := h(intent)
    return resp
})

// 发送意图
intent, _ := core.CreateIntent(agent,
    []float32{0.8, 0.2, 0.9},
    []string{"summarisation"},
    "Summarise this document",
)
resp, _ := host.SendIntent(ctx, targetPeerID, intent)
```

## 适用场景

- 多智能体协作系统
- 去中心化 AI 服务网格
- 跨组织智能体互操作
- 动态能力发现和协商

## 局限性

- 目前仅 Go SDK
- 签名验证尚未在接收端实现
- 需要统一的向量空间/嵌入模型

## 路线图

- v0.2: QUIC/WebRTC 传输，签名验证
- v0.3: 联邦 DID 解析，zk-SNARK 能力证明
- v1.0: 稳定格式，MCP 网关适配器，多语言 SDK

## 关联知识

- [[MCP]] - Anthropic Model Context Protocol
- [[多智能体系统]] - Multi-Agent Systems
- [[libp2p]] - P2P 网络库

---
*学习日期: 2026-02-23*
*来源: Hacker News / GitHub*
