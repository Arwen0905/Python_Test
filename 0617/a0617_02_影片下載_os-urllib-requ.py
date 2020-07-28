from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
import re

# url_Path = 'https://www.google.com.tw/imghp?hl=zh-TW&tab=wi'
# url_q = {'q':'黑人抬棺'}
# rq = requests.get(url_Path,params=url_q)
# url = 'https://www.google.com/search?q=%E9%BB%91%E4%BA%BA%E6%8A%AC%E6%A3%BA&tbm=isch&ved=2ahUKEwjgofKnmYnqAhUDyZQKHRT4C7IQ2-cCegQIABAA&oq=%E9%BB%91%E4%BA%BA%E6%8A%AC%E6%A3%BA&gs_lcp=CgNpbWcQDFAAWABg5AhoAHAAeACAAQCIAQCSAQCYAQCqAQtnd3Mtd2l6LWltZw&sclient=img&ei=JTvqXqD7DIOS0wSU8K-QCw&bih=898&biw=1237&hl=zh-TW'
# rq = requests.get(url)
# rs = BeautifulSoup(rq.text,'html.parser')
# r = rs.findAll('img')
# r = rs.findAll('div img') XXX
# r = rs.select('div')
# print(r)

# r = rs.findAll('div',string=re.compile('[黑人]'))
                            # re.compile('./Python_main/\w[庫]\w'))
# for i in r:
    # print(i['src'])


pic_url = "http://xunleia.zuida360.com/1801/擅长捉弄人的高木同学-01.mp4"
os.makedirs('./video/',exist_ok=True) #建立目錄存放檔案
urlretrieve(pic_url,f'./video/QQ.mp4') #將什麼檔案存放到什麼位置

r = requests.get(pic_url) 
with open('./pic/zDRf0B0.mp4','wb') as f: 
   f.write(r.content)
