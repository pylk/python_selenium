import os
from Public.ReadConfigIni import ReadConfigIni

#获取当前路径下的config.ini配置文件
file_path = os.path.split(os.path.realpath(__file__))[0]

#实例化并读取config.ini文件
readconfig = ReadConfigIni(os.path.join(file_path,"config.ini"))

#获取当前工程路径（从配置文件中）
poject_path = readconfig.get_section_value("project_path","project")

#获取日志路径
log_path = os.path.join(poject_path,"Report","Log")

#获取测试用例路径
testcase_path = os.path.join(poject_path,"TestCase")

#获取测试报告路径
testreport_path = os.path.join(poject_path,"Report","TestReport")

#获取测试数据路径
testdate_path = os.path.join(poject_path,"Date","TestData")

