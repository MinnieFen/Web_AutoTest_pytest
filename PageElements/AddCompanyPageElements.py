# conding:utf-8
from selenium.webdriver.common.by import By
def addCompany_elements():
    company_list_btn = (By.XPATH,'//*[@class = "company-name"]')    # 0 点击展开公司列表
    add_company_btn = (By.XPATH,'//*[@class = "lnr lnr-plus-circle"]')     # 1 点击添加公司按钮
    company_name_word = (By.XPATH,'//*[@class = "form-control"]')        # 2 公司名称输入框
    verify_add_company_btn = (By.XPATH,'//*[@class = "btn btn-primary"]')    # 3 确认添加公司
    company_name_text = (By.XPATH,'/html/body/div[1]/nav/div[2]/div/ul/li[2]/a/span')    # 4 header显示公司名称
    add_error_sever = (By.XPATH,'//*[@class = "layui-layer-content layui-layer-padding"]')      # 5 服务器错误信息提示
    select_vocation = (By.XPATH,'/html/body/div[2]/div/div/div[2]/form/div[2]/div[2]/select')   # 6 展开公司行业
    select_education = (By.XPATH,"//option[@value='教育培训']")                                 # 7 选择教育培训
    select_waterboard = (By.XPATH,"//option[@value='水利水电']")                                # 8 选择水利水电
    add_error_page = (By.XPATH,'//*[@class = "ui-tips-before"]')                                # 9 前端错误提示
    first_add_company = (By.XPATH,'//*[@id="companyModalLabel"]')                               # 10 新账号首次添加公司
    username_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/a')                            # 11 登录成功，用户名按钮
    mycompany_btn = (By.XPATH,'/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a')                  # 12 下拉框，我的公司
    return company_list_btn,add_company_btn,company_name_word,verify_add_company_btn,company_name_text,add_error_sever,select_vocation,\
    select_education,select_waterboard,add_error_page,first_add_company,username_btn,mycompany_btn
# addCompany_elements()