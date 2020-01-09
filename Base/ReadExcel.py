# coding:utf-8
import xlrd
import os

class ReadExcel(object):
    def __init__(self,excelpath,sheetname):
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetname)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def read_excel_data(self):
        file_list = []
        for i in range(1,self.rowNum):
            data_dict = {}
            for j in range(self.colNum):
                data = self.table.cell_value(i,j)
                data_dict[self.keys[j]] = data
            file_list.append(data_dict)
        return file_list