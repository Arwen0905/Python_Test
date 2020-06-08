import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.google.com.tw/")
 
#寫入內容
elem = driver.find_element_by_name("q")
elem.send_keys("HTML CSS")
time.sleep(1)
 
#刪除一個字符
elem.send_keys(Keys.BACK_SPACE)
elem.send_keys(Keys.BACK_SPACE)
elem.send_keys(Keys.BACK_SPACE)
elem.send_keys(Keys.BACK_SPACE)
time.sleep(1)
 
#輸入空格後 內容
elem.send_keys(Keys.SPACE)
elem.send_keys(u"博客萊")
time.sleep(1)
elem.send_keys(Keys.BACK_SPACE)
 
#ctrl+a 全選內容
elem.send_keys(Keys.CONTROL,'a')
time.sleep(1)
 
#ctrl+x 剪下內容
elem.send_keys(Keys.CONTROL,'x')
time.sleep(1)
 
#ctrl+v 貼上內容
elem.send_keys(Keys.CONTROL,'v')
time.sleep(1)
#輸入框補字
elem.send_keys(u"來") 
time.sleep(1)
#點擊
driver.find_element_by_name("q").send_keys(Keys.ENTER)
