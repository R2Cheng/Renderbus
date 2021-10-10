#coding = UTF-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest


class RenderTask(TestCase):
    '''全局搜索'''
    logger.info('=' * 30 + '[渲染作业模块用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)
        self.headers = Headers(read_excel('publicdata',2,1))
        self.sheet_num = 4
        self.public_num = 0
        self.public_sheet = 'publicdata'
        self.sheetName = 'render'
        self.preId = read_excel(self.public_sheet,3,1)  #预处理作业id
        self.renderdoneId = read_excel(self.public_sheet,6,1)  #完成的渲染作业id
        self.renderingId = read_excel(self.public_sheet,5,1)  #运行的渲染作业id
        self.firstId = read_excel(self.public_sheet,8,1)  #优先帧作业id
        self.analyzedoneId = read_excel(self.public_sheet,20,1)  #完成分析作业id


    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    def testcase_001(self,row=25):
        '''全局搜索预处理作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取的帧作业列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_002(self, row=25):
        '''全局搜索完成的渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.renderdoneId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取的帧作业列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_003(self, row=25):
        '''全局搜索运行的渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.renderingId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取的帧作业列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_004(self, row=25):
        '''全局搜索优先帧渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.firstId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取的帧作业列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_005(self, row=25):
        '''全局搜索完成的分析作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzedoneId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取的帧作业列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RenderTask('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)