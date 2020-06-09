import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome('../chromedriver.exe')
driver.get("https://www.google.com.tw/")
 
#寫入內容
elem = driver.find_element_by_name("q")
elem.send_keys(u"東")
time.sleep(1)
elem.send_keys(u"踏踏取蜜")
time.sleep(2)

# 退後刪除
elem.send_keys(Keys.BACK_SPACE)
elem.send_keys(Keys.BACK_SPACE)
time.sleep(1)
elem.send_keys(Keys.BACK_SPACE)
time.sleep(1)
 
#輸入空格後 內容
elem.send_keys(u"取")
time.sleep(1)
elem.send_keys(u"蜜")
time.sleep(1)
elem.send_keys(Keys.F12)
 
#ctrl+a 全選內容
elem.send_keys(Keys.CONTROL,'a')
time.sleep(1)

#點擊
# driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.find_element_by_name("q").submit()
