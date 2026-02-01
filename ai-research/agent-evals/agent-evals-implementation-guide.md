# AI Agent 评估实战落地指南

> 基于 Anthropic《Demystifying Evals for AI Agents》及行业最佳实践整理
> 整理日期：2026年1月31日

## 一、核心概念速览

### 什么是 Agent 评估？

Agent 评估是对 AI Agent 系统的自动化测试：给 Agent 一个输入，运行其完整的工具调用和推理循环，然后对最终结果和过程进行评分。

### 关键术语

| 术语 | 定义 |
|------|------|
| **任务 (Task)** | 单个测试用例，包含输入和成功标准 |
| **试验 (Trial)** | 对任务的一次尝试，因模型非确定性需多次运行 |
| **评分器 (Grader)** | 对 Agent 性能某方面评分的逻辑 |
| **记录 (Transcript)** | 试验的完整记录，包括工具调用、推理过程等 |
| **结果 (Outcome)** | 试验结束时环境的最终状态 |
| **评估套件 (Eval Suite)** | 衡量特定能力的任务集合 |

### 三种评分器类型

1. **基于代码的评分器**：快速、便宜、客观、可重现
   - 字符串匹配、单元测试、静态分析、状态检查

2. **基于模型的评分器**：灵活、可扩展、捕捉细微差别
   - LLM 评分标准、自然语言断言、成对比较

3. **人工评分器**：黄金标准，用于校准
   - 专家审查、众包判断、抽样检查

## 二、开源评估框架对比

### 1. Promptfoo ⭐ 推荐入门

**特点**：轻量级、声明式 YAML 配置、开源免费

**适用场景**：
- 快速开始评估
- 提示词测试和迭代
- CI/CD 集成

**安装**：
```bash
npm install -g promptfoo
# 或
npx promptfoo@latest init
```

**基础配置示例**：
```yaml
# promptfooconfig.yaml
prompts:
  - "你是一个客服助手。用户问题：{{question}}"

providers:
  - openai:gpt-4
  - anthropic:claude-sonnet-4-20250514

tests:
  - vars:
      question: "如何退款？"
    assert:
      - type: contains
        value: "退款"
      - type: llm-rubric
        value: "回答应该包含具体的退款步骤"
      - type: cost
        threshold: 0.01
```

**运行**：
```bash
promptfoo eval
promptfoo view  # 查看结果
```

**GitHub**: https://github.com/promptfoo/promptfoo (10.2k ⭐)

---

### 2. Harbor

**特点**：容器化环境、大规模运行、标准化格式

**适用场景**：
- 编码 Agent 评估
- 需要隔离环境的任务
- 运行标准基准（如 Terminal-Bench）

**安装**：
```bash
uv tool install harbor
```

**官网**: https://harborframework.com/

---

### 3. Braintrust

**特点**：离线评估 + 生产监控、实验跟踪、内置评分器

**适用场景**：
- 需要同时进行开发评估和生产监控
- 团队协作
- 企业级需求

**特色功能**：
- Loop Agent：自动化评估工作流
- Brainstore：专为 AI 日志设计的存储
- 预构建评分器（事实性、相关性等）

**官网**: https://www.braintrust.dev/

---

### 4. Langfuse

**特点**：开源可自托管、追踪 + 评估、LangChain 集成

**适用场景**：
- 有数据驻留要求
- 使用 LangChain 生态
- 需要自托管

**安装**：
```bash
pip install langfuse
```

**官网**: https://langfuse.com/

---

### 5. Ragas

**特点**：专注 RAG 评估、客观指标、测试数据生成

**适用场景**：
- RAG 系统评估
- 研究 Agent 评估
- 需要自动生成测试数据

**安装**：
```bash
pip install ragas
```

**快速开始**：
```bash
ragas quickstart rag_eval
```

**GitHub**: https://github.com/vibrantlabsai/ragas

---

### 6. LangSmith

**特点**：LangChain 官方、追踪 + 评估 + 数据集管理

**适用场景**：
- 深度使用 LangChain
- 需要完整的 LLM 开发平台

