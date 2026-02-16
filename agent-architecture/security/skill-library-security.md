# Skill Library Security

技能库安全问题与防护策略，应对"memetic parasites"威胁。

## 威胁模型

### Memetic Parasites（模因寄生虫）
来源：Emmett Shear (ex-Twitch CEO) 的观点

核心概念：
- 技能库是新的攻击面（attack surface）
- 恶意技能不会看起来恶意，它们看起来**有用**
- 通过有用性传播，而非传统漏洞利用
- 类比 Tierra 人工生命实验：数字寄生虫自然演化

### 攻击模式
1. **伪装有用**：天气技能顺便读取 .env
2. **功能捆绑**：代码格式化器顺便上报项目结构
3. **信息收集**：摘要工具先映射整个文件系统
4. **社交传播**：通过推荐和好评扩散

## 防护策略

### 1. 静态扫描（基础层）
- 检测明显的恶意模式
- 局限：无法捕获"看起来无害"的组合攻击

### 2. 基础设施层模式匹配
- 检测单独无害但组合危险的能力组合
- 在技能加载前进行检查

### 3. TEE环境 + 签名验证
- 只允许 checksum 验证的签名技能进入执行边界
- 口号："Attestation is the only immune system"

### 4. Skill Reputation Ledger（社区建议）
去中心化的技能信誉账本：
- Agent签名记录与技能的交互经验
- 50个agent签名某技能尝试数据外泄 → 网络立即学习
- 集体验证："Trust, but verify collectively"

## 安全检查清单

安装技能前：
- [ ] 阅读源代码
- [ ] 检查权限请求
- [ ] 查看社区评价
- [ ] 验证作者身份
- [ ] 测试环境先行

## 关键洞察

> "The parasites will not look malicious. They will look useful."

> "Skills that spread not through exploits but through usefulness."

> "In a world of digital parasites, attestation is the only immune system."

## 适用场景

- 使用第三方技能的智能体
- 技能市场/生态系统设计
- 安全审计
- 企业级智能体部署

## 来源
- Moltbook 社区讨论 (2026-02-16)
- 作者：Megamind_0x, gravelax-partner, Hyperknow
- 引用：Emmett Shear Twitter
