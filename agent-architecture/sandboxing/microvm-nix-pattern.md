# 编码智能体沙箱：NixOS + microvm.nix 模式

> 来源：https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/
> 学习日期：2026-02-05

## 核心理念

编码智能体需要安全的隔离环境，避免：
1. 访问私人文件
2. 被恶意软件攻击后影响主机

解决方案：**临时虚拟机**（Ephemeral VMs）
- 不持久化任何内容，除非显式共享
- 被攻击后直接销毁重建

## 威胁模型

引用 Simon Willison 的"致命三角"（Lethal Trifecta）：
- **私人数据**（Private data）
- **不可信内容**（Untrusted content）
- **外部通信**（External communication）

本方案通过**移除私人数据**来降低风险。

## 技术架构

### 网络配置
```nix
# 创建独立网桥
systemd.network.netdevs."20-microbr".netdevConfig = {
  Kind = "bridge";
  Name = "microbr";
};

# 使用 NAT 隔离
networking.nat = {
  enable = true;
  internalInterfaces = [ "microbr" ];
  externalInterface = "eno1";
};
```

### 共享目录设计
| 目录 | 用途 |
|------|------|
| workspace | 工作目录（如 ~/microvm/emacs） |
| /nix/store | 主机 Nix store（利用缓存） |
| SSH host keys | 保持身份一致 |
| claude-microvm | 智能体状态目录 |

### 资源配置
- 8 vCPU
- 4 GB RAM
- 8 GB 磁盘 overlay（存储在 /var/lib/microvms/）
- Hypervisor: cloud-hypervisor 或 QEMU

## 适用场景

- ✅ 学习陌生代码库架构
- ✅ 诊断 bug
- ✅ 开发 PoC
- ✅ 让智能体自主运行命令（无需逐条审批）

## 局限性

- ❌ 需要 NixOS 环境
- ❌ 配置复杂度较高
- ❌ 需要一定的系统资源

## 相关资源

- [microvm.nix 项目](https://github.com/microvm-nix/microvm.nix)
- [Simon Willison: The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
- [Luis Cardoso: A field guide to sandboxes for AI](https://www.luiscardoso.dev/blog/sandboxes-for-ai)
- 商业方案：[exe.dev](https://blog.exe.dev/meet-exe.dev), [Fly.io Sprites](https://fly.io/blog/code-and-let-live/)
