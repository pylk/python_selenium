
from Function.Login import LoginFuction
from Public.FindElement import FindElement
from selenium import webdriver
from time import sleep
class TradePage():
    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_buy_button_elem(self):
        return self.fd.get_element("buy_btn")

    def get_stock_elem(self):
        return self.fd.get_element("stock_code")

    def get_price_elem(self):
        return self.fd.get_element("price")

    def get_amount_elem(self):
        return self.fd.get_element("amount")

    def get_buybt_elem(self):
        return self.fd.get_element("submit")

    def get_confirm_elem(self):
        return self.fd.get_element("ok")

    def get_success_elem(self):
        return self.fd.get_element("success")

    def get_maxprice_elem(self):
        return self.fd.get_element("maxprice")

    def get_minprice_elem(self):
        return self.fd.get_element("minprice")

    def get_confirm_text_elem(self):
        res = self.fd.get_element("confirm_text")
        print(res)
        return res

if __name__ == '__main__':
    driver = webdriver.Firefox()
    ll = TradePage(driver)
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    login = LoginFuction(driver)
    login.login("15013695518","123456","7777")
    sleep(3)
    driver.find_element_by_css_selector("#myhome > a:nth-child(1)").click()
    sleep(3)
    driver.find_element_by_css_selector("#trade_center").click()
    driver.find_element_by_css_selector("#buy").click()
    sleep(3)
    driver.find_element_by_css_selector("#stockCode").send_keys("000001")
    sleep(5)
    driver.find_element_by_css_selector("#amount").send_keys("1000")
    sleep(3)
    driver.find_element_by_css_selector("#okbtn").click()
    sleep(3)
    driver.find_element_by_css_selector(".xubox_yes").click()
    # res = driver.find_element_by_css_selector("span.xubox_msg:nth-child(2)").text
    sleep(3)
    res = ll.get_confirm_text_elem().text
    print(res)
    # ll = TradePage(driver)
    # ll.get_minprice_elem()