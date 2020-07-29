import requests
import pandas as pd
from bs4 import BeautifulSoup as soup

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20190101&stockNo=2633&_=1595925201119"
# url = "https://rate.bot.com.tw/xrt/all/2020-01-06"
# def convertDate(date):
#     str1 = str(date)
#     yearst = str1[:3] #取出民國年
#     ryear = str(int(yearst)+1911) #轉為西元年
#     findata = ryear + str1[4:6] + str1[7:9]
#     return findata

# ans = lambda x:int(x)+1911
# print(ans("109"))

re = requests.get(url)
re.encoding = "utf-8"
rs = soup(re.text,"html.parser")
# rq = rs.select()
print(rs)
