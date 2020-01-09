# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from config import readconfig
from Base.GetExcelData import get_excel_data
from Base.BasePage import BasePage
from Base.SQLconnect import MySQLUtil
from PageElements.LoginPageElements import login_elements
from PageElements.AddCompanyPageElements import addCompany_elements
# from Base.DriverBase import start_driver
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)
sqldata = get_excel_data('sql_data')
class Login(BasePage):
    # 跳转到登录页面
    def login_page(self):
        self.click_btn(*(login_elements()[0]))
    # 切换密码登录
    def psw_login_page(self):
        self.click_btn(*(login_elements()[1]))
    # 输入手机号
    def login_phone(self,inputPhone):
        self.clear_word(*(login_elements()[2]))
        self.send_word(inputPhone,*(login_elements()[2]))
    # 输入密码
    def login_psw(self,inputPsw):
        self.clear_word(*(login_elements()[3]))
        self.send_word(inputPsw,*(login_elements()[3]))
    # 点击获取验证码
    def click_code(self):
        self.click_btn(*login_elements()[6])
    # 确定登录按钮
    def login_button(self):
        self.click_btn(*(login_elements()[4]))
    # 登录成功用户名
    def login_success_username(self):
        return self.get_text(*(login_elements()[5]))
    # 前端错误信息提示
    def login_error_page(self):
        return self.get_text(*(login_elements()[19]))
    # 服务器信息提示
    def login_error_sever(self):
        return self.get_text(*(login_elements()[20]))
    # 获取验证码
    def get_code(self,search,table,where):
        return mysql.select(search,table,where)
    # 注册账号成功，添加公司弹框
    def register_success(self):
        return self.get_text(*(addCompany_elements()[10]))
    # 密码登录
    def psw_login(self,inputPhone,inputPsw,url):
        self.open_url(url)
        self.login_page()
        self.psw_login_page()
        self.login_phone(inputPhone)
        self.login_psw(inputPsw)
        self.login_button()
        sleep(2)
    # 验证码登录
    def send_code_login(self,url,inputPhone):
        self.open_url(url)
        self.login_page()
        sleep(3)
        self.login_phone(inputPhone)
        self.click_btn(*(login_elements()[6]))
        sleep(3)
    def code_login(self,code):
        self.login_psw(code)
        self.login_button()
        sleep(2)
    # 忘记密码
    def send_code_reset(self,url,inputPhone):
        self.open_url(url)
        self.login_page()
        self.click_btn(*(login_elements()[7]))
        self.login_phone(inputPhone)
        self.click_code()
        sleep(3)
    def psw_reset(self,code,new_psw):
        self.login_psw(code)
        self.send_word(new_psw,*(login_elements()[8]))
        self.login_button()
        sleep(2)
    # 注册账号
    def register_heard(self,url):      # 点击heard注册按钮进入注册页面
        self.open_url(url)
        self.click_btn(*login_elements()[21])
    def register_loginpage(self,url):   #点击登录页面注册进入注册页面
        self.open_url(url)
        self.login_page()
        self.click_btn(*(login_elements()[9]))
    def send_code(self,phone,psw,name):
        self.send_word(phone, *(login_elements()[10]))
        self.send_word(psw, *(login_elements()[11]))
        self.send_word(name, *(login_elements()[12]))
        self.click_btn(*login_elements()[13])
        sleep(5)
    def send_code_register_heard(self,url,phone,psw,name):
        self.register_heard(url)
        self.send_code(phone,psw,name)
    def send_code_register_loginpage(self,url,phone,psw,name):
        self.register_loginpage(url)
        self.send_code(phone,psw,name)
    def wirte_code_register(self,code):
        self.send_word(code,*(login_elements()[14]))
    def select_deal(self):
        self.click_btn(*(login_elements()[15]))
    def register(self):
        self.click_btn(*(login_elements()[16]))
        sleep(3)
# if __name__ == '__main__':
#     login = Login(driver=webdriver.Firefox())
#     login.psw_login('18782038145','a123456','http://qiyuebao-t.yunxitech.cn/')
