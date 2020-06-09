import requests
from bs4 import BeautifulSoup
# driver = webdriver.Chrome('../chromedriver.exe')
# 產生cookies
rq = requests.session()
# 設定同意參數
data = {'from':'https://www.ptt.cc/bbs/Gossiping/index.html','yes':'yes'}
# 帶參數請求
rq.post('https://www.ptt.cc/ask/over18',data=data)
# 取得，預備解析，將取網址設定變數
res = rq.get('https://www.ptt.cc/bbs/Gossiping/index.html')
# 解析網內容，並且選擇 class="r-ent" 的元素
soup = BeautifulSoup(res.text,'html.parser')
# print(soup.prettify) #美化HTML
# 解析完，設定想找的元素
items = soup.select('.r-ent',limit=5)
# 利用迴圈，篩選出解析後的HTML元素內的文字
for i in items:
    print(i.select('.title')[0].text,end='')

# a_tags = soup.find_all(['a','div'])
# a_tags = soup.find_all('a',recursive=False)
# for tag in a_tags:
#     print(tag.text)

# a_tags = soup.find(id='action-bar-container')
# print(a_tags)