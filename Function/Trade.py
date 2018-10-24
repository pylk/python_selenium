from HandleElement.TradeHandle import TradeHandle
from selenium import webdriver
from Function.Login import LoginFuction
from time import sleep
class TradeFuction():

    def __init__(self,driver):
        self.driver = driver
        self.he =  TradeHandle(self.driver)
    #现价买入下单
    def buy_nowprice_order(self,stock,amount):
        self.he.click_buy()
        self.he.send_stock(stock)
        sleep(5)
        self.he.send_amount(amount)
        self.he.click_buy_btn()
        self.he.click_confirm()
        # sleep(3)
        # res = self.he.get_confirm_text()
        # print(res)
        # self.he.click_success()
        # return res
    #最高价买入下单
    def buy_maxprice_roder(self,stock,amount):
        self.he.click_buy()
        self.he.send_stock(stock)
        sleep(5)
        self.he.click_maxprice()
        self.he.send_amount(amount)
        self.he.click_buy_btn()
        self.he.click_confirm()
        self.he.click_success()

    #最低价买入下单
    def buy_minprice_order(self,stock,amount):
        self.he.click_buy()
        self.he.send_stock(stock)
        sleep(5)
        self.he.click_minprice()
        self.he.send_amount(amount)
        self.he.click_buy_btn()
        self.he.click_confirm()
        self.he.click_success()

    def buy_order(self,stock,price,amount):
        self.he.click_buy()
        self.he.send_stock(stock)
        sleep(12)
        self.he.clear_price()
        sleep(5)
        self.he.send_price(price)
        self.he.send_amount(amount)
        self.he.click_buy_btn()
        self.he.click_confirm()
        self.he.click_success()

    def sell_order(self):
        pass

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    login = LoginFuction(driver)
    login.login("15013695517", "123456", "7777")
    sleep(3)
    driver.find_element_by_css_selector("#myhome > a:nth-child(1)").click()
    sleep(3)
    driver.find_element_by_css_selector("#trade_center").click()
    sleep(3)
    ll = TradeFuction(driver)
    ll.buy_nowprice_order("000001","1000")



