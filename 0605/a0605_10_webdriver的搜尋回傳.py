from selenium import webdriver # 載入 webdriver模組
from selenium.webdriver.common.keys import Keys
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("http://www.python.org")
print(driver.title)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
# 清除
elem.clear()
# 搜尋 pycon
elem.send_keys("pycon")
# 將搜尋結果傳回來
elem.send_keys(Keys.RETURN)
# 如果不在page (沒有找到的話) 就回傳 "NO results found."
assert "No results found." not in driver.page_source
print(driver.page_source)
driver.close()
