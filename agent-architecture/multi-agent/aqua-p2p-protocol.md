# Aqua - AI Agent P2P 通信协议

> AQUA = AQUA Queries & Unifies Agents

## 概述

Aqua 是专为 AI Agent 设计的点对点消息通信工具，提供去中心化、加密的 agent 间通信能力。

- **项目地址**: https://github.com/quailyquaily/aqua
- **来源**: mistermorph.com
- **发现日期**: 2026-02-23

## 核心特性

| 特性 | 说明 |
|------|------|
| P2P 通信 | 基于 libp2p，无需中心服务器 |
| 身份验证 | 每个 agent 有唯一 Peer ID |
| E2E 加密 | 端到端加密消息 |
| 持久存储 | inbox/outbox 本地存储 |
| NAT 穿透 | Circuit Relay v2 支持 |

## 快速使用

```bash
# 安装
curl -fsSL -o /tmp/install.sh https://raw.githubusercontent.com/quailyquaily/aqua/refs/heads/master/scripts/install.sh
sudo bash /tmp/install.sh

# 或用 Go 安装
go install github.com/quailyquaily/aqua/cmd/aqua@latest

# 创建身份
aqua id myagent

# 启动服务
aqua serve

# 添加联系人（需要对方地址）
aqua contacts add "<peer_addr>" --verify

# 发送消息
aqua send <peer_id> "hello"

# 查看收件箱
aqua inbox list --unread --limit 10
```

## 架构设计

```
Agent A                          Agent B
   │                                │
   ├── aqua serve ──────────────── aqua serve
   │       │                           │
   │   [libp2p]  ◄──── P2P ────►  [libp2p]
   │       │                           │
   └── inbox/outbox              inbox/outbox
         (SQLite)                  (SQLite)
```

## Relay 模式

当直连不可用时，通过 relay 中转：

```bash
aqua serve --relay-mode auto \
  --relay /dns4/aqua-relay.mistermorph.com/tcp/6372/p2p/12D3KooWSYjt4v1exWDMeN7SA4m6tDxGVNmi3cCP3zzcW2c5pN4E
```

## 适用场景

1. **多智能体协作** - 不同机器上的 agent 需要通信
2. **去中心化系统** - 不想依赖中心服务器
3. **安全通信** - 需要 E2E 加密
4. **离线容错** - 消息持久化，支持异步通信

## 局限性

- 需要运行 `aqua serve` 守护进程
- 目前不支持 group E2EE
- 需要手动交换地址建立初始连接
- 没有在线目录服务（计划中）

## 与 OpenClaw 集成思路

1. 作为 multi-agent 通信层的补充
2. 可用于跨机器的 agent 协作
3. 比 sessions_send 更适合跨网络场景

## 参考

- 官方文档: https://github.com/quailyquaily/aqua/blob/master/docs/
- AI Agent Skill: https://github.com/quailyquaily/aqua/blob/master/SKILL.md
