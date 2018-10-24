from Public.ReadConfigIni import ReadConfigIni
from Log.Log import UserLog
from selenium import webdriver
from Config import GlobalConfig
log_path = GlobalConfig.log_path
import logging
class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
        self.log = UserLog()
    def get_element(self,element):
        read_ini = ReadConfigIni()
        data = read_ini.get_section_value(element)
        type = data.split('>>')[0]
        value = data.split('>>')[1]
        self.log.get_log().info("定位方式:"+ type +"--->定位值:"+value)
        try:
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)
            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)
            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_element_by_link_text(value)
            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("please input correct the type parameter")
        except Exception:
            raise NameError("this element not found!" +str(element))

        return elem

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    ll = FindElement(driver)
    res = ll.get_element("confirm_text")
    print(res)