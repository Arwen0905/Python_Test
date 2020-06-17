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

img_url = soup.select('img') #所有img標籤
print(len(img_url),'<< 檢查長度') #檢查長度
ul = img_url[11]['src'] #取得其中一個img的 src
img_src = 'https://www.monster-strike.com.tw' + ul #組裝img的完整位置
print(img_src,'\n') #完整位置
print(time,'<< 時間')
time_date = time.date()
time_time = time.time()
print(time_time)
time_time = str(time_time).split('.')[0].split(':')
print(time_time)


# print(time_name,type(time_name))
# time_name = time_name[0].split('.') #!需要從索引值抓出來切割才行
# print(time_name)
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
