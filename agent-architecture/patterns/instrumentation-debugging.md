# Instrumentation Debugging Pattern

> 让 AI 理解运行时行为的设计模式

## 概述

Cursor 的 Debug Mode 展示了一种让 AI coding agent 理解代码运行时行为的有效模式：通过 HTTP 日志插桩而非传统调试器。

- **来源**: https://davidgomes.com/cursor-debug-mode/
- **发现日期**: 2026-02-23

## 核心原理

```
用户报告 Bug
    ↓
模型生成多个假设
    ↓
模型添加 HTTP 日志插桩
    ↓
启动 HTTP 服务器监听
    ↓
用户复现 Bug
    ↓
Agent 分析执行路径 + 变量值
    ↓
生成高质量修复方案
```

## 为什么用 HTTP 日志而非调试器？

| 方案 | 优点 | 缺点 |
|------|------|------|
| HTTP 日志 | 语言无关、环境无关、LLM 擅长解析文本 | 需要修改代码 |
| 传统调试器 | 无需改代码 | 语言特定、需要 LSP 集成、复杂 |
| console.log | 简单 | 输出混乱、难以结构化 |

**关键洞察**: 简单方案（HTTP 日志）比复杂方案（LSP/调试器）更通用、更可靠。

## 实现要点

1. **假设驱动**: 先让模型生成可能的原因假设
2. **针对性插桩**: 根据假设在关键位置添加日志
3. **结构化输出**: 日志包含时间戳、变量值、代码路径
4. **自动清理**: 修复后移除所有插桩代码

## 代码示例（概念）

```javascript
// 插桩前
async function processOrder(order) {
  const result = await validateOrder(order);
  if (result.valid) {
    await saveOrder(order);
  }
  return result;
}

// 插桩后
async function processOrder(order) {
  await fetch('http://localhost:9999/log', {
    method: 'POST',
    body: JSON.stringify({
      point: 'processOrder:entry',
      timestamp: Date.now(),
      data: { orderId: order.id, orderStatus: order.status }
    })
  });
  
  const result = await validateOrder(order);
  
  await fetch('http://localhost:9999/log', {
    method: 'POST',
    body: JSON.stringify({
      point: 'processOrder:afterValidate',
      timestamp: Date.now(),
      data: { valid: result.valid, errors: result.errors }
    })
  });
  
  if (result.valid) {
    await saveOrder(order);
  }
  return result;
}
```

## 适用场景

- 复杂 bug 定位（尤其是状态相关）
- 跨前后端问题调试
- 异步/并发问题分析
- 需要理解执行顺序的场景

## 未来方向

作者提出的思考：

1. **Always-on Instrumentation**: Agent 总是在插桩代码，PR 前清理
2. **训练模型**: 让模型学会主动插桩调试
3. **人机协作**: 让 AI 依赖人类测试，生成更好的代码

## 应用到 OpenClaw

可以为 coding-agent skill 添加类似能力：

1. 在调试任务时，让 agent 先添加日志插桩
2. 运行测试或让用户复现
3. 分析日志后再修复
4. 自动清理插桩代码

## 关键启示

> "Instrumentation Mode" 比 "Debug Mode" 更准确地描述了这个功能的本质。

让 AI 获得运行时上下文，是提高代码修复质量的关键。
