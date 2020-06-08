from time import sleep
from selenium import webdriver
# 於chrome執行，軟體設定
driver = webdriver.Chrome('chromedriver.exe')
# ===================================
# 清除元素的內容
# 模擬按鍵輸入
# 點擊元素
# 提交表單
# =================================================================================================
#! (1):基本使用，開啟網站，自動搜尋寫入
# driver.get('https://www.google.com.tw/') #開啟網頁
# \n 等於按下ENTER
# driver.find_element_by_name('q').send_keys('game\n')
# driver.back() #回上一頁
# driver.find_element_by_partial_link_text('ail').click #接受不完整字串
# driver.quit()

# =================================================================================================
#! (2):搜尋多元素，並篩選條件
# driver.get('https://www.baidu.com/') #開啟網頁
# driver.maximize_window() #最大化
# sleep(3) #睡一會

# elments = driver.find_elements_by_tag_name('a')
# for index,elment in enumerate(elments):
#     # print(index,elment.text)
#     if index == 5: # 配對到第5項目 -> 地圖
#         elment.click()
#         print(elment.text)

# =================================================================================================
#! (3):nth-child & nth-of-type
driver.get('file:///C:/Users/user/Desktop/Python_Test/0603/a0606_HTML-Test.html')
#! 空一格就是之下，定位概念:於某標籤之下 :第n個元素 ， > 內層的元素
el = driver.find_element_by_css_selector("body a:nth-child(2)")
#! 黏住，定位概念:第n個黏住元素               #nth-child 不限類型，存在的標籤他都判斷 (不挑食不好掌握)                                
# el = driver.find_element_by_css_selector("body div.第二層:nth-of-type(3)  a.toggle:nth-child(4)")
                                            #nth-of-type 專一類型，只判斷同類標籤 (專一較好掌握)
sleep(2)
print(el.text)
# =================================================================================================

# driver.find_element_by_name('q').send_keys('大家好')
# driver.save_screenshot(r'C:\Users\user\Desktop\Python_Test\0605\截圖.png')
# el = driver.find_elements_by_xpath("//h3[contains(text(),'WHO')]").text
# print(el.text) #給讚
# print(driver.current_url)#獲取當前網址
# driver.back() #回上一頁
# driver.forward() #回下一頁

# pageSource = driver.page_source #獲取網站內容
# print(pageSource)
# driver.refresh() #重新整理

# select=Select(driver.find_element_by_css_selector("[id='odd']"))
# select.select_by_index(2)         #使用下標定位
# select.select_by_visible_text("使用文字定位")
# select.select_by_value("1")  #使用value值定位
driver.quit()