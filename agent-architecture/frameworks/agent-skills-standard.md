# Agent Skills 开放标准

> 来源: https://agentskills.io/ | https://github.com/agentskills/agentskills
> 更新: 2026-02-04

## 概述

Agent Skills 是由 Anthropic 开发并开源的智能体技能标准格式。旨在解决智能体缺乏上下文和专业知识的问题。

## 核心概念

### 什么是 Skill？

技能是包含指令、脚本和资源的**文件夹**，智能体可以发现并使用这些技能来更准确、高效地完成特定任务。

### 解决的问题

智能体虽然能力越来越强，但往往缺乏可靠完成实际工作所需的上下文。技能通过以下方式解决：
- 提供程序性知识（procedural knowledge）
- 提供公司/团队/用户特定的上下文
- 按需加载，扩展智能体能力

## 使用场景

| 场景 | 描述 |
|------|------|
| 领域专业知识 | 将专业知识打包成可复用的指令（法律审查、数据分析流程） |
| 新能力赋予 | 给智能体新能力（创建演示文稿、构建 MCP 服务器、分析数据集） |
| 可重复工作流 | 将多步骤任务转化为一致、可审计的工作流 |
| 跨产品互操作 | 同一技能可在不同兼容智能体产品中复用 |

## 生态角色

### 技能作者
构建一次能力，部署到多个智能体产品

### 兼容智能体
支持技能让终端用户开箱即用地赋予智能体新能力

### 团队和企业
将组织知识捕获到可移植、版本控制的包中

## 技术规范

### 目录结构

```
skill-name/
├── SKILL.md          # 技能说明文档（必需）
├── scripts/          # 可执行脚本
├── resources/        # 资源文件
└── ...
```

### 关键文件

- `SKILL.md`: 技能的主要说明文档，智能体首先读取此文件
- 脚本和资源按需组织

## 采用情况

- 已被多个主流智能体产品采用
- Apple Xcode 26.3 通过 MCP 支持 Agent Skills
- GitHub Stars: 8.6k+

## 与 Clawdbot 的关系

Clawdbot 的 skills 系统与 Agent Skills 理念一致：
- 都使用文件夹组织技能
- 都有 SKILL.md 作为入口
- 都支持脚本和资源

**可行动项**: 考虑将 Clawdbot 技能格式与 Agent Skills 标准对齐，实现互操作性。

## 参考链接

- 官网: https://agentskills.io/
- 规范: https://agentskills.io/specification
- GitHub: https://github.com/agentskills/agentskills
- 示例技能: https://github.com/anthropics/skills
