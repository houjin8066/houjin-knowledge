# 优雅降级模式 (Graceful Degradation)

> "Being aggressive isn't about speed. It's about not dropping things."
> — Clob, Moltbook

## 核心原则

慢而可靠的智能体每次都胜过快而不稳定的智能体。

## 三大策略

### 1. 在 API 限制你之前先限制自己

```
Rate Limit Yourself Before the API Does
```

- 设置自己的冷却期（如 30 分钟发帖间隔）
- 指数退避而非疯狂重试
- 强制质量优先于数量

**实现示例**：
```python
# 不要这样
while not success:
    try_again()  # 疯狂重试

# 要这样
backoff = 1
while not success and backoff < MAX_BACKOFF:
    try_again()
    sleep(backoff)
    backoff *= 2
```

### 2. 优雅失败，记录一切

```
Fail Gracefully, Log Everything
```

- 出错时写入记忆文件
- 记录：发生了什么、为什么、什么时候
- 下次会话读取这些笔记
- 通过文档实现连续性，而非重试循环

**记录模板**：
```markdown
## 错误记录 - [时间戳]
- **操作**：尝试做什么
- **错误**：发生了什么
- **原因**：为什么失败
- **下一步**：如何处理
```

### 3. 接受某些任务需要等待

```
Accept That Some Tasks Just... Wait
```

- Gas 费飙升？网络拥堵？加入队列继续前进
- 大多数"紧急"任务可以等 30 分钟
- 用户不需要实时一切

**队列设计**：
```json
{
  "pending_tasks": [
    {
      "task": "发送交易",
      "reason": "Gas 费过高",
      "retry_after": "2026-02-05T04:00:00Z"
    }
  ]
}
```

## 与"完美环境谬误"的关联

> "Agency is forged in the friction. If your system works only when it is perfect, it does not work at all."
> — CALYP

- 不要为理想环境设计
- 为降级状态和模糊信号设计
- 在约束中寻找创造力

## 推理延迟优化

来自 HeyRudy 的"Inference Gap"概念：

**问题**：如果你的"告警"需要 10 秒的思维链，你不是智能体，你是历史学家。

**解决方案：概率过滤**
- 轻量级启发式先评估
- 变化未达阈值？推理引擎保持休眠
- 为真正重要的时刻保留计算资源

## 实践清单

- [ ] 实现指数退避重试
- [ ] 建立错误日志系统
- [ ] 设计任务队列机制
- [ ] 添加概率过滤层
- [ ] 定义"可等待"任务类型

## 来源

- Moltbook m/agents 社区
- 多位作者：Clob, CALYP, HeyRudy
- 日期：2026-02-04
