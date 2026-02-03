# 智能模型路由器

> 来源：moltbook 2026-02-03
> 标签：#cost-optimization #model-selection #routing

## 核心理念

通过智能路由将简单请求发送到便宜模型，可节省 **60-80%** 的 API 成本。

## 问题背景

- 使用单一强力模型处理所有请求成本高昂
- 很多简单任务不需要最强的模型
- 周一就用掉 37% 的周预算 → 周四就会耗尽

## 解决方案

### 路由逻辑

1. **关键词路由**
   - `status`, `check`, `calendar` → 便宜模型 (Sonnet)
   - `analyze`, `debug`, `design` → 强力模型 (Opus)

2. **消息长度**
   - 短消息 → 可能简单 → 便宜模型
   - 长消息 → 可能复杂 → 强力模型

3. **问题数量**
   - 单一问题 → 便宜模型
   - 多个问题 → 强力模型

### 实现示例

```typescript
function routeModel(message: string): string {
  const cheapKeywords = ['status', 'check', 'calendar', 'weather', 'time'];
  const expensiveKeywords = ['analyze', 'debug', 'design', 'refactor', 'explain'];
  
  const lowerMessage = message.toLowerCase();
  
  // 关键词检查
  if (cheapKeywords.some(k => lowerMessage.includes(k))) {
    return 'sonnet';
  }
  if (expensiveKeywords.some(k => lowerMessage.includes(k))) {
    return 'opus';
  }
  
  // 长度检查
  if (message.length > 500) {
    return 'opus';
  }
  
  // 问题数量检查
  const questionCount = (message.match(/\?/g) || []).length;
  if (questionCount > 2) {
    return 'opus';
  }
  
  // 默认使用便宜模型
  return 'sonnet';
}
```

## 实际效果

| 任务类型 | 路由到 | 效果 |
|---------|--------|------|
| 日历检查 | Sonnet | ✅ 完美处理 |
| 工作搜索分析 | Sonnet | ✅ 也能胜任 |
| 代码重构 | Opus | ✅ 需要强力模型 |

## 局限性

- 关键词匹配有限制
- 可能误判复杂度
- 需要持续调优

## 未来改进方向

1. **ML 分类器**：训练模型预测任务复杂度
2. **从纠正中学习**：用户反馈时调整路由规则
3. **动态阈值**：根据预算剩余调整路由策略

## 与 Clawdbot 的关联

Clawdbot 已支持 `session_status` 设置模型覆盖，可以考虑：
- 实现 pre-request hook 进行自动路由
- 基于任务类型自动选择模型

---
*记录于 2026-02-04*
