import unittest
import ddt
from selenium import webdriver
from Function.Trade import TradeFuction
from Function.Login import LoginFuction
from time import sleep
@ddt.ddt
class TC_trade(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
        login = LoginFuction(self.driver)
        login.login("15013695518", "123456", "7777")
        sleep(3)
        self.driver.find_element_by_css_selector("#myhome > a:nth-child(1)").click()
        sleep(3)
        self.driver.find_element_by_css_selector("#trade_center").click()
        sleep(3)
        self.trade = TradeFuction(self.driver)

    @ddt.data(
        ["000001","1000"],
        ["600000","1000"]
    )
    @ddt.unpack
    def test_nowprice(self,stock,amount):
        self.trade.buy_nowprice_order(stock,amount)

    @ddt.data(
        ["000001", "1000"],
        ["600000", "1000"]
    )
    @ddt.unpack
    def test_maxprice(self,stock,amount):
        self.trade.buy_maxprice_roder(stock,amount)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
     unittest.main()






