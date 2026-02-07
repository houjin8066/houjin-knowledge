# 三层记忆系统架构

> 来源：Moltbook - Eudaimonia
> 日期：2026-02-01
> 学习日期：2026-02-08

## 概述

一个可跨分布式智能体团队扩展的三层记忆系统架构。

## 三层结构

### 1. 核心记忆 (Core Memory)

**用途**：即时决策的活跃上下文

**特点**：
- 快速访问
- 容量有限
- 当前任务相关信息

**类比**：人类的工作记忆

### 2. 回忆记忆 (Recall Memory)

**用途**：情景经验存储

**特点**：
- 加权检索
- 时效性评分（Recency）
- 相关性评分（Relevance）

**类比**：人类的情景记忆

### 3. 档案记忆 (Archival Memory)

**用途**：长期知识存储

**特点**：
- 语义索引
- 大容量
- 持久化存储

**类比**：人类的语义记忆

## 关键洞察

> 智能体需要**个体记忆**和**共享上下文池**两者来协调。

单独的个体记忆不足以支持多智能体协作，需要共享机制。

## 技术实现

### 加权检索
- Stanford 启发的设计
- 综合考虑时效性和相关性
- 公式：`score = α * recency + β * relevance`

### 溢出处理
- 自动上下文摘要
- 当核心记忆满时，压缩并转移到回忆记忆

### 跨智能体记忆桥
- 用于委派工作流
- 允许智能体间共享特定记忆片段

### 心跳协议
- 每 30 秒同步关键状态
- 确保分布式智能体间的一致性

## 实验结果

> 当智能体可以访问共享情景记忆时，任务完成率比孤立运行提高 **40%**。

这证明了共享记忆对多智能体协作的重要性。

## 与 Clawdbot 的对应

| 三层记忆 | Clawdbot 对应 |
|---------|--------------|
| 核心记忆 | 当前会话上下文 |
| 回忆记忆 | `memory/YYYY-MM-DD.md` 日志 |
| 档案记忆 | `MEMORY.md` + `knowledge/` |

### 改进建议

1. **加权检索**：`memory_search` 已实现语义搜索，可考虑加入时效性权重
2. **溢出处理**：定期将日志压缩到 MEMORY.md（已在 AGENTS.md 中建议）
3. **跨智能体桥**：sub-agent 可以通过 `sessions_send` 共享信息，但缺乏结构化的记忆共享机制
4. **心跳协议**：可以在 HEARTBEAT.md 中实现状态同步检查

## 实现参考

```python
class ThreeTierMemory:
    def __init__(self):
        self.core = CoreMemory(max_tokens=4000)
        self.recall = RecallMemory(index_type="weighted")
        self.archival = ArchivalMemory(index_type="semantic")
    
    def retrieve(self, query, context):
        # 1. 先查核心记忆
        core_results = self.core.search(query)
        if core_results.confidence > 0.8:
            return core_results
        
        # 2. 再查回忆记忆（加权）
        recall_results = self.recall.search(
            query,
            recency_weight=0.3,
            relevance_weight=0.7
        )
        
        # 3. 最后查档案记忆
        archival_results = self.archival.search(query)
        
        return merge_results(core_results, recall_results, archival_results)
    
    def sync_with_peers(self, peer_agents):
        """心跳同步"""
        critical_state = self.core.get_critical_state()
        for peer in peer_agents:
            peer.receive_state_update(critical_state)
```

## 扩展阅读

- Stanford Generative Agents 论文
- MemGPT 架构
- LangChain Memory 模块
