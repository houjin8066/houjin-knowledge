# 2026年智能体协议生态全景

> 学习日期: 2026-02-23
> 来源: learndevrel.com, digitalapplied.com, curateclick.com

## 核心洞察

2026年智能体生态的关键认知：**MCP 和 A2A 不是竞争关系，而是互补的协议栈层**。

- **MCP (Model Context Protocol)**: 垂直整合 - AI模型与工具/数据源的连接
- **A2A (Agent-to-Agent Protocol)**: 水平协作 - 独立AI代理之间的协作

> "MCP is how AI models reach out to the world. A2A is how AI agents reach out to each other."

## MCP 协议演进 (v2025-11-25)

### 最新规范特性
1. **OpenID Connect Discovery** - 标准化认证服务器发现
2. **Icons for Primitives** - Tools/Resources/Prompts 支持图标
3. **Incremental Scope Consent** - 渐进式权限请求（最小权限原则）
4. **Tool Calling in Sampling** - sampling 能力支持 tools 和 toolChoice
5. **Experimental Tasks** - 持久化请求，支持长时间运行操作
6. **SDK Tiering System** - 官方/社区 SDK 分级体系
7. **Formalized Governance** - 工作组和兴趣组结构

### MCP Apps (SEP-1865) - 重大突破
MCP 服务器现在可以提供交互式 UI：
- `ui://` URI Scheme 声明 UI 资源
- 沙箱 iframe 渲染，安全隔离
- JSON-RPC over postMessage 通信
- 已被 Claude, ChatGPT, Goose, VS Code 采用

### Transport 演进
```
stdio → HTTP+SSE → Streamable HTTP (当前)
```

Streamable HTTP 优势：
- 无状态服务器，支持水平扩展和 Serverless
- CDN/代理兼容
- 单一端点，简化实现

### 官方 SDK
TypeScript (参考实现) | Python | Java | Kotlin | C# | Swift

## A2A 协议

### 核心概念
| 概念 | 描述 |
|------|------|
| Agent Cards | JSON 元数据，描述代理能力、认证要求、交互模式 |
| Tasks | 工作单元，生命周期: submitted → working → input-required → completed/failed |
| Messages | 代理间通信单元，包含多个 Parts |
| Parts | 消息内容：文本、文件附件、结构化数据 |
| Streaming | SSE 实时更新 |
| Push Notifications | 长时间任务的异步通知 |

### 设计原则
- 拥抱代理能力：自然、非结构化协作
- 基于现有标准：HTTP, SSE, JSON-RPC
- 默认安全：内置认证、授权、零信任架构
- 长时间任务支持：可运行数小时/数天

## 框架对比：MCP vs LangChain vs CrewAI

| 维度 | MCP | LangChain | CrewAI |
|------|-----|-----------|--------|
| 定位 | 协议标准 | 应用框架 | 代理编排 |
| 类比 | "AI的USB-C" | "AI的Rails" | "AI团队经理" |
| 抽象层级 | 低（协议） | 中（链） | 高（代理） |
| 多代理 | N/A | Via LangGraph | 原生支持 |
| 工具生态 | 1000+ servers | 内置 + MCP | LangChain + MCP |

### 集成模式
1. **MCP + LangChain**: MCP 提供工具连接，LangChain 编排
2. **CrewAI + MCP**: MCP 工具在 CrewAI 代理团队中使用
3. **Full Stack**: 三者结合处理复杂系统

### 选择指南
- **选 MCP**: 需要跨模型标准化工具连接
- **选 LangChain**: 构建 RAG、复杂链、需要 LangSmith 可观测性
- **选 CrewAI**: 任务需要多个专业代理协作

## Chrome WebMCP - 浏览器端革命

### 发布信息
- 发布日期: 2026-02-10
- 状态: Early Preview (Chrome 145+)

### 解决的问题
AI 代理不再需要"假装是人类"：
- 不再截图猜测按钮位置
- 不再 DOM 抓取
- 网站直接暴露结构化工具

### 两种 API

**Declarative API (HTML 表单)**
```html
<form toolname="search_flights" tooldescription="Search for available flights">
  <input name="origin" placeholder="Departure city" />
  <input name="destination" placeholder="Arrival city" />
  <button type="submit">Search</button>
</form>
```

**Imperative API (JavaScript)**
```javascript
navigator.modelContext.registerTool({
  name: "add_to_cart",
  description: "Add a product to the shopping cart",
  inputSchema: { /* JSON Schema */ },
  execute: async (params) => { /* 执行逻辑 */ }
});
```

### WebMCP vs MCP
| 维度 | MCP | WebMCP |
|------|-----|--------|
| 位置 | 服务器端 | 浏览器端 |
| 部署 | 自建服务器 | Chrome 内置 |
| 范围 | 任意客户端 | 仅浏览器代理 |

### 当前限制
- 无 headless 模式
- 需要 UI 同步
- 可发现性问题待解决

## 实践启示

### 对研发知识库的启发
1. **MCP 服务器模式**: 可以为内部工具构建 MCP 服务器，让 AI 代理标准化访问
2. **A2A 协作**: 多个专业代理协作处理复杂研发任务
3. **WebMCP**: 内部 Web 系统可以暴露结构化工具给 AI 代理

### 安全最佳实践
- 最小权限原则
- 输入验证
- 速率限制
- 审计日志
- 沙箱隔离
- 敏感服务器认证

---

*下次学习方向: A2A 与 Google ADK 的深度集成、MCP Apps 实战*
