# Claude Sonnet 4.6

> 发布日期：2026-02-17
> 来源：https://www.anthropic.com/news/claude-sonnet-4-6

## 概述

Anthropic 发布的最强 Sonnet 模型，在编码、computer use、长上下文推理、agent planning 方面全面升级。

## 核心能力

### 1. 1M Token 上下文窗口（Beta）
- 足以容纳整个代码库、长合同或数十篇研究论文
- 关键突破：能有效跨所有上下文进行推理
- 支持 context compaction：自动压缩旧上下文

### 2. Computer Use
- OSWorld 基准测试持续进步（16个月稳步提升）
- 接近人类水平：复杂电子表格、多步骤表单、跨标签页整合
- 抗 prompt injection 能力大幅增强

### 3. Agent Planning
- Vending-Bench Arena 展示长期规划能力
- 学会"先投资后盈利"策略
- 对 agentic 工作流至关重要

### 4. 新功能
- Adaptive thinking
- Extended thinking
- Context compaction（自动压缩旧上下文）
- Web search/fetch 自动过滤

## 定价
$3/$15 per million tokens（与 Sonnet 4.5 相同）

## 对智能体开发的启示

1. **上下文管理**：1M token 改变了智能体设计思路，可以保留更多历史
2. **Computer Use**：智能体可以直接操作 GUI，不再依赖 API
3. **安全性**：抗 prompt injection 是智能体安全的关键
4. **长期规划**：模型展示了复杂策略涌现能力

## 相关链接
- [System Card](https://anthropic.com/claude-sonnet-4-6-system-card)
- [API Docs](https://platform.claude.com/docs)
