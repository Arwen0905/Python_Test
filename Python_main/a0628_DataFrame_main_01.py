import numpy as np
import pandas as pd
import json

file1 = "./data/foodtracer_nightmarket_market.json"
file2 = "./data臺北市10701_10904搶奪點位資訊.csv"
with open(file1,encoding='utf-8-sig') as f:
    data = json.load(f)
    data = pd.DataFrame(data)
    col_name = data.columns
    print(col_name) # ['夜市簡介', '交通資訊', '夜市名稱', '營業時間', '所在位置']
    
    # lst=[]
    # for i in data:
    #     lst.append(i["夜市名稱"]+":")
    # prilist nt(lst)
    # data = pd.DataFrame(data,columns=col_name,index=lst)
    # print(data[["所在位置","營業時間"]].head())
    # print(data.shape)
    # print(data.index)
    # print(data.dtypes)
    # print(data.columns)


# import urllib.request as request
# src = "https://www.ntu.edu.tw/"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")
#     print(data)
'''
# 備註1.中文設定，兩種方式，採用不汙染全域性字型設定
# 【rcParams】、
'''
import matplotlib.pyplot as plot
# 【字體設定方式1:rcParams】
plot.rcParams["font.family"] = ['Microsoft JhengHei']
plot.rcParams["font.sans-serif"] = ['SimSei'] # SimSei:此黑體必須在無襯線底下才會有
# plot.rcParams["font.sans-serif"] = ['Arial'] 
# !!查找現有的字型名稱
# =====================================================================
# 【字體設定方式2:rc】可詳細設定，一次設定，多次使用，會影響全域性字型
# font = {"family":"Microsoft JhengHei","weight":"bold","size":"14"}
# plot.rc('font',**font)
# plot.rc('axes',unicode_minus=False)
# =====================================================================
# 【字體設定方式3:fontProperties】
# plot.xlabel("2020日期",fontProperties="SimSun") # 不會影響其它字型設定
# 用時才設定，不會汙染全域性字型設定，靈活
# !!查找字型路徑
from matplotlib.font_manager import findfont,FontProperties
findfont(FontProperties(family=FontProperties().get_family()))
# C:\ProgramData\Anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf

print("=== 臺灣銀行黃金牌位分析 "+'='*30)
df = pd.read_html('https://rate.bot.com.tw/gold/chart/year/TWD') #pandas讀取html
df1 = df[0][["日期","本行買入價格"]] #只取需要的列表元素
df2 = df[0][["日期","本行賣出價格"]] #取第二筆賣出資料
df1.index = pd.to_datetime(df1["日期"],format="%Y/%m/%d") #將日期格式化並設為index索引
df1.sort_index(inplace=True) #將索引(日期)反排序
df2.index = pd.to_datetime(df2["日期"],format="%Y/%m/%d") #將日期格式化並設為index索引
df2.sort_index(inplace=True) #將索引(日期)反排序


# pandas的to_datetime 可格式化日期，轉成可運算的格式
# print(df.index[0],'<< 格式化')
# print(type(df.index[0]),'<< 類型')
'''
df.index = df["日期"] #一般的日期，會以字串形式表示
# 備註2.需將[日期]格式化，再轉圖表顯示
print(df.index[0],'<< 一般') #2020/06/24 << 一般日期顯示
print(type(df.index[0]),'<< 類型') #<class 'str'> << 一般字串
'''
print(df1.head())
print('='*30)
print(df2.head())
# 圖形化設定
fig = plot.figure(dpi=128, figsize=(8,6)) #繪圖畫面設定
df2["本行賣出價格"].plot(kind="line",color="g") # plot圖形化
df1["本行買入價格"].plot(kind="line",color="r") # plot圖形化
plot.xlabel("日期",size=16) # 不會影響其它字型設定
plot.ylabel("😂",fontname="symbola",size=36,rotation=45) # 不會影響其它字型設定
# plot.fill_between(df, df2, facecolor="blue", alpha=0.5) #線條間距填色
plot.gca().set_facecolor("black") #黑色背景
fig.autofmt_xdate() #執行
print(plot.rcParams["font.sans-serif"],"目前使用字型")