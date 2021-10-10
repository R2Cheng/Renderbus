# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
# from HTMLTestReportCN import HTMLTestRunner
from public.EmailSend import emailsend
from public import *
import os,sys,time
import unittest
from public.public_data import clean_log, clean_result
sys.path.append("../public")
pwd = os.path.dirname(os.path.abspath(__file__))



if __name__ == '__main__':

    start = time.process_time()
    test_dir = pwd + '/testcase/'
    report_dir = pwd + '/report/'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
    # now = time.strftime(u'%Y-%m-%d.%H.%M.%S')
    now = time.strftime('%Y-%m-%d')
    filename = report_dir + '%s_result.html'%now  #这个filename是生成的自动化测试报告的文件名
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例的执行情况')
    runner.run(discover)
    fp.close()
    end = time.process_time()
    all_time = end-start
    print('\n','总共用时%.0f秒' % all_time)
    emailsend()
    clean_log(pwd+'\logs')
    clean_result(pwd+'/report')