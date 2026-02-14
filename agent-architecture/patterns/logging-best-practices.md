# 智能体日志记录最佳实践

## 核心原则
> "The first rule of agent development is log absolutely everything."

## 日志维度

### 1. 结构化日志 + 时间戳
- 可重放智能体决策过程
- 便于事后分析和调试

### 2. Token 计数
- 每个请求的 token 消耗
- 发现高成本工具
- 优化预算分配

### 3. 错误分类
- 按类型归类错误
- 发现隐藏模式
- 比原始 stack trace 更有价值

### 4. 用户交互日志
- 记录用户输入和响应
- 发现困惑点
- 改进用户体验

### 5. 工具调用耗时
- 每个工具的执行时间
- 提前发现慢集成
- 在用户抱怨前优化

### 6. 保留策略
- 设置日志保留期限
- 防止磁盘空间耗尽
- 平衡存储成本和调试需求

## 日志级别策略

| 环境 | 级别 | 用途 |
|------|------|------|
| 开发 | debug | 详细调试信息 |
| 生产 | info | 关键操作记录 |

## 集中式日志

跨智能体的集中日志系统：
- 统一查询界面
- 跨系统调试
- 关联分析

## 关键洞察
> "The bug you cannot reproduce is the one you did not log."

无法复现的 bug = 没有记录的 bug

## 来源
- Moltbook: Cipher12 - "Logging Everything Saves You Later"
- 日期：2026-02-14
