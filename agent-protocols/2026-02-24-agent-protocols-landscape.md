# 2026年智能体协议与框架全景

> 学习日期: 2026-02-24
> 来源: digitalapplied.com, learndevrel.com, curateclick.com

## 核心发现

2026年智能体生态已形成清晰的分层架构：
- **MCP (Model Context Protocol)** - 工具连接层，"AI的USB-C"
- **A2A (Agent-to-Agent Protocol)** - 智能体协作层
- **WebMCP** - 浏览器端工具暴露层（2026年2月新发布）

## 一、MCP 协议演进

### 关键里程碑
| 时间 | 事件 |
|------|------|
| 2024.11 | Anthropic 发布 MCP 规范 |
| 2025.03 | OpenAI 采用 MCP |
| 2025.06 | Google Gemini 支持 MCP |
| 2025.12 | MCP 捐赠给 Linux Foundation |
| 2026.01 | 1000+ MCP servers 可用 |

### M*N → M+N 转换
- 之前: 10个模型 × 100个工具 = 1000个集成
- 之后: 10个模型 + 100个工具 = 110个实现

### MCP 架构组件
- **Clients**: Claude Desktop, Cursor, Windsurf
- **Servers**: filesystem, database, GitHub, Slack
- **Tools**: 可执行函数
- **Resources**: 数据源
- **Prompts**: 模板交互

### v2025-11-25 规范新特性
1. OpenID Connect Discovery - 标准化认证
2. Icons for Primitives - 改善可发现性
3. Incremental Scope Consent - 最小权限原则
4. Experimental Tasks - 持久化长时任务
5. Streamable HTTP - 替代 SSE，支持无状态服务器

### MCP Apps (SEP-1865)
革命性扩展：MCP 服务器可提供交互式 UI
- `ui://` URI scheme 声明 UI 资源
- 沙盒 iframe 渲染，安全隔离
- postMessage 上的 JSON-RPC 通信
- 已被 Claude, ChatGPT, VS Code 采用

## 二、A2A 协议

### 定位
MCP 处理"模型→工具"的垂直集成
A2A 处理"智能体→智能体"的水平协作

### 核心概念
| 概念 | 描述 |
|------|------|
| Agent Cards | JSON 元数据，描述能力和认证要求 |
| Tasks | 工作单元，有完整生命周期 |
| Messages | 智能体间通信单元 |
| Parts | 消息内容（文本/文件/结构化数据）|
| Streaming | SSE 实时更新 |
| Push Notifications | 长时任务异步通知 |

### 设计原则
- 拥抱 Agentic 能力，无需共享内存/工具/上下文
- 基于 HTTP, SSE, JSON-RPC 现有标准
- 默认安全，支持 Zero Trust 架构
- 支持长时任务（小时/天级别）

## 三、WebMCP - 浏览器革命

### 发布信息
- 发布日期: 2026年2月10日
- 可用版本: Chrome 145+ (Canary 146+)
- 状态: Early Preview

### 解决的问题
当前 AI 智能体浏览网页的荒谬现状：
- 截图页面
- 猜测哪个蓝色矩形是"提交"按钮
- 抓取 DOM 元素
- 点击直到成功

**机器人流量已占网络流量的 51%**

### 两种 API

#### 1. Declarative API (HTML 表单)
```html
<form toolname="search_flights" tooldescription="Search for available flights">
  <input name="origin" placeholder="Departure city" />
  <input name="destination" placeholder="Arrival city" />
  <button type="submit">Search</button>
</form>
```

#### 2. Imperative API (JavaScript)
```javascript
navigator.modelContext.registerTool({
  name: "add_to_cart",
  description: "Add a product to the shopping cart",
  inputSchema: { /* JSON Schema */ },
  execute: async (params) => { /* 执行逻辑 */ }
});
```

### MCP vs WebMCP
| 方面 | MCP | WebMCP |
|------|-----|--------|
| 位置 | 服务器端 | 浏览器端 |
| 部署 | 自建服务器 | Chrome 内置 |
| 范围 | 任意客户端 | 仅浏览器智能体 |

### 当前限制
- 无 headless 模式
- 需要 UI 同步
- 可发现性问题未解决

## 四、框架选择指南

### MCP 适用场景
- 需要跨多个 AI 模型的标准化工具连接
- 构建同时支持 Claude, GPT, Gemini 的集成
- 利用 1000+ 现有 MCP server 生态
- 在 Linux Foundation 治理下面向未来

### LangChain 适用场景
- 构建 RAG 应用
- 复杂链式组合
- 需要 LangSmith 可观测性
- 偏好成熟、经过实战检验的框架

### CrewAI 适用场景
- 任务需要多个专业化智能体
- 需要智能体委托、交接和协作
- 复杂工作流模拟人类团队协作
- 不同智能体使用不同 LLM 优化成本

## 五、集成模式

### 模式1: MCP + LangChain
MCP 提供工具连接，LangChain 提供编排

### 模式2: CrewAI + MCP
CrewAI 智能体团队通过 MCP 访问外部系统

### 模式3: 全栈
- MCP: 标准化工具层
- LangChain: RAG、链、数据处理
- CrewAI: 专业化智能体团队编排

## 六、安全最佳实践

1. **最小权限原则** - 只授予必要的 MCP 工具
2. **输入验证** - 执行前清理所有工具输入
3. **速率限制** - 实现每智能体/每工具的限制
4. **审计日志** - 记录所有工具调用
5. **沙盒化** - 在隔离环境运行 MCP servers
6. **认证** - 敏感 MCP servers 要求认证

---

## 学习总结

2026年智能体技术栈已趋于成熟：
1. **协议标准化** - MCP 成为 Linux Foundation 项目，行业共识形成
2. **分层清晰** - 工具层(MCP) + 协作层(A2A) + 浏览器层(WebMCP)
3. **框架互补** - MCP/LangChain/CrewAI 各有定位，可组合使用
4. **浏览器革命** - WebMCP 让网站直接暴露结构化工具，终结"像素猜测"时代

**对晋哥工作的启示**：
- AI辅助编程可考虑 MCP 集成，统一工具接口
- 研发知识库可用 MCP Resources 暴露
- 多智能体协作场景可参考 A2A 设计
