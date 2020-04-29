#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import smtplib
import time
reload(sys)
sys.setdefaultencoding("UTF-8")
'''
__author__ == junguo
__time__ == 2019/6/25 21:02
__detail__ ==
'''


# 发送邮件
def send_mail_to_group(html_file):
    sender = 'guojun01@css.com.cn'
    username = 'guojun01'
    # 下面填邮箱密码
    password = "GJgj1204"
    msg_root = MIMEMultipart()
    msg_root['to'] = 'guojun01@css.com.cn'
    msg_root['Subject'] = u"UI自动化测试报告"
    log_file = open(html_file).read()
    html_body = ""
    html_body = html_body+log_file
    msg_text = MIMEText(html_body, 'html', 'utf-8')
    msg_root.attach(msg_text)

    time.sleep(2)
    smtp = smtplib.SMTP()
    smtp.connect('mail.css.com.cn')
    smtp.login(username, password)
    smtp.sendmail(sender, msg_root['to'], msg_root.as_string())
    smtp.quit()
