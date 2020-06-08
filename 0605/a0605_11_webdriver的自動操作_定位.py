from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("http://www.imdb.com/")
# search_elem = driver.find_element_by_css_selector("#navbar-query")
search_elem = driver.find_element_by_css_selector("#suggestion-search")
search_elem.send_keys("The Shape of water")
# time.sleep(3)
# search_button_elem = driver.find_element_by_css_selector("#navbar-submit-button .navbarSprite")
search_button_elem = driver.find_element_by_css_selector("#suggestion-search-button")
search_button_elem.click()
# time.sleep(3)
# first_result_elem = driver.find_element_by_css_selector("#findSubHeader+ .findSection .odd:nth-child(1) .result_text a")
first_result_elem = driver.find_element_by_css_selector("td.result_text > a:nth-child(1)")
first_result_elem.click()
time.sleep(3)
rating_elem = driver.find_element_by_css_selector("strong span")
rating =float(rating_elem.text)
# cast_elem = driver.find_elements_by_css_selector(".itemprop")
# cast_list = [cast.text for cast in cast_elem]
cast_elem = driver.find_element_by_css_selector(".cast_list").text
print(rating, cast_elem)
driver.close()
