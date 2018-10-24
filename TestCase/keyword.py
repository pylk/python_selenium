import sys
sys.path.append(r"C:\Users\fantao\PycharmProjects\AutoMncg\Public")
from Public.DoExcel import DoExcel
from Pages.BasePage import BasePages
from time import sleep
class TC_keyword():
    def __init__(self):
        self.handle_method = BasePages()
        self.do_excel = DoExcel()

    def run_main(self):
        rows = self.do_excel.get_rows()
        for i in range(1,rows):
            run = self.do_excel.read_excel(i,3)
            if run == "yes":
                run_method = self.do_excel.read_excel(i,4)
                input_value = self.do_excel.read_excel(i,5)
                do_element = self.do_excel.read_excel(i,6)
                self.run_method(run_method, input_value, do_element)
                sleep(3)
                check_elem = self.do_excel.read_excel(i,7)
                expect_result = self.do_excel.read_excel(i,8)
                if  expect_result != '':
                    expect_value = self.get_except_result_value(expect_result)
                    if expect_value[0] == 'text':
                        # result = self.run_method(expect_result_method)
                        result = self.handle_method.get_text(check_elem)
                        # print(result)
                        if expect_value[1] in result:
                            self.do_excel.write_value(i, 'pass')
                        else:
                            self.do_excel.write_value(i, 'fail')
    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self,method, send_value = '' ,do_element = ''):
        method_value = getattr(self.handle_method,method)
        if send_value == '' and do_element !='':
            result = method_value(do_element)
        elif send_value == '' and do_element =='':
            result = method_value()
        elif send_value != '' and do_element =='':
            result = method_value(send_value)
        else:
            result = method_value(send_value,do_element)
        return result
if __name__ == '__main__':
    lo = TC_keyword()
    lo.run_main()
