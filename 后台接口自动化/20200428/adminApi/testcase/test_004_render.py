#coding = UTF-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest


class RenderTask(TestCase):
    '''渲染模块-运行/完成的渲染作业'''
    logger.info('=' * 30 + '[渲染作业模块用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)
        self.headers = Headers(read_excel('publicdata',2,1))
        self.sheet_num = 4
        self.public_num = 0
        self.public_sheet = 'publicdata'
        self.sheetName = 'render'
        self.taskid = read_excel(self.public_sheet,5,1)
        self.taskid2 = read_excel(self.public_sheet,6,1)
        self.userid = read_excel(self.public_sheet,7,1)
        self.preid = read_excel(self.public_sheet,8,1)
        self.taskid3 = read_excel(self.public_sheet,9,1)
        self.taskid4 = read_excel(self.public_sheet,10,1)

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)
        # setlogging().info(self.apiname)

    def testcase_001(self,row=1):
        '''访问运行的渲染列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers,verify=False)  #接口URL
        self.result = baseUrl.json()  #读取运行的渲染列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_002(self,row=2):
        '''访问完成的渲染列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #读取完成的渲染列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_003(self,row=3):
        '''根据用户名查询完成的渲染列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #读取完成的渲染列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        write_excel(self.public_num, 5, 1, str(self.result['data']['items'][0]['taskId']))  #返回第一个作业的作业ID，进行保存
        # write_excel(self.public_num, 6, 1, str(self.result['data']['items'][-1]['taskId']))  #返回最后一个作业的作业ID，进行保存
        write_excel(self.public_num, 7, 1, str(self.result['data']['items'][0]['userId']))  #返回第一个用户ID

        # for preid in self.result['data']['items']:
        #     if preid['taskStatus'] == 25 and preid['isDelete'] == 1:
        #         write_excel(self.public_num, 6, 1, str(preid['taskId']))   #获取没有删除的完成作业
        #         break
        for preid in self.result['data']['items']:
            if preid['preRender'] is not None and preid['isDelete'] == 1:
                write_excel(self.public_num, 8, 1, str(preid['taskId']))  #获取优先帧作业，将优先帧作业的ID保存到publicdata
                break
        for preid in self.result['data']['items']:
            if preid['preRender'] is None and preid['isDelete'] == 1:
                write_excel(self.public_num, 9, 1, str(preid['taskId']))   #获取不是优先帧作业，用于设置级别和节点机
                break
        for preid in self.result['data']['items']:
            if (preid['taskStatus'] == 10 or preid['taskStatus'] == 20 or preid['taskStatus'] == 23) and preid['isDelete'] == 1:  #获取状态为超时停止/欠费停止/停止的作业
                write_excel(self.public_num, 10, 1, str(preid['taskId']))
                break
        for preid in self.result['data']['items']:
            if preid['taskStatus'] == 25 and preid['isDelete'] == 1:  #获取状态为完成的作业
                write_excel(self.public_num, 11, 1, str(preid['taskId']))
                write_excel(self.public_num, 12, 1, str(preid['userId']))
                break
        for preid in self.result['data']['items']:
            if preid['taskType'] == "RenderPhoton" and preid['isDelete'] == 1:   # 获取光子作业id
                write_excel(self.public_num, 26, 1, str(preid['taskId']))
                break
        items = self.result['data']['items']
        items.reverse()
        for preid in items:
            if preid['taskStatus'] == 25 and preid['isDelete'] == 1:
                write_excel(self.public_num, 6, 1, str(preid['taskId']))  # 倒序获取没有删除的完成作业（防止最新的作业被操作）
                break

        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_004(self,row=4):
        '''平台切换'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_005(self,row=5):
        '''运行的渲染作业-平台任务统计'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_006(self,row=6):
        '''重提大任务-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.taskid,self.userid), ('taskIds','userIds'), self.parameter, 9)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_007(self,row=7):
        '''添加备注-运行渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter.encode(), headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_008(self,row=8):
        '''添加标签-运行渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter.encode(), headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_009(self,row=9):
        '''设置超时时间-运行渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_010(self,row=10):
        '''清除黑名单-运行渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    # def testcase_010(self,row=10):
    #     '''设置属性-运行渲染作业'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_011(self,row=11):
    #     '''设置群组-运行渲染作业'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言'''

    def testcase_013(self,row=13):
        '''停止大作业-运行渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_014(self,row=14):
        '''全速渲染-完成的渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.preid, self.userid), ('taskIds', 'userIds'), self.parameter, 9)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言


    # def testcase_014(self,row=14):
    #     '''设置属性-完成渲染作业'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_015(self,row=15):
    #     '''设置要求-完成渲染作业，要求和属性同个接口'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid2, 'taskIds', self.parameter, 8)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_016(self,row=16):
    #     '''设置约束-完成渲染作业'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言
    #
    #
    # def testcase_017(self,row=17):
    #     '''设置群组-完成渲染作业'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid, 'taskIds', self.parameter, 8)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言'''

    def testcase_019(self,row=19):
        '''修改级别-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid3, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_020(self,row=20):
        '''修改节点机-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid3, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_021(self,row=21):
        '''开始大作业-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.taskid, self.userid), ('taskIds', 'userIds'), self.parameter, 9)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_022(self,row=22):
        '''删除大作业-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid2, 'taskIds', self.parameter, 8)
        baseUrl = requests.patch(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_023(self,row=23):
        '''恢复大作业-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid2, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_024(self,row=24):
        '''设置超时停止-完成渲染作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.taskid3, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
        self.result = baseUrl.json()
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    # def testcase_025(self,row=25):
    #     '''全局搜索'''
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     self.parameter = shift(self.taskid3, 'taskId', self.parameter, 1)
    #     baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言


if __name__ == '__main__':
    suit = unittest.TestCase()
    suit.addTest(RenderTask('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suit)


