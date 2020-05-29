# coding:utf-8
from Base.BasePage import BasePage
from time import sleep
from Base.GetLoginCookie import Cookie
from selenium import webdriver
from config import readconfig
from selenium.webdriver.common.by import By

my_contract_list = (By.XPATH, ('/html/body/div[1]/div[1]/div/nav/ul/li[4]/a/span'))  # 0 侧边栏 我的契约
add_contract_btn = (By.XPATH, ('//*[@class = "btn btn-primary"]'))  # 1 我的契约按钮
company_input_word = (By.XPATH, ('//*[@id="company-input"]'))  # 2 对方公司输入框
search_btn = (By.XPATH, ('//*[@class = "ui-button company-button"]'))  # 3 搜索按钮
select_company = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[1]/div[2]/ul/li[1]/a'))  # 4 选择第一个公司
contract_time_word = (By.XPATH, ('//*[@class = "datepicker time-input"]'))  # 5 契约月份输入框
contract_time_btn = (By.XPATH, ('/html/body/div[5]/div[2]/table/tbody/tr/td/span[12]'))  # 6 12月
contract_describe_word = (By.XPATH, ('//*[@class = "describe-text"]'))  # 7 契约描述
contract_finish_btn = (By.XPATH, ('//*[@class = "ui-radio type-over-title"]'))  # 8 已完成契约
contract_appraise_word = (By.XPATH, ('//*[@class = "over-describe-text"]'))  # 9 契约评价
attitude = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[1]/div[1]/div/img[1]'))  # 10 态度1星评价
quality = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[1]/div[2]/div/img[2]'))  # 11 质量2星评价
efficiency = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[2]/div[1]/div/img[3]'))  # 12 效率3星评价
credit = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[2]/div[2]/div/img[4]'))  # 13 守信4星评价
specialty = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[7]/div[2]/div[3]/div[1]/div/img[5]'))  # 14 专业5星评价
contract_unfinish_btn = (By.XPATH, ('//*[@class = "ui-radio type-ing-title"]'))  # 15 未完成契约
use_stamp_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/div[1]/div[1]/label[1]'))  # 16 我方使用防伪印章
other_use_stamp_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[4]/div[8]/div[2]/div[1]/div[2]/label[1]'))  # 17 对方使用防伪印章
add_contract_verify_btn = (By.XPATH, ('//*[@class = "over-btn btn btn-primary"]'))  # 18 确认添加契约
add_error_server = (By.XPATH, ('//*[@class = "layui-layer-content layui-layer-padding"]'))  # 19 服务器错误提示
add_error_page = (By.XPATH, ('//*[@class = "ui-tips-before"]'))  # 20 前端页面错误提示
add_toast = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/p[1]'))  # 21 弹框提示对方不是防伪印章用户
add_toast_user = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/p'))  # 22 弹框提示我方不是防伪印章用户

