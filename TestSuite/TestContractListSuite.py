# coding:utf-8
from Base.DriverBase import DriverBase
from PageObject.AddContractPageObject import Add_Contract
from public.GetExcelData import get_excel_data
from config import readconfig
from public.SQLconnect import MySQLUtil
import unittest
from public.GetToastText import ToastText
driverbase = DriverBase()
contract_list_data = get_excel_data('contract_list')
sql_data = get_excel_data('sql_data')
mysql = MySQLUtil(db=readconfig.sql_db_qiyuebao)

class ContractList(unittest.TestCase):
    def setUp(self):
        self.driver = driverbase.open_broswer()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.add = Add_Contract(self.driver)
        self.toast = ToastText(self.driver)
    def tearDown(self):
        driverbase.quit_broswer()
    # 待我确认列表取消确认契约
    def test_cancel_confirm_contract(self):
        mysql.update(sql_data[0]['table'], sql_data[0]['set or search'], sql_data[0]['where'])  # 修改当前公司字段为0
        mysql.update(sql_data[1]['table'], sql_data[1]['set or search'], sql_data[1]['where'])  # 更新 成都知道创宇信息计数有限公司为当前公司
        self.add.select_wait_confirm(readconfig.url_admin)
        num_wait_confirm_1 = int(self.add.wait_confirm_num())
        self.add.confirm_cancel()
        num_wait_confirm_2 = int(self.add.wait_confirm_num())
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2)
    # 待我确认列表，确认契约
    def test_confirm_contract(self):
        self.add.select_wait_confirm(readconfig.url_admin)
        num_wait_confirm_1 = int(self.add.wait_confirm_num())
        num_wait_complete_1 = int(self.add.wait_complete_num())
        self.add.confirm_ensure()
        num_wait_confirm_2 = int(self.add.wait_confirm_num())
        num_wait_complete_2 = int(self.add.wait_complete_num())
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2+1)
        self.assertEqual(num_wait_complete_1,num_wait_complete_2-1)
    # 待我确认列表，确定拒绝契约
    def test_refuse_contract(self):
        self.add.select_wait_confirm(readconfig.url_admin)
        num_wait_confirm_1 = int(self.add.wait_confirm_num())
        self.add.refuse_ensure(contract_list_data[0]['reason'])
        num_wait_confirm_2 = int(self.add.wait_confirm_num())
        self.assertEqual(self.toast.sever_toast(),contract_list_data[0]['except_result'])
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2+1)
    # 待我确认列表，确定拒绝契约，内容为空
    def test_refuse_contract_empty(self):
        self.add.select_wait_confirm(readconfig.url_admin)
        self.add.refuse_ensure(contract_list_data[1]['reason'])
        self.assertEqual(self.toast.sever_toast(), contract_list_data[1]['except_result'])
    # 待我确认列表，取消拒绝契约
    def test_cancel_refuse_contract(self):
        self.add.select_wait_confirm(readconfig.url_admin)
        num_wait_confirm_1 = int(self.add.wait_confirm_num())
        self.add.refuse_cancel()
        num_wait_confirm_2 = int(self.add.wait_confirm_num())
        self.assertEqual(num_wait_confirm_1,num_wait_confirm_2)
    # 待我完成列表，取消确认完成
    def test_cancel_complete(self):
        self.add.select_wait_complete(readconfig.url_admin)
        num_wait_complete_1 = int(self.add.wait_complete_num())
        self.add.complete_cancel()
        num_wait_complete_2 = int(self.add.wait_complete_num())
        self.assertEqual(num_wait_complete_1,num_wait_complete_2)
    # 待我完成列表，确认完成
    def test_complete_contract(self):
        self.add.select_wait_complete(readconfig.url_admin)
        num_wait_complete_1 = int(self.add.wait_complete_num())
        self.add.complete_ensure()
        num_wait_complete_2 = int(self.add.wait_complete_num())
        self.assertEqual(num_wait_complete_1,num_wait_complete_2+1)
    # 待我评价列表，不输入评价内容，不选择评价等级，确认评价
    def test_apprise_empty(self):
        self.add.select_wait_appraise(readconfig.url_admin)
        # num_wait_apprise_1 = int(self.add.wait_appraise_num())
        self.add.appraise_cancel_empty(contract_list_data[2]['reason'])
        self.assertEqual(self.toast.sever_toast(),contract_list_data[2]['except_result'])
    # 输入评价内容，不选择评价等级，确认评价
    def test_appraise_empty_grade(self):
        self.add.select_wait_appraise(readconfig.url_admin)
        self.add.appraise_empty_grade(contract_list_data[3]['reason'])
        self.assertEqual(self.toast.sever_toast(),contract_list_data[3]['except_result'])
    # 输入评价内容，选择评价等级，取消评价
    def test_appraise_cancel(self):
        self.add.select_wait_appraise(readconfig.url_admin)
        num_wait_appraise_1 = int(self.add.wait_appraise_num())
        self.add.appraise_cancel(contract_list_data[4]['reason'])
        num_wait_appraise_2 = int(self.add.wait_appraise_num())
        self.assertEqual(num_wait_appraise_1,num_wait_appraise_2)
    # 输入评价内容，选择评价等级,确认评价
    def test_appraise_ensure(self):
        self.add.select_wait_appraise(readconfig.url_admin)
        num_wait_appraise_1 = int(self.add.wait_appraise_num())
        self.add.appraise_ensure(contract_list_data[5]['reason'])
        num_wait_appraise_2 = int(self.add.wait_appraise_num())
        self.assertEqual(num_wait_appraise_1,num_wait_appraise_2+1)
    # 待确认列表，编辑契约，不修改直接确认
    def test_waitconfirm_ensure(self):
        self.add.select_wait_other_confirm(readconfig.url_admin)
        num_wait_other_confirm_1 = int(self.add.wait_other_confirm_num())
        self.add.unaltered_ensure()
        num_wait_other_confirm_2 = int(self.add.wait_other_confirm_num())
        self.assertEqual(num_wait_other_confirm_1,num_wait_other_confirm_2)
    # 待确认列表，重新编辑，提交
    def test_alter_ensure(self):
        self.add.select_wait_other_confirm(readconfig.url_admin)
        num_wait_other_confirm_1 = int(self.add.wait_other_confirm_num())
        self.add.alter_ensure(contract_list_data[6]['reason'])
        num_wait_other_confirm_2 = int(self.add.wait_other_confirm_num())
        # self.assertEqual(self.add.waitconfirm_text(),contract_list_data[6]['result'])
        self.assertEqual(num_wait_other_confirm_1,num_wait_other_confirm_2)
    # 待确认列表，取消删除
    def test_waitconfirm_delect_cancel(self):
        self.add.select_wait_other_confirm(readconfig.url_admin)
        num_wait_other_confirm_1 = int(self.add.wait_other_confirm_num())
        self.add.delect_cancel()
        num_wait_other_confirm_2 = int(self.add.wait_other_confirm_num())
        self.assertEqual(num_wait_other_confirm_1,num_wait_other_confirm_2)
    # 待确认列表，确认删除
    def test_waitconfirm_delect_ensure(self):
        self.add.select_wait_other_confirm(readconfig.url_admin)
        num_wait_other_confirm_1 = int(self.add.wait_other_confirm_num())
        self.add.delect_ensure()
        num_wait_other_confirm_2 = int(self.add.wait_other_confirm_num())
        self.assertEqual(num_wait_other_confirm_1,num_wait_other_confirm_2+1)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(ContractList('test_cancel_confirm_contract'))
    # suite.addTest(ContractList('test_confirm_contract'))
    # suite.addTest(ContractList('test_refuse_contract'))
    # suite.addTest(ContractList('test_refuse_contract_empty'))
    # suite.addTest(ContractList('test_cancel_refuse_contract'))
    # suite.addTest(ContractList('test_cancel_complete'))
    # suite.addTest(ContractList('test_complete_contract'))
    # suite.addTest(ContractList('test_apprise_empty'))
    # suite.addTest(ContractList('test_appraise_empty_grade'))
    # suite.addTest(ContractList('test_appraise_cancel'))
    # suite.addTest(ContractList('test_appraise_ensure'))
    suite.addTest(ContractList('test_waitconfirm_ensure'))
    # suite.addTest(ContractList('test_alter_ensure'))
    # suite.addTest(ContractList('test_waitconfirm_delect_cancel'))
    # suite.addTest(ContractList('test_waitconfirm_delect_ensure'))
    unittest.TextTestRunner().run(suite)