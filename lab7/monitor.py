#!/usr/bin/env python3
"""
Lab 7: Crontab in Linux
Python script that logs system info and sends an email report to the server owner.
Designed to be run via cron job.
"""

import smtplib
import platform
import psutil
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "owner@example.com"

LOG_FILE = "/tmp/monitor.log"


def get_system_info() -> str:
    """Collect basic system stats."""
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return (
        f"System Report — {now}\n"
        f"Host:       {platform.node()}\n"
        f"OS:         {platform.system()} {platform.release()}\n"
        f"CPU usage:  {cpu}%\n"
        f"RAM usage:  {mem.percent}% ({mem.used // 1024 ** 2} MB / {mem.total // 1024 ** 2} MB)\n"
        f"Disk usage: {disk.percent}% ({disk.used // 1024 ** 3} GB / {disk.total // 1024 ** 3} GB)\n"
    )


def write_log(info: str) -> None:
    """Append report to local log file."""
    with open(LOG_FILE, "a") as f:
        f.write(info + "\n" + "-" * 40 + "\n")


def send_email(info: str) -> None:
    """Send system report via email."""
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = f"Server Monitor Report — {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
    msg.attach(MIMEText(info, "plain"))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())


if __name__ == "__main__":
    info = get_system_info()
    write_log(info)
    print(info)
    # Uncomment to enable email sending:
    # send_email(info)
