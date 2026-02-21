# Cord: 树状智能体协调协议

> 来源: https://www.june.kim/cord | https://github.com/kimjune01/cord
> 学习日期: 2026-02-21

## 核心理念

**让智能体自己构建任务树，而不是开发者预定义工作流。**

现有框架的问题：
- LangGraph: 静态状态机，无法运行时调整分解
- CrewAI: 角色由开发者定义，不能动态发现
- AutoGen: 群聊式协调，无结构、难追踪
- Swarm: 线性交接，无并行、无树结构
- Claude tool-use: 单智能体循环，上下文受限

## 核心创新: Spawn vs Fork

这是 Cord 最重要的贡献——上下文流动原语：

| 原语 | 上下文 | 类比 | 适用场景 |
|------|--------|------|----------|
| **Spawn** | 干净slate + 显式依赖结果 | 雇佣承包商 | 独立研究任务、可重启任务 |
| **Fork** | 继承所有已完成兄弟结果 | 团队成员汇报 | 综合分析、需要全局上下文 |

关键洞察：这不是关于并发（两者都可并行/串行），而是关于**子节点知道什么**。

## 五个协调原语

```python
spawn(goal, prompt, blocked_by)  # 创建独立子任务
fork(goal, prompt, blocked_by)   # 创建继承上下文的子任务  
ask(question, options)           # 向人类提问
complete(result)                 # 标记完成
read_tree()                      # 查看协调树
```

## 协议特性

1. **依赖解析**: `blocked_by` 声明前置依赖
2. **权限范围**: 智能体只能控制自己的子树
3. **人类参与**: ask 节点让人类成为树的参与者
4. **两阶段生命周期**: pending → active → complete

## 实现细节

- ~500行 Python
- SQLite 存储协调状态
- MCP 工具接口
- 基于 Claude Code CLI

## 使用示例

```bash
cord run "Should we migrate our API from REST to GraphQL?"
```

智能体自动分解为：
```
● #1 GOAL Should we migrate...
  ● #2 SPAWN Audit current REST API surface
  ● #3 SPAWN Research GraphQL trade-offs
  ○ #4 ASK How many concurrent users? (blocked-by: #2)
  ○ #5 FORK Comparative analysis (blocked-by: #3, #4)
  ○ #6 SPAWN Write recommendation (blocked-by: #5)
```

## 与现有工具的关系

- **claude-code-agent-teams**: Cord 可作为更轻量的替代方案
- **memory-layers**: Fork 原语天然支持上下文继承，与记忆层理念一致
- **haribo-pattern**: Spawn 的干净上下文有助于 token 优化

## 局限性

- 依赖 Claude Code CLI 订阅
- 仅在 Claude 上验证
- 单机 SQLite，多机需改用 Postgres

## 可行动项

- [ ] 研究 Cord 源码，理解 MCP 工具实现
- [ ] 考虑将 spawn/fork 概念应用到 OpenClaw sub-agent 设计
- [ ] 测试 Cord 在实际任务中的表现
