#coding = UTF-8

from unittest import TestCase
import sys
sys.path.append('..')
from public.public_data import *
import unittest


class RenderTask(TestCase):
    '''预处理模块-预处理作业'''
    logger.info('=' * 30 + '[预处理作业模块用例]' + '=' * 30)

    def setUp(self):
        self.host = read_excel('publicdata',1,1)
        self.headers = Headers(read_excel('publicdata',2,1))
        self.sheet_num = 3
        self.public_num = 0
        self.public_sheet = 'publicdata'
        self.sheetName = 'Preprocessing'
        self.preTaskid = read_excel(self.public_sheet,3,1)
        self.parentTsakid = read_excel(self.public_sheet,4,1)
        self.preUserid = read_excel(self.public_sheet,13,1)

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    def testcase_001(self,row=1):
        '''访问预处理列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #读取预处理列表操作
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_002(self,row=2):
        '''根据状态查询预处理作业列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparemeter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host+urlparemeter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #按状态进行查询，读取预处列表
        write_excel(self.sheet_num,row,8,self.result["message"]+ " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparemeter)  #断言

    def testcase_003(self,row=3):
        '''根据用户名查询预处理作业列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #按用户名进行查询，读取预处理列表
        write_excel(self.sheet_num,row,8,self.result["message"] + " " + str(self.result["code"]))
        write_excel(self.public_num,3,1,str(self.result['data']['items'][0]['taskId']))  #获取返回的第一条数据的预处理ID，为之后的操作提供测试数据
        write_excel(self.public_num,4,1,str(self.result['data']['items'][0]['layerParentId']))  #获取返回的第一条数据的作业ID，为之后的操作提供测试数据
        write_excel(self.public_num,13,1,str(self.result['data']['items'][0]['userId']))  #获取返回的第一条数据的用户id
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_004(self,row=4):
        '''根据作业ID查询预处理作业列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.parentTsakid, 'keywords', self.parameter, 6)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #按作业ID进行查询，读取预处理列表
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_005(self,row=5):
        '''根据预处理ID查询预处理作业列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskId', self.parameter, 6)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #按预处理ID进行查询，读取预处理列表
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_006(self,row=6):
        '''获取预处理renderlog'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.preTaskid, self.preUserid), ('id', 'userId'), self.parameter, 7)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #获取预处理renderlog
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_007(self,row=7):
        '''获取预处理debuglog'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.preTaskid, self.preUserid), ('id', 'userId'), self.parameter, 7)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #获取预处理debuglog
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_008(self,row=8):
        '''获取预处理munulog'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift((self.preTaskid,self.preUserid),('id','userId'), self.parameter, 7)
        baseUrl = requests.post(url=self.host + urlparameter, json=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #获取预处理munulog
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_009(self,row=9):
        '''重提作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #重提作业
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_010(self,row=10):
        '''停止作业'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #停止作业
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_011(self,row=11):
        '''添加属性'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置属性
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_012(self,row=12):
        '''删除属性'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置属性
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_013(self,row=13):
        '''添加要求'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置要求
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_014(self,row=14):
        '''删除要求'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置要求
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_015(self,row=15):
        '''添加约束'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置约束
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_016(self,row=16):
        '''删除约束'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置约束
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_017(self,row=17):
        '''添加群组'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置群组
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言

    def testcase_018(self,row=18):
        '''删除群组'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.preTaskid, 'taskIds', self.parameter, 8)
        baseUrl = requests.post(url=self.host + urlparameter, data=self.parameter, headers=self.headers, verify=False)  #接口URL
        self.result = baseUrl.json()  #设置群组
        write_excel(self.sheet_num, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self,self.sheetName,row,6,self.result,urlparameter)  #断言


if __name__ == '__main__':
    suit = unittest.TestCase()
    suit.addTest(RenderTask('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suit)