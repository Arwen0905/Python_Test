import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime
import re
time = datetime.now()
url = 'https://www.monster-strike.com.tw/news/20200212_ky.html'
os.makedirs('./img/',exist_ok=True) #建立目錄存放檔案
html = requests.get(url).text #獲取網頁html

soup = BeautifulSoup(html,'html.parser')
# print(soup.prettify())

img_url = soup.select('img') #獲取所有的img標籤,我在這裡只是演示下載，所有不做進一步的篩選
# print(img_url)
print(len(img_url))
ul = img_url[11]['src']

img_src = 'https://www.monster-strike.com.tw' + ul
print(img_src)
print(str(time)[:19],'時間')
time_name = str(time)[:19].split(' ')
time_head = time_name[0].split('-') #!需要從索引值抓出來切割才行
time_tail = time_name[1].split(':')
print(time_head) #頭
print(time_tail) #尾巴
qq = ''.join(time_head)
qq += ''.join(time_tail)
print(qq)
# 運用日期+時間不重複的特性，並取得網址末四碼字元的副檔名做存入命名
urlretrieve(img_src,'./pic/%s'%qq + img_src[-4:])

# name = soup.find('sapn')
# print(name)

# for url in img_url:
    # print(url)
    # print(url['src'])
    # ul = url['src'] #獲取src屬性
    # print(ul)
    # img = 'http://www.onegreen.net/' + ul #補全圖片url
    # print(img)
    # urlretrieve(img , './img/%s' % ul.split('/')[-1]) #儲存圖片
