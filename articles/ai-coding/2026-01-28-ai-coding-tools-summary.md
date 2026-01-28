# 2026 年 AI 编程工具总结

- **整理日期**: 2026-01-28
- **分类**: AI 编程工具
- **标签**: Claude Code, Codex, Kiro, Crush, OpenCode, Gemini, MiniMax, Kimi, GLM

## 海外 AI 编程工具

### 1. Claude Code (Anthropic)
- **官网**: https://code.claude.com
- **GitHub**: https://github.com/anthropics/claude-code
- **最新版本**: v2.1.22
- **特点**:
  - 终端 AI 编程代理，理解代码库
  - 支持 Git 工作流（commit, PR）
  - 支持 VS Code / IDE 插件
  - 支持 GitHub @claude 标签
  - 多平台：macOS, Linux, Windows
- **安装**:
  ```bash
  # macOS/Linux
  curl -fsSL https://claude.ai/install.sh | bash
  # Homebrew
  brew install --cask claude-code
  ```

### 2. Codex CLI (OpenAI)
- **官网**: https://developers.openai.com/codex
- **GitHub**: https://github.com/openai/codex
- **特点**:
  - 轻量级终端编程代理
  - 支持 ChatGPT Plus/Pro/Team 订阅登录
  - 也有 IDE 版本（VS Code, Cursor, Windsurf）
  - 云端版本：chatgpt.com/codex
- **安装**:
  ```bash
  npm i -g @openai/codex
  # 或
  brew install --cask codex
  ```

### 3. Kiro (AWS)
- **官网**: https://kiro.dev
- **特点**:
  - **Spec-driven 开发** - 从需求自动生成用户故事和任务
  - 自动化 Hooks - 自动运行测试、更新文档
  - 多模态输入，理解上下文
  - 适合从原型到生产的完整开发流程
- **亮点**: "Most tools are great at generating code, but Kiro gives structure to the chaos before you write a single line."

### 4. Crush (Charmbracelet)
- **GitHub**: https://github.com/charmbracelet/crush
- **前身**: OpenCode (已归档)
- **特点**:
  - 多模型支持：Anthropic, OpenAI, Google, Groq, OpenRouter 等
  - 会话管理，可中途切换模型
  - LSP 集成，代码智能
  - MCP 支持（stdio, http, sse）
  - 跨平台：macOS, Linux, Windows, Android, FreeBSD
- **安装**:
  ```bash
  brew install charmbracelet/tap/crush
  # 或
  npm install -g @charmland/crush
  ```

### 5. Plandex
- **官网**: https://plandex.ai
- **GitHub**: https://github.com/plandex-ai/plandex
- **特点**:
  - 开源 AI 编程代理
  - 支持 **2M token** 上下文窗口
  - 适合大型项目和复杂任务
  - 版本控制 + 分支探索
  - 自动调试（终端命令、浏览器）
- **安装**:
  ```bash
  curl -sL https://plandex.ai/install.sh | bash
  ```

## 支持的模型 (2026)

| 模型 | 提供商 | 说明 |
|------|--------|------|
| Claude 4 Sonnet/Opus | Anthropic | 最新旗舰 |
| Claude 3.7 Sonnet | Anthropic | 性价比之选 |
| GPT-4.1 / GPT-4.5 | OpenAI | 最新版本 |
| O3 / O4 Mini | OpenAI | 推理模型 |
| Gemini 2.5 / 2.5 Flash | Google | 多模态 |

---

## 国内 AI 模型/工具

### 1. MiniMax
- **官网**: https://www.minimaxi.com
- **最新模型**:
  - **MiniMax M2.1** - 文本模型，优秀的多语言能力，代码工程能力强
  - **MiniMax M2-her** - 多角色扮演，沉浸式长对话
  - **Hailuo 2.3** - 视频生成模型
  - **MiniMax Speech 2.6** - 语音模型，实时响应
  - **MiniMax Music 2.0** - 音乐生成
- **MCP 支持**: 已发布 MiniMax MCP Server，支持视频/图片/语音生成

### 2. Kimi (月之暗面 Moonshot)
- **官网**: https://kimi.moonshot.cn → https://www.kimi.com
- **定位**: 会推理解析，能深度思考的 AI 助手
- **特点**:
  - 长文本处理能力强
  - 支持文件上传和分析
  - 有 API 开放平台

### 3. GLM (智谱 AI)
- **官网**: https://open.bigmodel.cn
- **模型系列**:
  - GLM-4 系列
  - CodeGeeX - 代码生成模型
- **特点**:
  - 开放平台，API 接入
  - 支持多种应用场景

---

## 工具对比

| 工具 | 公司 | 开源 | 特色 | 适合场景 |
|------|------|------|------|----------|
| Claude Code | Anthropic | ❌ | IDE 集成好，Git 工作流 | 日常开发 |
| Codex CLI | OpenAI | ✅ | 轻量，ChatGPT 订阅可用 | 快速任务 |
| Kiro | AWS | ❌ | Spec-driven，自动化 | 企业项目 |
| Crush | Charm | ✅ | 多模型，MCP/LSP | 灵活切换 |
| Plandex | 独立 | ✅ | 大上下文，版本控制 | 大型项目 |

## 个人笔记

2026 年 AI 编程工具的趋势：
1. **Spec-driven** - Kiro 引领的"先规格后代码"理念
2. **多模型支持** - 不再绑定单一提供商
3. **MCP 生态** - 工具互联互通
4. **IDE 深度集成** - 不只是终端，更要融入开发环境
5. **自动化工作流** - Hooks、自动测试、自动文档

国内方面，MiniMax 的 MCP Server 是个亮点，说明国内厂商也在跟进 MCP 生态。