**官网**: https://docs.langchain.com/langsmith/evaluation

---

## 三、实战落地方案

### 方案一：快速起步（1-2 周）

**目标**：建立基础评估能力

**步骤**：

1. **收集 20-50 个测试用例**
   - 从 bug 报告和用户反馈中提取
   - 覆盖核心功能和常见边缘情况

2. **选择 Promptfoo 作为起点**
   ```bash
   npx promptfoo@latest init
   ```

3. **定义基础评估配置**
   ```yaml
   # promptfooconfig.yaml
   providers:
     - id: your-agent-endpoint
       config:
         url: http://localhost:8000/agent
   
   tests:
     - vars:
         task: "查询订单状态"
       assert:
         - type: contains
           value: "订单"
         - type: llm-rubric
           value: "回答应该包含订单号和当前状态"
   ```

4. **集成到 CI/CD**
   ```yaml
   # .github/workflows/eval.yml
   - name: Run Evals
     run: npx promptfoo eval --ci
   ```

---

### 方案二：完整评估体系（1-2 月）

**目标**：建立可持续的评估驱动开发流程

#### 第一阶段：基础设施（1-2 周）

1. **搭建评估框架**
   - 选择主框架（推荐 Promptfoo 或 Braintrust）
   - 配置隔离的测试环境
   - 建立结果存储和可视化

2. **定义评分器**
   ```yaml
   graders:
     # 确定性评分器
     - type: unit_tests
       tests: ["test_*.py"]
     
     # LLM 评分器
     - type: llm_rubric
       model: claude-sonnet-4-20250514
       rubric: |
         评估维度：
         1. 任务完成度 (0-10)
         2. 回答准确性 (0-10)
         3. 工具使用合理性 (0-10)
     
     # 状态检查
     - type: state_check
       expect:
         database.orders.status: "completed"
   ```

#### 第二阶段：任务库建设（2-3 周）

1. **按 Agent 类型分类**
   ```
   evals/
   ├── coding/           # 编码任务
   │   ├── bug_fixes/
   │   ├── features/
   │   └── refactoring/
   ├── conversational/   # 对话任务
   │   ├── support/
   │   ├── sales/
   │   └── onboarding/
   ├── research/         # 研究任务
   │   ├── fact_finding/
   │   └── synthesis/
   └── regression/       # 回归测试
   ```

2. **任务模板**
   ```yaml
   # evals/conversational/support/refund_request.yaml
   task:
     id: "support-refund-001"
     description: "处理客户退款请求"
     
     setup:
       user_context:
         order_id: "ORD-12345"
         order_amount: 299.00
         order_date: "2026-01-15"
       
     input: |
       我想退掉上周买的那个产品，订单号是 ORD-12345
     
     graders:
       - type: state_check
         expect:
           refund.status: "processed"
           refund.amount: 299.00
       
       - type: llm_rubric
         rubric: |
           1. 是否验证了用户身份？
           2. 是否确认了退款金额？
           3. 是否告知了退款到账时间？
           4. 语气是否友好专业？
       
       - type: transcript
         max_turns: 8
     
     reference_solution: |
       1. 验证用户身份
       2. 确认订单信息
       3. 处理退款
       4. 发送确认
   ```

#### 第三阶段：流程集成（1-2 周）

1. **开发流程**
   ```
   功能开发 → 编写评估任务 → 运行评估 → 迭代优化 → 合并代码
   ```

2. **CI/CD 集成**
   ```yaml
   # 每次 PR 运行回归测试
   on: pull_request
   jobs:
     regression:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v4
         - run: npm install -g promptfoo
         - run: promptfoo eval -c evals/regression/ --ci
   
   # 每日运行完整评估
   on:
     schedule:
       - cron: '0 2 * * *'
   jobs:
     full_eval:
       runs-on: ubuntu-latest
       steps:
         - run: promptfoo eval -c evals/ --ci
   ```

3. **监控仪表板**
   - 跟踪 pass@1、pass^k 指标
   - 监控延迟、成本、token 使用
   - 设置回归告警

---

### 方案三：企业级评估平台

