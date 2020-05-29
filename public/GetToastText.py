# coding:utf-8
from Base.BasePage import BasePage
from selenium.webdriver.common.by import By

add_error_server = (By.XPATH, ('//*[@class = "layui-layer-content layui-layer-padding"]'))  # 19 服务器错误提示
add_error_page = (By.XPATH, ('//*[@class = "ui-tips-before"]'))  # 20 前端页面错误提示

class ToastText(BasePage):
# 服务器错误提示
    def sever_toast(self):
        return self.get_text(*(add_error_server))
# 前端错误提示
    def page_toast(self):
        return self.get_text(*(add_error_page))