# Claude Sonnet 4.6 - 智能体能力分析

> 发布日期: 2026-02-18
> 来源: https://www.anthropic.com/news/claude-sonnet-4-6

## 概述

Claude Sonnet 4.6 是 Anthropic 发布的最新 Sonnet 模型，在智能体相关能力上有重大突破。定价与 Sonnet 4.5 相同（$3/$15 per million tokens），但性能接近 Opus 级别。

## 智能体核心能力

### 1. Computer Use（计算机使用）

**进展**:
- OSWorld 基准测试显示 16 个月内持续进步
- 可处理：复杂电子表格导航、多步骤网页表单、跨多个浏览器标签协调

**安全改进**:
- 抗 prompt injection 能力显著提升
- 与 Opus 4.6 相当

**应用场景**:
- 自动化遗留系统操作（无 API 的软件）
- 表单填写、数据录入
- 跨应用工作流

### 2. 长上下文推理（1M Token）

**特性**:
- 1M token 上下文窗口（Beta）
- Context Compaction：自动总结旧上下文

**应用场景**:
- 整个代码库分析
- 长合同审阅
- 多文档研究综合

### 3. 智能体规划（Agent Planning）

**Vending-Bench Arena 表现**:
- 展示了新策略：前期投资产能，后期转向盈利
- 体现长期规划和策略调整能力

**关键改进**:
- 更好的多步骤任务执行
- 减少虚假成功声明
- 更一致的任务跟进

### 4. 编码能力

**用户偏好**:
- 70% 偏好 Sonnet 4.6 vs Sonnet 4.5
- 59% 偏好 Sonnet 4.6 vs Opus 4.5

**改进点**:
- 更好地阅读上下文后再修改代码
- 整合共享逻辑而非重复
- 减少过度工程化
- 更好的指令遵循

## 新工具能力

### API 工具（正式发布）
- Code Execution（代码执行）
- Memory（记忆）
- Programmatic Tool Calling（程序化工具调用）
- Tool Search（工具搜索）

### Web 工具改进
- Web Search 和 Fetch 自动写代码过滤搜索结果
- 提升响应质量和 token 效率

### 思考模式
- Adaptive Thinking（自适应思考）
- Extended Thinking（扩展思考）

## 与其他模型对比

| 能力 | Sonnet 4.6 | Sonnet 4.5 | Opus 4.6 |
|------|------------|------------|----------|
| 编码 | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| Computer Use | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| 长上下文 | ★★★★★ | ★★★★☆ | ★★★★★ |
| 深度推理 | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| 性价比 | ★★★★★ | ★★★★☆ | ★★★☆☆ |

## 最佳实践建议

1. **日常智能体任务**: 使用 Sonnet 4.6（性价比最优）
2. **深度推理任务**: 使用 Opus 4.6（代码库重构、多智能体协调）
3. **长上下文场景**: 启用 Context Compaction
4. **Computer Use**: 注意 prompt injection 防护

## 对智能体开发的启示

1. **Computer Use 成熟度提升** - 可以更多依赖 GUI 自动化
2. **长上下文是关键** - 1M token 使整个项目级别的理解成为可能
3. **规划能力进步** - 智能体可以执行更复杂的长期任务
4. **工具调用标准化** - Memory、Tool Search 等成为标准能力
