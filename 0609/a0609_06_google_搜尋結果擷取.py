from bs4 import BeautifulSoup
import requests
from time import sleep

google_url = 'https://google.com'
my_params = {"q":"東踏取蜜"}
rq = requests.get('https://www.google.com.tw/search', params=my_params)
sleep(1)
if rq.status_code == requests.codes.ok:
    soup = BeautifulSoup(rq.text,'html.parser')
    # 可顯示 html的結構 BeautifulSoup的方法→ prettify()
    # print(soup.prettify())
    
    rs = soup.select('.kCrYT a') #若要取文字，需要疊代出來
    # rs = soup.select('.kCrYT a') #若要取文字，需要疊代出來
    # print(rs) #只能取元素，無法取文字
    # rs = soup.findAll('div') #只找單一
    # rs = soup.select('h3 > a[href^="/url"]')
    # print(rs)
    for index,row in enumerate(rs):
        print('標題: '+row.text)
        print('網址: '+row.get('href')) # 定位需指定至 a才會有 href的值
        # if 5 < index <8:
        #     print('標題: '+row.text)
        #     print('網址: '+row.get('href'))
            
    #     try:
    #         print('網址: '+row.get('href'))
    #     except:
    #         print('沒有這東西!')
