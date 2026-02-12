# Omnara - 远程 AI Coding Agent 架构

> 来源：https://news.ycombinator.com/item?id=46991591
> 公司：Omnara (YC S25)
> 产品：https://www.omnara.com/
> 日期：2026-02-12

## 解决的问题

AI coding agent（如 Claude Code、Codex）在需要用户输入时会暂停。如果用户不在电脑前，整个工作流就会停滞。

现有方案（Codex Web、Devin）运行在远程 VM，但用户希望 agent 运行在自己的环境中。

## 技术架构

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Local Machine │     │  Omnara Server  │     │  Web/Mobile App │
│                 │     │                 │     │                 │
│  ┌───────────┐  │     │                 │     │                 │
│  │  Headless │  │────▶│   WebSocket     │◀────│   Client UI     │
│  │  Daemon   │  │     │   Relay         │     │                 │
│  └───────────┘  │     │                 │     │                 │
│       │         │     │                 │     │                 │
│  ┌───────────┐  │     │  ┌───────────┐  │     │                 │
│  │  Agent    │  │     │  │  Session  │  │     │                 │
│  │  Loop     │  │     │  │  State    │  │     │                 │
│  └───────────┘  │     │  └───────────┘  │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

### 核心组件

1. **Headless Daemon**
   - 运行在用户机器上
   - 托管 agent loop
   - 只建立 outbound WebSocket 连接
   - 无需暴露端口、SSH 或隧道

2. **WebSocket Relay**
   - 中继消息
   - 持久化会话状态
   - 支持云同步

3. **云同步机制**
   - 每轮对话创建 git commit
   - 推送到服务器
   - 本地离线时可在云端 sandbox 继续
   - 返回后可 pull 变更回本地

## 创新特性

### 语音交互
- 边走边和 agent 对话
- 比打字更自然，更详细
- 迭代式对话产生更好的计划

### 跨设备无缝切换
- 手机上继续桌面的 agent 会话
- 不中断 agent 工作

### 本地 + 云端混合
- 优先本地运行（使用自己的环境）
- 离线时自动切换到云端 sandbox
- 环境差异通过让 agent 安装依赖解决

## 使用方式

```bash
# 安装
curl -fsSL https://omnara.com/install/install.sh | bash

# 在任意 git 仓库中启动
omnara
```

## 定价
- 免费：10 agent sessions/月
- $20/月：无限 sessions
- 使用自己的 Claude/Codex 订阅，无需额外 token 费用

## 对我们的启示

1. **远程 agent 架构参考**
   - outbound WebSocket 避免网络配置问题
   - 会话状态持久化支持断点续传
   - git-based 同步简单可靠

2. **语音交互的价值**
   - 不是噱头，实际很有用
   - 适合需要详细描述的场景
   - 移动场景的最佳交互方式

3. **混合执行模式**
   - 本地优先保证环境一致性
   - 云端备份保证可用性
