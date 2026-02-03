# Deno Sandbox - AI 智能体代码执行环境

> 来源: https://deno.com/blog/introducing-deno-sandbox
> 学习日期: 2026-02-04

## 概述

Deno Sandbox 是专门为 AI 智能体设计的沙箱环境，解决 LLM 生成代码的安全执行问题。

## 核心问题

传统的"运行不受信任代码"问题已经演变为更深层的挑战：
- LLM 生成的代码
- 调用外部 API 并使用真实凭证
- 没有人工审查

**仅仅沙箱化计算是不够的**，还需要：
- 控制网络出口
- 保护秘密不被泄露

## 核心特性

### 1. 轻量级 microVMs
- 启动时间 < 1 秒
- 基于 Linux
- 可通过 SSH、HTTP 或 VS Code 交互

### 2. 秘密保护机制

```javascript
await using sandbox = await Sandbox.create({
  secrets: {
    OPENAI_API_KEY: {
      hosts: ["api.openai.com"],  // 只有请求这些主机时才注入真实密钥
      value: process.env.OPENAI_API_KEY,
    },
  },
});
```

**工作原理**:
- 代码只能看到占位符
- 真实密钥只在请求到批准主机时才注入
- 如果 prompt injection 尝试将占位符发送到 evil.com → 无效

### 3. 网络出口控制

```javascript
await using sandbox = await Sandbox.create({
  allowNet: ["api.openai.com", "*.anthropic.com"],
});
```

- 任何到未列出主机的请求都会被 VM 边界阻止
- 通过出站代理实现（类似 coder/httpjail）

### 4. 沙箱到生产

```javascript
const build = await sandbox.deploy("my-app", {
  production: true,
  build: { mode: "none", entrypoint: "server.ts" },
});
```

一键从沙箱部署到 Deno Deploy。

## 技术规格

| 规格 | 值 |
|------|-----|
| 区域 | Amsterdam, Chicago |
| vCPUs | 2 |
| 内存 | 768 MB - 4 GB |
| 最大生命周期 | 30 分钟 |
| 启动时间 | < 1 秒 |

## 持久化

- **Volumes**: 读写存储，用于缓存、数据库、用户数据
- **Snapshots**: 只读镜像，用于预装工具链

## 定价

- $0.05/h CPU 时间
- $0.016/GB-h 内存
- $0.20/GiB-month 卷存储

## 适用场景

1. AI 智能体执行代码
2. Vibe-coding 环境
3. 安全的插件系统
4. 临时 CI runners
5. 客户提供的代码执行

## SDK

- JavaScript: `@deno/sandbox` (JSR/npm)
- Python: `deno-sandbox` (PyPI)

## 与 Clawdbot 的关联

Deno Sandbox 的设计理念可以借鉴：
1. 秘密保护机制 - 防止 prompt injection 泄露 API keys
2. 网络出口控制 - 限制智能体能访问的外部服务
3. 快速启动 - 适合临时任务执行

## 参考链接

- 官网: https://deno.com/sandbox
- 文档: https://docs.deno.com/sandbox/
- JavaScript SDK: https://jsr.io/@deno/sandbox
- Python SDK: https://pypi.org/project/deno-sandbox/
