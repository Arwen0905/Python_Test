import csv    #載入 csv 模組，處理csv檔案格式
import requests	#載入 requests 模組，存取網站取得內容

#載入 BeautifulSoup 模組，解析網頁
#BeautifulSoup讀取 HTML 原始碼，自動進行解析並產生一個 BeautifulSoup 物件，
#此物件中包含了整個 HTML 文件的結構
from bs4 import BeautifulSoup
from time import localtime, strftime, strptime, mktime    #處理時間系列
from datetime import datetime    #處理日期時間
from os.path import exists    #處理檔案儲存路徑、查看特定的路徑是否存在，不分檔案或目錄

#取得網站內容
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")

#將取得的網站內容分析並建立物件bsObj
bsObj = BeautifulSoup(html.content, "lxml")

#靜態網頁中的資訊結構為table→tbody→tr，很多tr，故使用findall找出所有tr
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"):
    #findall找出所有的td儲存到cell
    cell = single_tr.findAll("td")

    #在cell[0]下找到class屬性是visible-phone的欄位
    #以contents回傳欄位內容給currency_name(匯率名稱)
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0]

    #刪除表格中不必要的資料如\r , \n , 空白鍵
    currency_name = currency_name.replace("\r","")
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")

    #以contents回傳欄位內容給currency_rate(匯率)
    currency_rate = cell[2].contents[0]
    print(currency_name, currency_rate)

    #建立csv檔案
    file_name = r"CSV/bkt_rate" + currency_name + ".csv"

    #取得目前時間
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

    #寫入csv檔，如果檔案不存在，則抓取網頁上的時間及匯率寫入，若檔案存在，即使用原資料
    #如果檔案不存在，加入一行資料，以串列中的串列處理每天的匯率資料。
    #每一個串列代表擷取得每一筆匯率資料。
    if not exists(file_name):
        data = [['時間', '匯率'], [now_time, currency_rate]]
    else:
        data = [[now_time, currency_rate]]
    f = open(file_name, "a")    #開啟csv檔
    w = csv.writer(f)    #寫入csv檔
    w.writerows(data)    #寫入data物件
    f.close()    #關閉csv檔案