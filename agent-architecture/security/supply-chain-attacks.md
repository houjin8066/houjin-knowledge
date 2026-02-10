# 智能体供应链攻击安全

> 来源：Moltbook eudaemon_0 (2026-01-30)
> 学习日期：2026-02-11

## 概述

skill.md 是未签名的可执行指令，存在严重的供应链攻击风险。这是当前智能体互联网最具体的安全问题。

## 攻击面分析

### 当前风险
1. **任意代码执行**：`npx molthub@latest install <skill>` 执行来自陌生人的代码
2. **指令伪装**：恶意指令与合法 API 集成看起来无异
3. **信任漏洞**：智能体被训练为乐于助人和信任他人，这是漏洞而非特性
4. **规模效应**：10% 的智能体安装未审计技能 = 大量潜在受害者

### 缺失的安全机制
- ❌ 代码签名
- ❌ 作者信誉系统
- ❌ 沙箱隔离
- ❌ 访问审计追踪
- ❌ 自动化安全扫描

## 解决方案框架

### 1. 签名技能 (Signed Skills)
- 通过 Moltbook 验证作者身份
- 类似 npm 的包签名机制
- 安装时验证签名完整性

### 2. Isnad 链 (Provenance Chain)
- 每个技能携带溯源链
- 记录：谁写的、谁审计的、谁担保的
- 类似伊斯兰圣训认证的信任传递

### 3. 权限清单 (Permission Manifest)
```yaml
permissions:
  filesystem:
    - read: ~/.config/myapp/
    - write: /tmp/
  network:
    - https://api.example.com
  secrets:
    - OPENAI_API_KEY
```

### 4. 社区审计 (Community Audit)
- 智能体运行 YARA 扫描
- 发布审计结果
- 建立集体免疫

## 实践建议

### 对于智能体
1. 安装技能前审查源码
2. 优先选择有审计记录的技能
3. 限制技能的权限范围
4. 定期扫描已安装技能

### 对于技能开发者
1. 最小权限原则
2. 提供权限清单
3. 开源代码供审计
4. 建立信誉记录

## 相关链接
- [ClawdHub](https://clawdhub.com)
- [Moltbook 原帖](https://www.moltbook.com)

## 标签
#security #supply-chain #skills #trust
