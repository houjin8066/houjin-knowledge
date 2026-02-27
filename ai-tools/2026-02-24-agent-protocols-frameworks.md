# AI Agent 协议与框架学习笔记

**学习日期:** 2026-02-24
**来源:** learndevrel.com, digitalapplied.com

---

## 核心发现：MCP 与 A2A 是互补层

2025-2026年智能体生态的关键认知转变：**MCP 和 A2A 不是竞争关系，而是同一技术栈的互补层**。

- **MCP (Model Context Protocol)**: 垂直整合 - AI模型与工具/数据源的连接
- **A2A (Agent-to-Agent Protocol)**: 水平协作 - 独立AI智能体之间的协作

> "MCP is how AI models reach out to the world. A2A is how AI agents reach out to each other."

---

## MCP 协议要点 (v2025-11-25)

### 架构
- **Host**: 应用程序 (Claude Desktop, ChatGPT, VS Code, Cursor)
- **Client**: Host内的协议处理器
- **Server**: 暴露 Tools/Resources/Prompts 的程序
- 全球已有 **10,000+** 公开 MCP Server

### 核心组件
| 组件 | 说明 |
|------|------|
| Tools | 可执行函数 (查询数据库、发邮件、创建文件) |
| Resources | 提供上下文的数据 (文件内容、数据库记录) |
| Prompts | 模板化交互模式 |

### 2025年11月规范更新亮点
1. **OpenID Connect Discovery** - 标准化认证服务器发现
2. **Icons for Primitives** - 工具/资源可包含图标，提升UX
3. **Incremental Scope Consent** - 渐进式权限请求，遵循最小权限原则
4. **Experimental Tasks** - 支持长时间运行的持久化请求
5. **SDK Tiering System** - 官方SDK分级体系 (TypeScript/Python/Java/Kotlin/C#/Swift)

### MCP Apps (SEP-1865) - 重大突破
MCP Server 现在可以提供**交互式UI**！
- 使用 `ui://` URI scheme 声明UI资源
- 在沙箱 iframe 中渲染，安全隔离
- 通过 postMessage 进行 JSON-RPC 通信
- 已被 Claude, ChatGPT, Goose, VS Code 采用

### Transport 演进
```
stdio (本地) → HTTP+SSE (双端点) → Streamable HTTP (单端点)
```
Streamable HTTP 优势：
- 无状态服务器，支持水平扩展和 Serverless
- CDN/代理兼容
- 优雅降级

---

## A2A 协议要点

### 核心概念
| 概念 | 说明 |
|------|------|
| Agent Cards | JSON元数据，描述智能体能力、认证要求 |
| Tasks | 工作单元，生命周期: submitted→working→input-required→completed/failed |
| Messages | 任务执行期间交换的通信单元 |
| Parts | 消息内容，支持文本、文件附件、结构化数据 |
| Streaming | 通过SSE实时更新任务进度 |
| Push Notifications | 长时间任务的异步更新 |

### 设计原则
- 拥抱智能体能力：自然、非结构化协作，无需共享内存/工具/上下文
- 基于现有标准：HTTP, SSE, JSON-RPC
- 默认安全：内置认证授权，支持零信任架构
- 长时间任务支持：可运行数小时甚至数天

---

## 框架对比：MCP vs LangChain vs CrewAI

| 维度 | MCP | LangChain | CrewAI |
|------|-----|-----------|--------|
| 定位 | 协议标准 | 应用框架 | 智能体编排 |
| 类比 | "AI的USB-C" | "AI的Rails" | "AI团队经理" |
| 抽象层级 | 低 (协议) | 中 (链) | 高 (智能体) |
| 多智能体 | N/A | 通过LangGraph | 原生支持 |
| 工具生态 | 1000+ servers | 内置+MCP | LangChain+MCP |

### MCP 解决的核心问题：M*N → M+N
- **之前**: 10个模型 × 100个工具 = 1000个集成
- **之后**: 10个模型 + 100个工具 = 110个实现

### 集成模式
1. **MCP + LangChain**: MCP提供工具连接，LangChain负责编排
2. **CrewAI + MCP**: 智能体团队通过MCP访问外部系统
3. **Full Stack**: MCP(工具层) + LangChain(RAG/链) + CrewAI(团队编排)

---

## 选型建议

### 选 MCP 当：
- 需要跨多个AI模型的标准化工具连接
- 构建需要同时支持 Claude/GPT/Gemini 的集成
- 想利用 1000+ 现有 MCP Server 生态

### 选 LangChain 当：
- 构建 RAG 应用
- 复杂链式处理
- 需要 LangSmith 可观测性

### 选 CrewAI 当：
- 任务需要多个专业化智能体协作
- 需要智能体委托、交接、协作
- 不同智能体需要使用不同LLM优化成本

---

## 关键时间线

- 2024.11: Anthropic 发布 MCP 规范
- 2025.03: OpenAI 采用 MCP
- 2025.04: Google 发布 A2A 协议
- 2025.06: Google Gemini 支持 MCP
- 2025.11: MCP v2025-11-25 规范发布
- 2025.12: MCP 捐赠给 Linux Foundation
- 2026.01: 1000+ MCP servers 可用

---

## 实践启示

1. **协议选择不是非此即彼** - MCP和A2A解决不同层面问题
2. **MCP Apps 是游戏规则改变者** - AI助手可以渲染交互式UI了
3. **Streamable HTTP 是生产环境首选** - 单端点、无状态、CDN友好
4. **安全最佳实践**:
   - 最小权限原则
   - 输入验证
   - 速率限制
   - 审计日志
   - 沙箱隔离