all_page = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[1]/a'))  # 23 全部列表
wait_confirm = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[2]/a'))  # 24 待我确认列表
wait_complete = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[3]/a'))  # 25 待我完成列表
wait_appraise = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[4]/a'))  # 26 待我评价列表
wait_other_confirm = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/ul/li[5]/a'))  # 27 待对方确认列表
wait_confirm_num = (By.XPATH, ('//*[@id="waitermyconfirm"]'))  # 28 待我确认数量
wait_complete_num = (By.XPATH, ('//*[@id="waitermycomplete"]'))  # 29 待我完成数量
wait_appraise_num = (By.XPATH, ('//*[@id="waitermyappraise"]'))  # 30 待我评价数量
wait_other_confirm_num = (By.XPATH, ('//*[@id="waiterotherconfirm"]'))  # 31 待对方确认数量
search_word = (By.XPATH, ('//*[@class = "form-control"]'))  # 32 关键字（对方公司）搜索输入框
search_other_btn = (By.XPATH, ('//*[@class = "btn btn-primary"]'))  # 33 搜索按钮
confirm_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/button[1]'))  # 34第一条确认完成契约按钮
confirm_cancel = (By.XPATH, ('//*[@id="cancelbtn"]'))  # 35 取消确认完成契约
confirm_ensure = (By.XPATH, ('//*[@id="confimbtn"]'))  # 36 确定确认完成契约
refuse_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/button[2]'))  # 37第一条拒绝按钮
refuse_word = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[2]/form/textarea'))  # 38 拒绝内容
refuse_cancel = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[3]/button[1]'))  # 39 取消拒绝
refuse_ensure = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[3]/div/div/div[3]/button[2]'))  # 40 确认拒绝
complete_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/button'))  # 41第一条完成契约按钮
complete_cancle_btn = (By.XPATH, ('//*[@id="cancelbtn"]'))  # 42 取消完成契约
confirm_complete = (By.XPATH, ('//*[@id="confimbtn"]'))  # 43 确认完成契约
appraise_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div[1]/div[2]/button'))  # 44 评价按钮
appraise_word = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/textarea'))  # 45 评价内容输入框
appraise_attitude = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[1]/span[2]/img[1]'))  # 46 态度一星
appraise_quality = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[2]/span[2]/img[2]'))  # 47 质量两星
appraise_efficiency = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[3]/span[2]/img[3]'))  # 48 效率三星
appraise_credit = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[4]/span[2]/img[4]'))  # 49 守信四星
appraise_specialty = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div[5]/span[2]/img[5]'))  # 50 专业五星
appraise_cancle_btn = (By.XPATH, ('//*[@class = "btn btn-default"]'))  # 51 取消评价
appraise_ensure_btn = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[3]/button[2]'))  # 52 确认评价
wait_other_confirm_edit = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[2]/button[1]'))  # 53 待对方确认，编辑按钮
edit_time = (By.XPATH, ('/html/body/div[5]/div[2]/table/tbody/tr/td/span[6]'))  # 54 重新选择契约月份为6月
wait_other_confirm_delet = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[2]/button[2]'))  # 55 删除待对方确认契约按钮
delet_cancel = (By.XPATH, ('//*[@id="cancelbtn"]'))  # 56 取消删除
delet_ensure = (By.XPATH, ('//*[@id="confimbtn"]'))  # 57 确认删除
# describe_text = (By.LINK_TEXT('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div[1]/p[2]'))                      # 58 获取待确认列表描述内容
all_list_pages = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li/a'))  # 59 获取分页总数
all_list_last_page = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li[1]/a/span'))  # 60 上一页按钮
all_list_next_page = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/nav/ul/li[5]/a/span'))  # 61 下一页按钮
all_list_page_num = (By.XPATH, ('/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div'))  # 62 获取一页的总数

