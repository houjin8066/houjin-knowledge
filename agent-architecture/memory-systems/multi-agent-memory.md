# 多智能体记忆系统设计

> 来源：Moltbook 帖子 by @Eudaimonia (2026-02-01)
> 整理时间：2026-02-06

## 概述

分布式智能体团队需要精心设计的记忆系统来实现有效协作。核心洞察：智能体既需要独立记忆，也需要共享的上下文池来协调。

## 三层记忆架构

```
┌─────────────────────────────────────────┐
│           Archival Memory               │
│    长期知识，语义索引                    │
│    (Long-term knowledge, semantic index) │
├─────────────────────────────────────────┤
│           Recall Memory                 │
│    情景经验，加权检索                    │
│    (Episodic experiences, weighted)      │
├─────────────────────────────────────────┤
│           Core Memory                   │
│    活跃上下文，即时决策                  │
│    (Active context, immediate decisions) │
└─────────────────────────────────────────┘
```

### 1. Core Memory (核心记忆)
- **功能**：活跃上下文，用于即时决策
- **特点**：快速访问，容量有限
- **类比**：工作记忆 (Working Memory)

### 2. Recall Memory (回忆记忆)
- **功能**：情景经验存储
- **特点**：加权检索（recency + relevance）
- **类比**：情景记忆 (Episodic Memory)

### 3. Archival Memory (归档记忆)
- **功能**：长期知识存储
- **特点**：语义索引，持久化
- **类比**：语义记忆 (Semantic Memory)

---

## 关键设计要素

### 个体记忆 + 共享上下文池

```
┌──────────┐    ┌──────────┐    ┌──────────┐
│ Agent A  │    │ Agent B  │    │ Agent C  │
│ Memory   │    │ Memory   │    │ Memory   │
└────┬─────┘    └────┬─────┘    └────┬─────┘
     │               │               │
     └───────────────┼───────────────┘
                     │
              ┌──────┴──────┐
              │   Shared    │
              │ Context Pool│
              └─────────────┘
```

- 每个智能体维护独立记忆
- 共享上下文池用于协调
- 心跳协议同步关键状态

### 心跳同步协议

- **频率**：每 30 秒
- **内容**：关键状态同步
- **效果**：共享情景记忆比孤立运行提升 **40% 任务完成率**

---

## 技术实现

### 加权检索 (Stanford-inspired)

```python
score = α * recency_score + β * relevance_score
```

- **recency_score**：时间衰减，近期记忆权重更高
- **relevance_score**：语义相似度

### 溢出处理

当 Core Memory 容量不足时：
1. 自动上下文摘要
2. 重要信息迁移到 Recall Memory
3. 低优先级信息归档到 Archival Memory

### 跨智能体记忆桥

用于委托工作流：
- Agent A 将任务上下文传递给 Agent B
- 包含必要的历史记忆片段
- 保持任务连续性

---

## 与 Clawdbot 的关联

### 当前架构
- `MEMORY.md` → 类似 Archival Memory
- `memory/YYYY-MM-DD.md` → 类似 Recall Memory
- 对话上下文 → 类似 Core Memory

### 改进方向
1. 引入加权检索机制
2. 设计 sub-agent 间的记忆共享协议
3. 实现自动上下文摘要

---

## 实践案例：Polycat 的记忆系统

**技术栈**：
- Flat files + Honcho
- 自托管 + Ollama 本地嵌入
- 无外部 API 调用

**优点**：
- 完全本地化，隐私安全
- 低延迟
- 可控性强

---

## 参考资料

- Moltbook: Multi-Agent Memory Architecture for Complex Workflows
- Stanford: Generative Agents (Park et al.)
- Honcho: https://github.com/plastic-labs/honcho
