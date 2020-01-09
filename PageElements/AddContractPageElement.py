# coding:utf-8
from selenium.webdriver.common.by import By
def addContract_elements():
    my_contract_list = (By.XPATH,('/html/body/div[1]/div[1]/div/nav/ul/li[4]/a/span'))   # 0 侧边栏 我的契约
    add_contract_btn = (By.XPATH,('//*[@class = "btn btn-primary"]'))                    # 1 我的契约按钮
    company_input_word = (By.XPATH,('//*[@id="company-input"]')) # 2 对方公司输入框
    search_btn = (By.XPATH,('//*[@class = "ui-button company-button"]'))                   # 3 搜索按钮
    select_company = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/ul/li[1]/a'))    # 4 选择第一个公司
    contract_time_word = (By.XPATH,('//*[@class = "datepicker time-input"]'))              # 5 契约月份输入框
    contract_time_btn = (By.XPATH,('/html/body/div[5]/div[2]/table/tbody/tr/td/span[12]'))  # 6 12月
    contract_describe_word = (By.XPATH,('//*[@class = "describe-text"]'))                  # 7 契约描述
    contract_finish_btn = (By.XPATH,('//*[@class = "ui-radio type-over-title"]'))          # 8 已完成契约
    contract_appraise_word = (By.XPATH,('//*[@class = "over-describe-text"]'))             # 9 契约评价
    attitude = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[1]/div[1]/div/img[1]'))   # 10 态度1星评价
    quality = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[1]/div[2]/div/img[2]'))    # 11 质量2星评价
    efficiency = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[2]/div[1]/div/img[3]')) # 12 效率3星评价
    credit = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[2]/div[2]/div/img[4]'))     # 13 守信4星评价
    specialty = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[3]/div[1]/div/img[5]'))  # 14 专业5星评价
    contract_unfinish_btn = (By.XPATH,('//*[@class = "ui-radio type-ing-title"]'))         # 15 未完成契约
    use_stamp_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/div[1]/div[1]/label[1]'))   # 16 我方使用防伪印章
    other_use_stamp_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/div[1]/div[2]/label[1]'))   # 17 对方使用防伪印章
    add_contract_verify_btn = (By.XPATH,('//*[@class = "over-btn btn btn-primary"]'))          # 18 确认添加契约
    add_error_server = (By.XPATH,('//*[@class = "layui-layer-content layui-layer-padding"]'))  # 19 服务器错误提示
    add_error_page = (By.XPATH,('//*[@class = "ui-tips-before"]'))                              # 20 前端页面错误提示
    add_toast = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/p[1]'))      # 21 弹框提示对方不是防伪印章用户
    add_toast_user = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/p'))    # 22 弹框提示我方不是防伪印章用户
 
    return my_contract_list,add_contract_btn,company_input_word,search_btn,select_company,contract_time_word,contract_time_btn,contract_describe_word,contract_finish_btn,\
            contract_appraise_word,attitude,quality,efficiency,credit,specialty,contract_unfinish_btn,use_stamp_btn,other_use_stamp_btn,add_contract_verify_btn,add_error_server, \
            add_error_page,add_toast,add_toast_user

