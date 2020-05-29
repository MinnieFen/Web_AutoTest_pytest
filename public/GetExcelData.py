# coding:utf-8
from public.ReadExcel import ReadExcel
import os

# 调用read_excel方法，直接返回数据列表
def get_excel_data(sheetname):
    filepath_now = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    excel_path = filepath_now + '\TestData\\test_data.xlsx'
    # print(ReadExcel(excel_path,sheetname).read_excel_data())
    return ReadExcel(excel_path,sheetname).read_excel_data()
# get_excel_data('logindata')