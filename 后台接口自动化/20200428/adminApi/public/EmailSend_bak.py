# -*- comding:utf-8   -*-


import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup


# aXbAWHc2C5KCWx2R

def emailsend():
    '''发送自动化报告到指定邮箱'''
    sender = 'zuowangwang@rayvision.com'  # 发件人邮箱
    receivers = ['zuowangwang@rayvision.com',
                 'halley@rayvision.com',
                 'rachelxiao@rayvision.com',
                 'amber@rayvision.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    # receivers = ['amber@rayvision.com']

    # 创建一个带附件带图片的实例
    message = MIMEMultipart()
    message['From'] = Header("测试组", 'utf-8')  # 发件人
    message['To'] = Header('后管测试', 'utf-8')  # 收件人姓名
    subject = '后台管理接口自动化测试报告（测试环境）'  # 邮件标题
    message['Subject'] = Header(subject, 'utf-8').encode()

    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)

    mail_msg = """
    <h1><font size="5" coor="black">渲染新平台接口自动化测试报告（线上）</font></h1>
    <p><font size="4" coor="black"><a href="http://task.foxrenderfarm.com/">测试网址：task.foxrenderfarm.com</a></font><br><br>
    <font size="4" coor="black">各模块负责人：<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp;平台值班：<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;曾智  ：18165707890<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;徐洋洋：18594218384<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;谢贤国：18654169229<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;陈洁  ：18170146903<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;詹磊  ：13247552930<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp;镭速值班：<br><br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;欧阳增国：18681571990<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;周楚人  ：18675642612<br><br></font></p>
    <p><font size="4" color="red">详情请下载附件</font><br></p>
    <p><font color="red" size="5"><u>简介如下：</font><br></p>
    
    """
    now = time.strftime('%Y-%m-%d')
    path = 'C:/adminApi/report/' + '%s_result.html' % now
    f = open(path, 'rb')
    mail_body = f.read()
    f.close()

    # msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    msgAlternative.attach(MIMEText(mail_body, 'html', 'utf-8'))


    now = time.strftime('%Y-%m-%d')        #定义时间变量
    # 构造附件1，传送当前目录下的 test.txt 文件
    fujian1 = MIMEText(open('C:/adminApi/logs/' + '%s.log' % now, 'rb').read(), 'base64', 'utf-8')
    fujian1["Content-Type"] = 'application/octet-stream'
    fujian1["Content-Disposition"] = 'attachment; filename="%s.txt"'% now # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    message.attach(fujian1)


    # 构造附件2，传送当前目录下的 result.html 文件
    fujian2 = MIMEText(open('C:/adminApi/report/' + '%s_result.html' % now, 'rb').read(), 'html', 'utf-8')
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

