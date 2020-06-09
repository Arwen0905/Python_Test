import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
 
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.google.com.tw/")
 
# 取得圖片
elem_pic = driver.find_element_by_xpath("//img[@id='hplogo']")
# 圖片網址輸出
time.sleep(3)
print(elem_pic.get_attribute("src"),'<<< src')
# 滑鼠移動至圖片上
action = ActionChains(driver).move_to_element(elem_pic)
# 執行右鍵
action.context_click(elem_pic)
#! 語法重點: 當右鍵點擊後，彈出視窗，向下移動至右鍵菜單第一個選項
action.send_keys(Keys.ARROW_DOWN)
# 睡一會
print('睡一會')
time.sleep(3)
# 另存為
action.send_keys('v') # v快捷鍵
# 執行
action.perform()
