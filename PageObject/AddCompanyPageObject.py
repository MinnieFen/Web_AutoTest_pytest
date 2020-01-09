# coding:utf-8
from selenium import webdriver
from Base.BasePage import BasePage
from time import sleep
from PageElements.AddCompanyPageElements import addCompany_elements
from Base.SQLconnect import MySQLUtil
from Base.GetLoginCookie import Cookie
from config import readconfig
from PageObject.LoginPageObject import Login
class Add_company(BasePage):
    # 点击展开公司列表
    def company_list(self):
        self.click_btn(*(addCompany_elements()[0]))
    # 点击添加公司按钮
    def add_company_button(self):
        self.click_btn(*(addCompany_elements()[1]))
    # 输入添加公司名称
    def add_companyName(self,companyName):
        self.send_word(companyName,*(addCompany_elements()[2]))
    # 展开公司行业
    def company_vocation_list(self):
        self.click_btn(*(addCompany_elements()[6]))
    # 选择教育培训
    def select_education(self):
        self.click_btn(*(addCompany_elements()[7]))
    # 选择水利水电
    def select_waterboard(self):
        self.click_btn(*(addCompany_elements()[8]))
    # 确认添加公司
    def add_company_verify(self):
        self.click_btn(*(addCompany_elements()[3]))
        sleep(3)
    # hearde显示的公司名称
    def companyName(self):
        return self.get_text(*(addCompany_elements()[0]))
    # 添加公司，服务器报错信息
    def add_error_sever(self):
        return self.get_text(*(addCompany_elements()[5]))
    #添加公司，前端报错信息
    def add_error_page(self):
        return self.get_text(*(addCompany_elements()[9]))
    # 获取登录cookie
    def save_login_cookie(self,phone,psw,urlcookie):
        return Cookie(self.driver).save_cookie(phone,psw,urlcookie)
    # 保持登录状态
    def keep_login_cookie(self,url):
        return Cookie(self.driver).keep_login(url)
    # 添加公司,默认行业
    def add_company(self,companyName,url):
        self.keep_login_cookie(url)
        self.company_list()
        self.add_company_button()
        self.add_companyName(companyName)
        self.add_company_verify()
        sleep(3)
    # 选择教育行业
    def add_company_education(self,companyName,url):
        self.keep_login_cookie(url)
        self.company_list()
        self.add_company_button()
        self.add_companyName(companyName)
        self.company_vocation_list()
        self.select_education()
        self.add_company_verify()
        sleep(3)
    #选择水利水电行业
    def add_company_waterboard(self,companyName,url):
        self.keep_login_cookie(url)
        self.company_list()
        self.add_company_button()
        self.add_companyName(companyName)
        self.company_vocation_list()
        self.select_waterboard()
        self.add_company_verify()
        sleep(3)
    def first_login(self):
        self.click_btn(*(addCompany_elements()[11]))
        sleep(3)
        self.click_btn(*(addCompany_elements()[12]))
        sleep(3)
# if __name__ == '__main__':
#     a = Add_company(driver=webdriver.Firefox())
#     urlcookie = readconfig.url_login
#     phone = readconfig.inputPhone_cookie
#     psw = readconfig.inputPsw_cookie
#     url = readconfig.url_admin
#     companyName = '金控集团'
#     a.add_company(phone,psw,urlcookie,companyName,url)
#     companyName1 = '金控集团1'
#     a.add_company_education(companyName1,url)
#     companyName2 = '金控集团2'
#     a.add_company_waterboard(companyName2,url)
