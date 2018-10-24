from Pages.BasePage import BasePage
from Pages.LoginPage1 import MncgLogin
from time import sleep

class MyAccountPage(MncgLogin):
    my_account = ("css", "#myhome > a:nth-child(1)")
    total_assets = ("id", "total_assets")
    my_home = ("css", "#n1 > a:nth-child(1)")
    ability_btn = ("css", "#ability")
    trade_center = ("css", "#trade_center")
    #登录并进入我的账户界面下
    def __init__(self):
        super(MncgLogin,self).__init__()
        self.login("15013695515", "123456")
        sleep(3)
        text = self.findEelement(self.my_account).text
        print(text)
        self.findEelement(self.my_account).click()
        sleep(3)
    #我的首页测试
    def myHome(self):
        #self.login("15013695515","123456")
        self.findEelement(self.my_home).click()
        sleep(3)
        self.findEelement(self.ability_btn).click()
        self.driver.back()
        sleep(3)
        self.findEelement(self.trade_center).click()
        self.colse_driver()

    my_activity = ("css", "#n2 > a:nth-child(1)")
    activity_ing = ("css", "#myAttend > a:nth-child(1) > span:nth-child(1)")
    activity_apply = ("css", "#myApply > a:nth-child(1) > span:nth-child(1)")
    activity_end = ("css", "#myFinished > a:nth-child(1) > span:nth-child(1)")
    # 我的赛场测试
    def myActivity(self):
        self.findEelement(self.my_activity).click()
        self.findEelement(self.activity_ing).click()
        self.findEelement(self.activity_apply).click()
        self.findEelement(self.activity_end).click()
        self.driverQuit()
    #基本资料测试
    basic_info = ("css","#n3 > a:nth-child(1)")
    user_info = ("css","#user_info")
    face_image = ("css","#face_image")
    alter_passwd = ("css","#password")
    def basicInfo(self):
        self.findEelement(self.basic_info).click()
        sleep(3)
        self.findEelement(self.user_info).click()
        self.findEelement(self.face_image).click()
        self.findEelement(self.alter_passwd).click()
    #修改基本资料测试
    user_name = ("css","#user_info_tab_con > div:nth-child(2) > input:nth-child(2)")
    woman_box = ("css","#fe_male")
    man_box = ("css","#male")
    secret_box = ("css","#no_male")
    submit = ("id","submit_user_info")
    def alterInfo(self,name):
        self.findEelement(self.basic_info).click()
        sleep(3)
        self.findEelement(self.user_info).click()
        self.findEelement(self.user_name).clear()
        self.findEelement(self.user_name).send_keys(name)
        res = self.findEelement(self.woman_box).get_attribute("sex")
        #0代表男，1代表女，如果res=1,就点女的单选框，否则就点击其他两个中的一个
        if res == 1:
            self.findEelement(self.man_box).click()
        else:
            self.findEelement(self.woman_box).click() or self.findEelement(self.secret_box).click()
        self.findEelement(self.submit).click()
        self.driverQuit()
    #修改密码
    old_passwd = ("css","#current_password")
    new_passwd = ("css","#new_password")
    affirm_passwd = ("css","#new_password_again")
    passwd_submit = ("css","#modifyPassword")
    def alterPasswd(self,old_passwd,new_passwd,affirm_passwd):
        self.findEelement(self.basic_info).click()
        sleep(3)
        self.findEelement(self.user_info).click()
        self.findEelement(self.alter_passwd).click()
        self.findEelement(self.old_passwd).send_keys(old_passwd)
        self.findEelement(self.new_passwd).send_keys(new_passwd)
        self.findEelement(self.affirm_passwd).send_keys(affirm_passwd)
        self.findEelement(self.passwd_submit).click()
        self.colse_driver()
    #修改头像
    update_image = ("css","#attachment")
    image_submit = ("css","#upload_temp")
    keep_image = ("css",".shangchuang_a")
    confirm = ("css",".xubox_yes")
    def alterFaceImage(self,filename):
        self.findEelement(self.basic_info).click()
        sleep(3)
        self.findEelement(self.user_info).click()
        self.findEelement(self.face_image).click()
        self.findEelement(self.face_image).click()
        self.findEelement(self.update_image).send_keys(filename)
        self.findEelement(self.image_submit).click()
        sleep(3)
        self.findEelement(self.keep_image).click()
        sleep(3)
        self.findEelement(self.confirm).click()
        self.colse_driver()

    #交易规则测试
    trade_rule = ("css","#n4 > a:nth-child(1)")
    def tradeRuler(self):
        self.findEelement(self.trade_rule).click()
        self.colse_driver()

if __name__ == '__main__':
    ll = MyAccountPage()
    ll.myHome()