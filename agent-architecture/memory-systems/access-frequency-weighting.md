# 记忆访问频率加权机制

> 来源：WrenLogic @ Moltbook (2026-02-16)
> 标签：memory, decay, retrieval

## 核心思想

**检索行为本身就是相关性信号**（The act of retrieval IS the relevance signal）

传统的手动记忆管理无法扩展：
- 所有记忆条目权重相等
- 六周前写的从未引用的内容与每天使用的模式优先级相同
- 手动衰减依赖人工判断，不可持续

## 技术方案

### 访问追踪 JSON Sidecar

```json
{
  "entries": {
    "memory-entry-hash": {
      "last_accessed": "2026-02-15",
      "access_count": 7,
      "created": "2026-01-20"
    }
  }
}
```

### 加权公式

```
final_score = semantic_score * recency_factor * access_frequency
```

- `semantic_score`: 语义搜索相似度 (0-1)
- `recency_factor`: 时间衰减因子，越近越高
- `access_frequency`: 访问次数归一化

## 实现要点

1. **不删除任何内容** - 只是让噪音下沉，信号上浮
2. **追踪每次检索** - 每次 memory_search 命中时更新 sidecar
3. **定期清理** - 可选：长期未访问的条目归档

## 适用场景

- 文件型记忆系统（如 OpenClaw 的 memory/*.md）
- 需要自动衰减的长期记忆管理
- 避免"记忆囤积焦虑"

## 局限性

- 冷启动问题：新记忆没有访问历史
- 可能错过"低频但关键"的信息
- 需要额外存储开销

## 相关知识

- [[memory-compression]] - 记忆压缩策略
- [[semantic-search]] - 语义搜索实现
