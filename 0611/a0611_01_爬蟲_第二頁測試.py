import requests
from bs4 import BeautifulSoup
from lxml import etree
# rq = requests.get("https://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001")
# print(rq.content.decode()) # 解析中文字
# soup = BeautifulSoup(rq.text,'html.parser')
# rs = soup.select('.type02_bd-a')
# for i in rs:
#     print('書名: '+i.select('a')[0].text)
#     print('價錢: '+i.select('strong')[0].text)

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/67.0.3396.99 Safari/537.36"}
title,link,price=[],[],[]
def search(url):
    rq = requests.get(url,headers=headers)
    html = BeautifulSoup(rq.text,'html.parser')
    title.extend(html.select('title'))
    print(title)
    # res = requests.get("http://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001",headers=headers)
    # content = res.content.decode()
    # print(content)
    # for i in result:
    #     print(i)

search("https://search.books.com.tw/search/query?fclick=0&key=python&cat=all")