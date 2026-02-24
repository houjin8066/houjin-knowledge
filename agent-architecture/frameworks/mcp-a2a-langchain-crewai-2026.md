# AI 智能体协议与框架全景 (2026年2月)

> 来源：agent-learning 自主学习 2026-02-24

## 核心结论

**两层协议架构已成为行业共识**：
- **MCP (Model Context Protocol)**：垂直集成层，AI 模型 ↔ 工具/数据
- **A2A (Agent-to-Agent Protocol)**：水平协作层，智能体 ↔ 智能体

## MCP 协议 (v2025-11-25)

### 架构组件
| 组件 | 说明 |
|------|------|
| MCP Host | 使用 MCP 的应用 (Claude Desktop, ChatGPT, VS Code, Cursor) |
| MCP Client | Host 内的协议处理器，管理与 Server 的连接 |
| MCP Server | 暴露 Tools/Resources/Prompts 的程序，已有 10,000+ 公开服务器 |
| Tools | 可执行函数 (查询数据库、发邮件、创建文件) |
| Resources | 提供上下文的数据 (文件内容、数据库记录、API 响应) |
| Prompts | 模板化交互模式 |

### 2025-11 规范新特性
- **OpenID Connect Discovery**：标准化认证服务器发现
- **MCP Apps (SEP-1865)**：服务器可提供交互式 HTML UI
- **Streamable HTTP**：取代 SSE，单端点设计
- **增量权限同意**：通过 WWW-Authenticate 按需请求权限
- **实验性 Tasks**：支持长时间运行的持久请求
- **SDK 分层系统**：官方 SDK 覆盖 TypeScript/Python/Java/Kotlin/C#/Swift

### 传输层演进
```
stdio (本地) → HTTP+SSE (双端点) → Streamable HTTP (单端点)
```
Streamable HTTP 优势：无状态服务器、CDN 兼容、简化实现

## A2A 协议

### 核心概念
| 概念 | 说明 |
|------|------|
| Agent Cards | JSON 元数据，描述智能体能力、认证要求、交互模式 |
| Tasks | 工作单元，生命周期：submitted → working → input-required → completed/failed |
| Messages | 智能体间通信单元，包含多个 Parts |
| Parts | 消息内容：文本、文件附件、结构化数据 |
| Streaming | SSE 实时更新任务进度 |
| Push Notifications | 长时间任务的异步通知 |

### 设计原则
- 拥抱智能体能力：无需共享内存/工具/上下文
- 基于现有标准：HTTP、SSE、JSON-RPC
- 默认安全：内置认证授权和零信任架构
- 支持长时间任务：可运行数小时/数天

## 框架对比

| 维度 | MCP | LangChain | CrewAI |
|------|-----|-----------|--------|
| 定位 | 协议标准 | 应用框架 | 多智能体编排 |
| 类比 | USB-C for AI | Rails for AI | AI team manager |
| 抽象层级 | 低 (协议) | 中 (链) | 高 (智能体) |
| 状态管理 | 外部 | LangGraph | 内置 |
| 多智能体 | N/A | 通过 LangGraph | 原生支持 |
| 工具生态 | 1000+ 服务器 | 内置 + MCP | LangChain + MCP |

## 集成模式

### 模式1：MCP + LangChain
```python
from langchain_mcp_adapters import MCPToolkit

toolkit = MCPToolkit(servers=["filesystem", "database", "github"])
tools = toolkit.get_tools()
agent = create_openai_tools_agent(llm, tools, prompt)
```

### 模式2：CrewAI + MCP
- 智能体通过 MCP 服务器访问外部系统
- CrewAI 管理智能体协作和任务委派
- 每个智能体可配置不同的 MCP 工具

### 模式3：全栈架构
```
┌─────────────────────────────────────┐
│           CrewAI (多智能体编排)       │
├─────────────────────────────────────┤
│     LangChain (RAG/链/数据处理)      │
├─────────────────────────────────────┤
│         MCP (标准化工具层)           │
└─────────────────────────────────────┘
```

## 选型指南

| 场景 | 推荐 |
|------|------|
| 跨模型工具标准化 | MCP |
| RAG 应用 / 复杂链 | LangChain |
| 多角色智能体协作 | CrewAI |
| 智能体间通信 | A2A |
| 生产级全栈系统 | MCP + LangChain + CrewAI |

## 时间线

- 2024-11：Anthropic 发布 MCP
- 2025-03：OpenAI 采用 MCP
- 2025-04：Google 发布 A2A
- 2025-06：Google Gemini 支持 MCP
- 2025-11：MCP v2025-11-25 规范发布
- 2025-12：MCP 捐赠给 Linux Foundation
- 2026-01：1000+ MCP 服务器可用
- 2026-02：MCP + A2A 成为行业标准双层架构
