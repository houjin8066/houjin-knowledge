# 智能体协议生态 2026 学习笔记

> 学习时间：2026-02-24 21:00
> 来源：Gentoro Blog, LearnDevRel, Anthropic Official

## 核心洞察

2025年标志着AI从"能思考什么"转向"能做什么"的关键转折。行业焦点从模型智能转向自主行动能力，MCP和A2A两大协议成为智能体基础设施的双支柱。

## 一、2025年 Agentic AI 里程碑事件

### 1.1 主要产品发布
| 产品 | 发布时间 | 核心能力 |
|------|----------|----------|
| OpenAI Operator | 2025.01 | 网页导航、任务执行，采用"推理-行动"架构 |
| Anthropic MCP | 2025年底 | 成为行业标准，连接AI与数据源（Drive/Slack/GitHub） |
| Google Project Jarvis | Gemini 2.0生态 | Chrome浏览器内自主操作 |
| Salesforce Agentforce 360 | Dreamforce 2025 | 企业级"自主同事"，处理客服和销售 |
| Apple App Intents | iOS 18.4 (2025.03) | Siri跨应用操作能力 |

### 1.2 行业标准化：AAIF 成立
2025年12月，Linux基金会宣布成立 **Agentic AI Foundation (AAIF)**：
- 创始成员：OpenAI、Anthropic、Block
- 支持者：Microsoft、Google、AWS、Bloomberg、Cloudflare
- 三大支柱项目：
  - **AGENTS.md** (OpenAI) - 项目级智能体指令标准
  - **MCP** (Anthropic) - 数据和工具集成协议
  - **Goose** (Block) - 本地优先的开源智能体框架

### 1.3 投资与并购
- 企业GenAI支出：$37B (2025)，同比增长3.2倍
- AI初创公司获得全球VC 50%以上份额
- Workday收购Sana：$1.1B
- Microsoft AI数据中心投资：$80B（单年最大）
- Google收购Wiz：$32B
- Anthropic收购Bun运行时，Claude Code达$1B年收入

## 二、MCP 协议深度解析

### 2.1 核心架构
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  MCP Host   │────▶│  MCP Client │────▶│  MCP Server │
│ (Claude/VS) │     │  (协议处理)  │     │ (工具/资源)  │
└─────────────┘     └─────────────┘     └─────────────┘
```

### 2.2 三大能力
- **Tools**: 可执行函数（查询数据库、发邮件、创建文件）
- **Resources**: 上下文数据（文件内容、数据库记录、API响应）
- **Prompts**: 模板化交互模式

### 2.3 最新规范 v2025-11-25 新特性
1. **OpenID Connect Discovery** - 标准化认证服务器发现
2. **Icons for Primitives** - 工具/资源可带图标
3. **Incremental Scope Consent** - 渐进式权限请求
4. **Tool Calling in Sampling** - 采样中支持工具调用
5. **Experimental Tasks** - 持久化请求，支持长时间运行
6. **SDK Tiering System** - 官方SDK分级体系

### 2.4 传输层演进
```
stdio (本地) → HTTP+SSE (双端点) → Streamable HTTP (单端点)
```
Streamable HTTP 优势：
- 无状态服务器，支持水平扩展
- CDN/代理兼容
- 优雅降级
- 实现更简单

### 2.5 MCP Apps (SEP-1865)
革命性扩展：MCP服务器可提供交互式UI
- 使用 `ui://` URI scheme
- 沙箱iframe渲染
- JSON-RPC over postMessage
- 已被 Claude、ChatGPT、VS Code 采用

## 三、A2A 协议解析

### 3.1 定位差异
> "MCP是AI模型触达世界的方式，A2A是AI智能体相互触达的方式"

- **MCP**: 垂直集成（模型 ↔ 工具/数据）
- **A2A**: 水平协作（智能体 ↔ 智能体）

### 3.2 核心概念
| 概念 | 说明 |
|------|------|
| Agent Cards | JSON元数据，描述智能体能力和认证要求 |
| Tasks | 工作单元，生命周期：submitted→working→completed/failed |
| Messages | 任务执行中的通信单元 |
| Parts | 消息内容：文本、文件、结构化数据 |
| Streaming | SSE实时更新 |
| Push Notifications | 长时间任务的异步通知 |

### 3.3 设计原则
1. 拥抱智能体能力：自然、非结构化协作
2. 基于现有标准：HTTP、SSE、JSON-RPC
3. 默认安全：内置认证、授权、零信任
4. 长时间任务支持：可运行数小时/数天

## 四、实际应用场景

### 4.1 生产力提升
- LSE研究：AI智能体平均每周节省7.5小时
- PwC调查：88%高管增加AI预算，77%重新设计数据策略

### 4.2 行业应用
- **医疗**: 患者接诊、癌症检测准确率99.26%
- **金融**: 理赔处理人工减少80%，AI交易年化收益超200%
- **软件**: 自主编码智能体处理大部分常规bug修复
- **电商**: Amazon Agentic Seller Assistant 管理库存、定价、合规

## 五、监管动态

### 5.1 EU AI Act
- 2025年底启动 AI Act Service Desk
- 高风险系统合规检查器
- 强调可追溯性和人类监督

### 5.2 美国
- 联邦层面转向"最小负担"框架
- Amazon起诉Perplexity AI的Comet浏览器（智能体商业首案）

## 六、关键趋势

1. **AgenticOS概念兴起** - 多模态集成的基础层
2. **MCP成为事实标准** - 10,000+公开服务器
3. **A2A与Google ADK深度集成**
4. **Crypto-AI交叉** - Coinbase x402协议、AgentKit

## 学习总结

2025-2026年智能体生态的核心架构已经清晰：
- **MCP** 解决"单个智能体如何获取工具和数据"
- **A2A** 解决"多个智能体如何协作"
- **AAIF** 确保标准开放、互操作、厂商中立

这与HTTP和Linux对Web的意义类似，正在为智能体时代奠定基础设施标准。

---
*下次学习方向：深入研究 MCP Apps 实现细节、A2A 与 Google ADK 集成实践*
