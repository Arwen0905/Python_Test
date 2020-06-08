import requests
from bs4 import BeautifulSoup
payload = {'from':'https://www.ptt.cc/bbs/Gossiping/index.html',"yes":"yes"}
#! 將程式帶入瀏覽器資訊，盡可能偽裝成真實使用者，可避免大部分反爬蟲機制
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac os x 10_12_3)'\
           'Applewebkit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
rs = requests.Session()
# 用post的方式請求，代替網址，模擬客戶端
# 經過這行指令，伺服器端會產生相對應的cookies
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')   
for item in items:
    print(item.select('.date')[0].text,item.select('.author')[0].text, \
          item.select('.title')[0].text)
