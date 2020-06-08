from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get('https://www.google.com.tw/')
el = driver.find_element_by_name('q')
el.send_keys('hello world')
driver.find_element_by_css_selector('.gNO89b').click()
