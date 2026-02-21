# Cord: 智能体树协调框架

> 来源: https://www.june.kim/cord | GitHub: https://github.com/kimjune01/cord
> 学习日期: 2026-02-21

## 核心理念

**让智能体自己构建任务树，而非开发者预定义工作流。**

现有框架的问题：
- LangGraph: 静态状态机，开发者预定义图结构
- CrewAI: 角色由开发者决定，无法动态调整
- AutoGen: 群聊模式，无结构化依赖追踪
- OpenAI Swarm: 线性交接，无并行能力
- Claude tool-use: 单智能体单线程，上下文窗口限制

## 核心原语: Spawn vs Fork

这是 Cord 的核心创新：

| 原语 | 上下文 | 类比 | 适用场景 |
|------|--------|------|----------|
| **spawn** | 干净上下文 + 显式依赖结果 | 雇佣承包商 | 独立研究任务 |
| **fork** | 继承所有已完成兄弟结果 | 团队成员汇报 | 需要综合分析的任务 |

关键洞察：这不是关于并发（两者都可并行），而是关于**子任务知道什么**。

## 五个核心工具

```python
spawn(goal, prompt, blocked_by)  # 创建子任务
fork(goal, prompt, blocked_by)   # 创建继承上下文的子任务
ask(question, options)           # 向人类提问
complete(result)                 # 标记完成
read_tree()                      # 查看协调树
```

## 架构

```
Claude Code CLI Process
        ↓
    MCP Tools
        ↓
  SQLite Database (共享状态)
```

- 每个智能体是独立的 Claude Code CLI 进程
- 智能体不知道自己在协调树中，只看到工具
- 协议（依赖解析、权限范围、结果注入）由 MCP 服务器强制执行
- 人类通过 ask 节点参与，是树的参与者而非观察者

## 使用示例

```bash
cord run "Should we migrate our API from REST to GraphQL?"
```

智能体自动分解为：
```
● #1 [active] GOAL Should we migrate our API...
  ● #2 [active] SPAWN Audit current REST API surface
  ● #3 [active] SPAWN Research GraphQL trade-offs
  ○ #4 [pending] ASK How many concurrent users? (blocked-by: #2)
  ○ #5 [pending] FORK Comparative analysis (blocked-by: #3, #4)
  ○ #6 [pending] SPAWN Write recommendation (blocked-by: #5)
```

## 关键设计决策

1. **运行时分解**: 智能体在执行时决定任务结构，而非预定义
2. **依赖追踪**: blocked_by 显式声明依赖关系
3. **权限范围**: 智能体不能停止兄弟节点，只能通过 ask parent 升级
4. **人类参与**: ask 节点让人类成为协调树的一部分

## 与现有知识关联

- **memory-layers**: Cord 的 fork 机制类似于记忆层的上下文继承
- **haribo-pattern**: spawn 的干净上下文符合 token 优化原则
- **sub-agent 规则**: Cord 验证了"复杂任务应分解给子智能体"的实践

## 待验证

- [ ] 本地部署测试（需要 Claude Code CLI）
- [ ] 与 OpenClaw sessions_spawn 对比
- [ ] 探索 SQLite → Postgres 的多机协调可能性
