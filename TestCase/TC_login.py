

import unittest
from selenium import webdriver
from Function.Login import LoginFuction

class TC_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
        self.login =  LoginFuction(self.driver)

    def test_login01(self):
        self.login.login("15013695518","123456","125")

    def test_login02(self):
        self.login.login("15013695517","123456","25")

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()

