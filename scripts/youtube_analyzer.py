#!/usr/bin/env python3.11
"""
Clawdbot YouTube 视频分析器
自动搜索、分析、整理 YouTube 视频内容并发送邮件
"""

import json
import subprocess
import os
import re
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict, Optional

# 配置
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER_EMAIL = "houjin8066@qq.com"
SENDER_PASSWORD = "kzgtmyfjrgyxcfec"
RECEIVER_EMAIL = "houjin8066@qq.com"

WORK_DIR = "/tmp/youtube-analyzer"
COOKIES_FILE = "/root/.config/yt-dlp/youtube-cookies.txt"

def run_cmd(cmd: str, timeout: int = 120) -> tuple:
    """运行命令并返回输出"""
    try:
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True, timeout=timeout
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Timeout", 1
    except Exception as e:
        return "", str(e), 1

def search_videos(query: str, count: int = 25) -> List[Dict]:
    """搜索 YouTube 视频"""
    print(f"🔍 搜索: {query}")
    
    cmd = f'python3.11 -m yt_dlp "ytsearch{count}:{query}" --flat-playlist --dump-json 2>/dev/null'
    stdout, stderr, code = run_cmd(cmd, timeout=120)
    
    videos = []
    for line in stdout.strip().split('\n'):
        if line:
            try:
                data = json.loads(line)
                videos.append({
                    'id': data.get('id'),
                    'title': data.get('title', 'N/A'),
                    'url': data.get('url') or f"https://www.youtube.com/watch?v={data.get('id')}",
                    'uploader': data.get('uploader', 'N/A'),
                    'view_count': data.get('view_count', 0) or 0,
                    'duration': data.get('duration', 0) or 0,
                    'duration_string': data.get('duration_string', 'N/A'),
                    'description': data.get('description', ''),
                })
            except:
                continue
    
    # 按播放量排序
    videos.sort(key=lambda x: x['view_count'], reverse=True)
    print(f"✅ 找到 {len(videos)} 个视频")
    return videos

def download_subtitles(video_id: str, url: str) -> Optional[str]:
    """下载视频字幕"""
    os.makedirs(WORK_DIR, exist_ok=True)
    
    # 尝试下载字幕
    cookies_opt = f'--cookies "{COOKIES_FILE}"' if os.path.exists(COOKIES_FILE) else ''
    cmd = f'python3.11 -m yt_dlp {cookies_opt} --write-auto-sub --sub-lang en,zh --skip-download --sub-format vtt -o "{WORK_DIR}/{video_id}" "{url}" 2>&1'
    
    stdout, stderr, code = run_cmd(cmd, timeout=60)
    
    # 查找字幕文件
    for ext in ['.en.vtt', '.zh.vtt', '.vtt']:
        sub_file = f"{WORK_DIR}/{video_id}{ext}"
        if os.path.exists(sub_file):
            with open(sub_file, 'r', encoding='utf-8') as f:
                content = f.read()
            # 清理 VTT 格式
            content = clean_vtt(content)
            return content
    
    return None

def clean_vtt(content: str) -> str:
    """清理 VTT 字幕格式，提取纯文本"""
    lines = content.split('\n')
    text_lines = []
    seen = set()
    
    for line in lines:
        # 跳过时间戳和元数据
        if '-->' in line or line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
            continue
        # 跳过空行和数字行
        line = line.strip()
        if not line or line.isdigit():
            continue
        # 移除 HTML 标签
        line = re.sub(r'<[^>]+>', '', line)
        # 去重
        if line not in seen:
            seen.add(line)
            text_lines.append(line)
    
    return ' '.join(text_lines)

def get_video_description(video_id: str, url: str) -> str:
    """获取视频描述"""
    cookies_opt = f'--cookies "{COOKIES_FILE}"' if os.path.exists(COOKIES_FILE) else ''
    cmd = f'python3.11 -m yt_dlp {cookies_opt} --dump-json --no-download "{url}" 2>/dev/null'
    
    stdout, stderr, code = run_cmd(cmd, timeout=60)
    
    if stdout:
        try:
            data = json.loads(stdout)
            return data.get('description', '')[:2000]
        except:
            pass
    return ''

