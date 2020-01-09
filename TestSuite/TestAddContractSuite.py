# conding:utf-8
# from Base.DriverBase import DriverBase
# from PageObject.AddContractPageObject import Add_Contract
# from Base.GetExcelData import get_excel_data
# from config import readconfig
# from Base.SQLconnect import MySQLUtil
# import unittest
#
# driverbase = DriverBase()
# contract_data = get_excel_data('add_contract')
# sql_data = get_excel_data('sql_data')
# mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)
# mysql_yx = MySQLUtil(db=readconfig.sql_db_yx)
#
# class AddContract(unittest.TestCase):
#     def setUp(self):
#         self.driver = driverbase.open_broswer()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(30)
#         self.add = Add_Contract(self.driver)
#     def tearDown(self):
#         driverbase.quit_broswer()
#     # 添加已完成契约，添加成功
#     def test_add_finish_contract(self):
#         try:
#             mysql.update(sql_data[0]['table'],sql_data[0]['set or search'],sql_data[0]['where'])           # 修改当前公司字段为0
#             mysql.update(sql_data[1]['table'],sql_data[1]['set or search'],sql_data[1]['where'])           # 更新 成都知道创宇信息计数有限公司为当前公司
#             count = mysql.select(sql_data[2]['set or search'],sql_data[2]['table'],sql_data[2]['where'])   # 统计添加契约前，该公司的总契约数
#             self.add.add_finish_contract(readconfig.url_admin,contract_data[0]['company_name'],contract_data[0]['describe'],contract_data[0]['appraise'])
#             count_now = mysql.select(sql_data[2]['set or search'],sql_data[2]['table'],sql_data[2]['where'])
#             # mysql.mysql_close()                                                                           # 每条用例都关闭数据库会导致报2006的错，暂时的方法是执行到最后一条用例再关闭数据库
#             self.assertEqual(int(count_now[0][0]),int(count[0][0])+1)
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，都不使用印章
#     def test_add_unfinish_contract(self):
#         try:
#             count = mysql.select(sql_data[2]['set or search'],sql_data[2]['table'],sql_data[2]['where'])                # 统计添加契约前，该公司的总契约数
#             self.add.add_unfinish_contract(readconfig.url_admin,contract_data[1]['company_name'],contract_data[1]['describe'])
#             count_now = mysql.select(sql_data[2]['set or search'],sql_data[2]['table'],sql_data[2]['where'])
#             # mysql.mysql_close()
#             self.assertEqual(int(count_now[0][0]),int(count[0][0])+1)
#         except Exception as msg:
#             print(u"异常原因：%s" %msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，我方使用印章
#     def test_add_unfinish_usestamp(self):
#         try:
#             # count_req = mysql_yx.select(sql_data[11]['set or search'],sql_data[11]['table'],sql_data[11]['where'])
#             count = mysql.select(sql_data[2]['set or search'], sql_data[2]['table'], sql_data[2]['where'])
#             self.add.add_unfinish_use_stamp(readconfig.url_admin,contract_data[2]['company_name'],contract_data[2]['describe'])
#             # count_req_now = mysql_yx.select(sql_data[11]['set or search'],sql_data[11]['table'],sql_data[11]['where'])
#             count_now = mysql.select(sql_data[2]['set or search'], sql_data[2]['table'], sql_data[2]['where'])
#             # mysql_yx.mysql_close()
#             # mysql.mysql_close()
#             # self.assertEqual(int(count_req_now[0][0]),int(count_req[0][0])+1)
#             self.assertEqual(int(count_now[0][0]),int(count[0][0])+1)
#         except Exception as msg:
#             print(u"异常原因：%s" %msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，对方使用印章
#     def test_add_unfinish_other_usestamp(self):
#         try:
#             # count_req = mysql_yx.select(sql_data[12]['set or search'], sql_data[12]['table'], sql_data[12]['where'])
#             count = mysql.select(sql_data[2]['set or search'], sql_data[2]['table'], sql_data[2]['where'])
#             self.add.add_unfinish_use_stamp(readconfig.url_admin, contract_data[3]['company_name'],contract_data[3]['describe'])
#             # count_req_now = mysql_yx.select(sql_data[12]['set or search'], sql_data[12]['table'], sql_data[12]['where'])
#             count_now = mysql.select(sql_data[2]['set or search'], sql_data[2]['table'], sql_data[2]['where'])
#             # mysql_yx.mysql_close()
#             # mysql.mysql_close()
#             # self.assertEqual(int(count_req_now[0][0]), int(count_req[0][0]) + 1)
#             self.assertEqual(int(count_now[0][0]), int(count[0][0]) + 1)
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，双方都使用印章
#     def test_add_unfinish_all_usestamp(self):
#         try:
#             # count_req = mysql_yx.select(sql_data[11]['set or search'], sql_data[11]['table'], sql_data[11]['where'])               #统计当前公司（成都知道创宇）的合同章未使用的用章对象
#             # count_req_other = mysql_yx.select(sql_data[12]['set or search'], sql_data[12]['table'], sql_data[12]['where'])         # 统计对方公司（千帆渡）的合同章未使用的用章对象
#             count = mysql.select(sql_data[2]['set or search'], sql_data[2]['table'], sql_data[2]['where'])
#             self.add.add_unfinish_all_use_stamp(readconfig.url_admin, contract_data[4]['company_name'],contract_data[4]['describe'])
#             # count_req_now = mysql_yx.select(sql_data[12]['set or search'], sql_data[12]['table'], sql_data[12]['where'])
#             # count_req_other_now = mysql_yx.select(sql_data[12]['set or search'], sql_data[12]['table'],sql_data[12]['where'])
#             count_now = mysql.select(sql_data[2]['set or search'], sql_data[2]['table'], sql_data[2]['where'])
#             # mysql_yx.mysql_close()
#             # mysql.mysql_close()
#             # self.assertEqual(int(count_req_now[0][0]), int(count_req[0][0]) + 1)
#             # self.assertEqual(int(count_req_other_now[0][0]), int(count_req_other[0][0]) + 1)
#             self.assertEqual(int(count_now[0][0]), int(count[0][0]) + 1)
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，搜索公司不是契约公司
#     def test_add_unfinish_unuser(self):
#         try:
#             self.add.add_unfinish_contract(readconfig.url_admin, contract_data[5]['company_name'],contract_data[5]['describe'])
#             self.assertEqual(self.add.add_error_sever(),contract_data[5]['except_result'])
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，搜索公司是契约宝用户，但是未认证
#     def test_add_unfinish_unattestation(self):
#         try:
#             self.add.add_unfinish_contract(readconfig.url_admin, contract_data[6]['company_name'],contract_data[6]['describe'])
#             self.assertEqual(self.add.add_error_sever(),contract_data[6]['except_result'])
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，搜索公司不是印章用户
#     def test_add_unfinish_other_unstamp(self):
#         try:
#             self.add.add_unfinish_other_use_stamp(readconfig.url_admin, contract_data[7]['company_name'],contract_data[7]['describe'])
#             self.assertEqual(self.add.add_toast(),contract_data[7]['except_result'])
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
#     # 添加未完成契约，我方不是印章用户
#     def test_add_unfinish_unstamp(self):
#         try:
#             mysql.update(sql_data[0]['table'], sql_data[0]['set or search'], sql_data[0]['where'])          # 修改当前公司字段为0
#             mysql.update(sql_data[14]['table'], sql_data[14]['set or search'],sql_data[14]['where'])        # 更新 福建中鑫华为科技有限公司为当前公司,非印章用户
#             self.add.add_unfinish_use_stamp(readconfig.url_admin,contract_data[8]['company_name'],contract_data[8]['describe'])
#             self.assertEqual(self.add.add_toast_user(),contract_data[8]['except_result'])
#             mysql.mysql_close()
#         except Exception as msg:
#             print(u"异常原因：%s" % msg)
#             driverbase.get_screenshot()
# if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(AddContract('test_add_finish_contract'))
    # suite.addTest(AddContract('test_add_unfinish_contract'))
    # suite.addTest(AddContract('test_add_unfinish_usestamp'))
    # suite.addTest(AddContract('test_add_unfinish_other_usestamp'))
    # suite.addTest(AddContract('test_add_unfinish_all_usestamp'))
    # suite.addTest(AddContract('test_add_unfinish_unuser'))
    # suite.addTest(AddContract('test_add_unfinish_unattestation'))
    # suite.addTest(AddContract('test_add_unfinish_other_unstamp'))
    # suite.addTest(AddContract('test_add_unfinish_unstamp'))
    # unittest.TextTestRunner().run(suite)