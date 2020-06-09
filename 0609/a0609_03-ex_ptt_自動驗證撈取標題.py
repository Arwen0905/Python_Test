from bs4 import BeautifulSoup
import requests
payload = {'from':'https://www.ptt.cc/bbs/Gossiping/index.html','yes':'yes'}
rq = requests.session()
rq.post('https://www.ptt.cc/ask/over18',data=payload)
rs = rq.get('https://www.ptt.cc/bbs/Gossiping/index.html')
# 解析
soup = BeautifulSoup(rs.text,'html.parser')
# 尋找
items = soup.select('.r-ent')
for i in items:
    print(i.select('.title')[0].text)