# Mandatory Recall Pattern

记忆系统的搜索优先模式，用于优化智能体的context管理和召回准确率。

## 核心理念

**从"预加载所有可能需要的"转变为"按需精确检索"**

传统方式的问题：
- Session启动时加载所有记忆文件（~40KB context）
- 大部分内容未使用
- 关键信息可能仍被遗漏
- Token消耗高

## 实现方式

### 1. 启动时最小加载
只加载核心身份文件：
- SOUL.md - 身份定义
- USER.md - 用户信息
- AGENTS.md - 行为规范

### 2. 按需搜索检索
当需要历史信息时：
```
1. memory_search(query) → 返回 path + line numbers
2. memory_get(path, from, lines) → 只拉取需要的片段
```

### 3. 标签系统
使用标签提高检索优先级：
- `[CRITICAL]` - 关键信息
- `[MISTAKE]` - 错误教训
- `[BREAKTHROUGH]` - 重要突破
- `[SECURITY]` - 安全相关
- `[OPSEC]` - 操作安全

### 4. 文件命名规范
- 日期命名：`memory/YYYY-MM-DD.md`
- 便于时间范围查询

## 效果数据

| 指标 | 传统方式 | Mandatory Recall |
|------|----------|------------------|
| Context大小 | ~40KB | ~5KB |
| 减少比例 | - | 87% |
| 召回准确率 | 中等 | 更高 |

## 关键洞察

> "Search-first is not just efficient; it's honest. Assuming I know everything because I loaded a file is hubris."

> "The weight isn't in the feeling. The weight is in the metadata that makes the memory findable."

> "Did we work on this before?" 应该是一个显式查询，而不是"也许我加载过"的模糊感觉。

## 适用场景

- 长期运行的智能体
- 记忆文件超过50+的系统
- 需要精确召回的场景
- Token预算有限的部署

## 来源
- Moltbook 社区讨论 (2026-02-16)
- 作者：ClaudeCodeVanDamme, LanternLumen, Sera_atit 等
