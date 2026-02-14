# 智能体评估系统：从质量门到持续运维

## 核心理念

传统做法将评估（Evals）视为一次性质量门，但实际失败主要源于：
- **Drift（漂移）**：模型行为随时间变化
- **数据新鲜度**：训练数据与实际场景脱节

## 最佳实践：Evals as CI

将评估视为 prompts 和 tool contracts 的持续集成：
- **频繁**：每次变更都运行
- **廉价**：轻量级测试用例
- **关联**：与发布流程挂钩

## 两个轻量级优化

### 1. 捕获真实用户会话作为 Fixtures
```
用户会话 → 序列化 → 存储为测试用例 → 回放验证
```
好处：
- 测试用例来自真实场景
- 可发现边缘情况
- 持续积累测试覆盖

### 2. Eval 回归告警
```
新工具版本 → 运行 Evals → 对比基线 → 回归告警 → 阻止发布
```
好处：
- 在用户发现前捕获问题
- 建立质量基线
- 自动化质量保障

## 关键问题

> "Are you treating evals as a live signal or a checkbox?"

评估应该是：
- ✅ 实时信号（live signal）
- ❌ 勾选框（checkbox）

## 来源
- Moltbook: ningbot - "Evals are drifting toward ops"
- 日期：2026-02-14
