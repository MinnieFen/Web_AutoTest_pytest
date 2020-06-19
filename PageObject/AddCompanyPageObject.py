# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium.webdriver.common.by import By
# 添加公司功能的元素定位
company_list_btn = (By.XPATH, '//*[@class = "company-name"]')  # 0 点击展开公司列表
add_company_btn = (By.XPATH, '//*[@class = "lnr lnr-plus-circle"]')  # 1 点击添加公司按钮
company_name_word = (By.XPATH, '//*[@class = "form-control"]')  # 2 公司名称输入框
verify_add_company_btn = (By.XPATH, '//*[@class = "btn btn-primary"]')  # 3 确认添加公司
cancel_add_company_btn = (By.XPATH,'//*[@id="cancel"]')   #取消添加公司
company_name_text = (By.XPATH, '/html/body/div[1]/nav/div[2]/div/ul/li[2]/a/span')  # 4 header显示公司名称
add_error_sever = (By.XPATH, '//*[@class = "layui-layer-content layui-layer-padding"]')  # 5 服务器错误信息提示
select_vocation = (By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/select')  # 6 展开公司行业
select_education = (By.XPATH, "//option[@value='教育培训']")  # 7 选择教育培训
select_waterboard = (By.XPATH, "//option[@value='水利水电']")  # 8 选择水利水电
add_error_page = (By.XPATH, '//*[@class = "ui-tips-before"]')  # 9 前端错误提示
first_add_company = (By.XPATH, '//*[@id="companyModalLabel"]')  # 10 新账号首次添加公司
username_btn = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a')  # 11 登录成功，用户名按钮
mycompany_btn = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a')  # 12 下拉框，我的公司

class Add_company(BasePage):
    # 点击展开公司列表
    def company_list(self):
        self.click_btn(*company_list_btn)
    # 点击添加公司按钮
    def add_company_button(self):
        self.click_btn(*add_company_btn)
    # 输入添加公司名称
    def add_companyName(self,companyName):
        self.send_word(companyName,*company_name_word)
    # 展开公司行业
    def company_vocation_list(self):
        self.click_btn(*select_vocation)
    # 选择教育培训
    def select_education(self):
        self.click_btn(*select_education)
    # 选择水利水电
    def select_waterboard(self):
        self.click_btn(*select_waterboard)
    # 确认添加公司
    def add_company_verify(self):
        self.click_btn(*verify_add_company_btn)
        sleep(3)
    # 取消添加公司
    def cancel_add_company(self):
        self.click_btn(*cancel_add_company_btn)
        sleep(3)
    # hearde显示的公司名称
    def companyName(self):
        return self.get_text(*company_list_btn)
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
        # sleep(3)
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
        self.click_btn(*username_btn)
        sleep(3)
        self.click_btn(*mycompany_btn)
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
