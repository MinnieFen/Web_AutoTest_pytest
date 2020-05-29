# coding:utf-8
import unittest
from PageObject.LoginPageObject import Login
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.GetToastText import ToastText
url = readconfig.url_login
logindata = get_excel_data('code_login')
sqldata = get_excel_data('sql_data')
driverBase = DriverBase()
class Test_code_login(unittest.TestCase):
   def setUp(self):
       self.driver = driverBase.open_broswer()
       driverBase.max_window()
       self.login = Login(self.driver)
       self.driver.implicitly_wait(10)
       self.toast = ToastText(self.driver)
   def tearDown(self):
       driverBase.quit_broswer()
   def test_code_login_success(self):
       '''账号验证码正确登录'''
       self.login.send_code_login(url,logindata[0]['phone'])
       codes = self.login.get_code(sqldata[4]['set or search'],sqldata[4]['table'],sqldata[4]['where'])
       self.login.code_login(codes[0])
       self.assertEqual(self.login.login_success_username(),logindata[0]['except_result'])
   def test_code_login_nullcode(self):
       '''账号正确，验证码为空登录'''
       self.login.send_code_login(url,logindata[1]['phone'])
       self.login.code_login(code = '')
       self.assertEqual(self.toast.page_toast(),logindata[1]['except_result'])
   def test_code_login_allnull(self):
       '''账号、验证码为空'''
       self.login.send_code_login(url,logindata[2]['phone'])
       self.assertEqual(self.toast.page_toast(),logindata[2]['except_result'])
   def test_code_login_mismatch(self):
       '''账号和验证码不匹配'''
       self.login.send_code_login(url,logindata[3]['phone'])
       codes = self.login.get_code(sqldata[4]['set or search'],sqldata[4]['table'],sqldata[4]['where'])
       self.login.code_login(codes[1])
       self.assertEqual(self.toast.sever_toast(),logindata[3]['except_result'])
   def test_code_login_newphone(self):
       '''系统中不存在的账号，验证码登录成功'''
       self.login.send_code_login(url,logindata[4]['phone'])
       codes = self.login.get_code(sqldata[4]['set or search'],sqldata[4]['table'],sqldata[4]['where'])
       self.login.code_login(codes[0])
       self.assertEqual(self.login.login_success_username(),logindata[4]['except_result'])
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(Test_code_login('test_code_login_success'))
#     suite.addTest(Test_code_login('test_code_login_nullcode'))
#     suite.addTest(Test_code_login('test_code_login_allnull'))
#     suite.addTest(Test_code_login('test_code_login_mismatch'))
#     suite.addTest(Test_code_login('test_code_login_newphone'))
#     unittest.TextTestRunner().run(suite)
