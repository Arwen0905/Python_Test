from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve

url = 'https://data.gov.tw/dataset/27396'
rq = requests.get(url)
soup = BeautifulSoup(rq.text,"html.parser")
# print(soup.prettify())
re = soup.find_all("a",{"title":"下載格式為 CSV"})
count = 0
for index,i in enumerate(re):
    print(i.get("href"))
    try:
        csv_url = i.get("href")
        count+=1
        os.makedirs('./csv/',exist_ok=True) #建立目錄存放檔案
        urlretrieve(csv_url,f'./output/{count}.csv') #將什麼檔案存放到什麼位置
    except:
        print('沒有這東西!')
    # if index==1:
    #     print(i.get("href"))
    #     csv_url = i.get("href")
    #     count+=1
    #     os.makedirs('./csv/',exist_ok=True) #建立目錄存放檔案
    #     urlretrieve(csv_url,f'./output/{count}.csv') #將什麼檔案存放到什麼位置



# filename = "測試檔案名稱"
# with open(filename, 'wb') as f:
#   for chunk in r,iter_content(chunk_size=32):
#       f.write(chunk)

# dataTag = objSoup.select('.contents_box02')

# balls = dataTag[2].find_all('div', {'class': 'ball_tx ball_yellow'})

# sleep(1)
# if rq.status_code == requests.codes.ok:
#     soup = BeautifulSoup(rq.text,'html.parser')
#     # 可顯示 html的結構 BeautifulSoup的方法→ prettify()
#     # print(soup.prettify())
    
#     rs = soup.select('.kCrYT a') #若要取文字，需要疊代出來
#     # rs = soup.select('.kCrYT a') #若要取文字，需要疊代出來
#     # print(rs) #只能取元素，無法取文字
#     # rs = soup.findAll('div') #只找單一
#     # rs = soup.select('h3 > a[href^="/url"]')
#     # print(rs)
#     for index,row in enumerate(rs):
#         print('標題: '+row.text)
#         print('網址: '+row.get('href')) # 定位需指定至 a才會有 href的值
        # if 5 < index <8:
        #     print('標題: '+row.text)
        #     print('網址: '+row.get('href'))
            
    #     try:
    #         print('網址: '+row.get('href'))
    #     except:
    #         print('沒有這東西!')
