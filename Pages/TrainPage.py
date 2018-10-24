from Pages.BasePage import BasePage
from time import sleep
class TrainPage(BasePage):

    url = "http://218.17.161.51:32982/simulate/views/navigate/practiceIndex.html?r=0.4663516327780577"
    two_page = ("css", "#paginate2 > div:nth-child(1) > span:nth-child(3) > a:nth-child(2)")
    next_page = ("css", "#paginate2 > div:nth-child(1) > a:nth-child(4)")
    forward_page = ("css", "#paginate2 > div:nth-child(1) > a:nth-child(2)")
    last_page = ("css", "#paginate2 > div:nth-child(1) > a:nth-child(5)")
    first_page = ("css", "#paginate2 > div:nth-child(1) > a:nth-child(1)")
    input_num = ("css", "#paginate2 > div:nth-child(2) > input:nth-child(1)")
    go = ("css", "#paginate2 > div:nth-child(2) > a:nth-child(2)")
    user_url = (
    "xpath", "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/table/tbody/tr[2]/td[2]/div/div[2]/a")

    def userRanking(self,numpage):
        self.openUrl(self.url)
        sleep(3)
        self.findEelement(self.user_url).click()
        self.driver.back()
        sleep(3)
        self.findEelement(self.two_page).click()
        self.findEelement(self.next_page).click()
        sleep(3)
        self.findEelement(self.forward_page).click()
        sleep(3)
        self.findEelement(self.last_page).click()
        sleep(3)
        self.findEelement(self.first_page).click()
        sleep(3)
        self.findEelement(self.input_num).send_keys(numpage)
        self.findEelement(self.go).click()
        self.driverQuit()
    user_name = ("css","#Pradealrank > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > a:nth-child(1)")
    today_buy = ("link_text","今日热门买入")
    today_sell = ("link_text", "今日热门卖出")
    big_stock = ("link_text","重仓股")
    trade_info = ("link_text","成交动态")
    infromation = ("link_text","详情")
    ability_info = ("link_text","能力透视")
    def orderInfo(self):
        self.openUrl(self.url)
        sleep(3)
        self.findEelement(self.today_buy).click()
        self.findEelement(self.today_sell).click()
        self.findEelement(self.big_stock).click()
        self.findEelement(self.trade_info).click()
        sleep(3)
        self.findEelement(self.user_name).click()
        sleep(3)
        self.findEelement(self.infromation).click()
        sleep(3)
        self.findEelement(self.ability_info).click()
        self.driverQuit()
    three = ("css","#paginate1 > div:nth-child(1) > span:nth-child(3) > a:nth-child(3)")
    Next_page = ("css","#paginate1 > div:nth-child(1) > a:nth-child(4)")
    Forward_page = ("css","#paginate1 > div:nth-child(1) > a:nth-child(2)")
    Last_page =("css","#paginate1 > div:nth-child(1) > a:nth-child(5)")
    First_page = ("xpath","//*[@id=first]")
    input_key = ("css","#paginate1 > div:nth-child(2) > input:nth-child(1)")
    gohome = ("css","#paginate1 > div:nth-child(2) > a:nth-child(2)")
    def tradeInfoQuery(self,num1):
        self.openUrl(self.url)
        sleep(3)
        self.findEelement(self.three).click()
        self.findEelement(self.Next_page).click()
        self.findEelement(self.Forward_page).click()
        self.findEelement(self.Last_page).click()
        sleep(3)
        self.findEelement(self.Forward_page).click()
        self.findEelement(self.input_key).send_keys(num1)
        self.findEelement(self.gohome).click()



if __name__ == '__main__':
    run = TrainPage()
    #ll.userRanking(3)
    #ll.orderInfo()
    run.tradeInfoQuery(12)