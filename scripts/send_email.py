#!/usr/bin/env python3
"""
AI知识库邮件发送脚本
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

# QQ邮箱SMTP配置
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 465
SENDER_EMAIL = "houjin8066@qq.com"
SENDER_PASSWORD = "gpygddbireelbihf"
RECEIVER_EMAIL = "houjin8066@qq.com"

def send_digest_email(subject: str, content: str) -> bool:
    """发送摘要邮件"""
    try:
        # 创建邮件
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = SENDER_EMAIL
        message["To"] = RECEIVER_EMAIL

        # 添加纯文本和HTML内容
        text_part = MIMEText(content, "plain", "utf-8")
        message.attach(text_part)

        # 使用SSL连接发送
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        
        print(f"✅ 邮件发送成功: {subject}")
        return True
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        return False

def read_today_digest() -> str:
    """读取今日摘要"""
    today = datetime.now()
    digest_path = f"/root/clawd/knowledge/daily-digests/{today.year}/{today.month:02d}/{today.strftime('%Y-%m-%d')}.md"
    
    if os.path.exists(digest_path):
        with open(digest_path, "r", encoding="utf-8") as f:
            return f.read()
    return None

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 3:
        # 自定义标题和文件路径: python3 send_email.py "标题" "文件路径"
        subject = sys.argv[1]
        file_path = sys.argv[2]
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            send_digest_email(subject, content)
        else:
            print(f"❌ 文件不存在: {file_path}")
    elif len(sys.argv) > 1 and sys.argv[1] == "test":
        # 测试发送
        send_digest_email(
            "🦞 测试邮件 - AI知识库",
            "这是一封测试邮件，说明邮件配置成功！\n\n—— 龙虾"
        )
    else:
        # 发送今日摘要
        content = read_today_digest()
        if content:
            today = datetime.now().strftime("%Y年%m月%d日")
            send_digest_email(f"🤖 AI知识库每日摘要 - {today}", content)
        else:
            print("今日摘要不存在")
