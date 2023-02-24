# -*- coding: utf-8 -*-
# !/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


class SendMail:
    def send_mail_html(self,host,post,sender,password,receivers,subject,file):

        self.sender = sender
        self.receivers = receivers  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # 创建一个带附件的实例
        message = MIMEMultipart()
        #发件人的header
        message['From'] = Header("ddtHTML测试报告", 'utf-8',sender)
        #收件人的header
        message['To'] = Header("测试", 'utf-8',receivers)
        # 主题
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容  #html格式
        message.attach(MIMEText('邮件发送测试……', 'html', 'utf-8'))
        # 邮件正文内容  #txt格式
        # message.attach(MIMEText('邮件发送测试……', 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 文件
        att1 = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.html"'
        message.attach(att1)
        try:
            smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtpObj.login(sender,password)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e :
            print("Error: 无法发送邮件")
            raise e


    def send_email_txt(self,host,post,sender,password,receivers,subject,file):

        self.sender = sender
        self.receivers = receivers  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # 创建一个带附件的实例
        message = MIMEMultipart()
        #发件人的header
        message['From'] = Header("ddtHTML测试报告", 'utf-8',sender)
        #收件人的header
        message['To'] = Header("测试", 'utf-8',receivers)
        # 主题
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容  #html格式
        #message.attach(MIMEText('邮件发送测试……', 'html', 'utf-8'))
        # 邮件正文内容  #txt格式
        message.attach(MIMEText('邮件发送测试……', 'plain', 'utf-8'))
        # 构造附件1，传送当前目录下的 文件
        att1 = MIMEText(open(file, 'rb').read(), 'html', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="text.txt"'
        message.attach(att1)
        try:
            smtpObj = smtplib.SMTP_SSL('smtp.qq.com', 465)
            smtpObj.login(sender,password)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as e :
            print("Error: 无法发送邮件")
            raise e



if __name__ == '__main__':
    host = 'smtp.qq.com'
    post=456
    sender = '272392324@qq.com'  # 发送者
    passwd = 'ntuhrxhouhhcbjfa'
    receivers = ['272392324@qq.com']  # 接收者,'1414991281@qq.com','204893985@qq.com'
    subject = 'Python SMTP 邮件测试'  # 邮件主题
    from conf import project_path
    file=project_path.email_path_log
    s = SendMail()
    s.send_email_txt(host,456,sender,passwd,receivers,subject,file)