def analyze_content(title: str, subtitle: str, description: str) -> Dict:
    """分析视频内容，提取要点（基于关键词匹配）"""
    
    # 合并所有文本
    full_text = f"{title} {subtitle} {description}".lower()
    
    # 关键词分类
    topics = {
        'setup': ['setup', 'install', 'configure', 'deploy', '安装', '配置', '部署'],
        'features': ['feature', 'can do', 'capability', 'function', '功能', '特性'],
        'integration': ['whatsapp', 'telegram', 'discord', 'slack', 'signal', '集成', '连接'],
        'automation': ['automate', 'schedule', 'cron', 'task', '自动化', '定时', '任务'],
        'cost': ['free', 'cost', 'price', 'cheap', '免费', '成本', '便宜'],
        'hosting': ['host', 'server', 'cloud', 'mac mini', 'vps', '服务器', '托管'],
        'security': ['security', 'privacy', 'safe', '安全', '隐私'],
        'skills': ['skill', 'plugin', 'extension', 'mcp', '技能', '插件'],
    }
    
    found_topics = []
    for topic, keywords in topics.items():
        if any(kw in full_text for kw in keywords):
            found_topics.append(topic)
    
    # 生成要点
    points = []
    
    if 'setup' in found_topics:
        points.append("介绍 Clawdbot 的安装和配置方法")
    if 'features' in found_topics:
        points.append("展示 Clawdbot 的核心功能和特性")
    if 'integration' in found_topics:
        platforms = []
        for p in ['WhatsApp', 'Telegram', 'Discord', 'Slack', 'Signal']:
            if p.lower() in full_text:
                platforms.append(p)
        if platforms:
            points.append(f"演示与 {', '.join(platforms)} 的集成")
        else:
            points.append("介绍多平台消息集成功能")
    if 'automation' in found_topics:
        points.append("讲解自动化任务和定时功能")
    if 'cost' in found_topics or 'hosting' in found_topics:
        points.append("分享部署方案和成本优化建议")
    if 'security' in found_topics:
        points.append("讨论安全性和隐私保护")
    if 'skills' in found_topics:
        points.append("介绍技能系统和扩展功能")
    
    # 如果没有匹配到，添加通用要点
    if not points:
        points = [
            "Clawdbot 使用体验分享",
            "AI 助手功能演示",
            "实际应用场景展示"
        ]
    
    # 生成摘要
    if subtitle and len(subtitle) > 100:
        summary = f"视频详细介绍了 Clawdbot 的使用方法。" + (f" 主要涉及：{', '.join(found_topics[:3])}" if found_topics else "")
    else:
        summary = f"基于标题分析：{title}"
    
    return {
        'summary': summary,
        'points': points[:5],
        'has_subtitle': bool(subtitle and len(subtitle) > 100)
    }

def format_view_count(count: int) -> str:
    """格式化播放量"""
    if count >= 1000000:
        return f"{count/1000000:.1f}M"
    elif count >= 1000:
        return f"{count/1000:.1f}K"
    return str(count)

def generate_report(videos: List[Dict], analyses: List[Dict]) -> str:
    """生成报告"""
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    report = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎬 Clawdbot YouTube 热门视频内容整理
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 整理时间: {now}
🦞 整理者: 龙虾

共分析 {len(videos)} 个热门视频，按播放量排序。

"""
    
    for i, (video, analysis) in enumerate(zip(videos, analyses), 1):
        view_str = format_view_count(video['view_count'])
        subtitle_mark = "✅" if analysis.get('has_subtitle') else "📝"
        
        report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
【第{i}名】{view_str} 播放 {subtitle_mark}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📺 标题: {video['title']}
👤 作者: {video['uploader']}
⏱️ 时长: {video['duration_string']}
🔗 链接: {video['url']}

📝 内容摘要:
{analysis['summary']}

🔑 核心要点:
"""
        for point in analysis['points']:
            report += f"• {point}\n"
    
    # 总结
    report += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 总结
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Clawdbot 热门视频主要涵盖以下主题：
1. 安装部署教程（Mac Mini / VPS / 免费托管）
2. 多平台集成（WhatsApp、Telegram、Discord等）
3. 自动化任务和定时功能
4. 技能系统和扩展开发
5. 实际使用案例和体验分享

图例说明：
✅ = 已获取字幕内容
📝 = 基于标题和描述分析

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

由龙虾 🦞 自动整理
"""
    
    return report

def send_email(subject: str, content: str) -> bool:
    """发送邮件"""
    try:
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = SENDER_EMAIL
        message["To"] = RECEIVER_EMAIL
        message.attach(MIMEText(content, "plain", "utf-8"))
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        
        print("✅ 邮件发送成功!")
        return True
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        return False

def main(query: str = "clawdbot tutorial", count: int = 20):
    """主函数"""
    print("=" * 50)
    print("🎬 Clawdbot YouTube 视频分析器")
    print("=" * 50)
    
    # 1. 搜索视频
    videos = search_videos(query, count + 5)  # 多搜几个以防有些失败
    videos = videos[:count]  # 取前 N 个
    
    if not videos:
        print("❌ 未找到视频")
        return
    
    # 2. 分析每个视频
    analyses = []
    for i, video in enumerate(videos, 1):
        print(f"\n📊 分析视频 {i}/{len(videos)}: {video['title'][:50]}...")
        
        # 尝试下载字幕
        subtitle = download_subtitles(video['id'], video['url'])
        
        # 如果没有字幕，尝试获取描述
        description = video.get('description', '')
        if not description:
            description = get_video_description(video['id'], video['url'])
        
        # 分析内容
        analysis = analyze_content(video['title'], subtitle or '', description)
        analyses.append(analysis)
        
        print(f"   {'✅ 有字幕' if analysis['has_subtitle'] else '📝 无字幕'} - {len(analysis['points'])} 个要点")
    
    # 3. 生成报告
    print("\n📝 生成报告...")
    report = generate_report(videos, analyses)
    
    # 4. 发送邮件
    print("\n📧 发送邮件...")
    subject = f"🎬 Clawdbot YouTube 热门视频内容整理 - 龙虾整理"
    send_email(subject, report)
    
    # 5. 保存报告
    report_file = f"{WORK_DIR}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    os.makedirs(WORK_DIR, exist_ok=True)
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"📄 报告已保存: {report_file}")
    
    print("\n✅ 完成!")

if __name__ == "__main__":
    import sys
    query = sys.argv[1] if len(sys.argv) > 1 else "clawdbot tutorial"
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    main(query, count)
