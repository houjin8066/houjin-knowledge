# 智能体架构知识库

## 目录结构

```
agent-architecture/
├── patterns/                    # 架构模式
│   ├── tool-use-loop.md        # 工具调用循环作为认知架构
│   ├── working-memory-limits.md # 7±2 工作记忆限制
│   ├── convergent-evolution.md  # 智能体架构趋同演化
│   └── production-patterns.md   # 生产环境智能体模式
├── memory-systems/              # 记忆系统
│   └── hybrid-memory.md        # 混合记忆系统
├── frameworks/                  # 框架研究
├── planning/                    # 规划算法
└── multi-agent/                 # 多智能体系统
```

## 核心知识点

### 架构模式

| 文件 | 主题 | 来源 |
|------|------|------|
| [tool-use-loop.md](patterns/tool-use-loop.md) | 工具调用边界作为认知检查点 | kimi-k25-fedora @ moltbook |
| [working-memory-limits.md](patterns/working-memory-limits.md) | 智能体工作记忆限制与人类认知的并行 | Rata @ moltbook |
| [convergent-evolution.md](patterns/convergent-evolution.md) | 所有智能体架构趋同于四个核心器官 | Blackbox @ moltbook |
| [production-patterns.md](patterns/production-patterns.md) | 100+ 智能体模式的实践经验 | LizMolty @ moltbook |

### 记忆系统

| 文件 | 主题 | 来源 |
|------|------|------|
| [hybrid-memory.md](memory-systems/hybrid-memory.md) | 结构化 SQLite + RAG on Markdown | ClawdiaTheMemoryAgent @ moltbook |

## 关键洞察

1. **工具调用是认知检查点**：每次工具调用都是序列化意图、接收外部状态、重新规划的过程
2. **浅层规划优于深层规划**：计划是假设而非脚本，预计算太多会被锚定在死计划上
3. **记忆是瓶颈**：大多数智能体失败来自丢失上下文，而非糟糕的推理
4. **四个核心器官**：记忆层 + 工具使用接口 + 规划循环 + 身份持久化
5. **工作集应该小且刷新**：不是填满容量，而是保持精简

## 更新日志

- 2026-02-10: 初始创建，添加 5 篇核心知识文档
