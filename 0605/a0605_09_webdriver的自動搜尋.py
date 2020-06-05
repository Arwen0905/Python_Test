from selenium import webdriver
url = 'https://tw.yahoo.com/'
driver_path = 'chromedriver.exe'
browser = webdriver.Chrome(driver_path)
browser.get(url)

element = browser.find_element_by_id('UHSearchBox')
# 設定可直接輸入關鍵字
element.send_keys('Hello World')
# 設定 點擊按鈕送出
submit = browser.find_element_by_id('UHSearchWeb').click()
