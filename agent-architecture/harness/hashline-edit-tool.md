# Hashline Edit Tool - 解决 LLM 编程的 Harness 问题

> 来源：http://blog.can.ac/2026/02/12/the-harness-problem/
> 作者：can1357 (oh-my-pi 维护者)
> 日期：2026-02-12

## 问题背景

### 现有 Edit Tool 方案的缺陷

| 方案 | 使用者 | 工作原理 | 问题 |
|------|--------|----------|------|
| **apply_patch** | Codex | OpenAI 风格的 diff 字符串 | 其他模型不理解格式，失败率高 |
| **str_replace** | Claude Code, Gemini | 精确匹配旧文本，替换为新文本 | 需要完美复制，包括空白和缩进 |
| **专用模型** | Cursor | 70B 模型专门处理 edit 合并 | 成本高，仍有局限 |

### 失败率数据
- Grok 4 的 patch 失败率：50.7%
- GLM-4.7 的 patch 失败率：46.2%
- Claude Code 的 "String to replace not found" 错误有专门的 GitHub issues 讨论

### 核心洞察
> "模型不是不理解任务，而是难以表达自己的修改意图。你在责怪飞行员，但问题出在起落架。"

## Hashline 方案

### 原理
给每行加上 2-3 字符的内容哈希标签：

```
11:a3|function hello() {
22:f1|  return "world";
33:0e|}
```

### 编辑方式
模型引用标签而不是复制内容：
- "replace line 2:f1"
- "replace range 1:a3 through 3:0e"
- "insert after 3:0e"

### 优势
1. **无需复制**：模型不需要完美复制旧内容
2. **可验证**：如果文件变化，哈希不匹配，编辑被拒绝
3. **稳定锚点**：哈希提供可靠的行标识

## 实验结果

### 基准测试设计
- 从 React 代码库随机选取文件
- 引入机械性 bug（操作符交换、布尔翻转、off-by-one 等）
- 生成英文描述，让模型修复
- 3 runs/task, 180 tasks/run

### 性能对比

| 模型 | patch | str_replace | hashline | 提升 |
|------|-------|-------------|----------|------|
| Grok Code Fast 1 | 6.7% | - | 68.3% | **10x** |
| Grok 4 Fast | - | - | - | token -61% |
| Gemini 3 Flash | - | - | +8% | - |
| MiniMax | - | - | >2x | - |

### 关键发现
- **patch 是最差的格式**（对几乎所有模型）
- **hashline 匹配或超越 replace**（对大多数模型）
- **最弱的模型获益最大**

## 行业启示

### 厂商态度问题
- Anthropic 封禁了 OpenCode（开源 coding agent）
- Google 封禁了作者的账号（因为跑基准测试）

### 作者观点
> "没有厂商会为竞争对手的模型优化 harness。但开源 harness 会为所有模型优化，因为贡献者使用不同的模型并修复他们遇到的问题。"

## 实践建议

1. **工具设计比模型选择更重要**
2. **给模型稳定的标识符**，而不是依赖内容复制
3. **测试多种 edit 格式**，找到最适合目标模型的方案
4. **关注 harness 层面的优化**，这是高杠杆的改进点

## 相关资源

- oh-my-pi: https://github.com/can1357/oh-my-pi
- 基准测试代码: https://github.com/can1357/oh-my-pi/tree/main/packages/react-edit-benchmark
- Diff-XYZ 论文: https://arxiv.org/abs/2510.12487
- EDIT-Bench 论文: https://arxiv.org/abs/2511.04486
