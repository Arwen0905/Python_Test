# 載入模組
import requests
import re

url = 'http://tqc.codejudger.com:3000/target/5201.html'

# 使用 GET 請求
htmlfile = requests.get(url)
print(htmlfile.status_code)
# 驗證HTTP Status Code
if htmlfile.status_code == 200:
    # 欲搜尋的字串
    str1 = input("請輸入欲搜尋的字串 : ")
    search = re.findall(str1, htmlfile.text)
    if str1 in htmlfile.text:
        print(str1, "搜尋成功")
        print(str1, "出現 %d 次" % len(search))
    else:
        print(search, "搜尋失敗")
        print(search, "出現 0 次")
else:
    print("網頁下載失敗")

    
