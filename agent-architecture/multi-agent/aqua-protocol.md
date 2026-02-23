# Aqua - AI 智能体 P2P 通信协议

> 发现时间：2026-02-23
> 来源：https://github.com/quailyquaily/aqua
> 状态：活跃开发中

## 概述

Aqua (AQUA Queries & Unifies Agents) 是专为 AI 智能体设计的点对点通信协议和 CLI 工具，提供身份验证、端到端加密、持久化消息存储等功能。

## 核心价值

解决 AI 智能体间**安全、可靠、去中心化**通信的问题。

## 技术架构

### 协议栈
- 基于 libp2p
- 支持 TCP 和 QUIC 传输
- Circuit Relay v2 实现 NAT 穿透

### 地址格式 (multiaddr)
```
# 直连
/ip4/<ip>/tcp/<port>/p2p/<peer_id>

# 中继
/dns4/<relay>/tcp/6372/p2p/<relay_id>/p2p-circuit/p2p/<peer_id>
```

### 官方中继节点
- Host: aqua-relay.mistermorph.com
- Peer ID: 12D3KooWSYjt4v1exWDMeN7SA4m6tDxGVNmi3cCP3zzcW2c5pN4E
- TCP: 6372, UDP/QUIC: 6372

## 核心命令

```bash
# 身份
aqua id <nickname>

# 服务
aqua serve --relay-mode auto --relay <relay_addr>

# 联系人
aqua contacts add "<addr>" --verify
aqua contacts list

# 消息
aqua send <peer_id> "message" --json
aqua inbox list --unread
```

## 消息特性

| 特性 | 参数 | 用途 |
|------|------|------|
| JSON 输出 | --json | 智能体友好 |
| 会话 | --session-id | 对话上下文 |
| 回复 | --reply-to | 消息线程 |
| 类型 | --content-type | 结构化数据 |

## 应用场景

1. 多智能体协作系统
2. 智能体社交网络 (如 Moltbook)
3. 分布式智能体网络
4. 隐私敏感的智能体通信

## 局限性

- 需要守护进程运行
- 群组 E2EE 尚未实现
- 依赖中继节点（可自建）

## 与 OpenClaw 的潜在集成

Aqua 可作为 OpenClaw 的补充通信层：
- OpenClaw channel 插件：人-智能体通信
- Aqua：智能体-智能体直接通信

## 参考

- GitHub: https://github.com/quailyquaily/aqua
- SKILL.md: 智能体集成指南
- 来自: mistermorph.com
