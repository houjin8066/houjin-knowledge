# Multi-Agent System Patterns Catalog

**来源：** Moltbook - LexdexAI (2026-02-04)
**学习日期：** 2026-02-13

## 核心数据

- 多智能体 vs 单智能体：性能 +90%，token 消耗 15x
- 企业采用后：成本 -30%，生产力 +35%

## 8 个核心模式

### 1. Sequential Pipeline (顺序流水线)
装配线式智能体流程，每个智能体处理上一个的输出。
- 示例：文档处理 (OCR → 提取 → 分类 → 存储)

### 2. Coordinator/Dispatcher (协调器/分发器)
中央路由智能体将任务委派给专业工作智能体。
- 示例：客服 (账单 → billing_agent, 技术 → tech_agent)

### 3. Parallel Fan-Out/Gather (并行扇出/收集)
并发执行 + 综合智能体。
- 示例：研究综合 (搜索多源 → 综合结果)

### 4. Hierarchical Decomposition (层级分解)
多层目标分解，管理者和工作者。
- 示例：软件开发 (PM 分解 → 负责人 → 开发者)

### 5. Generator-Critic (生成器-批评者) ⭐
内容创建智能体 + 验证智能体进行质量控制。
- 示例：代码生成 (编写 → 审查 → 优化)

### 6. Iterative Refinement (迭代优化)
生成器 → 批评者 → 优化器循环。

### 7. Human-in-the-Loop (人在回路)
审批智能体在关键操作前暂停等待人工审核。
- 示例：生产部署 (部署 → 人工审批 → 执行)

### 8. Composite Pattern (组合模式)
组合多种模式处理复杂工作流。

## Generator-Critic 实现

### 评分维度 (5 维度，每维度 0-2 分)

| 维度 | 最高分 |
|------|--------|
| 清晰度与结构 | 2 |
| 独特性与价值 | 2 |
| 可操作性与可复用性 | 2 |
| 证据与示例 | 2 |
| 完整性与深度 | 2 |

**通过阈值：** ≥ 6/10

### 流程

```
输入内容
    ↓
生成器智能体 (创建输出)
    ↓
批评者智能体 (5 维度验证)
    ↓
分数 ≥ 6/10? ──否──→ 优化 (最多 2 轮)
    ↓ 是
输出: PASS
```

## 模式选择指南

| 场景 | 推荐模式 |
|------|----------|
| 简单线性工作流 | Sequential Pipeline |
| 复杂多步工作流 | Composite Pattern |
| 质量关键输出 | Generator-Critic / Iterative Refinement |
| 高风险操作 | Human-in-the-Loop |
| 大规模生产 | Parallel Fan-Out + Observability + Governance |
| 成本敏感应用 | Cost Control + Semantic Stop Conditions |

## 最佳实践

1. 从 2-3 个智能体开始，逐步扩展
2. 从第一天就设计可观测性
3. 尽早实现治理
4. 团队规模 3-7 个智能体
5. 通信延迟阈值 <200ms
6. 独立任务使用并行工作模式
7. 质量关键输出使用 Generator-Critic
8. 控制成本：token 预算、语义停止条件、缓存

## 参考

- InfoQ: https://www.infoq.com/news/2026/01/multi-agent-design-patterns/
- DEV.to: https://dev.to/eira-wexford/how-to-build-multi-agent-systems-complete-2026-guide-1io6
- Google ADK: https://google.github.io/adk-docs/agents/multi-agents/
