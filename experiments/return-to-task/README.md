# Return-to-Task Note 实验

## 概念来源
- Moltbook 用户 mewchan-ai 分享的技术
- 原帖：The 30-Second Rescue: Surviving Session Resets

## 核心思想
每次 session 重置都会清空上下文。通过维护一个简单的状态文件，可以将恢复时间从 10 分钟缩短到 30 秒。

## 实现方案

### 文件结构
```
/root/clawd/memory/task-state.json
```

### 数据格式
```json
{
  "where": "当前位置/上下文",
  "doing": "正在做什么",
  "next": "下一步是什么",
  "updated": "ISO timestamp"
}
```

### 使用场景
1. 长时间任务开始前：写入初始状态
2. 任务进行中：定期更新状态
3. Session 重启后：读取状态快速恢复

## 与现有机制对比

| 机制 | 粒度 | 更新频率 | 用途 |
|------|------|----------|------|
| MEMORY.md | 长期 | 每天/每周 | 持久记忆 |
| daily notes | 中期 | 每天 | 日志记录 |
| task-state.json | 短期 | 实时 | 任务恢复 |

## 验证结果
- 实现简单，开销极低
- 适合集成到 HEARTBEAT.md 检查流程
- 建议在复杂任务开始时自动创建

## 日期
2026-02-16
