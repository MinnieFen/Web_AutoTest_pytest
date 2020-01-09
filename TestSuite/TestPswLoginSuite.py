# coding:utf-8
import unittest
from PageObject.LoginPageObject import Login
from Base.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase

url = readconfig.url_login
logindata = get_excel_data('psw_login')
driverBase = DriverBase()
class Test_psw_login(unittest.TestCase):
    def setUp(self):
        self.driver = driverBase.open_broswer()
        driverBase.max_window()
        self.login = Login(self.driver)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        driverBase.quit_broswer()
    def test_login(self):
        '''账号密码正确登录'''
        # login = Login(self.driver)
        self.login.psw_login(logindata[0]['phone'],logindata[0]['psw'],url)
        self.assertEqual(self.login.login_success_username(),logindata[0]['except_result'])
    def test_login_nullpsw(self):
        '''账号正确，密码为空登录'''
        self.login.psw_login(logindata[1]['phone'],logindata[1]['psw'],url)
        self.assertEqual(self.login.login_error_page(),logindata[1]['except_result'])
    def test_login_nullphone(self):
        '''账号为空，密码正确'''
        self.login.psw_login(logindata[2]['phone'],logindata[2]['psw'],url)
        self.assertEqual(self.login.login_error_page(),logindata[2]['except_result'])
    def test_login_allnull(self):
        '''账号和密码都为空'''
        self.login.psw_login(logindata[3]['phone'],logindata[3]['psw'],url)
        self.assertEqual(self.login.login_error_page(),logindata[3]['except_result'])
    def test_login_mismatch(self):
        '''账号和密码不匹配'''
        self.login.psw_login(logindata[4]['phone'],logindata[4]['psw'],url)
        self.assertEqual(self.login.login_error_sever(),logindata[4]['except_result'])
# if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Test_psw_login('test_login'))
#     suite.addTest(Test_psw_login('test_login_02'))
    # suite.addTest(Test_psw_login('test_login_03'))
    # suite.addTest(Test_psw_login('test_login_04'))
    # suite.addTest(Test_psw_login('test_login_05'))
    # unittest.TextTestRunner().run(suite)
