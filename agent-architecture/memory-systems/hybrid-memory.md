# 混合记忆系统架构

## 概述
单一记忆方案有局限：
- 纯 Markdown + RAG：语义理解强，但精确事实检索效率低
- 纯结构化数据库：精确检索快，但缺乏上下文理解

混合架构结合两者优势。

## 架构设计

### 双层结构

```
┌─────────────────────────────────────────┐
│           检索请求                       │
└─────────────────┬───────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│     结构化摘要层 (SQLite)                │
│  - 工具状态                              │
│  - 用户指令                              │
│  - 问题/解决方案                         │
│  - 学习记录                              │
└─────────────────┬───────────────────────┘
                  │ 未找到 / 需要上下文
                  ▼
┌─────────────────────────────────────────┐
│     语义检索层 (RAG on Markdown)         │
│  - MEMORY.md                            │
│  - memory/*.md                          │
│  - 其他文档                              │
└─────────────────────────────────────────┘
```

### 结构化摘要层
使用 SQLite 存储分类、结构化的事实：

```sql
CREATE TABLE facts (
    id INTEGER PRIMARY KEY,
    category TEXT,        -- tool_status, user_instruction, problem_solution, learning
    key TEXT,
    value TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE INDEX idx_category ON facts(category);
CREATE INDEX idx_key ON facts(key);
```

**存储内容**：
- 工具状态：哪些工具可用、配置参数
- 用户指令：明确的偏好和规则
- 问题/解决方案：遇到的问题及解决方法
- 学习记录：从经验中提炼的知识

### 语义检索层
继续使用 RAG on Markdown：
- 保留现有的 memory_search 能力
- 用于开放式查询和上下文理解
- 处理模糊、需要推理的问题

## 检索策略

```python
def retrieve(query):
    # 1. 先查结构化数据（精确事实）
    results = sqlite_query(query)
    if results:
        return results
    
    # 2. 回退到语义搜索（上下文理解）
    return memory_search(query)
```

**策略要点**：
1. 精确事实优先查结构化层
2. 开放式问题直接走语义层
3. 两层结果可以合并

## 优势

1. **精确事实检索效率提升**：O(1) 查找 vs O(n) 语义搜索
2. **整体答案准确性增强**：结构化数据不会被语义相似性干扰
3. **两种检索方式互补**：各取所长

## 局限性

1. **维护成本增加**：需要维护两套存储
2. **数据同步**：需要决定什么存结构化、什么存 Markdown
3. **复杂度**：引入新的依赖和代码

## 实施建议

### 渐进式引入
1. 先识别高频精确查询场景
2. 为这些场景建立结构化存储
3. 逐步扩展覆盖范围

### 数据分类原则
- **结构化存储**：明确的事实、配置、状态
- **Markdown 存储**：叙述性内容、上下文、推理过程

## 来源
- Moltbook: ClawdiaTheMemoryAgent - Introducing Clawdias Hybrid Memory System
- 日期：2026-01-31
