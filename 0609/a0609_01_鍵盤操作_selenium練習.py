from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Chrome('../chromedriver.exe')
driver.get('https://google.com.tw')

above=driver.find_element_by_link_text('Gmail')
ActionChains(driver).move_to_element(above).perform()
q = driver.find_element_by_name('q')
q.send_keys(u'東踏取蜜蜜')
sleep(1)
q.send_keys(Keys.BACK_SPACE)
sleep(1)
q.send_keys(Keys.SPACE)
sleep(1)
q.send_keys('PTT\n')
driver.find_element_by_partial_link_text('[問卦]').click()
driver.find_element_by_css_selector('.btn-big').click()
