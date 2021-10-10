# -*- comding:utf-8   -*-


import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


import time,os
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
from bs4 import BeautifulSoup


# aXbAWHc2C5KCWx2R
pwd = os.path.dirname(os.path.abspath(__file__))
print()
def emailsend():
    '''发送自动化报告到指定邮箱'''
    sender = 'zuowangwang@rayvision.com'  # 发件人邮箱
    receivers = [
        'zuowangwang@rayvision.com',
        'halley@rayvision.com',
        'loujian@rayvision.com',
        'amber@rayvision.com',
        'beyond_lee@rayvision.com',
        'rachelxiao@rayvision.com',
        'caojing@rayvision.com'
    ]
    # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # receivers = ['halley@rayvision.com','rachelxiao@rayvision.com']
    receivers = 'zuowangwang@rayvision.com'

    #读取报告文件内容放到邮件当中
    now = time.strftime('%Y-%m-%d')
    path = os.path.dirname(pwd)+'/report/' + '%s_result.html' % now
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()

    #读取报告指定行数来判断传参
    soup = BeautifulSoup(open(path, 'rb'),'lxml')
    a = str(soup.select('#total_row'))
    percent = a.split('\n')[-2].replace("<td>" ,"").replace("</td>" ,"")

    message = MIMEMultipart()
    message['From'] = Header("渲染测试组", 'utf-8')  # 发件人
    message['To'] = Header('渲染后台', 'utf-8')  # 收件人姓名
    subject = percent + '后台管理接口自动化测试报告（线上）'   # 邮件标题


    message['Subject'] = Header(subject, 'utf-8').encode()
    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)


    mail_msg = """
    <h1><font size="5" coor="black">如果要查看具体详情请下载HTML附件，即可展开查看详情</font></h1>
    """

    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msgAlternative.attach(MIMEText(mail_body, 'html', 'utf-8'))


    now = time.strftime('%Y-%m-%d')        #定义时间变量
    # 构造附件1，传送当前目录下的 test.txt 文件
    fujian1 = MIMEText(open(os.path.dirname(pwd)+'/logs/' + '%s.log' % now, 'rb').read(), 'base64', 'utf-8')
    fujian1["Content-Type"] = 'application/octet-stream'
    fujian1["Content-Disposition"] = 'attachment; filename="%s.txt"'% now # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    message.attach(fujian1)


    # 构造附件2，传送当前目录下的 result.html 文件
    fujian2 = MIMEText(open(os.path.dirname(pwd)+'/report/' + '%s_result.html' % now, 'rb').read(), 'html', 'utf-8')
    fujian2["Content-Type"] = 'application/octet-stream'
    fujian2["Content-Disposition"] = 'attachment; filename="%s_result.html"' % now
    message.attach(fujian2)

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
        smtpObj.login('zuowangwang@rayvision.com', '6B5FEbSa34zJFXTH')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

