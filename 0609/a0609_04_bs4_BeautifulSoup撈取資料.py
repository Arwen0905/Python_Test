from bs4 import BeautifulSoup
import requests
# 產生cookies
rq = requests.session()
data = {'from':'http://localhost:8080/a0606_HTML-Test.html','yes':'yes'}
# 請求才需要代入參數
rq.post('http://localhost:8080/a0606_HTML-Test.html',data=data)
rs = rq.get('http://localhost:8080/a0606_HTML-Test.html')
# data = {'from':'https://www.ptt.cc/bbs/Gossiping/index.html','yes':'yes'}
# # 請求才需要代入參數
# rq.post('https://www.ptt.cc/ask/over18',data=data)
# rs = rq.get('https://www.ptt.cc/bbs/Gossiping/index.html')

soup = BeautifulSoup(rs.text,'html.parser')
# items = soup.find(attrs={"data-back":"round"}) # data-屬性
# items = soup.find_all(class_="Level_2") # class_= soup專用常數
# items = soup.find_all("div",class_="Level_2") #只找div標籤下的class
# items = soup.find("a",text="彰化") # 文字定位
items = soup.find("a",text="新北") # 文字定位
print(items.text)
print("===================================================")
# 往下一個找
# link2 = items.find_next_siblings("div")
# print(link2)
link3 = items.find_previous_siblings("div")
print(link3)
# link4 = items.find_parent("div")
# print(link4)
# items2 = items.find_next_siblings("div")
# print(items2.text)
# for i in items:
#     print(i.text)

