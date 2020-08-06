from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests
from bs4 import BeautifulSoup
import random

driver = webdriver.Chrome('../chromedriver')
driver.implicitly_wait(5)
driver.get('https://hahow.in/courses')

print(driver.title)
soup = BeautifulSoup(driver.page_source,'lxml')
fp = open('hahow.html','w',encoding="utf8")
fp.write(soup.prettify())
print("寫入檔案hahow.html")
fp.close()
driver.quit()



# url = "https://hahow.in/courses"
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# rq = requests.get(url, headers=headers)
# # print(rq.text)
# soup = BeautifulSoup(rq.text,"html.parser")
# rs = soup.select(".title.marg-t-20.marg-b-10")
# print(rs)