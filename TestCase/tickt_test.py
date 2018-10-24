from selenium import webdriver
from PIL import Image
from time import sleep
from Public.ShowapiRequest import ShowapiRequest
def saveTickt():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://218.17.161.51:32982/simulate/views/sso/index.html?key=login")
    driver.find_element_by_id("login_id").send_keys("15013695517")
    driver.find_element_by_id("password").send_keys("123456")
    driver.save_screenshot("E:/tickt01.png")
    sleep(3)
    heightpage = int(driver.execute_script("var a = $(window).height();return a"))
    print(heightpage)
    widthpage = int(driver.execute_script("var a = $(window).width();return a"))
    print(widthpage)


    # elem = driver.find_element_by_css_selector("#ticket_image")
    # left = elem.location["x"]
    # top = elem.location["y"]+15
    # right = left+elem.size["width"]
    # height = top+elem.size["height"]
    # im = Image.open("E:/tickt01.png")
    # new_image = im.resize((1536,759),Image.BILINEAR)
    # new_image.save("E:/tickt02.png")
    # sleep(3)
    # last_image = Image.open("E:/tickt02.png")
    # img = last_image.crop((left,top,right,height))
    # img.save("E:/tickt10.png")
    # r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
    # r.addBodyPara("typeId", "34")
    # r.addBodyPara("convert_to_jpg", "0")
    # r.addFilePara("image", r"E:/tickt10.png")  # 文件上传时设置
    # res = r.post()
    # text = res.json()['showapi_res_body']['Result']
    # driver.find_element_by_id("ticket_image_value").send_keys(text)
    #driver.find_element_by_id()

if __name__ == '__main__':
    saveTickt()