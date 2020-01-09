# coding:utf-8
import unittest
import os
import time
from HTMLTestRunner import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from config import readconfig
# from tomorrow import threads

cur_path = os.path.dirname(os.path.realpath(__file__))
def add_case(caseName = 'TestSuite',rule = 'Test*.py'):
    case_path = os.path.join(cur_path,caseName)
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover

def run_case(all_case,reportName = 'report'):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    report_abspath = os.path.join(report_path,now + 'result.html')
    print('report path:%s' %report_abspath)
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner(stream=fp,title=u'UI自动化测试报告，测试结果：',description=u'用例执行详情')
    runner.run(all_case)
    fp.close()
def get_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getatime(os.path.join(report_path,fn)))
    report_file = os.path.join(report_path,lists[-1])
    return report_file
def send_email(mail_host,mail_pass,mail_user,sender,receiver,new_file):
    f = open(new_file,'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = u'自动定时发送测试报告'
    msg['From'] = '517110453@qq.com'
    msg['To'] = '437889925@qq.com'
    smtp = smtplib.SMTP(mail_host,25)     # 创建SMTP对象
    smtp.login(mail_user,mail_pass)
    smtp.sendmail(sender,receiver,msg.as_string())    #SMTP对象使用sendmail方法发送邮件
    smtp.quit()
if __name__ == '__main__':
    # 加载用例
    all_case = add_case()
    #执行用例，生成测试报告的路径
    run_case(all_case)
    # for i,j in zip(all_case,range(len(list(all_case)))):
    #     run_case(i, nth = j)
#获取最新的测试报告
    report_path = os.path.join(cur_path,'report')
    report_file = get_report_file(report_path)
    # send_email(report_file)
    #邮箱配置
    mail_host = readconfig.mail_host
    mail_pass = readconfig.mail_pass
    mail_user = readconfig.mail_user
    sender = readconfig.sender
    receiver = readconfig.receiver
    send_email(mail_host,mail_pass,mail_user,sender,receiver,report_file)
