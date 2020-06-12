from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("http://www.imdb.com/")
search_elem = driver.find_element_by_css_selector("#suggestion-search")
search_elem.send_keys("The Shape of water")
time.sleep(3)
search_button_elem = driver.find_element_by_css_selector("#suggestion-search-button")
search_button_elem.click()
time.sleep(3)
first_result_elem = driver.find_element_by_css_selector(".findResult.odd .result_text a")
first_result_elem.click()
time.sleep(3)
rating_elem = driver.find_element_by_css_selector("strong span")
rating =float(rating_elem.text)
cast_elem = driver.find_element_by_css_selector("#titleCast")
cast_list = [cast.text for cast in cast_elem]
driver.close()
print(rating, cast_elem.text)
