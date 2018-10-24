from datetime import datetime
from time import time
from time import sleep
def baseUrl():
    return "http://192.168.1.155:8066"

#获取当前时间
def getCurrentTime():
    format = "%Y-%m-%d %H:%M:%S"
    return datetime.now().strftime(format)

#获取持续时间
def getDuration(starttime,endtime):
    format = "%Y-%m-%d %H:%M:%S"
    date = datetime.strptime(endtime,format) - datetime.strptime(starttime,format)
    return str(date)


if __name__ == '__main__':
    res = getCurrentTime()
    print(res)
    print(type(res))
    sleep(3)
    res1 = getCurrentTime()
    print(res1)

    res2 = getDuration(res,res1)
    print(res2)
    print(type(res2))