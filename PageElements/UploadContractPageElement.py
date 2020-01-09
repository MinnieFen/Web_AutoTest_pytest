# coding:utf-8
from selenium.webdriver.common.by import By
def contractProtect_elements():
    contract_protect_list = (By.XPATH,('/html/body/div[1]/div[1]/div/nav/ul/li[5]/a/span'))                     # 0 侧边栏 纸质合同数字保护
    select_contract_btn = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div/div[3]/div[3]/div[2]/button'))       # 1 上传按钮
    toast_page = (By.XPATH,('/html/body/div[1]/div[2]/div/div/div/div[3]/div[4]/div/div[2]/div[1]/p/span'))     # 2 弹框提示
    upload_error_server= (By.XPATH,'//*[@class = "layui-layer-content"]')                                       # 3 服务器提示
    upload_contract = (By.XPATH,'//*[@id="file"]')                                                              # 4 选择上传的文件
    return contract_protect_list,select_contract_btn,toast_page,upload_error_server,upload_contract