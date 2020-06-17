import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re

url = 'http://localhost:8080/a0606_HTML-Test.html'
# os.makedirs('./img/',exist_ok=True) #建立目錄存放檔案
html = requests.get(url).text #獲取網頁html
# print(html)
soup = BeautifulSoup(html,'html.parser')
# print(soup)
# rs = soup.select('img')
print(ord('彌'),'<<彌')
# rs = soup.findAll(src=re.compile('^./Python_main/[^.]'))
# rs = soup.findAll(src=re.compile('^./Python_main/\d'))
# rs = soup.findAll(attrs={'data-qq':'美好世界'})
# rs = soup.select('div .toggle')[-1:]

# rs = soup.find('img',src=re.compile('./Python_main/\w[庫]\w')).find_parent('h5').find_previous('h5').text
rs = soup.select('img')[1].find_parent('h5').find_previous('h5').text
print(rs)
# for i in rs:
    # print(i)

