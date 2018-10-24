from Pages.TradePage import TradePage
from Function.Login import LoginFuction
from selenium import webdriver
from time import sleep
from Log.Log import UserLog


class TradeHandle():
    def __init__(self,driver):
        self.driver = driver
        self.log = UserLog()
        self.get_elem = TradePage(self.driver)

    def click_buy(self):
        self.get_elem.get_buy_button_elem().click()

    def send_stock(self,stock):
        self.log.get_log().info("输入股票代码" + stock)
        self.get_elem.get_stock_elem().send_keys(stock)

    def clear_price(self):
        self.get_elem.get_price_elem().clear()

    def send_price(self,price):
        self.log.get_log().info("输入价格" + price)
        self.get_elem.get_price_elem().send_keys(price)

    def send_amount(self,amount):
        self.log.get_log().info("输入股票数量" + amount)
        self.get_elem.get_amount_elem().send_keys(amount)

    def click_buy_btn(self):
        self.get_elem.get_buybt_elem().click()

    def click_confirm(self):
        self.get_elem.get_confirm_elem().click()

    def click_success(self):
        self.get_elem.get_success_elem().click()

    def click_maxprice(self):
        self.get_elem.get_maxprice_elem().click()

    def click_minprice(self):
        self.get_elem.get_minprice_elem().click()

    def get_confirm_text(self):
        res = self.get_elem.get_confirm_text_elem()
        print(res)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    ll = TradePage(driver)
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    login = LoginFuction(driver)
    login.login("15013695518", "123456", "7777")
    sleep(3)
    driver.find_element_by_css_selector("#myhome > a:nth-child(1)").click()
    sleep(3)
    driver.find_element_by_css_selector("#trade_center").click()
    sleep(3)
    driver.find_element_by_css_selector("#buy").click()
    sleep(3)
    driver.find_element_by_css_selector("#stockCode").send_keys("000001")
    sleep(5)
    driver.find_element_by_css_selector("#amount").send_keys("1000")
    sleep(3)
    driver.find_element_by_css_selector("#okbtn").click()
    driver.find_element_by_css_selector(".xubox_yes").click()

    ll = TradeHandle(driver)
    res = ll.get_confirm_text()
    print(res)
