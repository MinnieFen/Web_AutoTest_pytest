# coding:utf-8
from PageObject.AddCompanyPageObject import Add_company
from Base.DriverBase import DriverBase
import unittest
from config import readconfig
from public.GetExcelData import get_excel_data
from PageObject.LoginPageObject import Login
from public.GetToastText import ToastText
driverbase = DriverBase()
companyName = get_excel_data('add_company')
logindata = get_excel_data(('register'))

class AddCompany(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        driverbase.max_window()
        self.driver.implicitly_wait(10)
        self.add = Add_company(self.driver)
        self.login = Login(self.driver)
        self.toast = ToastText(self.driver)
    def tearDown(self):
        driverbase.quit_broswer()
    # 公司名为空
    def test_add_nullname(self):
        self.add.save_login_cookie(readconfig.inputPhone_cookie,readconfig.inputPsw_cookie,readconfig.url_login)    # 登录一次，后面的不用再次登录
        self.add.add_company(companyName[0]['name'],readconfig.url_admin)
        self.assertEqual(self.toast.page_toast(),companyName[0]['except_result'])
    # 添加公司，默认行业
    def test_default_vocation(self):
        self.add.add_company(companyName[1]['name'],readconfig.url_admin)
        self.assertEqual(self.add.companyName(),companyName[1]['except_result'])
    # 添加公司，选择教育培训行业
    def test_select_education(self):
        self.add.add_company_education(companyName[2]['name'],readconfig.url_admin)
        self.assertEqual(self.add.companyName(),companyName[2]['except_result'])
    #添加公司，选择水利水电行业
    def test_select_waterboard(self):
        self.add.add_company_waterboard(companyName[3]['name'],readconfig.url_admin)
        self.assertEqual(self.add.companyName(),companyName[3]['except_result'])
    #添加已存在的公司
    def test_exist_company(self):
        self.add.add_company_education(companyName[4]['name'],readconfig.url_admin)
        self.assertEqual(self.toast.sever_toast(),companyName[4]['except_result'])
    # 添加已被认证的公司
    def test_attestation_company(self):
        self.add.add_company_education(companyName[5]['name'],readconfig.url_admin)
        self.assertEqual(self.toast.sever_toast(),companyName[5]['except_result'])
    # 新账号首次添加公司
    def test_first_addcompany(self):
        self.login.psw_login(logindata[0]['phone'],logindata[0]['psw'],readconfig.url_login)
        self.add.first_login()
        self.add.add_companyName(companyName[7]['name'])
        self.add.add_company_verify()
        self.assertEqual(self.add.companyName(),companyName[7]['except_result'])
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(AddCompany('test_add_nullname'))
#     suite.addTest(AddCompany('test_default_vocation'))
#     suite.addTest(AddCompany('test_select_education'))
#     suite.addTest(AddCompany('test_select_waterboard'))
#     suite.addTest(AddCompany('test_exist_company'))
#     suite.addTest((AddCompany('test_exist_company')))
#     suite.addTest((AddCompany('test_first_addcompany')))
#     unittest.TextTestRunner().run(suite)