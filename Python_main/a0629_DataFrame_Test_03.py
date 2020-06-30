import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ['Microsoft JhengHei']

file1 = "./data/離婚統計_臺中市各區100年-105年結離婚對數.json"
with open(file1,encoding='utf-8-sig') as f:
    data = json.load(f)
    data = pd.DataFrame(data)
    col_name = data.columns
    print(col_name)
    print(data)
    
file2 = './data/離婚統計_離婚登記對數-按區域別分.csv'
with open(file2,encoding="utf-8") as f:
    f = pd.read_csv(f) # Index(['離婚對數', '離婚對數.1', '粗離婚率']
    df1 = pd.DataFrame([])
    # 處理日期
    dateTime2 =f["離婚對數"].str.split("/")

    # print('↓='*50)
    # for i in dateTime2:
    #     if i[1] == "區域別總計":
    #         print(i[1])
    # print('^='*50)
    # print(dateTime2.head())

    lst_city=[i[1] for i in dateTime2]
    lst_datatime2=[i[0] for i in dateTime2]
    # 處理日期完畢，重設年份、日期
    
    df1["區域"],df1["年份"],df1["離婚對數"],df1["離婚率"] = lst_city,lst_datatime2,f["離婚對數.1"],f["粗離婚率"]
    
    
    # df1_year = df1["年份"].str.strip("年")
    # df1.index = df1_year
    
    print(df1["離婚率"])
    print('='*50)
    # 清除不乾淨元素
    print("離婚率的 髒東西:",df1["離婚率"][91])
    print("離婚對數的 髒東西:",df1["離婚對數"][91])
    # df1 = df1.drop(91,axis=0) #怒刪91
    df1["離婚對數"] = df1["離婚對數"].str.replace(",","")
    df1["離婚對數"] = df1["離婚對數"].str.replace("-","")
    df1["離婚率"] = df1["離婚率"].str.replace("-","")
    df1["離婚對數"] = pd.to_numeric(df1["離婚對數"])
    df1["離婚率"] = pd.to_numeric(df1["離婚率"])
    
    print(df1.head(10))

# 圖形化設定
fig = plt.figure(dpi=128, figsize=(12,6)) #繪圖畫面設定
df1[["離婚對數"]].plot(kind="line",color="#ff2244")
plt.xlabel("日期",size=16,fontname="SimSun") # 不會影響其它字型設定
plt.ylabel("😂",fontname="symbola",size=36,rotation=0,ha="right") # 不會影響其它字型設定
# plt.fill_between(f["粗離婚率"], facecolor="pink", alpha=0.5) #線條間距填色
plt.gca().set_facecolor("black") #黑色背景
fig.autofmt_xdate() #執行
    