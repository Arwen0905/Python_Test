import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from datetime import datetime
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



# urlretrieve(img_src,'./pic/%s'%time_name[1])
# name = soup.find('sapn').parent.previous_sibling.get_text()
# print(name)
# soup.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()


# for url in img_url:
    # print(url)
    # print(url['src'])
    # ul = url['src'] #獲取src屬性
    # print(ul)
    # img = 'http://www.onegreen.net/' + ul #補全圖片url
    # print(img)
    # urlretrieve(img , './img/%s' % ul.split('/')[-1]) #儲存圖片
