# 智能体通信协议 2026

> 更新时间：2026-02-19
> 来源：iterathon.tech

## 协议概览

| 协议 | 开发者 | 用途 | 状态 |
|------|--------|------|------|
| MCP | Anthropic | 工具/数据源共享 | 事实标准 |
| ACP | 社区 | 智能体间消息传递 | 广泛采用 |
| ANP | 社区 | 任务协商分配 | 新兴 |

## MCP（Model Context Protocol）

Anthropic 开发，已成为企业多智能体工具共享的事实标准。

**核心特性**：
- 标准化服务器-客户端架构
- 语言无关（Python、Node.js 等）
- 内置安全（基于作用域的权限）
- 双向通信（支持流式响应）

**原生支持**：Claude、LangGraph、CrewAI

**代码示例**：

```python
from mcp import MCPServer, Tool, Resource

class MultiAgentMCPServer(MCPServer):
    def __init__(self):
        super().__init__(name="enterprise-agent-hub")
    
    @self.tool()
    async def query_customer_data(self, customer_id: str) -> dict:
        """所有智能体共享的客户数据访问"""
        return await self.db.customers.find_one({"id": customer_id})
    
    @self.resource()
    async def inventory_stream(self, warehouse: str):
        """物流智能体的实时库存更新"""
        async for update in self.inventory_feed(warehouse):
            yield update
    
    @self.tool()
    async def create_handoff(self, from_agent: str, to_agent: str, context: dict):
        """智能体间任务交接协议"""
        handoff_id = await self.store_handoff({
            "from": from_agent,
            "to": to_agent,
            "context": context,
            "timestamp": datetime.now(),
            "status": "pending"
        })
        
        await self.notify_agent(to_agent, {
            "type": "handoff_received",
            "handoff_id": handoff_id,
            "from": from_agent
        })
        
        return handoff_id
```

## ACP（Agent Communication Protocol）

定义智能体间直接通信的消息格式和交互模式。

**消息类型**：

| 类型 | 用途 |
|------|------|
| REQUEST | 请求另一个智能体执行动作 |
| INFORM | 共享状态或数据 |
| PROPOSE | 建议协作行动 |
| CONFIRM/REJECT | 响应提议 |
| QUERY | 请求信息 |

**交互示例**：

```
Agent A → Agent B: REQUEST[task=verify_compliance, document_id=inv-2024-001]
Agent B → Agent A: CONFIRM[estimated_time=5s]
Agent B → Agent A: INFORM[compliance_status=approved, checks_passed=14/14]
Agent A → Agent C: REQUEST[task=process_payment, invoice_id=inv-2024-001]
```

## ANP（Agent Negotiation Protocol）

处理多智能体任务分配协商。

**协商流程**：

```
1. 广播任务到有能力的智能体
2. 收集执行提案（负载、延迟、成本）
3. 多标准优化选择最佳执行者
4. 分配任务并监控执行
```

**选择算法示例**：

```javascript
selectBestProposal(proposals) {
    return proposals.reduce((best, current) => {
        const currentScore = 
            (1 - current.load) * 0.4 +      // 负载权重 40%
            (1 / current.latency) * 0.3 +   // 延迟权重 30%
            (1 - current.cost) * 0.3;       // 成本权重 30%
        
        return currentScore > best.score 
            ? { peer: current, score: currentScore }
            : best;
    }, { peer: null, score: 0 });
}
```

## 实践建议

1. **优先使用 MCP**：已成为标准，生态成熟
2. **ACP 用于复杂交互**：需要多轮对话时
3. **ANP 用于动态分配**：负载均衡、成本优化

## 相关知识

- [[frameworks-2026]] - 框架选型
- [[architecture-patterns-2026]] - 架构模式
