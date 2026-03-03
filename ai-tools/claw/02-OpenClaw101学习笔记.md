# OpenClaw 101 学习笔记

**来源**: github.com/mengjian-github/openclaw101
**日期**: 2026-03-03

---

## 一、什么是 OpenClaw 101？

OpenClaw 101 是一个**开源的 OpenClaw 资源聚合站**，旨在帮助中文用户快速上手 OpenClaw。

- 🌐 在线访问: openclaw101.dev
- 📚 资源聚合: 35+ 篇教程
- 📅 7天学习路径

---

## 二、收录来源

| 来源 | 类型 |
|------|------|
| 阿里云 | 钉钉接入、企业微信 AppFlow |
| 腾讯云 | 飞书接入、企业微信接入 |
| DigitalOcean | 一键部署、概览介绍 |
| Hostinger | VPS 部署教程 |
| Codecademy | 结构化安装教程 |
| B站 (Bilibili) | 视频教程 |
| 博客园 / CSDN | 飞书/Telegram 对接 |
| Reddit | 完整指南、技能分享 |

---

## 三、快速开始

```bash
# 克隆仓库
git clone https://github.com/mengjian-github/openclaw101.git
cd openclaw101

# 安装依赖
npm install

# 本地开发
npm run dev

# 构建
npm run build
```

---

## 四、项目结构

```
src/
├── app/
│   ├── page.tsx          # 首页
│   ├── resources/
│   │   └── page.tsx      # 资源聚合页
│   ├── layout.tsx        # 全局布局
│   └── globals.css       # 全局样式
├── components/
│   ├── Hero.tsx           # 首屏
│   ├── WhatIs.tsx         # 介绍
│   ├── LearningPath.tsx   # 7天学习路径
│   ├── Skills.tsx         # 技能推荐
│   └── ...
└── data/
    └── resources.ts       # 所有资源数据
```

---

## 五、资源分类

| 分类 | 说明 |
|------|------|
| `official` | 官方资源 |
| `getting-started` | 入门部署教程 |
| `channel-integration` | 平台接入 |
| `skill-dev` | 技能开发 |
| `video` | 视频教程 |
| `deep-dive` | 深度分析 |
| `tools` | 工具与插件 |
| `cloud-deploy` | 云平台部署 |

---

## 六、7天学习路径

| 天数 | 内容 |
|------|------|
| Day 1 | 认识 OpenClaw |
| Day 2 | 基础配置，连接飞书/Telegram |
| Day 3 | 模型配置，API Key 设置 |
| Day 4 | Skills 技能系统详解 |
| Day 5 | 工具使用：浏览器、Canvas |
| Day 6 | 自定义 Skill 开发 |
| Day 7 | 进阶：多 Agent、Cron 任务 |

---

## 七、技术栈

- Next.js 14
- TypeScript
- Tailwind CSS
- Cloudflare Pages

---

*学习资源来源：OpenClaw 101 项目*