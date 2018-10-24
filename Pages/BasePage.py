from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Public.FindElement import FindElement
class BasePages():
    """
    封装所有页面的公共方法
    """
    #打开火狐浏览器
    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        except Exception:
            raise NameError("Not Firfox")
    #打开指定网页
    def openUrl(self,url):
        if url != "":
            self.driver.get(url)
        else:
            raise NameError("please input a valid url")
    # 根据参数从当前浏览器中定位一个元素
    def findEelement(self,element):
        try:
            type = element[0]
            value = element[1]
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

    # 根据参数从当前浏览器中定位一组元素
    def findEelements(self,element):
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_elements_by_id(value)
            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_elements_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_elements_by_class_name(value)
            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_elements_by_link_text(value)
            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_elements_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("please input correct the type parameter")
        except Exception:
            raise NameError("this element not found!" +str(element))
        return elem

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    #定义输入类容
    def send_value(self,content,key):
        elem = self.get_element(key)
        elem.clear()
        elem.send_keys(content)

    # 定义点击
    def click_element(self,element):
        elem = self.get_element(element)
        try:
            elem.click()
        except Exception as e:
            elem.click()

    #定义点击enter建
    def click_enter(self,element):
        elem = self.get_element(element)
        elem.send_keys(Keys.RETURN)

    #定义退出浏览
    def colse_driver(self):
        self.driver.quit()

    #获取指定元素的某一个属性值
    def getAttribute(self,element,attribute):
        return element.get_attribute(attribute)

    #获取指定元素是否当前在页面显示，返回值为True / False
    def display(self,element):
        elem = self.findEelement(element)
        return elem.is_displayed(elem)

    #获取页面标题
    def get_titile(self):
        return self.driver.title

    #获取浏览器的URL
    def get_url(self):
        return self.driver.current_url

    #JS提示框点确定
    def accepet_alert(self):
        self.driver.switch_to.alert.accept()

    # JS提示框点取消
    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    #隐式等待
    def implicitly_wait(self,second):
        self.driver.implicitly_wait(second)

    # 获取指定元素的文本内容
    def get_text(self,element):
        return  self.get_element(element).text

    # 提交一个指定的form
    def submit(self,element):
        elem = self.findEelement(element)
        elem.submit()
if __name__ == '__main__':
    ll = BasePages()
    # res1 = ll.openUrl("http://192.168.1.155:8066/simulate/views/sso/index.html?key=login")
    res = getattr(ll,"openUrl")
    # res = ll.get_text("my")
    print(res)










