#設定Python程式中新舊版本對unicode字串與輸出入的相容性
from __future__ import unicode_literals,print_function
import urllib #存取網頁
from bs4 import BeautifulSoup #網頁解析器
import urllib.request #存取網頁
request_url = 'http://invoice.etax.nat.gov.tw/' #取得網址，財政部官網
#! 以urllib.request.urlopen開啟網頁物件並以read()讀取網頁內容
#透過模組 urllib的方法 request 讀取網址，讀入後設定給 htmlContent變數
htmlContent = urllib.request.urlopen(request_url).read()
#! 將取得的網站內容分析並建立物件soup，以html.parser方法解析(解析HTML、XHTML)
#透過模組 bs4的方法 beautiful美麗Soup湯，解析網址內容
soup = BeautifulSoup(htmlContent,"html.parser")
#! 搜尋所有網頁中標籤為span，且class屬性為t18Red者設定給results
#再用soup.方法，進階尋找目標標籤("span",尋找類的值)，設定給 soup變數
results = soup.find_all("span",class_="t18Red")
#設定欲尋找的關鍵字，設為串列
subTitle = ['特別獎','特獎','頭獎','增開六獎'] #! 設定獎項串列
#搜尋所有網頁中標籤為h2，且id屬性為tabTitle者設定給months
months = soup.find_all('h2', {'id':'tabTitle'})
#最新一期，使用months物件的find_next_sibling方法找尋標籤為'h2'下的內容
month_newest = months[0].find_next_sibling('h2').text
# 上一期
month_previous = months[1].find_next_sibling('h2').text
print("最新一期統一發票開獎號碼 ({0}):".format(month_newest))
    #enumerate：列舉資料中的每一個項目
for index, item in enumerate(results[:4]):
    print('>> {0} : {1}'.format(subTitle[index], item.text))
for index2, item2 in enumerate(results[4:8]):
    print('>> {0} : {1}'.format(subTitle[index2], item2.text))
