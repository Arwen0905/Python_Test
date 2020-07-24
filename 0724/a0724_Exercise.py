import requests
from bs4 import BeautifulSoup
url = "https://hk.appledaily.com/realtime/index"
re = requests.get(url)
re.encoding = "utf-8"
soup = BeautifulSoup(re.text, "html.parser")
# rs = soup.select('div.LHSContent_inner.NoTab > div.item > div.text > a')
rs = soup.select('div.LHSContent_inner.NoTab > div.item.Top3 > div.text')

for v,i in enumerate(rs):
    if v < 3:
        print(i.text)
    
# for v,i in enumerate(rs):
#     if v < 10:
#         print(f"第{v+1}則新聞:\n{i.text.lstrip()}\n")


    