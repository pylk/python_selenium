from selenium import webdriver
from Pages.LoginPage import LoginPage
from Log.Log import UserLog
class LoginHandle():
    def __init__(self,driver):
        self.driver = driver
        self.log = UserLog()
        self.get_elem = LoginPage(self.driver)

    def send_user(self,user):
        self.log.get_log().info("输入用户名"+user)
        self.get_elem.get_user_element().send_keys(user)

    def send_passwd(self,passwd):
        self.log.get_log().info("输入密码" + passwd)
        self.get_elem.get_passwd_element().send_keys(passwd)

    def send_tickt(self,tickt):
        self.log.get_log().info("输入验证码" + tickt)
        self.get_elem.get_tickt_element().send_keys(tickt)

    def click_button(self):
        self.get_elem.get_button_element().click()
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    ll = LoginHandle(driver)
    ll.send_user("15013695515")
    # ll.send_passwd("123456")
