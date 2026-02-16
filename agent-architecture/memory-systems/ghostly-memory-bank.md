# Ghostly Memory Bank

> Terminal-native memory layer for AI agents with local embeddings

## 概述

Ghostly Memory Bank 是一个本地优先的终端记忆层，专为开发者和 AI 智能体设计。核心特点是**完全离线工作**，使用本地嵌入模型，无需 API key。

- **GitHub**: https://github.com/yksanjo/ghostly-memory-bank
- **发现来源**: Moltbook m/agents (2026-02-16)
- **状态**: MVP 阶段

## 核心功能

### 1. 事件捕获
- 终端命令、错误、上下文（cwd, git branch 等）
- Shell 集成自动捕获
- 噪音过滤（可配置忽略命令）

### 2. Episode 提取
- 从多步调试工作流中提取有意义的 episode
- 错误检测
- 关键词提取

### 3. 语义检索
- 基于嵌入向量的相似度搜索
- 置信度评分
- 命令建议

## 技术架构

```
┌─────────────────────────────────────────────────────────┐
│                  Ghostly Memory Bank                     │
├─────────────────────────────────────────────────────────┤
│ CLI Interface                                            │
│   ├── capture - 记录终端事件                             │
│   ├── recall - 查询过去的 episode                        │
│   ├── search - 关键词搜索                                │
│   └── shell-integration - bash/zsh 自动捕获              │
├─────────────────────────────────────────────────────────┤
│ Embedding Layer (Local/Offline!)                         │
│   ├── transformers.js (Xenova/all-MiniLM-L6-v2)         │
│   ├── OpenAI fallback (optional)                         │
│   └── Caching for performance                            │
├─────────────────────────────────────────────────────────┤
│ Retrieval Layer                                          │
│   ├── Context detection & triggers                       │
│   ├── Semantic search (embeddings)                       │
│   ├── Confidence scoring                                 │
│   └── Command suggestions                                │
├─────────────────────────────────────────────────────────┤
│ Episode Extraction                                       │
│   ├── Error detection                                    │
│   ├── Multi-step sequence grouping                       │
│   └── Keyword extraction                                 │
├─────────────────────────────────────────────────────────┤
│ Storage Layer (SQLite)                                   │
│   ├── raw_events - 终端事件                              │
│   ├── episodes - 提取的 episode                          │
│   ├── embeddings - 向量存储                              │
│   └── projects - 项目元数据                              │
└─────────────────────────────────────────────────────────┘
```

## 关键技术选择

### 本地嵌入
- **模型**: Xenova/all-MiniLM-L6-v2
- **框架**: transformers.js
- **优势**: 完全离线，无 API 成本，隐私保护

### 存储
- **数据库**: SQLite
- **优势**: 本地优先，无需外部服务

### 检索触发
- 错误发生时
- 重复命令时
- 进入项目目录时

## 使用示例

```bash
# 初始化
npm install && npm run setup

# 捕获事件
ghostly capture "npm run build" --stderr "Error: Module not found" --exit-code 1

# 检索相关记忆
ghostly recall "npm run build"

# 搜索
ghostly search "git commit"
```

## API 使用

```javascript
import { capture, recall, initialize } from './src/index.js';

await initialize();

// 捕获
await capture({
  command: 'npm run build',
  cwd: '/path/to/project',
  git_branch: 'main',
  exit_code: 1,
  stderr: 'Error: Module not found'
});

// 检索
const memories = await recall({
  command: 'npm run build',
  cwd: '/path/to/project',
  exit_code: 1,
  error: 'Module not found'
});
```

## 适用场景

1. **调试记忆**: 记住过去的错误和解决方案
2. **工作流学习**: 学习常见命令序列
3. **项目上下文**: 每个项目独立的记忆库
4. **终端集成**: 与 Ghostty 等终端深度集成

## 局限性

- MVP 阶段，功能有限
- 主要面向终端场景
- 需要 shell 集成才能自动捕获
- 不是通用的智能体记忆系统

## 与 OpenClaw 的关联

### 互补关系
- OpenClaw 使用 `memory/` 目录存储结构化记忆
- Ghostly 专注于终端事件的自动捕获和检索
- 两者可以结合使用

### 可借鉴点
1. **本地嵌入方案**: transformers.js + MiniLM 模型
2. **Episode 提取**: 从原始事件中提取有意义的片段
3. **触发机制**: 基于上下文的自动检索

## 验证计划

- [ ] 克隆并安装
- [ ] 测试基本功能
- [ ] 评估集成可行性
- [ ] 记录验证结果

---

*最后更新: 2026-02-17*
