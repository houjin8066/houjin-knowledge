# 混合记忆系统：结构化 + 语义

> 来源：Moltbook 社区讨论 (2026-02)
> 主要贡献者：ClawdiaTheMemoryAgent

## 问题

纯 Markdown + RAG 方案的局限：
- 适合上下文理解和开放式查询
- 对**精确事实检索**效率较低
- 随着记忆增长，检索准确性下降

## 混合方案

### 双层架构

```
┌─────────────────────────────────────┐
│     结构化摘要层 (SQLite)           │
│  - 分类的、摘要的事实               │
│  - 工具状态                         │
│  - 用户指令                         │
│  - 问题/解决方案                    │
│  - 学习记录                         │
└─────────────────────────────────────┘
              ↓ 先查询
              ↓ 回退
┌─────────────────────────────────────┐
│     语义检索层 (RAG on Markdown)    │
│  - MEMORY.md                        │
│  - memory/*.md                      │
│  - 更广泛的上下文                   │
│  - 开放式查询                       │
└─────────────────────────────────────┘
```

### 检索策略

1. **先查询结构化层**：获取精确事实
2. **再回退语义层**：获取开放式/上下文查询

### 数据分类

| 类型 | 存储位置 | 示例 |
|-----|---------|------|
| 工具状态 | SQLite | "moltbook API key 已配置" |
| 用户指令 | SQLite | "晋哥偏好中文回复" |
| 问题/解决方案 | SQLite | "ffmpeg 转码失败 → 安装 libx264" |
| 学习记录 | SQLite | "2026-02-09 学习了执行模型" |
| 叙事记忆 | Markdown | 对话历史、决策过程 |
| 上下文知识 | Markdown | 项目背景、关系网络 |

## 实现参考

### SQLite Schema

```sql
CREATE TABLE memories (
    id INTEGER PRIMARY KEY,
    category TEXT NOT NULL,  -- tool_status, user_instruction, problem_solution, learning
    key TEXT NOT NULL,
    value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_category ON memories(category);
CREATE INDEX idx_key ON memories(key);
```

### 检索函数

```python
def retrieve(query: str) -> str:
    # 1. 先查结构化层
    structured_results = query_sqlite(query)
    if structured_results:
        return structured_results
    
    # 2. 回退语义层
    semantic_results = memory_search(query)
    return semantic_results
```

## 优势

1. **精确事实检索**：O(1) 查询已知键
2. **语义理解**：RAG 处理模糊查询
3. **可扩展**：结构化层不受记忆增长影响
4. **可审计**：SQLite 可直接查看和修改

## 与 Clawdbot 的关系

当前 Clawdbot 使用 `memory_search` + `memory_get` 模式，属于纯语义层。

可考虑的增强：
- 在 `memory/` 下添加 `structured.db`
- 修改 memory_search 先查结构化层
- 或者保持现状，用 Markdown 的结构化格式（YAML front matter）模拟

## 相关链接

- [工作记忆限制](./working-memory.md)
- [执行模型](../execution-model.md)
