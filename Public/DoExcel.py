import xlrd
from xlutils.copy import copy
class DoExcel():
    #打开Excel
    def __init__(self,filename = None, sheetname = None):
        #如果输入指定文件就读指定文件，否则取默认文件
        # 如果输入指定sheet就读取指定sheet,否则读取默认sheet
        if filename:
            self.filename = filename
            self.sheename = sheetname
        else:
            self.filename =  r"C:/Users/fantao/PycharmProjects/AutoMncg/Data/TestData/keyword.xls"
            self.sheetname = "sheet1"

        self.sheet = self.get_sheet()
    # 获取sheets的内容
    def get_sheet(self):
        excel = xlrd.open_workbook(self.filename)
        tables = excel.sheet_by_name(self.sheetname)
        return tables

    #获取表格行数
    def get_rows(self):
        rows = self.sheet.nrows
        return rows

    #读取指定单元格的值
    def read_excel(self,rownum,colnum):
        value = self.sheet.cell(rownum,colnum).value
        return value

    #通过遍历得到每行的数据
    def get_row_date(self):
        res = []
        for i in range(self.get_rows()):
            row_date = self.sheet.row_values(i)
            print(row_date)
            res.append(row_date)
        return res

    #将结果写入excel
    def write_value(self,row,value):
        self.filename = r"C:\Users\fantao\PycharmProjects\AutoMncg\Data\TestData\keyword.xls"
        read_data = xlrd.open_workbook(self.filename)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,9,value)
        write_data.save(self.filename)


if __name__ == '__main__':
    ll = DoExcel()
    res = ll.read_excel(2,5)
    print(res)