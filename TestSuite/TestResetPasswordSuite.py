# coding:utf-8
# import unittest
# from PageObject.LoginPageObject import Login
# from Base.GetExcelData import get_excel_data
# from config import readconfig
# from Base.DriverBase import DriverBase
#
# url = readconfig.url_login
# resetdata = get_excel_data('reset_psw')
# sqldata = get_excel_data('sql_data')
# driverBase = DriverBase()
# logindata = get_excel_data('psw_login')
#
# class Reset_password(unittest.TestCase):
#     def setUp(self):
#         self.driver = driverBase.open_broswer()
#         driverBase.max_window()
#         self.login = Login(self.driver)
#         self.driver.implicitly_wait(30)
#     def tearDown(self):
#         driverBase.quit_broswer()
#     # 修改密码成功
#     def reset_success(self):
#         '''密码修改成功'''
#         self.login.send_code_reset(url,resetdata[0]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'],sqldata[3]['table'],sqldata[3]['where'])
#         self.login.psw_reset(codes[0],resetdata[0]['psw'])
#         self.assertEqual(self.login.login_error_sever(),resetdata[0]['except_result'])
#     # 手机号为空
#     def reset_empty_phone(self):
#         '''请输入手机号'''
#         self.login.send_code_reset(url,resetdata[1]['phone'])
#         self.assertEqual(self.login.login_error_page(),resetdata[1]['except_result'])
#     # 错误的验证码
#     def error_code(self):
#         '''验证码错误'''
#         self.login.send_code_reset(url,resetdata[2]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
#         self.login.psw_reset(codes[1], resetdata[2]['psw'])
#         self.assertEqual(self.login.login_error_sever(), resetdata[2]['except_result'])
#     # 新密码为全数字
#     def error_new_psw(self):
#         '''密码为全数字'''
#         self.login.send_code_reset(url,resetdata[3]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
#         self.login.psw_reset(codes[0], resetdata[3]['psw'])
#         self.assertEqual(self.login.login_error_sever(), resetdata[3]['except_result'])
#     # 新密码为全英文
#     def new_psw_error(self):
#         '''密码为全英文'''
#         self.login.send_code_reset(url,resetdata[4]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
#         self.login.psw_reset(codes[0], resetdata[4]['psw'])
#         self.assertEqual(self.login.login_error_sever(), resetdata[4]['except_result'])
#     # 新密码小于6位
#     def less_new_psw(self):
#         '''密码少于6位数'''
#         self.login.send_code_reset(url,resetdata[5]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
#         self.login.psw_reset(codes[0], resetdata[5]['psw'])
#         self.assertEqual(self.login.login_error_sever(), resetdata[5]['except_result'])
#     # 密码为空
#     def empty_psw(self):
#         '''请输入密码'''
#         self.login.send_code_reset(url,resetdata[6]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
#         self.login.psw_reset(codes[0],resetdata[6]['psw'])
#         self.assertEqual(self.login.login_error_page(), resetdata[6]['except_result'])
#     # 修改密码成功后，登录
#     def reset_login(self):
#         '''修改密码成功后，登录'''
#         self.login.send_code_reset(url, resetdata[7]['phone'])
#         codes = self.login.get_code(sqldata[3]['set or search'], sqldata[3]['table'], sqldata[3]['where'])
#         self.login.psw_reset(codes[0], resetdata[7]['psw'])
#         self.login.login_psw(logindata[5]['psw'])
#         self.login.login_button()
#         self.assertEqual(self.login.login_success_username(),logindata[5]['except_result'])
# if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Reset_password('reset_success'))
    # suite.addTest(Reset_password('reset_empty_phone'))
    # suite.addTest(Reset_password('error_code'))
    # suite.addTest(Reset_password('error_new_psw'))
    # suite.addTest(Reset_password('new_psw_error'))
    # suite.addTest(Reset_password('less_new_psw'))
    # suite.addTest(Reset_password('empty_psw'))
    # suite.addTest(Reset_password('reset_login'))
    # unittest.TextTestRunner().run(suite)