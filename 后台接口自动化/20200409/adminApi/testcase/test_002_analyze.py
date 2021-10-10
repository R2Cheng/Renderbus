# coding=utf-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest


class AnalyzeTask(TestCase):
    '''分析模块-运行/完成的分析作业'''
    logger.info('=' * 30 + '[分析作业模块用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)              #公共host
        self.headers = Headers(read_excel('publicdata',2,1))  #公共的headers
        self.all_sheet = 2                                    #当前业务模块所在的表序号
        self.public_num = 0                                   #公共表的表序号
        self.public_sheet = 'publicdata'                      #公共表的表名称
        self.sheetName = 'analyze'                            #当前业务模块所在的表名称
        self.analyzingId = read_excel(self.public_sheet,18,1)
        self.analyzdoneId1 = read_excel(self.public_sheet,19,1)
        self.analyzdoneId2 = read_excel(self.public_sheet,20,1)

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    def testcase_001(self,row=1):
        '''访问完成的分析列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取完成的分析列表操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_002(self,row=2):
        '''根据用户名访问完成的分析列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取完成的分析列表操作
        for analysisID in self.result['data']['items']:
            if analysisID['isDelete'] == 1 and (analysisID['status'] == 40 or analysisID['status'] == 35):
                write_excel(self.public_num, 19, 1, str(analysisID['taskId']))  #获取第一个没有被删除的已提交或自动提交的分析作业
                break
        for analysisID in self.result['data']['items']:
            if analysisID['isDelete'] == 1 and (analysisID['status'] == 0 or analysisID['status'] == 10 or analysisID['status'] == 5):
                write_excel(self.public_num, 20, 1, str(analysisID['taskId']))  #获取第一个没有被删除的完成状态的分析作业
                break
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_003(self,row=3):
        '''根据ID访问完成的分析列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId1, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取完成的分析列表操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_004(self,row=4):
        '''完成的分析作业-删除分析任务'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId1, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-删除分析任务操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_005(self,row=5):
        '''完成的分析作业-恢复分析任务'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId1, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-恢复分析任务操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_006(self,row=6):
        '''完成的分析作业-重提作业进行判断'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId1, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-重提作业操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_007(self,row=7):
        '''完成的分析作业-重提作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId1, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-重提作业操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    # def testcase_008(self,row=8):
    #     '''根据用户名访问运行的分析列表'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #读取运行的分析列表操作
    #     write_excel(self.public_num,18,1,str(self.result['data']['items'][0]['taskId']))   #将运行分析作业列表的第一个ID写入公共表内
    #     write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_009(self,row=9):
        '''根据ID访问运行的分析列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzingId, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取运行的分析列表操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    # def testcase_010(self,row=10):
    #     '''运行的分析作业-属性设置'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.analyzingId, 'taskIds', self.parameter, 2)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #完成的分析作业-属性设置操作
    #     write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_011(self,row=11):
    #     '''运行的分析作业-约束设置'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.analyzingId, 'taskIds', self.parameter, 2)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #完成的分析作业-约束设置操作
    #     write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_012(self,row=12):
    #     '''运行的分析作业-群组设置'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.analyzingId, 'taskIds', self.parameter, 2)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #完成的分析作业-群组设置操作
    #     write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_013(self,row=13):
    #     '''运行的分析作业-批量停止'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.analyzingId, 'taskIds', self.parameter, 2)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #获取分析文件全路径操作
    #     write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_014(self,row=14):
    #     '''获取分析文件全路径'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.analyzdoneId2, 'taskId', self.parameter, 1)
    #     baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
    #     self.result = baseUrl.json()  #获取分析文件全路径操作
    #     write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_015(self,row=15):
        '''完成的分析作业-添加属性'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-属性设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_016(self,row=16):
        '''完成的分析作业-删除属性'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-属性设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_017(self,row=17):
        '''完成的分析作业-添加要求'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-属性设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_018(self,row=18):
        '''完成的分析作业-删除要求'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-属性设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_019(self,row=19):
        '''完成的分析作业-添加约束'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-约束设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_020(self,row=20):
        '''完成的分析作业-删除约束'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-约束设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_021(self,row=21):
        '''完成的分析作业-添加群组'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-群组设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_022(self,row=22):
        '''完成的分析作业-删除群组'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskIds', self.parameter, 2)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #完成的分析作业-群组设置操作
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_023(self,row=23):
        '''获取分析任务renderlog'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #获取分析任务renderlog
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_024(self,row=24):
        '''获取分析任务debuglog'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #获取分析任务debuglog
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_025(self,row=25):
        '''获取分析任务munulog'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.analyzdoneId2, 'taskId', self.parameter, 1)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #获取分析任务munulog
        write_excel(self.all_sheet,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AnalyzeTask('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)