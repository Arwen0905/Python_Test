from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
import re
import pandas as pd
import numpy as np

url = 'https://data.gov.tw/dataset/27396'
rq = requests.get(url)
soup = BeautifulSoup(rq.text,"html.parser")
# print(soup.prettify())
rs = soup.find_all("a",{"title":"下載格式為 CSV"})

name_q= soup.find_all("div",class_=("field-items"))

lst_file =[]
for i in name_q:
    s = i.text
    res = re.findall('\d{3}\w{4}["年結婚對數"]',s)
    if res == [s]:
        lst_file.append(res[0])
        print(res,"檔名捕捉!")
        
print("\n獲得的名稱串列:\n",lst_file)

# for index,i in enumerate(rs):
#     print(i.get("href"),"儲存中..")
#     try:
#         csv_url = i.get("href")
#         count = index
#         os.makedirs('./csv/',exist_ok=True) #建立目錄存放檔案
#         urlretrieve(csv_url,f'./output/{lst_file[index]}.csv') #將什麼檔案存放到什麼位置
#     except:
#         print('無法下載，跳過!')

lst_f = ["102年結婚對數","103年結婚對數","104年結婚對數",
         "105年結婚對數","106年結婚對數","108年結婚對數",
         "107年結婚對數"]
print("第一年份的檔案"+"="*50)
print(lst_f)
with open(f'.\output\{lst_f[1]}.csv',encoding="utf-8") as f:
    df1 = pd.DataFrame(f)
    print(df1)
print("第二年份的檔案"+"="*50)
with open(f'.\output\{lst_f[3]}.csv',encoding="utf-8") as f:
    df2 = pd.DataFrame(f)
    print(df2)
print("合併作業"+"="*50)
father_path = os.getcwd()

path_csv = father_path+r'.\output\test_write.csv'


# 寫入
df2.to_csv(path_csv)