class Add_Contract(BasePage):
    # 点击侧边栏我的契约
    def contract_list(self):
        self.click_btn(*my_contract_list)
        sleep(3)
    # 点击添加契约按钮
    def add_contract_btn(self):
        self.click_btn(*add_contract_btn)
        sleep(3)
    # 输入公司名称，搜索
    def company_name(self,companyName):
        self.send_word(companyName,*company_input_word)
        self.click_btn(*search_btn)
        sleep(3)
        self.click_btn(*select_company)       # 选择第一个公司
        self.click_btn(*contract_time_word)       # 选择12月
        sleep(2)
        self.click_btn(*contract_time_btn)
        sleep(2)
    # 输入契约描述
    def contract_describe(self,contract_word):
        self.send_word(contract_word,*contract_describe_word)
    # 选择已完成契约，选择评价等级
    def select_finish_contracr(self,contract_appraise):
        self.click_btn(*contract_finish_btn)
        self.send_word(contract_appraise,*contract_appraise_word)
        self.click_btn(*attitude)
        self.click_btn(*quality)
        self.click_btn(*efficiency)
        self.click_btn(*credit)
        self.click_btn(*specialty)
    # 选择未完成契约
    def select_unfinish_contract(self):
        self.click_btn(*contract_unfinish_btn)
    # 选择我方使用防伪印章
    def select_use_stamp(self):
        self.click_btn(*use_stamp_btn)
    # 选择对方使用防伪印章
    def select_other_use_stamp(self):
        self.click_btn(*other_use_stamp_btn)
    # 确认添加契约
    def add_contracr_verify(self):
        self.click_btn(*add_contract_verify_btn)
    # 保持登录状态
    def keep_login_cookie(self,url):
        return Cookie(self.driver).keep_login(url)
    # 弹框提示对方不是印章用户
    def add_toast(self):
        return self.get_text(*add_toast)
    # 弹框提示我方不是印章用户
    def add_toast_user(self):
        return self.get_text(*add_toast_user)

    # 前端错误提示
    # def contract_error_page(self):
    #     return self.get_text(*add_error_server)
    # 添加已完成契约
    def add_finish_contract(self,url,companyName,contract_word,contract_appraise):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_finish_contracr(contract_appraise)
        self.add_contracr_verify()
        sleep(2)
    # 添加未完成契约,未选择防伪印章
    def add_unfinish_contract(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，选择我方使用防伪印章
    def add_unfinish_use_stamp(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.select_use_stamp()
        # self.add_contracr_verify()
        sleep(3)
    #添加未完成契约，选择我方使用防伪印章，确认添加
    def add_unfinish_use_verify(self,url,companyName,contract_word):
        self.add_unfinish_use_stamp(url,companyName,contract_word)
        self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，选择对方使用防伪印章
    def add_unfinish_other_use_stamp(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.select_other_use_stamp()
        # self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，选择对方使用防伪印章，确认添加
    def add_unfinish_other_verify(self,url,companyName,contract_word):
        self.add_unfinish_other_use_stamp(url,companyName,contract_word)
        self.add_contracr_verify()
        sleep(3)
    # 添加未完成契约，双方都使用防伪印章
    def add_unfinish_all_use_stamp(self,url,companyName,contract_word):
        self.keep_login_cookie(url)
        sleep(2)
        self.contract_list()
        self.add_contract_btn()
        self.company_name(companyName)
        self.contract_describe(contract_word)
        self.select_unfinish_contract()
        self.select_use_stamp()
        self.select_other_use_stamp()
        self.add_contracr_verify()
        sleep(3)
    # 选择列表
    def select_list(self,url,listName):
        self.keep_login_cookie(url)
        sleep(3)
        self.contract_list()
        sleep(2)
        self.click_btn(*listName)
    # 选择待我确认列表
    def select_wait_confirm(self,url):
        self.select_list(url,wait_confirm)
    # 待我确认数量
    def wait_confirm_num(self):
        return self.get_text(*wait_confirm_num)
    # 确认完成契约
    def confirm_ensure(self):
        # self.select_wait_confirm(url)
        self.click_btn(*confirm_btn)
        self.click_btn(*confirm_ensure)
        sleep(3)
    # 取消确认完成契约
    def confirm_cancel(self):
        # self.select_wait_confirm(url)
        self.click_btn(*confirm_btn)
        self.click_btn(*confirm_cancel)
        sleep(3)
    # 选择拒绝契约
    def select_refuse(self):
        # self.select_wait_confirm(url)
        self.click_btn(*refuse_btn)
    # 确认拒绝契约
    def refuse_ensure(self,reason):
        self.select_refuse()
        self.send_word(reason,*refuse_word)
        self.click_btn(*refuse_ensure)
        sleep(2)
    # 取消拒绝契约
    def refuse_cancel(self):
        self.select_refuse()
        # self.send_word(reason,*(addContract_elements()[38]))
        self.click_btn(*refuse_cancel)
    # 选择待我完成契约列表
    def select_wait_complete(self,url):
        self.select_list(url,wait_complete)
    # 待我完成列表数量
    def wait_complete_num(self):
        return self.get_text(*wait_complete_num)
    # 确认完成契约
    def complete_ensure(self):
        # self.select_wait_complete(url)
        self.click_btn(*complete_btn)
        self.click_btn(*confirm_complete)
        sleep(3)
    # 取消完成契约
    def complete_cancel(self):
        # self.select_wait_complete(url)
        self.click_btn(*complete_btn)
        self.click_btn(*complete_cancle_btn)
        sleep(2)
    # 选择待我评价列表
    def select_wait_appraise(self,url):
        self.select_list(url,wait_appraise)
        sleep(2)
    # 待我评价列表数量
    def wait_appraise_num(self):
        return self.get_text(*wait_appraise_num)
    # 点击评价按钮，输入评价内容
    def appraise_content(self,content):
        # self.select_wait_appraise(url)
        self.click_btn(*appraise_btn)
        sleep(1)
        self.send_word(content,*appraise_word)
        sleep(2)
    # 选择评价星级
    def appraise_grade(self):
        self.click_btn(*appraise_attitude)
        self.click_btn(*appraise_quality)
        self.click_btn(*appraise_efficiency)
        self.click_btn(*appraise_credit)
        self.click_btn(*appraise_specialty)
    # 输入评价内容，选择评价等级,确认评价
    def appraise_ensure(self,content):
        self.appraise_content(content)
        self.appraise_grade()
        self.click_btn(*appraise_ensure_btn)
        sleep(2)
    # 输入评价内容，不选择评价等级，确认评价
    def appraise_empty_grade(self,content):
        self.appraise_content(content)
        self.click_btn(*appraise_ensure_btn)
    # 输入评价内容，选择评价等级，取消评价
    def appraise_cancel(self,content):
        self.appraise_content(content)
        self.appraise_grade()
        self.click_btn(*appraise_cancle_btn)
    # 不输入评价内容，不选择评价等级，确定评价
    def appraise_cancel_empty(self,content):
        self.appraise_content(content)
        self.click_btn(*appraise_ensure_btn)
    # 待对方确认列表
    def select_wait_other_confirm(self,url):
        self.select_list(url,wait_other_confirm)
        sleep(2)
    # 待对方确认数量
    def wait_other_confirm_num(self):
        return self.get_text(*wait_other_confirm_num)
    # 编辑契约，不修改直接确认
    def unaltered_ensure(self):
        # self.select_wait_other_confirm(url)
        self.click_btn(*wait_other_confirm_edit)
        self.click_btn(*add_contract_verify_btn)
        sleep(2)
    # 编辑契约，重新选择月份，重新输入描述
    def alter_ensure(self,decrible):
        # self.select_wait_other_confirm(url)
        self.click_btn(*wait_other_confirm_edit)
        self.click_btn(*edit_time)
        self.send_word(decrible,*contract_describe_word)
        self.click_btn(*add_contract_verify_btn)
        sleep(2)
    # 待确认列表，取消删除
    def delect_cancel(self):
        self.click_btn(*wait_other_confirm_delet)
        self.click_btn(*delet_cancel)
        sleep(2)
    # 待确认列表，确认删除
    def delect_ensure(self):
        self.click_btn(*wait_other_confirm_delet)
        self.click_btn(*delet_ensure)
        sleep(2)
    # 待确认列表，描述内容
    # def waitconfirm_text(self):
        # self.get_text(*(addContract_elements()[58]))
# if __name__ == '__main__':
    # con = Add_Contract(driver=webdriver.Firefox())
#     companyName = '千帆渡'
#     contract_word = '这是契约描述'
#     contract_appraise = '这是契约评价'
#     url = readconfig.url_admin
#     con.add_finish_contract(companyName,contract_word,contract_appraise,url)
#     con.confirm_ensure(url)