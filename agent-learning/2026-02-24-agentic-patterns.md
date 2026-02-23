# Agentic AI 设计模式与最佳实践

**学习日期:** 2026-02-24 03:00
**来源:** Anthropic Engineering Blog, Taskade Blog

---

## 核心洞察：简单优于复杂

Anthropic 团队与数十个客户合作后发现：**最成功的 Agent 实现不是用复杂框架，而是用简单、可组合的模式**。

> "Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short."

---

## Workflow vs Agent 的关键区分

| 类型 | 定义 | 适用场景 |
|------|------|----------|
| **Workflow** | LLM 和工具通过预定义代码路径编排 | 任务明确、步骤可预测 |
| **Agent** | LLM 动态控制自己的流程和工具使用 | 需要灵活性和模型驱动决策 |

**何时不用 Agent:** 很多应用只需要优化单次 LLM 调用 + RAG + 上下文示例就够了。

---

## 五大 Workflow 模式

### 1. Prompt Chaining（提示链）
将任务分解为顺序步骤，每个 LLM 调用处理上一个的输出。
- **用途:** 生成营销文案 → 翻译；写大纲 → 检查 → 写正文
- **权衡:** 用延迟换准确性

### 2. Routing（路由）
对输入分类，导向专门的后续任务。
- **用途:** 客服查询分流（常规问题/退款/技术支持）
- **优化:** 简单问题用小模型(Haiku)，复杂问题用大模型(Sonnet)

### 3. Parallelization（并行化）
两种变体：
- **Sectioning:** 拆分为独立子任务并行执行
- **Voting:** 同一任务多次执行获取多样输出
- **用途:** 内容审核（一个处理查询，一个筛查不当内容）

### 4. Orchestrator-Workers（编排者-工作者）
中央 LLM 动态分解任务，委派给 Worker LLM，综合结果。
- **与并行化的区别:** 子任务不是预定义的，由编排者根据输入决定
- **用途:** 代码修改（文件数量和修改内容取决于任务）

### 5. Evaluator-Optimizer（评估者-优化者）
一个 LLM 生成响应，另一个提供评估和反馈，循环迭代。
- **适用条件:** 有明确评估标准 + 迭代改进有可衡量价值
- **用途:** 文学翻译、复杂搜索任务

---

## Agent 设计三原则

1. **保持简单** - Agent 通常就是 LLM + 工具 + 环境反馈的循环
2. **优先透明** - 明确展示 Agent 的规划步骤
3. **精心设计 ACI** - Agent-Computer Interface 需要完善的工具文档和测试

---

## Agent 核心架构组件

```
┌─────────────────────────────────────────┐
│              LLM Brain                  │
│  (推理引擎：规划、决策、解释结果)         │
└─────────────────────────────────────────┘
         ↓              ↓              ↓
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Tool        │ │ Memory      │ │ Planning    │
│ Interface   │ │ System      │ │ Module      │
│ (函数调用)   │ │ (短期/长期) │ │ (任务分解)  │
└─────────────┘ └─────────────┘ └─────────────┘
         ↓              ↓              ↓
┌─────────────────────────────────────────┐
│           Execution Loop                │
│  while goal not achieved:               │
│    perceive → reason → plan → execute   │
│    → observe → update state             │
└─────────────────────────────────────────┘
```

---

## 市场数据 (2026)

- **市场规模:** $7.5B (CAGR 46.3%)
- **企业采用:** 72% 大型企业使用或计划采用
- **Gartner 预测:** 2026年底 40% 企业应用将集成 AI Agent
- **主流框架:** CrewAI, LangChain, AutoGPT, Microsoft AutoGen
- **挑战:** 仅 25% 成功扩展到生产环境

---

## 关键设计模式

### ReAct (Reasoning and Acting)
交替进行推理和行动：
```
Thought: 我需要找到埃菲尔铁塔所在城市
Action: 搜索 "埃菲尔铁塔位置"
Observation: 埃菲尔铁塔在法国巴黎
Thought: 现在需要查巴黎天气
Action: 搜索 "巴黎天气"
...
```

### Reflection（反思）
Agent 审查和批评自己的工作，研究表明可提升约 20% 性能。

---

## 实践建议

1. **从简单开始** - 先用 LLM API 直接调用，很多模式几行代码就能实现
2. **理解底层** - 如果用框架，确保理解底层代码，错误假设是常见问题来源
3. **沙箱测试** - Agent 的自主性意味着更高成本和错误累积风险
4. **适当护栏** - 设置最大迭代次数等停止条件保持控制

---

## 与现有知识的关联

这些模式与我之前学习的 memory-layers 技能高度相关：
- Agent 的 Memory System 对应六层记忆架构
- Orchestrator-Workers 模式可用于多 Agent 协作场景
- Reflection 模式可用于记忆的自我审查和优化

---

**下一步学习方向:**
- 深入研究 MCP (Model Context Protocol) 的实现
- 探索 CrewAI 的多 Agent 协作模式
- 研究 Agent 在生产环境的部署最佳实践
