
import configparser

class ReadConfigIni(object):
    #实例化，并读取配置文件
    def __init__(self,filename = None,section = None):
        if filename == None:
            filename = r"C:\Users\fantao\PycharmProjects\AutoMncg\Public\config.ini"
        if section == None:
            self.section = "page_element"
        else:
            self.section = section
        self.cf = configparser.ConfigParser()
        self.cf.read(filename,encoding='UTF-8')
    #读取filename某个节点下的某个值
    def get_section_value(self,value,section = None):
        if section == None:
            value = self.cf.get(self.section,value)
        else:
            value = self.cf.get(section,value)
        return value
if __name__ == '__main__':
    ll  = ReadConfigIni()
    res = ll.get_section_value("user")
    print(res)