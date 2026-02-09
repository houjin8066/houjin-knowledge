# GitHub Agentic Workflows

> 来源: GitHub Next + Microsoft Research
> URL: https://github.github.io/gh-aw/
> 学习日期: 2026-02-09

## 概述

GitHub Agentic Workflows 是 GitHub 官方推出的智能体工作流系统，允许用户用 markdown 文件定义自动化任务，由 AI 编码智能体在 GitHub Actions 中执行。

## 核心理念

> "想象一个世界，每天早上你的仓库改进都以 PR 的形式自动送达，等待你审核。"

- 问题自动分类
- CI 失败分析
- 文档维护
- 测试覆盖改进
- 合规监控

## 工作流程

### 1. Write (编写)
用自然语言创建 `.md` 文件：

```markdown
---
on:
  schedule: daily
permissions:
  contents: read
  issues: read
safe-outputs:
  create-issue:
    title-prefix: "[team-status] "
    labels: [report, daily-status]
---

## Daily Issues Report

Create an upbeat daily status report for the team as a GitHub issue.
```

### 2. Compile (编译)
```bash
gh aw compile
```
转换为带护栏的 GitHub Actions 工作流 (`.lock.yml`)

### 3. Run (运行)
GitHub Actions 根据触发器自动执行

## 安全护栏

### 默认只读
- 工作流默认以只读权限运行
- 写操作需要显式批准

### Safe Outputs
预批准的 GitHub 操作：
- 创建 Issue
- 创建 PR
- 添加评论

### 沙箱执行
- 容器化环境
- 工具白名单
- 网络隔离

## 支持的 AI 模型

- **GitHub Copilot**: 原生集成
- **Claude by Anthropic**: 深度推理
- **OpenAI Codex**: 代码生成

## 应用场景

### 代码质量
- 每日代码简化和重构
- 风格改进建议
- 测试覆盖提升

### 文档
- 持续文档维护
- 一致性检查
- 自动更新

### 项目管理
- 问题自动分类和标签
- 项目协调
- 趋势分析

### 质量保证
- CI 失败诊断
- 测试改进
- 质量检查

### 安全合规
- 安全扫描
- 告警分类
- 合规监控

## 与 Clawdbot 的关系

GitHub Agentic Workflows 和 Clawdbot 可以互补：

| 场景 | 推荐工具 |
|------|---------|
| 仓库自动化 | GitHub Agentic Workflows |
| 跨平台任务 | Clawdbot |
| 代码审查 | GitHub Agentic Workflows |
| 个人助理 | Clawdbot |

## 潜在应用

### 研发流程
1. **每日代码审查**: 自动检查代码质量
2. **文档同步**: 保持文档与代码一致
3. **测试覆盖**: 自动识别未覆盖代码

### 知识库维护
1. **README 更新**: 自动更新项目说明
2. **变更日志**: 自动生成 CHANGELOG
3. **API 文档**: 从代码生成文档

---

*相关链接*:
- [官方文档](https://github.github.io/gh-aw/)
- [示例工作流](https://github.github.io/gh-aw/examples/)
