from selenium import webdriver
driver_path = 'chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.get("https://tw.finance.yahoo.com/")
more_rank_elem = driver.find_element_by_css_selector\
    (".yui-text-left .yui-text-left table tr:")