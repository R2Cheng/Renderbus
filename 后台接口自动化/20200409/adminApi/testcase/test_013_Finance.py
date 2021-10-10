# coding=utf-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest



class Finance(TestCase):
    '''财务报销'''
    logger.info('=' * 30 + '[财务报销列表测试用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)              #公共host
        self.headers = Headers(read_excel('publicdata',2,1))  #公共的headers
        self.all_sheet = 13                                   #当前业务模块所在的表序号
        self.sheetName = 'Finance'                            #当前业务模块所在的表名称

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    def testcase_001(self,row=1):
        '''发票列表查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言






if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Finance('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)