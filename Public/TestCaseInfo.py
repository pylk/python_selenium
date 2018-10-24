
class TestCaseInfo():
    #定义测试用例信息
    def __init__(self,id="",name="",owner="",result="",starttime="",endtime="",duration="",errorinfo=""):
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.duration = duration
        self.errorinfo = errorinfo
    #获得用例id
    def get_id(self):
        return self.id

    # 获得用例name
    def get_name(self):
        return self.name

    # 获得用例owner
    def get_owner(self):
        return self.owner

    # 获得用例开始时间
    def get_starttime(self):
        return "开始时间"+self.starttime

    # 获得用例获得用例结束时间
    def get_endtime(self):
        return self.endtime

    # 获得用例持续时间
    def get_duration(self):
        return self.duration

    # 获得用例错误信息
    def errorinfo(self):
        return self.errorinfo

if __name__ == '__main__':
    ll = TestCaseInfo(name="登录")
    res = ll.get_name()
    print(res)

