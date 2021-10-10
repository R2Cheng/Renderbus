# -*- coding:utf-8   -*-
from unittest import TestCase
import unittest
import sys
sys.path.append('..')
from public.public_data import *


class UserManagement(TestCase):
    '''用户管理模块'''

    logger.info('=' * 30 +'[开始用户管理模块用例]'+'='* 30)

    def setUp(self):
        self.urlsite = (read_excel("publicdata", 1, 1))  # 公共的URL
        self.Head = Headers(read_excel("publicdata",2,1))  # 公共的Head
        self.all_sheet = 6  # 写入的数据是第几张表
        self.sheetName = "UserManagement"  # 读取的表的名字是那一张
        self.TrackRecordId = read_excel("publicdata", 22, 1) #公共跟踪id
        self.StudentID = read_excel("publicdata",23,1) #学生认证id
        self.Couponid = (read_excel("publicdata", 27, 1)) #券id

    def tearDown(self):
        logger.info(self.apiname)
        logger.info(self.parameter)
        logger.info(self.result)

    def testcase_001(self, row=1):
        '''获取用户列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_002(self,row=2):
        '''停用用户'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_003(self,row=3):
        '''启用用户'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
        compile

    # def testcase_004(self,row=4):
    #     """导出用户列表"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
    #     patterns = re.compile(r'phone.*?\.xlsx')
    #
    # def testcase_005(self,row=5):
    #     """导出所有手机号"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_006(self,row=6):
        """分配管理员列表"""
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter.encode(), headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_007(self,row=7):
        '''分配PC'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter.encode(), headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_008(self,row=8):
        '''添加备注'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_009(self,row=9):
        '''查询用户详情'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_0010(self,row=10):
        '''修改用户基本信息'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_011(self,row=11):
        '''获取临时密码'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter,data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_012(self,row=12):
        '''重置密码'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_013(self,row=13):
        '''获取充值窗口'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_014(self,row=14):
        '''充值渲染券'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter.encode(encoding='UTF-8'), headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_015(self,row=15):
        '''充值记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_016(self,row=16):
        '''充值记录(退现金)'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_017(self,row=17):
        '''充值记录（渲染券记录）'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_018(self,row=18):
        '''充值记录（渲染券列表）'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        for coupid in self.result['data']['userCoupons']:
            if coupid['discard'] == 0:   # 获取券id
                write_excel(0, 27, 1, str(coupid['id']))
                break
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_019(self,row=19):
        '''充值记录（作废渲染券）'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.Couponid, 'id', self.parameter, 11)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_020(self,row=20):
        '''获取API接口'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    # def testcase_021(self,row=21):
    #     """导出详细帧扣费记录"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
    #
    # def testcase_022(self,row=22):
    #     """导出历史重复帧"""
    #     self.apiname = read_excel(self.sheetName, row, 3)
    #     urlparameter = (read_excel(self.sheetName, row, 2))
    #     self.parameter = read_excel(self.sheetName, row, 5)
    #     baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
    #     self.result = baseUrl.json()
    #     write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
    #     assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_023(self,row=23):
        '''修改用户详情价格设置'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_024(self,row=24):
        '''修改用户详情渲染设置'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_025(self,row=25):
        '''获取用户平台设置'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_026(self,row=26):
        '''修改用户详情平台设置'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_027(self,row=27):
        '''用户存储设置'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_028(self,row=28):
        '''查看用户存储'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_029(self,row=29):
        '''修改用户风险开关'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_030(self,row=30):
        '''查询所有软件'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_031(self,row=31):
        '''新增跟踪记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_032(self,row=32):
        '''客户跟踪记录查看'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
        write_excel(0, 22, 1, str(self.result['data']['items'][0]['id']))

    def testcase_033(self,row=33):
        '''删除跟踪记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.TrackRecordId, 'id', self.parameter, 1)
        baseUrl = requests.post(url=self.urlsite + urlparameter, json=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_034(self,row=34):
        '''价格更改历史记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_035(self,row=35):
        '''查询主子账号'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_036(self,row=36):
        '''修改总额度'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_037(self,row=37):
        '''修改子账户额度'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_038(self,row=38):
        '''用户操作日志查看'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_039(self,row=39):
        '''获取客户登录记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_040(self,row=40):
        '''获取包机信息列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_041(self,row=41):
        '''获取包项目管理'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_042(self,row=42):
        '''获取节点机租赁'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_043(self,row=43):
        '''获取效果图会员变更记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_044(self,row=44):
        '''发票申请记录'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_045(self,row=45):
        '''余额充值明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_046(self,row=46):
        '''渲染券充值明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_047(self,row=47):
        '''退现金查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_048(self,row=48):
        '''转账记录查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_049(self,row=49):
        '''包机消费明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_050(self,row=50):
        '''包项目消费明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_051(self,row=51):
        '''租赁消费明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_052(self,row=52):
        '''租赁过期消费明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_053(self,row=53):
        '''客户余额统计查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_054(self,row=54):
        '''作业消费明细查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_055(self,row=55):
        '''效果图会员升级记录查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_056(self,row=56):
        '''查询学生认证列表'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言
        if self.result['data'] == None:
            print("没有学生认证的数据")
        else:
            write_excel(0,23,1,str(self.result['data']['items'][0]['id']))

    def testcase_057(self,row=57):
        '''查看学生上传图片'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        self.parameter = shift(self.StudentID, "id", self.parameter, 1)
        baseUrl = requests.post(url=self.urlsite + urlparameter, json=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_058(self,row=58):
        '''查询代理商申请'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言

    def testcase_059(self,row=59):
        '''客户端意见反馈查询'''
        self.apiname = read_excel(self.sheetName, row, 3)
        urlparameter = (read_excel(self.sheetName, row, 2))
        self.parameter = read_excel(self.sheetName, row, 5)
        baseUrl = requests.post(url=self.urlsite + urlparameter, data=self.parameter, headers=self.Head, verify=False)
        self.result = baseUrl.json()
        write_excel(self.all_sheet, row, 8, self.result["message"] + " " + str(self.result["code"]))
        assert_num(self, self.sheetName, row, 6, self.result, urlparameter)  # 断言


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserManagement('testcase_001'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
