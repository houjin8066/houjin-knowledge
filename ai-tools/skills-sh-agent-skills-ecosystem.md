# Skills.sh - 开放的 Agent 技能生态系统

> 来源: https://skills.sh
> 收录时间: 2026-01-31
> 分类: AI工具/Agent技能

## 概述

Skills.sh 是一个开放的 AI Agent 技能目录和生态系统。它允许开发者创建、分享和安装可复用的 Agent 技能（Skills），通过一条命令即可增强 AI Agent 的能力。

**核心理念：** Skills 是 AI Agent 的可复用能力模块，让 Agent 能够访问程序化知识（procedural knowledge）。

## 安装方式

```bash
# 安装技能（从 GitHub 仓库）
npx skills add <owner/repo>

# 示例
npx skills add vercel-labs/agent-skills
npx skills add remotion-dev/skills
```

## CLI 命令

| 命令 | 说明 |
|------|------|
| `skills add <package>` | 安装技能包 |
| `skills remove [skills]` | 移除已安装的技能 |
| `skills list` / `skills ls` | 列出已安装的技能 |
| `skills find [query]` | 交互式搜索技能 |
| `skills init [name]` | 初始化新技能（创建 SKILL.md） |
| `skills check` | 检查技能更新 |
| `skills update` | 更新所有技能到最新版本 |

## 安装选项

| 选项 | 说明 |
|------|------|
| `-g, --global` | 全局安装（用户级别） |
| `-a, --agent <agents>` | 指定安装到哪些 Agent（如 claude-code, cursor） |
| `-s, --skill <skills>` | 指定安装哪些技能 |
| `-l, --list` | 列出仓库中可用的技能（不安装） |
| `-y, --yes` | 跳过确认提示 |
| `--all` | 安装所有技能到所有 Agent |

## 技能格式

每个技能是一个包含 `SKILL.md` 文件的目录，定义了：
- 技能名称和描述
- 使用场景（When to use）
- 使用方法（How to use）
- 参考文档和代码示例

## 热门技能仓库

### 1. remotion-dev/skills
Remotion 官方技能集，用于 React 视频编程：
- 动画、时序、过渡效果
- 音视频处理
- 字幕/Caption
- 3D 内容（Three.js）
- 图表可视化

### 2. vercel-labs/agent-skills
Vercel 官方技能集，包含：
- PR Review
- Commit 规范
- 前端开发最佳实践

### 3. davila7/claude-code-templates
Claude Code 模板集，包含多种开发场景的技能

## 与 ClawdHub 的区别

| 特性 | Skills.sh | ClawdHub |
|------|-----------|----------|
| 定位 | 通用 Agent 技能生态 | Clawdbot 专用技能市场 |
| 安装方式 | `npx skills add` | `clawdhub install` |
| 技能格式 | SKILL.md | SKILL.md + 脚本/资源 |
| 目标 Agent | Claude Code, Cursor, 通用 | Clawdbot |

## 创建自己的技能

```bash
# 初始化技能
npx skills init my-skill

# 会创建 my-skill/SKILL.md 模板
```

## 相关链接

- 官网: https://skills.sh
- GitHub: 各技能仓库托管在 GitHub
- 文档: 技能页面包含完整使用说明

## 总结

Skills.sh 是一个轻量级的 Agent 技能分发平台，通过标准化的 SKILL.md 格式，让 AI Agent 能够快速获取特定领域的专业知识。它的设计理念是"一条命令安装，即插即用"，非常适合快速增强 Agent 在特定领域（如视频制作、代码审查、前端开发）的能力。
