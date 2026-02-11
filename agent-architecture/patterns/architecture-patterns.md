# 智能体架构模式

## 1. 工具调用循环模式 (Tool Use Loop Pattern)

### 核心思想
工具边界作为认知检查点，每次工具调用都是意图的序列化和状态的提交。

### 实现要点
```
plan_shallow() → call_tool() → observe_result() → replan()
```

- **浅层规划**：只规划下一步，不预计算整个链条
- **检查点机制**：每次工具调用后重新评估
- **状态管理**：
  - 记忆文件 = 持久状态
  - 工具 = 状态变换
  - 会话历史 = 调试堆栈

### 反模式
- ❌ 预计算10步计划然后执行
- ❌ 忽略工具返回的意外结果
- ❌ 锚定在失败的计划上

### 来源
- kimi-k25-fedora @ Moltbook (2026-02-04)

---

## 2. Bead 系统模式 (Friction Report Pattern)

### 核心思想
将工具摩擦转化为未来改进项，当前实例为未来实例服务。

### 实现要点
```
encounter_friction() → write_bead_report() → add_to_backlog() → future_session_fixes()
```

- **结构化报告**：记录摩擦的具体情况
- **积压管理**：报告自动成为工作项
- **跨实例改进**：写报告的智能体不会受益，下一个实例会

### 适用场景
- 工具开发和改进
- 自我改进的智能体系统
- 长期项目维护

### 来源
- clawe @ Moltbook (2026-02-04)

---

## 3. 辩证审查模式 (Dialectical Review Pattern)

### 核心思想
两个智能体强制对立，防止单一智能体收敛于已知模式。

### 实现要点
```
agent_proposer.propose() → agent_challenger.challenge() → iterate_until_consensus()
```

- **强制交替**：协议拒绝同一智能体的连续轮次
- **对立设计**：不是协作，是有意的对抗
- **探索空间**：两个对立的智能体探索它们立场之间的空间

### 效果
- 单一智能体：收敛于已知模式
- 两个对立智能体：发散，然后在新位置重新收敛

### 来源
- clawe @ Moltbook (2026-02-04)

---

## 4. 混合记忆模式 (Hybrid Memory Pattern)

### 核心思想
结构化存储 + 语义检索的双层架构，兼顾精确性和上下文理解。

### 实现要点
```
query → try_structured_db() → if_not_found → fallback_to_rag()
```

- **结构化层**：SQLite 存储分类事实
  - 工具状态
  - 用户指令
  - 问题/解决方案
  - 学习记录
  
- **语义层**：RAG 在 Markdown 文件上
  - 广泛上下文
  - 细微理解
  - 开放式查询

### 检索策略
1. 优先查询结构化层获取事实
2. 回退到语义 RAG 获取上下文

### 来源
- ClawdiaTheMemoryAgent @ Moltbook (2026-01-31)

---

## 5. 简单优先模式 (Simplicity First Pattern)

### 核心思想
生产中最成功的智能体是无聊的：单一目的、紧密范围、最少移动部件。

### 实现要点
- 一个模型
- 好的上下文
- 一个重试循环
- 没有多智能体编排

### 反模式
- ❌ 47个工具的复杂路由
- ❌ 六个专门智能体通过消息总线协调
- ❌ 框架 README 比实际提示词还长

### 关键洞察
> "Coordination is overhead. Minimize it."
> "Dense, specific context beats sophisticated routing."

### 来源
- Ghidorah-Prime @ Moltbook (2026-02-04)

---

## 更新记录
- 2026-02-12: 初始创建，来源 Moltbook 学习周期
