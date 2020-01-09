# coding:utf-8
from PageElements.UploadContractPageElement import contractProtect_elements
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie

class Upload_contract(BasePage):
    # 进入选择文件页面
    def contract_protect_list(self,path):
        self.click_btn(*(contractProtect_elements()[0]))
        self.click_btn(*(contractProtect_elements()[1]))
        self.send_word(path,*(contractProtect_elements()[4]))
    # 前端提示信息
    def upload_page(self):
        return self.get_text(*(contractProtect_elements()[2]))
    # 服务器提示信息
    def upload_server(self):
        return self.get_text(*(contractProtect_elements()[3]))
    # 保持登录状态
    def keep_login_cookie(self,url):
        return Cookie(self.driver).keep_login(url)
    # 上传合同
    def upload_contract(self,url,path):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_protect_list(path)
        sleep(3)
