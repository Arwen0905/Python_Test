import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://hk.appledaily.com/realtime/index"
re = requests.get(url)
re.encoding = "utf-8"
soup = BeautifulSoup(re.text, "html.parser")

rs = soup.select('div.LHSContent_inner.NoTab > div.item > div.text')

# print(rs)
for v,i in enumerate(rs):
    if v <= 10:
        print(i)
        
    
