from email.mime.text import MIMEText
from email.header import Header
from Config import GlobalConfig
from HTMLTestRunner import HTMLTestRunner
import smtplib,os,unittest,time
class SendEmail():

    def sendReport(self,file_new):
        #打开文件并并把文件的类容赋值给 mail_body
        with open(file_new,"rb") as f:
            mail_body = f.read()

        msg = MIMEText(mail_body,"html","utf-8")              #测试报告文本内容与格式
        msg['Subject'] = Header('自动化测试报告','utf-8')    #测试报告标题
        msg['from'] = '15013695512@163.com'
        msg['to'] = '739930126@qq.com'

        smtp = smtplib.SMTP("smtp.163.com")                    #链接smtp.163的服务
        smtp.login("15013695512@163.com","8023xifu")         #登录163邮件
        smtp.sendmail(msg['from'],msg['to'],msg.as_string())  #发送邮件
        smtp.quit()
        print("发送邮件成功")
    def newReport(self,testreport):
        lists = os.listdir(testreport)
        lists2 = sorted(lists)
        file_new = os.path.join(testreport,lists2[-1])
        return file_new

if __name__ == '__main__':
    ll = SendEmail()
    test_dir = GlobalConfig.testcase_path                               #测试用例路径
    test_report = GlobalConfig.testreport_path                          #测试报告路径
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="TC_login.py")
    now = time.strftime("%Y-%m-%d %H.%M.%S")                          #获取当前时间
    filename = test_report +"\\"+now+"result20.html"                  #拼接测试报告路径
    print(filename)
    f = open(filename,"wb")
    runner = HTMLTestRunner(stream=f,title="测试结果",description="测试用例执行情况")
    runner.run(discover)
    f.close()
    new_report = ll.newReport(test_report)
    print(new_report)
    ll.sendReport(new_report)