#coding:utf-8
import os
import configparser
import pymysql

base_dir = str(os.path.dirname(os.path.dirname(__file__))) #项目所在目录
base_dir = base_dir.replace('\\','/')
file_path = base_dir + '/datas/db_config.ini'
# print(file_path)

conf = configparser.ConfigParser()
conf.read(file_path)
host = conf.get('mysqlconf','host')
port = conf.get('mysqlconf','port')
user = conf.get('mysqlconf','user')
password = conf.get('mysqlconf','password')


def sqlQuery(sql,db_name):
        # 打开数据库连接
        db = pymysql.connect (host=host,
                              port=int(port),
                              user=user,
                              password=password,
                              db=db_name)
        cursor = db.cursor()   # 使用cursor()方法获取操作游标
        try:
            cursor.execute(sql) # 执行SQL语句
            db.commit() # 提交到数据库执行
            results = cursor.fetchall() # 获取所有记录列表
            return  results
        except:
            db.rollback()            # 发生错误时回滚
        db.close()  # 关闭数据库连接



