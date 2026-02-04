# Deno Sandbox

> 专为 LLM 生成代码设计的安全执行环境

## 概述

Deno Sandbox 提供轻量级 Linux microVMs，专门解决 LLM 生成代码的安全执行问题。核心创新在于 secrets 保护和网络出口控制。

## 核心问题

传统沙箱只隔离计算，但 LLM 生成的代码需要：
- 调用外部 API
- 使用真实凭证
- 没有人工审查

这需要更深层的安全机制。

## 技术规格

| 规格 | 值 |
|------|-----|
| 区域 | Amsterdam, Chicago |
| vCPUs | 2 |
| 内存 | 768 MB - 4 GB |
| 启动时间 | < 1 秒 |
| 最长生命周期 | 30 分钟 |

## 核心特性

### 1. Secrets 保护（创新点）

```javascript
const sandbox = await Sandbox.create({
  secrets: {
    OPENAI_API_KEY: {
      hosts: ["api.openai.com"],  // 只有访问这些 host 时才注入真实 key
      value: process.env.OPENAI_API_KEY,
    },
  },
});
```

**工作原理**：
- 代码只能看到占位符
- 真实 key 只在请求批准的 host 时才会出现
- 防止 prompt injection 导致的 key 泄露到 evil.com

### 2. 网络出口控制

```javascript
const sandbox = await Sandbox.create({
  allowNet: ["api.openai.com", "*.anthropic.com"],
});
```

- 通过 outbound proxy 实现（类似 coder/httpjail）
- 未列出的 host 请求被阻止

### 3. 一键部署

```javascript
const build = await sandbox.deploy("my-app", {
  production: true,
  build: { mode: "none", entrypoint: "server.ts" },
});
```

从 sandbox 直接部署到 Deno Deploy，无需重新构建。

### 4. 持久化

- **Volumes**：读写存储
- **Snapshots**：只读镜像，用于预装工具链

## 适用场景

- AI agents 执行代码
- Vibe-coding 环境
- 安全插件系统
- 临时 CI runners
- 客户提供的代码执行

## 定价

- $0.05/h CPU 时间
- $0.016/GB-h 内存
- $0.20/GiB-month 存储

## 与 Clawdbot 的关系

可以考虑将 Deno Sandbox 作为 Clawdbot 的代码执行后端：
- 安全执行用户代码
- 保护 API keys
- 控制网络访问

## 参考

- [Deno Sandbox 官网](https://deno.com/sandbox)
- [文档](https://docs.deno.com/sandbox/)
- [JavaScript SDK](https://jsr.io/@deno/sandbox)
- [Python SDK](https://pypi.org/project/deno-sandbox/)
- 学习日期：2026-02-04
