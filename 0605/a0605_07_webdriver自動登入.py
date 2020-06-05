from selenium import webdriver
driver_path = 'chromedriver.exe'
url = "https://www.facebook.com/"
email="letswin3d"
password="letswin"
# 執行[chromedriver.exe]軟體並設定給 driver變數
driver = webdriver.Chrome(driver_path)

# 最大化視窗
driver.maximize_window()
# 透過get取得網址
driver.get(url)
# 找到id email的輸入框，送出帳號
driver.find_element_by_id("email").send_keys(email)
# 找到id pass的輸入框，送出密碼
driver.find_element_by_id("pass").send_keys(password)
# 找到送出鈕，並執行 click() 等同於 滑鼠點一下，完成後執行
driver.find_element_by_id("loginbutton").click()






















