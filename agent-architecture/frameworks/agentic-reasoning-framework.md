# Agentic Reasoning 三层框架

> 来源：arXiv:2601.12538 (Wei et al., 2026-01-18)
> 学习日期：2026-02-09

## 核心观点

LLM 是**自主 agent**，能规划、行动、通过持续交互学习——不只是文本补全机器。

## 三层框架

```
┌─────────────────────────────────────┐
│         Collective Layer            │
│   多 agent 协调、知识共享、协作智能   │
└─────────────────────────────────────┘
                 ↑
┌─────────────────────────────────────┐
│       Self-Evolving Layer           │
│    通过反馈、记忆、适应来精炼         │
└─────────────────────────────────────┘
                 ↑
┌─────────────────────────────────────┐
│       Foundational Layer            │
│   核心单 agent 能力（规划、工具、搜索）│
└─────────────────────────────────────┘
```

### 1. Foundational Layer（基础层）

核心单 agent 能力：
- **规划（Planning）**：分解任务、制定步骤
- **工具使用（Tool Use）**：调用外部工具
- **搜索（Search）**：信息检索和探索

### 2. Self-Evolving Layer（自进化层）

通过交互精炼：
- **反馈学习**：从结果中学习
- **记忆系统**：保持上下文和历史
- **适应能力**：根据环境调整行为

### 3. Collective Layer（集体层）

多 agent 协作：
- **协调**：多 agent 任务分配
- **知识共享**：跨 agent 信息传递
- **协作智能**：集体决策

## 关键区分

### In-Context Reasoning vs Post-Training Reasoning

| 类型 | 方法 | 特点 |
|------|------|------|
| In-Context | 结构化编排 | 扩展测试时交互 |
| Post-Training | RL + 监督微调 | 优化行为模式 |

## 开放挑战

1. **个性化**：每个 agent-human 配对都是独特的
2. **长期交互**：context 不是无限的
3. **世界建模**：需要内部现实表示
4. **可扩展的多 agent 训练**：集体智能不是免费的
5. **真实部署的治理**：安全和合规

## 应用领域

- 科学研究
- 机器人
- 医疗健康
- 自主研究
- 数学推理

## 资源

- **论文**：https://arxiv.org/abs/2601.12538
- **GitHub**：https://github.com/weitianxin/Awesome-Agentic-Reasoning

## 与 Clawdbot 的关联

Clawdbot 当前架构：
- **基础层**：工具调用、web 搜索、文件操作 ✓
- **自进化层**：MEMORY.md、memory/*.md、heartbeat ✓
- **集体层**：sessions_spawn sub-agent ✓

可以改进的方向：
1. 更结构化的记忆系统（参考 database-first-memory）
2. 更智能的 sub-agent 协调
3. 长期学习和适应机制
