# AI Agent 协议学习笔记：MCP vs A2A (2026-02-24)

## 核心结论

**MCP 和 A2A 不是竞争关系，而是互补的协议栈层级：**
- **MCP (Model Context Protocol)** - 垂直整合：AI 模型与工具/数据源的连接
- **A2A (Agent-to-Agent Protocol)** - 水平协作：独立 AI Agent 之间的通信

> "MCP is how AI models reach out to the world. A2A is how AI agents reach out to each other."

---

## MCP 协议详解

### 架构组件
| 组件 | 说明 |
|------|------|
| MCP Host | 使用 MCP 的应用（Claude Desktop, ChatGPT, VS Code, Cursor）|
| MCP Client | Host 内的协议处理器，管理与 MCP Server 的连接 |
| MCP Server | 暴露 Tools/Resources/Prompts 的程序，公开注册表已有 10,000+ |
| Tools | AI 可调用的可执行函数（查询数据库、发邮件、创建文件）|
| Resources | 服务器提供的上下文数据（文件内容、数据库记录、API 响应）|
| Prompts | 服务器提供的模板化交互模式 |

### v2025-11-25 规范更新
- **OpenID Connect Discovery** - 标准化认证服务器发现
- **Icons for Primitives** - Tools/Resources/Prompts 可包含图标
- **Incremental Scope Consent** - 通过 WWW-Authenticate 增量请求权限
- **Tool Calling in Sampling** - sampling 能力支持 tools 和 toolChoice
- **Experimental Tasks** - 支持长时间运行操作的持久请求
- **SDK Tiering System** - 官方和社区 SDK 的分级要求

### MCP Apps (SEP-1865) - 重大突破
MCP 服务器现在可以提供交互式 UI：
- **ui:// URI Scheme** - 通过 ui:// 声明交互式 UI 资源
- **Sandboxed Iframe** - 所有 HTML 在沙箱 iframe 中渲染，安全隔离
- **JSON-RPC over postMessage** - iframe 与 host 通过 postMessage 通信
- **向后兼容** - 现有 MCP 实现无需修改

**应用场景**：Kubernetes 管理仪表板、数据库查询构建器、交互式图表

### Transport 演进
1. **stdio** - 本地进程通信（仍支持）
2. **HTTP+SSE** - 需要两个端点（已弃用）
3. **Streamable HTTP** - 单一端点，支持无状态服务器、CDN 兼容、水平扩展

### 官方 SDK
TypeScript（参考实现）、Python、Java、Kotlin、C#、Swift

---

## A2A 协议详解

### 核心概念
| 概念 | 说明 |
|------|------|
| Agent Cards | JSON 元数据文档，描述 agent 能力、认证要求、交互模式 |
| Tasks | 工作单元，生命周期：submitted → working → input-required → completed/failed |
| Messages | agent 间交换的通信单元，包含一个或多个 Parts |
| Parts | 消息内容，支持文本、文件附件、结构化数据 |
| Streaming | 通过 SSE 实时更新任务进度 |
| Push Notifications | 长时间任务的异步更新 |

### 设计原则
- 拥抱 Agentic 能力：agent 以自然、非结构化方式协作
- 基于现有标准：HTTP、SSE、JSON-RPC
- 默认安全：内置认证、授权、零信任架构
- 支持长时间任务：可运行数小时或数天

### 与 Google ADK 深度集成
A2A 已与 Google Agent Development Kit 深度整合

---

## 框架对比：MCP vs LangChain vs CrewAI

| 维度 | MCP | LangChain | CrewAI |
|------|-----|-----------|--------|
| 定位 | 协议标准 | 应用框架 | Agent 编排 |
| 类比 | "USB-C for AI" | "Rails for AI" | "AI team manager" |
| 抽象层级 | 低（协议）| 中（chains）| 高（agents）|
| 多 Agent | N/A | 通过 LangGraph | 原生支持 |
| 工具生态 | 1000+ servers | 内置 + MCP | LangChain + MCP |

### 选择建议
- **MCP**：需要跨多个 AI 模型的标准化工具连接
- **LangChain**：构建 RAG 应用、复杂 chain 组合、需要 LangSmith 可观测性
- **CrewAI**：任务需要多个专业化 agent 协作、agent 委托和交接

### 集成模式
1. **MCP + LangChain**：MCP 提供工具连接，LangChain 编排
2. **CrewAI + MCP**：agent 通过 MCP 访问外部系统
3. **Full Stack**：MCP（工具层）+ LangChain（RAG/chains）+ CrewAI（agent 团队）

---

## MCP 发展时间线
- 2024-11：Anthropic 发布 MCP 规范
- 2025-03：OpenAI 采用 MCP
- 2025-06：Google Gemini 支持 MCP
- 2025-12：MCP 捐赠给 Linux Foundation
- 2026-01：1000+ MCP servers 可用

---

## 关键洞察

1. **M*N → M+N 转变**：MCP 解决了集成爆炸问题（10 模型 × 100 工具 = 1000 集成 → 110 实现）

2. **协议分层清晰**：
   - MCP = 工具访问层（垂直）
   - A2A = Agent 协作层（水平）

3. **MCP Apps 是游戏规则改变者**：AI 助手不再只能返回文本，可以渲染交互式 UI

4. **Linux Foundation 治理**：MCP 已成为行业标准，有正式的工作组和治理结构

---

## 来源
- https://learndevrel.com/blog/mcp-vs-a2a
- https://www.digitalapplied.com/blog/mcp-vs-langchain-vs-crewai-agent-framework-comparison
