import os #資料夾
from urllib.request import urlretrieve #存放圖片
pic_url = "https://i.imgur.com/V92HB7I.gif" # 圖片網址
os.makedirs('./pic/',exist_ok=True) # os的建立目錄，並且存放檔案開啟
urlretrieve(pic_url,f'./pic/Q.jpg') # 將什麼檔案存放到什麼位置