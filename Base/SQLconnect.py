# coding:utf-8
import MySQLdb
from config import readconfig
from Base.GetExcelData import get_excel_data
import json
import ast
class MySQLUtil():
    def __init__(self,db):
        self.sql_info = {'host': readconfig.sql_host,
                    'user': readconfig.sql_uer,
                    'port': readconfig.sql_port,
                    'password': readconfig.sql_password,
                    'db': db,
                    'charset': readconfig.sql_charset}
        # self.host = readconfig.sql_host
        # self.user = readconfig.sql_uer
        # self.port = readconfig.sql_port
        # self.password = readconfig.sql_password
        # self.dbb = readconfig.sql_db_yx
        # self.charset = readconfig.sql_charset
        self.conn = MySQLUtil.__connect(self.sql_info)
    @staticmethod    # 声明静态方法，调用该函数时不需要实例化
    def __connect(sql_info):
        try:
            # conn = MySQLdb.connect(host = self.host,
            #                        user = self.user,
            #                        port = int(self.port),
            #                        password = self.password,
            #                        db = self.dbb,
            #                        charset = self.charset)
            conn = MySQLdb.connect(host = sql_info['host'],
                                   user = sql_info['user'],
                                   port = int(sql_info['port']),
                                   password = sql_info['password'],
                                   db = sql_info['db'],
                                   charset = sql_info['charset'])
            return conn
        except Exception as a:
            print('数据库连接异常：%s' %a)
    # 执行sql
    def get_execute(self,sql):
        # cursor = MySQLUtil().connect().cursor()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as a:
            # MySQLUtil().connect().rollback()
            self.conn.rollback()
            print('执行SQL异常：%s' %a)
        else:
            self.conn.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
            # MySQLUtil().connect().commit()
        # search_data = cursor.fetchall()
        # return search_data
    # 获取执行sql的数据
    def get_rows(self,sql):
        # cursor = MySQLUtil().connect().cursor()
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as a:
            print('执行SQL异常:%s' %a)
        else:
            # MySQLUtil().connect().commit()
            self.conn.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
    # 查询数据库
    def select(self,search,table,where):
        search_list = ast.literal_eval(search)         # 将从excel获取的字符串转换成list
        sql_search = ','.join(search_list)             # search_list 的类型需要为list
        sql = 'select %s from %s where %s;' %(sql_search,table,where)
        return self.get_execute(sql)
    # 更新数据库
    def update(self,table,set,where):
        sql = 'update %s set %s where %s;' %(table,set,where)
        return self.get_execute(sql)
    # 关闭数据库连接
    def mysql_close(self):
        try:
            # MySQLUtil().connect().close()
            self.conn.close()
        except Exception as a:
            print('关闭数据库异常：%s' %a)
# if __name__ == '__main__':
#     data = get_excel_data('sql_data')
#     mysql = MySQLUtil(db= readconfig.sql_db_qiyuebao)
    # sql = '''SELECT `CODE` from sms_code_record WHERE PHONE = '18782038146' ORDER BY CTIME DESC'''
    # sql = '''UPDATE com_user_relation SET IsActive = 1 WHERE UserId = '571499710155046449' AND CompanyId = '934753474143848109' '''
    # table = 'sms_code_record'
    # where = 'PHONE = "18782038146" ORDER BY CTIME DESC'
    # sql_search = ['phone','CODE']
    # result = mysql.select(sql_search,table ,where)
    # print(result)
    # table2 = data[0]['table']
    # set2 = data[0]['set or search']
    # where2 = data[0]['where']
    # print(type(table2))
    # mysql.update(table,set,where)
    # mysql.update(table2,set2,where2)
    # mysql.get_execute(sql)
    # codes = mysql.get_rows(sql)
    # print(codes)
    # print(codes[0])
    # mysql.mysql_close()