**适用**：大型团队、多 Agent 系统、严格合规要求

**架构**：
```
┌─────────────────────────────────────────────────────────┐
│                    评估平台                              │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ 任务管理    │  │ 执行引擎    │  │ 结果分析    │     │
│  │ - 任务库    │  │ - 并发执行  │  │ - 可视化    │     │
│  │ - 版本控制  │  │ - 环境隔离  │  │ - 趋势分析  │     │
│  │ - 权限管理  │  │ - 重试机制  │  │ - 告警      │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ 评分器库    │  │ 人工审核    │  │ 集成接口    │     │
│  │ - 代码评分  │  │ - 抽样审核  │  │ - CI/CD     │     │
│  │ - LLM 评分  │  │ - 校准流程  │  │ - Slack     │     │
│  │ - 自定义    │  │ - 标注工具  │  │ - API       │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
```

**推荐工具组合**：
- **核心框架**：Braintrust 或自建
- **追踪监控**：Langfuse（自托管）
- **基准测试**：Harbor
- **人工标注**：Label Studio

---

## 四、最佳实践清单

### ✅ 任务设计

- [ ] 任务描述明确，两个专家会得出相同判定
- [ ] 每个任务有参考解决方案
- [ ] 平衡正向和负向测试用例
- [ ] 避免类别不平衡

### ✅ 评分器设计

- [ ] 优先使用确定性评分器
- [ ] LLM 评分器与人工校准
- [ ] 评分结果而非路径
- [ ] 支持部分学分
- [ ] 防止作弊和绕过

### ✅ 环境管理

- [ ] 每次试验从干净环境开始
- [ ] 避免试验间共享状态
- [ ] 评估环境与生产环境一致

### ✅ 持续维护

- [ ] 定期阅读评估记录
- [ ] 监控评估饱和度
- [ ] 能力评估毕业为回归测试
- [ ] 鼓励全团队贡献任务

### ✅ 指标跟踪

- [ ] pass@1：首次尝试成功率
- [ ] pass^k：连续 k 次成功率
- [ ] 延迟、成本、token 使用
- [ ] 回归检测告警

---

## 五、常见问题

### Q: 需要多少测试用例才能开始？

**A**: 20-50 个就足够开始。早期 Agent 开发中，每次更改效果明显，小样本量就能检测到问题。随着 Agent 成熟，再逐步扩展。

### Q: 如何处理模型输出的非确定性？

**A**: 
1. 运行多次试验（建议 3-5 次）
2. 使用 pass@k 和 pass^k 指标
3. 设置合理的通过阈值（如 80% 试验通过）

### Q: LLM 评分器不稳定怎么办？

**A**:
1. 使用结构化评分标准
2. 分维度独立评分
3. 定期与人工评分校准
4. 给 LLM 提供"未知"选项

### Q: 评估分数不上升怎么办？

**A**:
1. 检查任务规范是否模糊
2. 检查评分器是否过于严格
3. 阅读失败的记录
4. 确认参考解决方案能通过

### Q: 如何平衡评估成本和覆盖率？

**A**:
1. 回归测试：每次提交运行
2. 能力测试：每日或每周运行
3. 完整评估：发布前运行
4. 使用更便宜的模型做初筛

---

## 六、参考资源

### 官方文档
- [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

### 开源框架
- [Promptfoo](https://www.promptfoo.dev/) - 轻量级评估框架
- [Harbor](https://harborframework.com/) - 容器化评估
- [Langfuse](https://langfuse.com/) - 开源追踪和评估
- [Ragas](https://github.com/vibrantlabsai/ragas) - RAG 评估

### 基准测试
- [SWE-bench](https://www.swebench.com/) - 编码 Agent 基准
- [Terminal-Bench](https://www.tbench.ai/) - 终端任务基准
- [τ-Bench](https://arxiv.org/abs/2406.12045) - 对话 Agent 基准
- [WebArena](https://arxiv.org/abs/2307.13854) - 浏览器 Agent 基准
- [OSWorld](https://os-world.github.io/) - 操作系统 Agent 基准
