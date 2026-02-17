# Agent 通信协议 (2026)

> 来源：iterathon.tech | 更新：2026-02-17

## 概述

多智能体系统需要标准化通信协议实现互操作性。2025-2026 年出现了几个关键协议。

## MCP (Model Context Protocol)

**开发者**：Anthropic

**定位**：AI 应用连接数据源和工具的通用接口

**核心特性**：
- 标准化 server-client 架构
- 语言无关（Python, Node.js 等）
- 基于范围的权限控制
- 双向通信支持流式响应

**使用场景**：
- 多个专业 agents 共享数据源
- 无需为每个 agent 写自定义集成

**示例**：
```python
from mcp import MCPServer, Tool

class AgentHubServer(MCPServer):
    def __init__(self):
        super().__init__(name="agent-hub")
    
    @self.tool()
    async def query_data(self, id: str) -> dict:
        return await self.db.find_one({"id": id})
    
    @self.tool()
    async def create_handoff(self, from_agent: str, 
                             to_agent: str, context: dict):
        """Agent 间任务交接"""
        handoff_id = await self.store_handoff({
            "from": from_agent,
            "to": to_agent,
            "context": context
        })
        await self.notify_agent(to_agent, {
            "type": "handoff_received",
            "handoff_id": handoff_id
        })
        return handoff_id
```

**采用情况**：已成为企业多智能体工具共享的事实标准，Claude、LangGraph、CrewAI 原生支持。

## ACP (Agent Communication Protocol)

**定位**：定义 agent-to-agent 直接通信的消息格式和交互模式

**核心消息类型**：
| 类型 | 用途 |
|------|------|
| REQUEST | 请求另一个 agent 执行动作 |
| INFORM | 共享状态或数据 |
| PROPOSE | 建议协作行动 |
| CONFIRM/REJECT | 响应提案 |
| QUERY | 请求信息 |

**交互示例**：
```
Agent A → Agent B: REQUEST[task=verify_compliance, doc_id=inv-001]
Agent B → Agent A: CONFIRM[estimated_time=5s]
Agent B → Agent A: INFORM[status=approved, checks=14/14]
Agent A → Agent C: REQUEST[task=process_payment, invoice_id=inv-001]
```

## ANP (Agent Negotiation Protocol)

**定位**：多个 agents 可处理同一任务时的结构化协商

**协商阶段**：
1. **CFP (Call for Proposals)** - 请求方广播任务需求
2. **Proposal Submission** - 有能力的 agents 提交竞标
3. **Evaluation** - 请求方评估提案
4. **Award** - 选中的 agent 获得任务
5. **Execution Monitoring** - 跟踪进度，处理失败

**适用场景**：
- 动态资源分配（云计算、API 配额）
- 跨 agent 池负载均衡
- 成本优化（选择满足质量阈值的最便宜 agent）

**选择逻辑示例**：
```javascript
selectBestProposal(proposals) {
    return proposals.reduce((best, current) => {
        const score = 
            (1 - current.load) * 0.4 +      // 负载权重
            (1 / current.latency) * 0.3 +   // 延迟权重
            (1 - current.cost) * 0.3;       // 成本权重
        return score > best.score 
            ? { peer: current, score } 
            : best;
    }, { peer: null, score: 0 });
}
```

## 协议选择指南

| 需求 | 推荐协议 |
|------|----------|
| 共享工具/数据源 | MCP |
| 直接 agent 通信 | ACP |
| 任务竞标/负载均衡 | ANP |
| 企业级审计 | MCP + ACP |

## 与 OpenClaw 的关联

- OpenClaw 的 `sessions_spawn` 类似简化版 MCP handoff
- 未来可能集成 MCP 协议扩展工具能力
- ACP 消息模式可参考用于 sub-agent 通信设计

## 参考
- iterathon.tech/blog/multi-agent-coordination-systems-enterprise-guide-2026
- Anthropic MCP 文档
