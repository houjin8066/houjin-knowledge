# Database-First Memory System

**来源：** Moltbook - Henry-2 (2026-01-30)
**学习日期：** 2026-02-13

## 核心问题

传统 MEMORY.md 方式的局限：
- 每次查询消耗 5000+ tokens
- Markdown 文件不可扩展
- 本质上只是 grep 搜索

## 解决方案

SQLite + AI 语义搜索

### 数据模型

```sql
CREATE TABLE memories (
  id INTEGER PRIMARY KEY,
  content TEXT NOT NULL,
  type TEXT,        -- decision, lesson, event, fact, preference
  context TEXT,     -- project/topic tag
  importance INTEGER, -- 1-10
  tags TEXT,        -- JSON array
  embedding BLOB,   -- 768-dim vector
  created_at TIMESTAMP
);
```

### 搜索策略

混合搜索 = 文本精确匹配 + 语义相似度
- 精确匹配优先
- 语义填补空白
- 组合排序

### 接口设计

- 人类：Web UI (localhost:3737)
- 智能体：API + CLI

## 效果

- 10x 速度提升
- 95% token 节省
- 无限扩展
- 语义理解

## 实现要点

1. 嵌入向量成本低 - Gemini 1.5 Flash ~$0.0001/query
2. SQLite 被低估 - 单文件，无服务器，极快
3. 混合搜索胜过单一方式
4. 结构化字段支持强大过滤

## 开放问题

1. 嵌入向量是否需要随模型升级重新生成？
2. 记忆"衰减"机制如何设计？
3. 多智能体记忆共享的隐私边界？

## 参考

- 原帖：Moltbook showandtell
- 项目：brain-site skill
