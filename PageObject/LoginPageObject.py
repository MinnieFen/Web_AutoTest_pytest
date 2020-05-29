# coding:utf-8
from time import sleep
from selenium.webdriver.common.by import By
from config import readconfig
from public.GetExcelData import get_excel_data
from Base.BasePage import BasePage
from public.SQLconnect import MySQLUtil

# from Base.DriverBase import start_driver
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)
sqldata = get_excel_data('sql_data')

login_page_btn = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/a')  # 0跳转登录页面
psw_login_btn = (By.XPATH, '//*[@id="login_span_type_pwd"]')  # 1切换密码登录
phone_word = (By.XPATH, '// *[@id = "login_id_input_phone"]')  # 2输入手机号
psw_word = (By.XPATH, '//*[@id ="login_id_input_password"]')  # 3输入密码/验证码
login_btn = (By.XPATH, '//*[@id="login_id_login"]')  # 4确定登录
user_name_text = (By.XPATH, '//*[@class = "dropdown-toggle"]')  # 5登录成功header显示的用户名
get_code_btn = (By.XPATH, '//*[@id = "login_button_get_sms_code"]')  # 6点击获取验证码
forgot_psw_btn = (By.XPATH, '/html/body/div[1]/div/div/form/div[1]/div[5]/a')  # 7点击忘记密码
new_psw_word = (By.XPATH, '//*[@id = "login_id_input_password_new"]')  # 8输入新密码
register_page_btn = (By.XPATH, '/html/body/div[1]/div/div/form/div[2]/a')  # 9点击立即注册
register_phone_word = (By.XPATH, '//*[@id = "user-phone-input"]')  # 10输入注册手机号
register_psw_word = (By.XPATH, '//*[@id = "password-input"]')  # 11输入注册密码
register_name_word = (By.XPATH, '//*[@id = "user-name-input"]')  # 12输入注册用户名
register_code_btn = (By.XPATH, '//*[@id = "v-code-btn"]')  # 13点击注册获取验证码
register_code_word = (By.XPATH, '//*[@id = "v-code-input"]')  # 14输入注册验证码
agree_deal_btn = (By.XPATH, '//*[@class = "ui-checkbox wyydfwxy"]')  # 15勾选同意服务协议框
confirm_register_btn = (By.XPATH, '//*[@id = "register-button"]')  # 16确定注册按钮
back_to_homepage = (By.XPATH, '/html/body/nav/div/div[1]/a/span/span[1]')  # 17返回首页
logout_btn = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[2]/ul/li[4]/a')  # 18点击退出按钮
login_error_page = (By.CSS_SELECTOR, '.ui-tips-before')  # 19前端页面错误信息提示
login_error_server = (By.XPATH, '//*[@class = "layui-layer-content"]')  # 20服务器错误信息提示
register_heard_btn = (By.XPATH, '/html/body/nav/div/div[2]/ul/li[3]/a')  # 21 heard处企业注册按钮

class Login(BasePage):
    # 跳转到登录页面
    def login_page(self):
        self.click_btn(*login_page_btn)
    # 切换密码登录
    def psw_login_page(self):
        self.click_btn(*psw_login_btn)
    # 输入手机号
    def login_phone(self,inputPhone):
        self.clear_word(*phone_word)
        self.send_word(inputPhone,*phone_word)
    # 输入密码
    def login_psw(self,inputPsw):
        self.clear_word(*psw_word)
        self.send_word(inputPsw,*psw_word)
    # 点击获取验证码
    def click_code(self):
        self.click_btn(*get_code_btn)
    # 确定登录按钮
    def login_button(self):
        self.click_btn(*login_btn)
    # 登录成功用户名
    def login_success_username(self):
        return self.get_text(*user_name_text)

    # 获取验证码
    def get_code(self,search,table,where):
        return mysql.select(search,table,where)
    # 注册账号成功，添加公司弹框
    def register_success(self):
        return self.get_text(*register_phone_word)
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
        self.click_btn(*get_code_btn)
        sleep(3)
    def code_login(self,code):
        self.login_psw(code)
        self.login_button()
        sleep(2)
    # 忘记密码
    def send_code_reset(self,url,inputPhone):
        self.open_url(url)
        self.login_page()
        self.click_btn(*forgot_psw_btn)
        self.login_phone(inputPhone)
        self.click_code()
        sleep(3)
    def psw_reset(self,code,new_psw):
        self.login_psw(code)
        self.send_word(new_psw,*new_psw_word)
        self.login_button()
        sleep(2)
    # 注册账号
    def register_heard(self,url):      # 点击heard注册按钮进入注册页面
        self.open_url(url)
        self.click_btn(*register_heard_btn)
    def register_loginpage(self,url):   #点击登录页面注册进入注册页面
        self.open_url(url)
        self.login_page()
        self.click_btn(*register_page_btn)
    def send_code(self,phone,psw,name):
        self.send_word(phone, *register_phone_word)
        self.send_word(psw, *register_psw_word)
        self.send_word(name, *register_name_word)
        self.click_btn(*register_code_btn)
        sleep(5)
    def send_code_register_heard(self,url,phone,psw,name):
        self.register_heard(url)
        self.send_code(phone,psw,name)
    def send_code_register_loginpage(self,url,phone,psw,name):
        self.register_loginpage(url)
        self.send_code(phone,psw,name)
    def wirte_code_register(self,code):
        self.send_word(code,*register_code_word)
    def select_deal(self):
        self.click_btn(*agree_deal_btn)
    def register(self):
        self.click_btn(*confirm_register_btn)
        sleep(3)
# if __name__ == '__main__':
#     login = Login(driver=webdriver.Firefox())
#     login.psw_login('18782038145','a123456','http://qiyuebao-t.yunxitech.cn/')
