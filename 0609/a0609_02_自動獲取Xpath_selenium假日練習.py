from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome('../chromedriver.exe')
driver.get('http://google.com.tw')
search_q = driver.find_element_by_name('q')
search_q.send_keys('Chrome線上應用程式商店\n')
sleep(1)
driver.find_element_by_partial_link_text('線上應用程式商店').click()
driver.find_element_by_css_selector('#searchbox-input').send_keys('chroPath\n')
