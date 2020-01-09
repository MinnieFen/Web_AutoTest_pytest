# coding:utf-8
from selenium.webdriver.common.by import By
def login_elements():
    login_page_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')     # 0跳转登录页面
    psw_login_btn =(By.XPATH, '//*[@id="login_span_type_pwd"]')    # 1切换密码登录
    phone_word = (By.XPATH,'// *[@id = "login_id_input_phone"]')   # 2输入手机号
    psw_word = (By.XPATH,'//*[@id ="login_id_input_password"]')    # 3输入密码/验证码
    login_btn = (By.XPATH,'//*[@id="login_id_login"]')     # 4确定登录
    user_name_text = (By.XPATH,'//*[@class = "dropdown-toggle"]')   # 5登录成功header显示的用户名
    get_code_btn = (By.XPATH,'//*[@id = "login_button_get_sms_code"]')     # 6点击获取验证码
    forgot_psw_btn = (By.XPATH,'/html/body/div[1]/div/div/form/div[1]/div[5]/a')   # 7点击忘记密码
    new_psw_word = (By.XPATH,'//*[@id = "login_id_input_password_new"]')   # 8输入新密码
    register_page_btn = (By.XPATH,'/html/body/div[1]/div/div/form/div[2]/a')   # 9点击立即注册
    register_phone_word = (By.XPATH,'//*[@id = "user-phone-input"]')   # 10输入注册手机号
    register_psw_word = (By.XPATH,'//*[@id = "password-input"]')   # 11输入注册密码
    register_name_word = (By.XPATH,'//*[@id = "user-name-input"]')     # 12输入注册用户名
    register_code_btn = (By.XPATH,'//*[@id = "v-code-btn"]')       # 13点击注册获取验证码
    register_code_word = (By.XPATH,'//*[@id = "v-code-input"]')    # 14输入注册验证码
    agree_deal_btn = (By.XPATH,'//*[@class = "ui-checkbox wyydfwxy"]')     # 15勾选同意服务协议框
    confirm_register_btn = (By.XPATH,'//*[@id = "register-button"]')       # 16确定注册按钮
    back_to_homepage = (By.XPATH,'/html/body/nav/div/div[1]/a/span/span[1]')       # 17返回首页
    logout_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/ul/li[4]/a')        # 18点击退出按钮
    login_error_page = (By.CSS_SELECTOR,'.ui-tips-before')          # 19前端页面错误信息提示
    login_error_server = (By.XPATH,'//*[@class = "layui-layer-content"]')   # 20服务器错误信息提示
    register_heard_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[3]/a')   # 21 heard处企业注册按钮
    return login_page_btn, psw_login_btn, phone_word, psw_word, login_btn, user_name_text,get_code_btn, forgot_psw_btn, new_psw_word,\
            register_page_btn,register_phone_word,register_psw_word,register_name_word,register_code_btn,register_code_word,agree_deal_btn,\
            confirm_register_btn,back_to_homepage,logout_btn,login_error_page,login_error_server,register_heard_btn
# login_elements()
# print(login_elements())