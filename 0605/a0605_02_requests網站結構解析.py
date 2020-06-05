import requests #! requests網頁擷取的基礎
#取得網址列
url = 'https://tw.yahoo.com/'
# url = 'https://www.google.com.tw/'
# 利用 requests模組的方法get，去請求網頁的內容
html = requests.get(url)
# 中文解碼
html.encoding="utf8"
# 取得回應狀態碼: request.codes.ok == 200
if html.status_code == requests.codes.ok:
    print(html.text)
# 取得回應狀態碼: html.status_cod == 200
print(html.status_code,'<< html.status_cod')     #狀態碼200
print(requests.codes.ok,'<< requests.codes.ok:') #狀態碼200