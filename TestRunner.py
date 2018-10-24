from HTMLTestRunner import HTMLTestRunner
from Public.SendEmail import SendEmail
from Config import GlobalConfig
import unittest,time

test_dir = GlobalConfig.testcase_path                 # 测试用例路径
test_report = GlobalConfig.testreport_path            # 测试报告路径

class MncgTestRunner():
    def __init__(self):
        self.sendemail = SendEmail()

    #批量读取python文件获取所有测试用例,并发送测试报告
    def run_suites(self,testcasename):
        now = time.strftime("%Y-%m-%d %H.%M.%S")
        filename = test_report + "\\" + now + "result.html"
        file = open(filename, "wb")
        #加载testcase,下所有的测试用例
        all_cases = unittest.defaultTestLoader.discover(test_dir, pattern=testcasename)
        runner = HTMLTestRunner(stream=file, title="测试结果", description="测试用例执行情况")
        runner.run(all_cases)
        file.close()
        new_report = self.sendemail.newReport(test_report)
        self.sendemail.sendReport(new_report)

if __name__ == '__main__':
    ll = MncgTestRunner()
    ll.run_suites("TC_*.py")

