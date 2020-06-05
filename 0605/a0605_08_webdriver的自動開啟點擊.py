from selenium import webdriver
import time

driver_path = 'chromedriver.exe'
# 使用 webdriver模組並執行 chromedriver.exe 軟體，設定給 web變數
web = webdriver.Chrome(driver_path)
# 設定要前往的網站
web.get('http://www.cwb.gov.tw/V7/')
# 設定瀏覽器的位置(0,0)
web.set_window_position(0,0)
# 打開視窗 設定視窗大小(700,700)
web.set_window_size(1920,1080)
# 設定運行時間停滯幾秒後，進入下一步
time.sleep(1)
# (找到"衛星"按鈕後，進入該頁面)
web.find_element_by_link_text('衛星').click()
# 設定運行時間持續幾秒後關閉，進行下一步
time.sleep(1)
# (關閉)
web.close()
