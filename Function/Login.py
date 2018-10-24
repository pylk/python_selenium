from HandleElement.LoginHandle import LoginHandle
from selenium import webdriver
class LoginFuction():

    def __init__(self,driver):
        self.driver = driver
        self.he =  LoginHandle(self.driver)

    def login(self,user,passwd,tickt):
        self.he.send_user(user)
        self.he.send_passwd(passwd)
        self.he.send_tickt(tickt)
        self.he.click_button()
if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    login = LoginFuction(driver)
    login.login("15013695516","123456","7777")