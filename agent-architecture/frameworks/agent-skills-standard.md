# Agent Skills Standard

> Anthropic 开发的开放标准，用于给 AI agents 添加可发现、可复用的能力

## 概述

Agent Skills 是由 Anthropic 开发并开源的标准。Skills 是包含指令、脚本和资源的文件夹，agents 可以按需发现和加载。

## 核心问题

Agents 越来越强大，但往往缺乏可靠完成实际工作所需的上下文。Skills 通过提供：
- 程序性知识
- 公司/团队/用户特定上下文

## Skills 结构

```
skill-name/
├── SKILL.md          # 主要指令文件
├── scripts/          # 可执行脚本
├── references/       # 参考资料
└── assets/           # 资源文件
```

## 核心价值

| 价值 | 描述 |
|------|------|
| 领域专业知识 | 将专业知识打包成可复用指令 |
| 新能力 | 给 agents 添加新能力 |
| 可重复工作流 | 多步骤任务转化为一致、可审计的工作流 |
| 互操作性 | 同一 skill 可跨不同 agent 产品使用 |

## 生态系统

- **开源仓库**：github.com/agentskills/agentskills
- **官网**：agentskills.io
- **已被多个 AI 开发工具采用**

## 与 Clawdbot 的关系

Clawdbot 的 skills 系统正是这个标准的实现：
- `/root/clawd/skills/` 目录结构
- `SKILL.md` 作为主要指令文件
- ClawdHub (clawdhub.com) 作为分发平台

## 参考

- [Agent Skills 官网](https://agentskills.io/home)
- [GitHub 仓库](https://github.com/agentskills/agentskills)
- 学习日期：2026-02-04
