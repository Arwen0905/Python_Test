import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
 
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.google.com.tw/")
 
# 取得圖片位置
elem_pic = driver.find_element_by_xpath("//img[@id='hplogo']")
# 取得圖片網址，輸出
print(elem_pic.get_attribute("src"))
# 滑鼠移動到圖片上
action = ActionChains(driver).move_to_element(elem_pic)
# 執行動作! 右鍵儲存
action.context_click(elem_pic)
#! 語法重點: 當右鍵點擊後，彈出視窗，向下移動至右鍵菜單第一個選項
action.send_keys(Keys.ARROW_DOWN)
# 睡一會
print('睡一會')
time.sleep(1)
# 另存為
action.send_keys('v') # v快捷鍵
# 執行
action.perform()
