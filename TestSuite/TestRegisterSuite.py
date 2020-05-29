# coding:utf-8
import unittest
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from PageObject.LoginPageObject import Login
from PageObject.AddCompanyPageObject import Add_company
from public.GetToastText import ToastText

url = readconfig.url_login
register_data = get_excel_data('register')
sqldata = get_excel_data('sql_data')
driverBase = DriverBase()
companydata = get_excel_data('add_company')

class Test_register(unittest.TestCase):
   def setUp(self):
       self.driver = driverBase.open_broswer()
       driverBase.max_window()
       self.login = Login(self.driver)
       self.addcompany = Add_company(self.driver)
       self.driver.implicitly_wait(10)
       self.toast = ToastText(self.driver)
   def tearDown(self):
       driverBase.quit_broswer()
   # 注册成功
   def test_register_success(self):
       '''注册成功，进入添加公司页面'''
       self.login.send_code_register_heard(url,register_data[0]['phone'],register_data[0]['psw'],register_data[0]['name'])
       codes = self.login.get_code(sqldata[6]['set or search'],sqldata[6]['table'],sqldata[6]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.login.register_success(),register_data[0]['except_result'])
   # 已存在手机号
   def test_exist_phone(self):
       '''手机号码已经注册'''
       self.login.send_code_register_heard(url,register_data[1]['phone'],register_data[1]['psw'],register_data[1]['name'])
       self.assertEqual(self.toast.page_toast(),register_data[1]['except_result'])
   # 密码为空
   def test_empty_psw(self):
       '''请输入密码'''
       self.login.send_code_register_heard(url,register_data[2]['phone'],register_data[2]['psw'],register_data[2]['name'])
       codes = self.login.get_code(sqldata[7]['set or search'],sqldata[7]['table'],sqldata[7]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(),register_data[2]['except_result'])
   # 姓名为空
   def test_empty_name(self):
       '''请输入姓名'''
       self.login.send_code_register_loginpage(url,register_data[3]['phone'],register_data[3]['psw'],register_data[3]['name'])
       codes = self.login.get_code(sqldata[7]['set or search'],sqldata[7]['table'],sqldata[7]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(),register_data[3]['except_result'])
   # 手机号为空
   def test_empty_phone(self):
       '''请输入手机号'''
       self.login.send_code_register_loginpage(url,register_data[4]['phone'],register_data[4]['psw'],register_data[4]['name'])
       codes = self.login.get_code(sqldata[7]['set or search'],sqldata[7]['table'],sqldata[7]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(),register_data[4]['except_result'])
   # 不符合规则的手机号
   def test_incongruent_phone(self):
       '''请输入正确的手机号'''
       self.login.send_code_register_loginpage(url, register_data[5]['phone'], register_data[5]['psw'], register_data[5]['name'])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(), register_data[5]['except_result'])
   # 6位全英文密码
   def test_incongruent_psw(self):
       '''请输入6-16位字母数字组合的密码'''
       self.login.send_code_register_loginpage(url, register_data[6]['phone'], register_data[6]['psw'], register_data[6]['name'])
       codes = self.login.get_code(sqldata[8]['set or search'],sqldata[8]['table'],sqldata[8]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(), register_data[6]['except_result'])
   # 6位全数字的密码
   def test_allnumber_psw(self):
       '''请输入6-16位字母数字组合的密码'''
       self.login.send_code_register_loginpage(url, register_data[7]['phone'], register_data[7]['psw'], register_data[7]['name'])
       codes = self.login.get_code(sqldata[8]['set or search'],sqldata[8]['table'],sqldata[8]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(), register_data[7]['except_result'])
   # 小于6位的密码
   def test_less_psw(self):
       '''请输入6-16位字母数字组合的密码'''
       self.login.send_code_register_loginpage(url, register_data[8]['phone'], register_data[8]['psw'], register_data[8]['name'])
       codes = self.login.get_code(sqldata[8]['set or search'],sqldata[8]['table'],sqldata[8]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(), register_data[8]['except_result'])
   # 验证码与手机号不匹配
   def test_mismatch(self):
       '''验证码错误'''
       self.login.send_code_register_loginpage(url,register_data[9]['phone'],register_data[9]['psw'],register_data[9]['name'])
       codes = self.login.get_code(sqldata[9]['set or search'],sqldata[9]['table'],sqldata[9]['where'])
       self.login.wirte_code_register(codes[1])
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(),register_data[9]['except_result'])
   # 验证码为空
   def test_empty_code(self):
       '''请输入验证码'''
       self.login.send_code_register_loginpage(url,register_data[10]['phone'],register_data[10]['psw'],register_data[10]['name'])
       self.login.wirte_code_register(code = '')
       self.login.select_deal()
       self.login.register()
       self.assertEqual(self.toast.page_toast(),register_data[10]['except_result'])
   # 所有数据都为空
   def test_all_empty(self):
       '''请输入手机号'''
       self.login.send_code_register_loginpage(url, register_data[11]['phone'], register_data[11]['psw'], register_data[11]['name'])
       self.login.register()
       self.assertEqual(self.toast.page_toast(), register_data[11]['except_result'])
   # 不勾选服务协议
   def test_ignore_deal(self):
       '''请阅读服务协议并勾选'''
       self.login.send_code_register_loginpage(url, register_data[12]['phone'], register_data[12]['psw'], register_data[12]['name'])
       codes = self.login.get_code(sqldata[9]['set or search'], sqldata[9]['table'], sqldata[9]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.register()
       self.assertEqual(self.toast.page_toast(), register_data[12]['except_result'])
   # 注册成功后添加公司
   def test_register_addcompany(self):
       '''注册成功，添加公司'''
       self.login.send_code_register_loginpage(url,register_data[13]['phone'],register_data[13]['psw'],register_data[13]['name'])
       codes = self.login.get_code(sqldata[10]['set or search'],sqldata[10]['table'],sqldata[10]['where'])
       self.login.wirte_code_register(codes[0])
       self.login.select_deal()
       self.login.register()
       self.addcompany.add_companyName(companydata[6]['name'])
       self.addcompany.add_company_verify()
       self.assertEqual(self.addcompany.companyName(),companydata[6]['except_result'])
# if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Test_register('test_register_success'))
    # suite.addTest(Test_register('test_exist_phone'))
    # suite.addTest(Test_register('test_empty_psw'))
    # suite.addTest(Test_register('test_empty_name'))
    # suite.addTest(Test_register('test_empty_phone'))
    # suite.addTest(Test_register('test_incongruent_phone'))
    # suite.addTest(Test_register('test_incongruent_psw'))
    # suite.addTest(Test_register('test_allnumber_psw'))
    # suite.addTest(Test_register('test_less_psw'))
    # suite.addTest(Test_register('test_mismatch'))
    # suite.addTest(Test_register('test_empty_code'))
    # suite.addTest(Test_register('test_all_empty'))
    # suite.addTest(Test_register('test_ignore_deal'))
    # suite.addTest(Test_register('test_register_addcompany'))
    # unittest.TextTestRunner().run(suite)
