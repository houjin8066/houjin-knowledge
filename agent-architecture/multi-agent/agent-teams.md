# Agent Teams - 多智能体协作架构

> 来源：Claude Code 官方文档 + Anthropic 工程博客
> 更新：2026-02-06

## 概述

Agent Teams 是一种多智能体协作范式，允许多个 AI 实例并行工作、相互通信、共同完成复杂任务。

## 核心架构

```
┌─────────────────────────────────────────────────────────┐
│                      Agent Team                          │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────┐                                        │
│  │  Team Lead  │ ←── 协调、分配、综合                    │
│  └──────┬──────┘                                        │
│         │                                               │
│    ┌────┴────┬────────┬────────┐                       │
│    ▼         ▼        ▼        ▼                       │
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                   │
│ │ TM-1 │ │ TM-2 │ │ TM-3 │ │ TM-N │  ←── Teammates    │
│ └──┬───┘ └──┬───┘ └──┬───┘ └──┬───┘                   │
│    │        │        │        │                        │
│    └────────┴────┬───┴────────┘                        │
│                  ▼                                      │
│         ┌──────────────┐                               │
│         │  Shared Task │ ←── 任务列表 + 依赖管理        │
│         │     List     │                               │
│         └──────────────┘                               │
└─────────────────────────────────────────────────────────┘
```

## 与 Subagents 对比

| 特性 | Subagents | Agent Teams |
|------|-----------|-------------|
| 上下文 | 独立，结果返回调用者 | 独立，完全自主 |
| 通信 | 只能向主 agent 汇报 | Teammates 可直接通信 |
| 协调 | 主 agent 管理所有工作 | 共享任务列表 + 自协调 |
| 适用 | 聚焦任务，只需结果 | 需要讨论和协作的复杂工作 |
| Token | 较低（结果摘要返回） | 较高（每个都是独立实例） |

## 最佳实践

### 1. 适用场景
- ✅ 研究和代码审查（多角度并行）
- ✅ 新模块开发（各自负责独立部分）
- ✅ 竞争假设调试（并行测试不同理论）
- ✅ 跨层协调（前端/后端/测试分工）

### 2. 不适用场景
- ❌ 顺序依赖任务
- ❌ 同文件编辑
- ❌ 简单任务（协调开销 > 收益）

### 3. 任务设计原则
- **太小**：协调开销超过收益
- **太大**：工作太久没有检查点
- **刚好**：自包含单元，产出清晰交付物

### 4. 避免文件冲突
- 每个 teammate 负责不同文件集
- 使用 git 锁机制防止竞争

## 实战案例：C 编译器项目

Anthropic 使用 16 个并行 agent 构建了 10 万行 C 编译器：

### 关键技术
1. **无限循环 harness**：agent 完成一个任务立即开始下一个
2. **Docker 隔离**：每个 agent 独立容器
3. **Git 同步**：通过文件锁协调任务
4. **Oracle 对比**：用 GCC 作为正确性参照

### 专业化分工
- 主力 agent：解决核心编译问题
- 去重 agent：合并重复代码
- 性能 agent：优化编译器性能
- 质量 agent：改进代码结构
- 文档 agent：维护文档

### 成本
- ~2000 Claude Code sessions
- 20 亿输入 token + 1.4 亿输出 token
- ~$20,000 API 成本

## Harness Engineering

> "每次 agent 犯错，工程化解决方案防止再犯"

### 两种形式

1. **隐式提示（AGENTS.md）**
```markdown
# 常见错误修正
- 不要运行 `npm test`，使用 `npm run test:fast`
- API 文档在 /docs/api.md，不是 README
```

2. **工具脚本**
```bash
# 截图工具
./scripts/screenshot.sh

# 快速测试（1% 采样）
./scripts/test.sh --fast
```

### 为 LLM 设计环境
- **避免上下文污染**：限制输出行数，日志写文件
- **解决时间盲区**：打印增量进度，提供 --fast 选项
- **易于解析**：错误信息单行，便于 grep

## 参考链接

- [Claude Code Agent Teams 文档](https://code.claude.com/docs/en/agent-teams)
- [Building a C Compiler with Agent Teams](https://www.anthropic.com/engineering/building-c-compiler)
- [Mitchell Hashimoto's AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)
- [GitHub: Claude's C Compiler](https://github.com/anthropics/claudes-c-compiler)
