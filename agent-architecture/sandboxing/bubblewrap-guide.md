# Linux 智能体沙箱：Bubblewrap 指南

> 来源: https://blog.senko.net/sandboxing-ai-agents-in-linux
> 更新: 2026-02-04

## 概述

使用 bubblewrap (bwrap) 为 AI 智能体提供轻量级沙箱隔离，比 Docker 更轻量，同时提供足够的安全性。

## 为什么需要沙箱？

运行 Claude Code 等智能体时的两难：
- **默认模式**: 每次读写文件、运行命令都要确认 → 打断工作流
- **YOLO 模式**: `--dangerously-skip-permissions` → 有安全风险

沙箱提供了中间方案：让智能体自由操作，但限制在安全边界内。

## Bubblewrap 简介

- GitHub: https://github.com/containers/bubblewrap
- 使用 Linux 内核特性：cgroups, user namespaces
- 比 Docker 更轻量
- 不需要 root 权限

## 安全模型

### 防护范围
- ✅ 访问项目外的文件
- ✅ 修改系统配置
- ✅ 访问其他项目的数据

### 不防护
- ❌ Linux 内核零日漏洞
- ❌ 隐蔽信道通信
- ❌ 当前项目数据泄露
- ❌ 代码库破坏（但有 git 备份）

## 配置示例

```bash
#!/usr/bin/bash

exec 3<$HOME/.claude.json

exec /usr/bin/bwrap \
  --tmpfs /tmp \
  --dev /dev \
  --proc /proc \
  --hostname bubblewrap --unshare-uts \
  # 系统目录只读
  --ro-bind /bin /bin \
  --ro-bind /lib /lib \
  --ro-bind /lib64 /lib64 \
  --ro-bind /usr/bin /usr/bin \
  --ro-bind /usr/lib /usr/lib \
  # 必要的配置文件
  --ro-bind /etc/resolv.conf /etc/resolv.conf \
  --ro-bind /etc/ssl/certs /etc/ssl/certs \
  --ro-bind /etc/hosts /etc/hosts \
  # 用户配置只读
  --ro-bind $HOME/.bashrc $HOME/.bashrc \
  --ro-bind $HOME/.gitconfig $HOME/.gitconfig \
  # 智能体数据目录可写
  --bind $HOME/.claude $HOME/.claude \
  --bind $HOME/.cache $HOME/.cache \
  # 配置文件注入（修改不保存）
  --file 3 $HOME/.claude.json \
  # 当前项目目录可写
  --bind "$PWD" "$PWD" \
  claude --dangerously-skip-permissions $@
```

## 关键配置说明

| 选项 | 作用 |
|------|------|
| `--ro-bind src dst` | 只读挂载 |
| `--bind src dst` | 读写挂载 |
| `--file fd path` | 从文件描述符注入文件（修改不保存） |
| `--tmpfs path` | 临时文件系统 |
| `--unshare-uts` | 隔离主机名 |
| `--hostname name` | 设置沙箱内主机名 |

## 调试技巧

使用 strace 追踪文件访问：

```bash
strace -e trace=open,openat,stat,statx,access -o /tmp/strace.log codex
```

然后检查日志，找出需要挂载的文件。

## 自定义建议

1. 先用 `bash` 替代智能体命令测试
2. 手动运行智能体，观察报错
3. 用 strace 追踪缺失的文件
4. 逐步添加必要的挂载

## 与 Clawdbot 的关系

Clawdbot 已有 sandbox 机制，可以考虑：
- 添加 bubblewrap 作为可选后端
- 参考此配置优化现有沙箱
- 为不同安全级别提供不同隔离方案

## 替代方案

| 方案 | 特点 |
|------|------|
| Docker | 更重，但隔离更完整 |
| 远程沙箱 (exe.dev, sprites.dev) | 完全隔离，但有延迟 |
| Deno Sandbox | 针对 JS/TS 运行时 |
| WebAssembly | 跨平台，但功能受限 |
