import csv #讀取csv模組
from datetime import datetime #設定時間模組
from matplotlib import pyplot as plt #圖形化模組
filename = 'death_valley_2014.csv' #指定抓取的文件
with open(filename) as f: #讀入資料
    reader = csv.reader(f) #讀取文件後，設定變數
    # 讀取 列標題
    header_row = next(reader) #讀取資料下一頁
    dates, highs, lows =[],[],[] #設定三個串列
    for row in reader: #迴圈挖取 讀入的資料
        try:                      # 將 csv檔的字串轉成時間格式
            current_date = datetime.strptime(row[0], "%Y-%m-%d") #設定時間 (年、月、日)
            high = (int(row[1])-32)*5/9 #行資料
            low = (int(row[3])-32)*5/9 #列資料
        except ValueError: #捕捉錯誤訊息
            print(current_date, "missing data")
        else: #如果沒有出錯，將以每筆資料設定到該串列
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 設定繪圖區域的大小(寬,高)
fig = plt.figure(dpi=128, figsize=(5,3)) #圖畫尺寸 設定
plt.plot(dates, highs, c="red", alpha=0.5) #行的線條顏色 設定
plt.plot(dates, lows, c="blue", alpha=0.5) #列的線條顏色 設定
#! fill_between 繪圖填充的功能解釋:
#! plt.fill 填充區域繪圖區的顏色
plt.fill_between(dates, highs, facecolor="blue", alpha=0.2) #線條內部面顏色 設定

title = "Daily high and low temperatures - 2014\nDeath valley, CA" #標題文字
plt.title(title, fontsize=20) #標題字型大小 設定
plt.xlabel("", fontsize=16) #列下方文字 設定
fig.autofmt_xdate() #執行
plt.ylabel("Temperature (C)", fontsize=16) #行標題與字型大小 設定
plt.tick_params(axis="both", which="major", labelsize=16) #下方間距設定
plt.show() #呈現畫面
