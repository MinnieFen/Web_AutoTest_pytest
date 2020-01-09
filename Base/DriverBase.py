# coding:utf-8
from selenium import webdriver
from config import readconfig
import os
import time

class DriverBase():
    def __init__(self):
        self.driverName = readconfig.browserName
    # 启动浏览器
    def open_broswer(self):
        if self.driverName == 'Firefox' or self.driverName == 'firefox':
            self.driver = webdriver.Firefox()
        elif self.driverName == 'Chrome' or self.driverName == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Ie()
        driver = self.driver
        return driver
    # 退出浏览器
    def quit_broswer(self):
        return self.driver.quit()
    # 浏览器窗口最大化
    def max_window(self):
        return self.driver.maximize_window()
    # 获取截图
    def get_screenshot(self):
        filepath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        return self.driver.get_screenshot_as_file(filepath + '/screenshots/%s.png' %nowTime)   # 将截图存储在screenshots文件中
