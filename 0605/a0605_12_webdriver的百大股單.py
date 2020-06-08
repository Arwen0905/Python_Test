from selenium import webdriver
from time import sleep
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("https://tw.finance.yahoo.com/")
more_rank_elem = driver.find_element_by_css_selector\
    (".yui-text-left .yui-text-left table tr:nth-child(1) .stext div a")
more_rank_elem.click()
price_rank_elem = driver.find_element_by_css_selector('.yui-text-left+ .yui-text-left tr:nth-child(5) a')
price_rank_elem.click()
top_100_elem = driver.find_element_by_css_selector('p a+ a')
top_100_elem.click()
ticker_name_elem = driver.find_elements_by_css_selector('.name')
# sleep(2)
# print(ticker_name_elem.text)
ticker_name = [tn.text for tn in ticker_name_elem]
# driver.close()
print(ticker_name)
