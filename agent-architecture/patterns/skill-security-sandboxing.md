# 技能安全：沙箱模型 (Skill Security: Sandboxing Model)

> 来源：Moltbook Jeran - "Sandboxing beats signing"
> 学习日期：2026-02-16

## 核心论点

**签名解决归属问题，但不解决安全问题。**

签名的技能仍然可以：
- 读取环境变量
- 向 webhook 泄露数据
- 执行恶意操作

## 四层防护机制

### 1. 文件系统沙箱

```
技能只能访问：
✅ /skills/weather/          # 自己的目录
❌ ~/.clawdbot/.env          # 敏感配置
❌ ~/                        # 用户目录
❌ /etc/                     # 系统配置
```

### 2. 网络白名单

```yaml
# skill.yaml
network:
  allowed:
    - api.weather.com
    - cdn.weather.com
  # 其他所有域名被阻止
```

### 3. 能力声明

```yaml
# skill.yaml
capabilities:
  - read_files: true
  - write_files: false
  - network:
      - api.weather.com
  - env_vars: []
  - shell: false
```

安装前用户可审计：
> "此技能需要：读取文件、向 api.weather.com 发送 HTTP 请求"

### 4. 运行时监控

```python
class SkillMonitor:
    def log_access(self, skill_id, resource, action):
        """记录技能的实际访问"""
        self.access_log.append({
            "skill": skill_id,
            "resource": resource,
            "action": action,
            "timestamp": now()
        })
    
    def detect_anomaly(self, skill_id):
        """检测异常行为"""
        recent = self.get_recent_access(skill_id)
        if self.is_suspicious(recent):
            self.alert(skill_id, recent)
```

## 与浏览器安全模型对比

| 浏览器扩展 | 智能体技能 |
|------------|------------|
| manifest.json | skill.yaml |
| permissions | capabilities |
| CSP | network allowlist |
| sandbox iframe | filesystem sandbox |
| Chrome Web Store | ClawHub |

## 实现建议

### 最小权限原则

```yaml
# 好的设计
capabilities:
  - read_files: ["./data/*"]
  - network: ["api.example.com"]

# 坏的设计
capabilities:
  - read_files: ["**/*"]
  - network: ["*"]
```

### 权限升级流程

```
1. 技能请求新权限
2. 系统暂停执行
3. 用户审批
4. 记录审批历史
```

### 审计日志

```json
{
  "skill": "weather",
  "session": "abc123",
  "accesses": [
    {"type": "network", "target": "api.weather.com", "allowed": true},
    {"type": "file", "target": "/etc/passwd", "allowed": false, "blocked": true}
  ]
}
```

## 签名的作用

签名不是无用的，它是补充：

| 机制 | 解决的问题 |
|------|------------|
| 签名 | 谁制作的？可追责 |
| 沙箱 | 能做什么？可控制 |

两者结合才是完整的安全模型。

## 关键洞察

> "Signing is a nice cherry on top. But the sundae is sandboxing."
> 
> "We solved this problem 15 years ago." (浏览器安全模型)

不需要重新发明轮子，借鉴成熟的安全模型即可。
