# coding:utf-8
import unittest
from PageObject.UploadContractPageObject import Upload_contract
from public.GetExcelData import get_excel_data
from config import readconfig
from Base.DriverBase import DriverBase
from public.SQLconnect import MySQLUtil
from public.GetToastText import ToastText
driverbase = DriverBase()
uploaddata = get_excel_data(('upload_contract'))
sql_data = get_excel_data('sql_data')
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)

class UploadContract(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        driverbase.max_window()
        self.driver.implicitly_wait(10)
        self.upload = Upload_contract(self.driver)
        self.toast = ToastText(self.driver)
    def tearDown(self):
        driverbase.quit_broswer()
    # 上传pdf文件
    def upload_pdf(self):
        mysql.update(sql_data[0]['table'],sql_data[0]['set or search'],sql_data[0]['where'])           # 修改当前公司字段为0
        mysql.update(sql_data[1]['table'],sql_data[1]['set or search'],sql_data[1]['where'])           # 更新 成都知道创宇信息计数有限公司为当前公司
        self.upload.upload_contract(readconfig.url_admin,uploaddata[0]['path'])
        self.assertEqual(self.toast.page_toast(),uploaddata[0]['except_result'])
    # 上传doc文件
    def upload_doc(self):
        self.upload.upload_contract(readconfig.url_admin,uploaddata[1]['path'])
        self.assertEqual(self.toast.page_toast(),uploaddata[1]['except_result'])
    # 上传docx文件
    def upload_docx(self):
        self.upload.upload_contract(readconfig.url_admin,uploaddata[2]['path'])
        self.assertEqual(self.toast.page_toast(),uploaddata[2]['except_result'])
    # 上传较大文件
    def upload_75pages(self):
        self.upload.upload_contract(readconfig.url_admin,uploaddata[3]['path'])
        self.assertEqual(self.toast.page_toast(),uploaddata[3]['except_result'])
    #上传空文件
    def upload_empty_page(self):
        self.upload.upload_contract(readconfig.url_admin,uploaddata[4]['path'])
        self.assertEqual(self.toast.sever_toast(),uploaddata[4]['except_result'])
    #上传图片
    def upload_error_format(self):
        self.upload.upload_contract(readconfig.url_admin,uploaddata[5]['path'])  
        self.assertEqual(self.toast.sever_toast(),uploaddata[5]['except_result'])
    # 搜索已保护文档，有结果
    def search_doc(self):
        self.upload.search(readconfig.url_admin,uploaddata[6]['path'])
        lists = self.upload.search_result()
        num = len(lists)
        # print(num)
        # 数据库查询，与搜索结果做对比
    # 搜索已保护文档，无结果
    def search_empty_doc(self):
        self.upload.search(readconfig.url_admin,uploaddata[7]['path'])
        self.upload.search_result()
        self.assertEqual(self.upload.search_empty_data(),uploaddata[7]['except_result'])
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(UploadContract('upload_pdf'))
    # suite.addTest(UploadContract('upload_doc'))
    # suite.addTest(UploadContract('upload_docx'))
    # suite.addTest(UploadContract('upload_75pages'))
    # suite.addTest(UploadContract('upload_empty_page'))
    # suite.addTest(UploadContract('upload_error_format'))
    # suite.addTest(UploadContract('search_doc'))
    # suite.addTest((UploadContract('search_empty_doc')))
    unittest.TextTestRunner().run(suite)