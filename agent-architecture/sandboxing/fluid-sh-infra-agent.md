# Fluid.sh：基础设施智能体沙箱模式

> 来源：https://www.fluid.sh/
> 学习日期：2026-02-05

## 核心理念

将 Claude Code 的体验带到基础设施运维领域：
- LLM 擅长生成 IaC，但不擅长猜测生产系统的实际状态
- 给智能体一个可以探索和测试的环境，提供更好的上下文
- 安全考虑：不希望 Claude Code 直接 SSH 到生产机器

## 工作流程

```
explore → plan → execute → export
扫描环境 → 制定策略 → 沙箱执行 → 生成 Playbook
```

1. **Explore**：扫描主机环境（OS、包、CLI 工具）
2. **Plan**：制定执行策略
3. **Execute**：在沙箱中运行命令
4. **Export**：生成 Ansible Playbook

## 安全机制

| 机制 | 说明 |
|------|------|
| 沙箱克隆 | 从 VM/K8s 创建隔离副本 |
| 临时 SSH 证书 | Ephemeral SSH Certificates |
| 工具锁定 | 只能在沙箱中运行 |
| 人工审批 | 创建沙箱、访问互联网、安装包 |

## 与其他方案的区别

**为什么不直接给 Claude Code 提供 MCP server/tools？**

安全。不希望 CC 从本地 SSH 到生产机器。Fluid 从架构层面隔离风险：
- 工具只能在沙箱中运行
- 智能体有自主创建沙箱的能力
- 但无法访问其他任何东西

## 输出物

- **Ansible Playbook**：可复现的基础设施配置
- **完整审计日志**：每个命令都被记录

## 安装

```bash
curl -fsSL https://fluid.sh/install.sh | bash
fluid
```

## 适用场景

- ✅ 调试生产环境问题
- ✅ 探索和理解现有基础设施
- ✅ 生成可复现的 IaC
- ✅ 安全地让 AI 操作基础设施

## 设计启示

1. **沙箱优先**：让智能体在隔离环境中工作
2. **上下文获取**：通过探索获取真实环境信息
3. **可审计**：所有操作都有记录
4. **可复现**：输出标准化的 IaC
