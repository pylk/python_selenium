
from Public.FindElement import FindElement
from selenium import webdriver
class LoginPage():

    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_user_element(self):
        return self.fd.get_element("user")

    def get_passwd_element(self):
        return self.fd.get_element("passwd")

    def get_tickt_element(self):
        return  self.fd.get_element("tickt")

    def get_button_element(self):
        return self.fd.get_element("button")
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    ll = LoginPage(driver)
    ll.get_button_element()