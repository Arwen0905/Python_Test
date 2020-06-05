html='''
<html><head><title class="hello">網頁標題</title></head>
<p class="header"><h2>文件標題</h2></p>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
        <div class="hi">明天放假</div>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img class="one" src="http://examp.com/three.jpg">Third
        <img class="two" src="https://www.google.com.tw/">Third
        <img class="two" src="https://tw.yahoo.com/">二號
        <img class="two" src="QQQ">三號
    </a>
</div>
'''
from bs4 import BeautifulSoup
#! sp就是網頁程式碼的內容，經使用BeautifulSoup的方法解析後取得
sp = BeautifulSoup(html,'html.parser')
# 取得title標籤
# print(sp.title)
# print(sp.find('h2'))
# print(sp.find_all('a'))
# find_all可以找到全部的
# print(sp.find_all('a',{"class": "red"}))

# 可以找到 a標籤有此網址的元素
data1 = sp.find("a",{"href":"http://example.com/one"})
# print(data1.text)

# 找到#id為 link1的，傳回來的是串列資料型態
data2 = sp.select("#link1")
# print(data2[0].text)
# print(type(data2[0].text)) #檢查類型
# print(data2[0].get)
# print(data2[0]["href"])
# print(sp.find_all(["title","h2"]))

#! 讀取sp網頁內容裡面的 div的 img的 第幾筆的 "src屬性"
# print(sp.select("div img")[1]["src"])
# print(sp.select("img")[0]["src"])
print(sp.find_all("img",{"class":"two"})[0:3])
print('=====================================')
print(sp.select("img",{"class":"two"})[0:3])
# for row in sp:
#     print(row[0])
# print(sp.find_all("div",{"class":"hi"}))
# print(sp.select("div",{"class":"red"}))
# print(sp.select("a",{"class":"blue"}))
# print(sp.find_all("div",{"class":"item1"}))

