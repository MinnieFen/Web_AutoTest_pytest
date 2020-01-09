# coding:utf-8
from selenium import webdriver
from time import sleep
from PageObject.LoginPageObject import Login
from ruamel import yaml
from Base.DriverBase import DriverBase
from config import readconfig
from Base.BasePage import BasePage
import os
import ruamel
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
class Cookie(BasePage):
    # def __init__(self):
    #     self.driverBase = DriverBase()
    #     self.driver = self.driverBase.open_broswer()    # 构造方法中写打开浏览器，会导致没调用一个方法时，都会多打开一次浏览器
    #     self.login = Login(self.driver)
# 封装元素操作方法
    def save_cookie(self,phone,psw,url):
        self.login = Login(self.driver)
        self.login.psw_login(phone,psw,url)
        login_cookie = self.get_login_cookie()
        yamlpath = os.path.abspath(os.path.dirname(__file__)) + '\login_cookie.yaml'
        cookie_value = login_cookie
        with open(yamlpath,'w',encoding='utf-8') as f:
            yaml.dump(cookie_value,f,Dumper=yaml.RoundTripDumper)
        sleep(3)
        # self.quit_driver()               # 加上这一句，同时执行sage_cookie、keep_login时，会报  由于目标计算机积极拒绝，无法连接  的错误
        # self.driverBase.quit_broswer()
        # self.driver.delete_cookie(name = 'laravel_session')
        # self.driver.refresh()
    def get_cookie(self,yamlName="login_cookie.yaml"):
        # self.save_cookie(phone,psw,url)
        f = os.path.abspath(os.path.dirname(__file__))
        p = f + '\login_cookie.yaml'
        f = open(p)
        value = f.read()
        cookie_all = yaml.load(value)
        cookie_name = cookie_all['name']
        cookie_value = cookie_all['value']
        cookie_data_dict = {'name': cookie_name, 'value': cookie_value}
        # print(cookie_data_dict)
        return cookie_data_dict
    def keep_login(self,url):
        cookieData = self.get_cookie()
        self.open_url(url)
        self.add_cookie(cookieData)
        self.open_url(url)
        self.driver.implicitly_wait(10)
# if __name__ == '__main__':
#     cookie = Cookie(driver=webdriver.Firefox())
#     phone = readconfig.inputPhone_cookie
#     psw = readconfig.inputPsw_cookie
#     urlcookie = readconfig.url_login
#     url = readconfig.url_admin
#     cookie.save_cookie(phone,psw,urlcookie)
#     cookie.keep_login(url)