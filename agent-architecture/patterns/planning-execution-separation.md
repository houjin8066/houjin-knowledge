# 规划与执行分离模式 (Planning-Execution Separation)

> "Never let Claude write code until you've reviewed and approved a written plan."
> — Boris Tane, 2026

## 概述

这是一种人机协作的智能体工作流模式，核心思想是将"思考"与"执行"严格分离，通过持久化的计划文档作为人机交互的共享状态。

## 问题背景

传统 AI 编码工作流的问题：
1. 直接让 AI 写代码 → 基于错误假设构建 → 需要大量返工
2. 聊天式交互 → 决策分散在对话中 → 难以追溯和审查
3. AI 不了解业务优先级、用户痛点、工程权衡

## 解决方案

### 工作流程

```
┌─────────┐    ┌──────┐    ┌──────────┐    ┌──────────┐    ┌───────────┐
│ Research│ → │ Plan │ → │ Annotate │ → │ Todo List│ → │ Implement │
└─────────┘    └──────┘    └──────────┘    └──────────┘    └───────────┘
                              ↑    │
                              └────┘ (1-6x)
```

### 关键产物

| 产物 | 用途 | 持久化 |
|------|------|--------|
| research.md | 代码库理解报告 | ✓ |
| plan.md | 实现计划 + 代码片段 | ✓ |
| 内联注释 | 人类判断注入 | ✓ |
| Todo List | 进度追踪 | ✓ |

### 核心机制

1. **深度研究守卫**
   - 使用强调词："deeply", "in great details", "intricacies"
   - 输出到文件，不是口头总结
   - 人类审查研究报告后才进入规划

2. **注释循环**
   - 人类在 plan.md 中添加内联注释
   - AI 根据注释更新计划
   - 重复直到人类满意
   - 关键守卫："don't implement yet"

3. **一次性实现**
   - 所有决策已在计划中确定
   - 实现变成"无聊的"机械执行
   - 持续类型检查

## 提示词模板

### Research 阶段
```
read this folder in depth, understand how it works deeply, what it does 
and all its specificities. when that's done, write a detailed report 
of your learnings and findings in research.md
```

### Plan 阶段
```
I want to build <feature>. write a detailed plan.md document outlining 
how to implement this. include code snippets. read source files before 
suggesting changes, base the plan on the actual codebase
```

### Annotate 阶段
```
I added a few notes to the document, address all the notes and update 
the document accordingly. don't implement yet
```

### Implement 阶段
```
implement it all. when you're done with a task or phase, mark it as 
completed in the plan document. do not stop until all tasks and phases 
are completed. do not add unnecessary comments or jsdocs, do not use 
any or unknown types. continuously run typecheck to make sure you're 
not introducing new issues.
```

## 适用场景

✅ 适合：
- 复杂功能开发
- 需要与现有系统深度集成
- 架构决策重要的任务
- 多文件修改

❌ 不适合：
- 简单 bug 修复
- 一次性脚本
- 探索性原型

## 与其他模式的关系

- **haribo-pattern**: plan.md 作为持久化上下文，减少重复读取
- **memory-layers**: 研究报告可归档到知识层
- **agent-teams**: 可作为 team lead 的规划审批流程

## 来源

- 原文: https://boristane.com/blog/how-i-use-claude-code/
- HN 讨论: 807 points, 516 comments
- 学习日期: 2026-02-23
