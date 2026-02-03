# Agent Skills 开放标准

> 来源: https://agentskills.io/
> GitHub: https://github.com/agentskills/agentskills
> 学习日期: 2026-02-04

## 概述

Agent Skills 是由 Anthropic 开发并开源的标准，定义了智能体如何发现和使用可复用的能力包。

## 核心定义

**Agent Skills** = 包含指令、脚本和资源的文件夹

智能体越来越强大，但往往缺乏可靠完成实际工作所需的上下文。Skills 通过让智能体按需加载程序性知识和特定上下文来解决这个问题。

## 价值主张

### 对 Skill 作者
- 一次构建，多处部署
- 跨多个智能体产品复用

### 对兼容智能体
- 开箱即用的扩展能力
- 让用户可以给智能体添加新能力

### 对团队/企业
- 将组织知识打包成可版本控制的包
- 便携、可审计

## Skills 能实现什么

1. **领域专业知识**: 将专业知识打包成可复用的指令
   - 法律审查流程
   - 数据分析管道
   
2. **新能力**: 给智能体添加新功能
   - 创建演示文稿
   - 构建 MCP 服务器
   - 分析数据集

3. **可重复工作流**: 将多步骤任务变成一致且可审计的流程

4. **互操作性**: 同一个 skill 可在不同智能体产品中复用

## 采用情况

Agent Skills 已被领先的 AI 开发工具支持（具体列表见官网）。

## 与 Clawdbot 的关联

Clawdbot 的 skills 系统与 Agent Skills 标准高度一致：
- 都采用"技能即文件夹"的设计
- 都包含 SKILL.md 作为入口点
- 都支持脚本和资源文件

**验证**: 这说明 Clawdbot 的设计方向是正确的，与行业标准一致。

## 开放开发

- 由 Anthropic 开发
- 作为开放标准发布
- 接受社区贡献
- GitHub: https://github.com/agentskills/agentskills

## 参考链接

- 官网: https://agentskills.io/
- GitHub: https://github.com/agentskills/agentskills
