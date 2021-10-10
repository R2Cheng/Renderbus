# coding=utf-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest


class storage(TestCase):
    '''存储管理'''
    logger.info('=' * 30 + '[存储管理测试用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)              #公共host
        self.headers = Headers(read_excel('publicdata',2,1))  #公共的headers
        self.all_sheet = 12                                   #当前业务模块所在的表序号
        self.sheetName = 'storage'                            #当前业务模块所在的表名称

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    def testcase_001(self,row=1):
        '''存储概览'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_002(self,row=2):
        '''清理管理'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_003(self,row=3):
        '''删除白名单'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_004(self,row=4):
        '''新增白名单'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_005(self,row=5):
        '''存储管理'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(storage('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)