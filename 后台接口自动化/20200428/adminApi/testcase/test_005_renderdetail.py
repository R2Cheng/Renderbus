#coding = UTF-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest
import time


class RenderTask(TestCase):
    '''帧详情作业'''
    logger.info('=' * 30 + '[渲染作业模块用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)
        self.headers = Headers(read_excel('publicdata',2,1))
        self.sheet_num = 4
        self.public_num = 0
        self.public_sheet = 'publicdata'
        self.sheetName = 'renderdetail'
        self.doneId = read_excel(self.public_sheet,5,1)
        self.doneIds = read_excel(self.public_sheet,11,1)
        self.doneuserIds = read_excel(self.public_sheet, 12, 1)
        self.doneuserId = read_excel(self.public_sheet,7,1)
        self.detailid = read_excel(self.public_sheet,14,1)
        self.filepath = read_excel(self.public_sheet,15,1)
        self.detailstus = read_excel(self.public_sheet,16,1)
        self.detailType= read_excel(self.public_sheet,17,1)
        self.photoId = read_excel(self.public_sheet,26,1)

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)
        # setlogging().info(self.apiname)

    def testcase_001(self,row=1):
        '''访问帧作业列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.doneIds, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取的帧作业列表操作
        write_excel(self.public_num, 14, 1,str(self.result['data']['items'][0]['id']))
        write_excel(self.public_num, 16, 1, str(self.result['data']['items'][0]['frameStatus']))
        write_excel(self.public_num, 17, 1, str(self.result['data']['items'][0]['frameType']))
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_002(self,row=1):
        '''访问光子作业详情'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.photoId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_003(self,row=2):
        '''重提第一个帧任务'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.doneIds,self.detailid), ('taskIds','ids'), self.parameter, 9)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #重提第一个帧作业操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_004(self,row=3):
        '''停止重提的帧任务'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.doneIds,self.detailid), ('taskIds','ids'), self.parameter, 9)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #停止刚刚重提的帧作业操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
        time.sleep(61)

    # def testcase_004(self,row=4):
    #     '''开始停止的帧任务'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift((self.doneIds,self.detailid, self.doneuserIds), ('taskIds','ids', 'userId'), self.parameter, 7)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #开始刚刚停止的帧作业操作
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #     time.sleep(1)

    def testcase_005(self,row=5):
        '''查看历史重渲记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.detailid, 'id', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #对重提过的帧作业查看历史重渲操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_006(self,row=6):
        '''查询帧耗时分布图&帧完成情况'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.doneId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #对重提过的帧作业查看历史重渲操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_007(self,row=7):
        '''查询配置文档'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.doneId, self.doneuserId), ('taskId', 'userId'), self.parameter, 10)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #发送请求，查询配置文档
        write_excel(self.public_num,15,1,str(self.result['data']['task.json']))
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_008(self,row=8):
        '''查询配置文档-task.json'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.filepath, 'filePath', self.parameter, 6)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #发送请求，查看配置文档task.json
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_009(self,row=9):
        '''查询配置详情'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.doneId, self.doneuserId), ('taskId', 'userId'), self.parameter, 10)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #发送请求，查询配置详情
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_011(self,row=11):
        '''加载任务缩略图/查看截图'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.doneId, self.doneuserId, self.detailid, self.detailstus), ('taskId', 'userId', 'id', 'frameStatus'), self.parameter, 10)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #加载任务缩略图/查看截图
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    # def testcase_012(self,row=12):
    #     '''查看日志-renderlog'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.afterparameter = self.parameter.replace("false","12345")
    #     self.parameter = shift((self.detailid, self.doneuserId, self.detailType), ('id', 'userId', 'frameType'), self.afterparameter, 10)
    #     self.parameter = self.afterparameter.replace("12345", "false")
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #发送请求，查看日志-renderlog
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_013(self,row=13):
    #     '''查看日志-debuglog'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.afterparameter = self.parameter.replace("false","12345")
    #     self.parameter = shift((self.detailid, self.doneuserId, self.detailType), ('id', 'userId', 'frameType'), self.afterparameter, 10)
    #     self.parameter = self.afterparameter.replace("12345", "false")
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #发送请求，查看日志-debuglog
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_014(self,row=14):
    #     '''查看日志-munulog'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.detailid, 'id', self.parameter, 1)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #发送请求，查看日志-munulog
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_015(self,row=15):
        '''查询任务帧总数及总扣费'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.doneId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #发送请求，查询历史重复帧以及费用
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_016(self,row=16):
        '''查看任务帧扣费信息'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.doneId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #发送请求，查询历史重复帧列表
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RenderTask('testcase_016'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
