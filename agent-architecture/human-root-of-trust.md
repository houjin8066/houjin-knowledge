# Human Root of Trust - 智能体问责框架

> 来源: https://humanrootoftrust.org/
> 日期: 2026-02-22
> 版本: v1.0 (February 2026)
> 许可: Public Domain

## 核心原则

**"Every agent must trace to a human."**
（每个智能体必须追溯到人类）

## 问题背景

商业互联网建立以来的所有数字系统都基于一个隐含假设：另一端有人类存在。

- 银行账户、合同、API 密钥 — 都围绕人类单一性概念设计
- 一个账户、一个人、一个可问责实体

**这个假设已经被打破：**
- AI 智能体现在可以自主浏览、交易、通信、协调
- 它们正在通过为人类设计的身份检查
- 执行金融交易、签署合同、管理基础设施
- 没有人类明显在循环中

**核心问题**: 没人知道哪个人类对智能体的行为负责

## 利益相关者的问题

| 角色 | 问题 |
|------|------|
| 监管者 | 谁对这个智能体的行为负责？ |
| 交易对手 | 这笔交易背后有真人吗？ |
| 审计员 | 展示从行动到授权到人类委托人的链条 |

**能回答这些问题的公司可以运营，不能的则不行。**

## 架构

### 信任链（Trust Chain）- 六步

1. **Human Principal** - 人类委托人
2. **Identity Verification** - 身份验证
3. **Authorization Grant** - 授权授予
4. **Agent Registration** - 智能体注册
5. **Action Logging** - 行动记录
6. **Audit Trail** - 审计追踪

### 双路径架构（Dual-Path Architecture）

框架支持两种路径：
- **Direct Path**: 人类直接控制智能体
- **Delegated Path**: 通过中间层委托控制

## 三大支柱

1. **Cryptographic Accountability** - 加密问责
2. **Trust Chain** - 信任链
3. **Open Framework** - 开放框架

## 意义

### 对智能体开发者
- 需要在设计中考虑问责机制
- 每个智能体行动都应可追溯

### 对企业
- 合规要求将越来越严格
- 提前建立问责架构是竞争优势

### 对监管
- 提供了可操作的框架基础
- 从原则到实现的桥梁

## 开放邀请

> "We are not the right people to finish this. No small group of people is."

框架在公共领域，概念可自由使用、扩展、实现和改进。

需要的贡献者：
- 安全工程师 - 发现并填补框架空白
- 密码学家 - 将信任链形式化为协议
- 律师 - 将问责架构映射到监管要求
- 实现者 - 构建第一个真实系统

## 与其他知识的关联

- **memory-layers**: 人类监督层与 Human Root of Trust 的问责原则一致
- **haribo-pattern**: 审计追踪可以作为压缩后的关键信息保留
- **多智能体系统**: 每个智能体都需要明确的人类委托人

## 参考

- 网站: https://humanrootoftrust.org/
- GitHub: https://github.com/humanrootoftrust
- 联系: hello@humanrootoftrust.org
