import requests
from bs4 import BeautifulSoup

# url = "https://ani.gamer.com.tw/"
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
# rq = requests.get(url, headers=headers)
# print(rq.text)
    
    
url2 = "https://www.ptt.cc/bbs/Gossiping/index.html"
# rq = requests.get(url2)
rq = requests.get(url2,cookies={"over18":"1"})
rq.encoding = "utf-8"
soup = BeautifulSoup(rq.text,"lxml")
rs = soup.select(".title > a")
for i in rs:
    print(i.text)

