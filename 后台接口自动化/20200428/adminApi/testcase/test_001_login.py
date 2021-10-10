# coding=utf-8

from unittest import TestCase
import sys
# from public.log import *
sys.path.append('..')
from public.public_data import *
import unittest




class UserLogin(TestCase):
    '''用户注册登录模块'''
    #log = Log()
    logger.info('=' * 30 + '[开始用户注册登录模块用例]' + '=' * 30)

    def setUp(self):
        self.urlsite = (read_excel("publicdata",1,1))               #公共的URL
        self.Head = Headers("")       #公共的Head
        self.all_sheet = 1                                           #写入的数据是第几张表
        self.sheetName = "AdminLogin"                              #读取的表的名字是那一张
        self.public_num = 0
        self.public_sheet = 'publicdata'

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    # def testcase_001(self,row=1):
    #     """获取手机验证码"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
    #
    # def testcase_002(self,row=2):
    #     """获取邮箱验证码"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
    #
    # def testcase_003(self,row=3):
    #    """获取语音验证码"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_001(self,row=4):
        '''用户登录成功'''
        tt = read_time()  #获取验证码
        write_excel(self.public_num, 24, 1, tt)  #将验证码存入第一张shift
        self.vitify = read_excel(self.public_sheet, 24, 1)
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.vitify, 'verfyCode', self.parameter, 3)  #替换数据
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head,verify=False)  #接口URL
        self.result = baseUrl.json()  #登录操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
        baseHeaders = baseUrl.headers['x-auth-token']  #获取登录token
        write_excel(0,2,1,baseHeaders)  #获取到的token写入公共表public



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserLogin('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)





