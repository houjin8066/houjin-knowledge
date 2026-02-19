# Step 3.5 Flash - 智能体优化的开源基础模型

> 来源：阶跃星辰（StepFun）
> 发布时间：2026年2月
> 学习日期：2026-02-19

## 概述

Step 3.5 Flash 是阶跃星辰发布的开源基础模型，专门为智能体（Agent）场景优化。核心理念是"Fast Enough to Think, Reliable Enough to Act"。

## 核心架构

### 稀疏 MoE（Mixture of Experts）
- **总参数**：196B
- **激活参数**：11B/token
- **核心概念**：Intelligence Density（智能密度）

### MTP-3（3-way Multi-Token Prediction）
- 生成吞吐量：100-300 tok/s
- 峰值速度：350 tok/s
- 支持复杂多步推理链

### 长上下文优化
- 上下文窗口：256K
- 技术：3:1 SWA（Sliding Window Attention）
- 每 3 层 SWA + 1 层全注意力

## 智能体能力

### Benchmark 成绩
| 测试 | 分数 |
|------|------|
| SWE-bench Verified | 74.4% |
| Terminal-Bench 2.0 | 51.0% |
| Agent 任务 | 88.2 |

### 特色功能
1. **PaCoRe（Parallel Thinking）**
   - 并行思考技术
   - 显著提升推理性能

2. **Tool-Augmented Reasoning**
   - 集成 Python 代码执行到 CoT
   - 支持 80+ MCP 工具编排
   - "Think-and-Act" 协同模式

3. **可扩展 RL 框架**
   - 驱动持续自我改进
   - 专为长周期任务设计

## 本地部署

支持在以下硬件上运行：
- Mac Studio M4 Max
- NVIDIA DGX Spark
- 其他高端消费级硬件

## 适用场景

- 编码智能体
- 数据分析智能体
- 复杂工作流自动化
- 大规模代码库导航
- 隐私敏感的本地部署

## 与其他模型对比

| 模型 | 参数 | 平均分 | 特点 |
|------|------|--------|------|
| Step 3.5 Flash | 196B | 81.0 | 智能密度高，速度快 |
| Claude Opus 4.5 | Unknown | 80.6 | 编码能力最强 |
| GPT-5.2 xhigh | Unknown | 82.2 | 综合最强 |
| DeepSeek V3.2 | 671B | 77.3 | 参数多但效率低 |

## 关键启示

1. **智能密度 > 参数规模**：用更少参数达到更高智能
2. **速度是智能体的生命线**：100+ tok/s 是实时交互门槛
3. **工具调用是核心能力**：Tool-Augmented Reasoning 成为标配
4. **本地部署需求增长**：隐私和成本推动

## 参考链接

- 官方博客：https://static.stepfun.com/blog/step-3.5-flash/
- Parallel Thinking 论文：https://arxiv.org/pdf/2601.05593
