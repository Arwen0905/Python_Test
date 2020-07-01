import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ['Microsoft JhengHei']
    
file1 = '失業率－婚姻狀況別.csv'
file1 = '年齡組別失業率.csv'
file1 = '人力資源調查失業率.csv'
with open(file1,encoding="utf-8") as f:
    df1 = df = pd.read_csv(f)
    df = df.rename(columns={"項目別_Iterm":"年份"}) #重新命名
    df["年份"] = df["年份"].str.replace("M","/") #修改結構
    
    for i in df: print(i) #檢查類別

    df1 = df1[["男_Male","女_Female"]] #取需要資料
    df1.index = df["年份"] #替換index元素
    df = df.dropna() #沒有刪除會有空窗年份
    print(df)
    
    fig = plt.figure(dpi=1920, figsize=(5,3)) #出圖設定
    df1[["男_Male","女_Female"]].iloc[-100:].plot(kind="line") # !年份軸
    
    plt.title("失業率－男女別", fontsize=14) #標題
    plt.xlabel("年份",size=16) #X軸
    plt.ylabel("😂",fontname="symbola",size=12,rotation=0,ha="right") #Y軸
    plt.gca().set_facecolor("#001111") #背景顏色
    fig.autofmt_xdate()
    plt.show()
    print('='*60)

    df["age_60-64"] = df["age_60-64"].replace("-","0.0")#轉為空值
    df = df.dropna()
    df["age_60-64"] = df["age_60-64"].astype(float)
    check = [i for i in  df["age_60-64"]]
    for i in df["age_60-64"]:
        print(i)
    print(check)
    print(df["age_60-64"].sum()) #檢查元素
    
    # print(df["age_60-64"].iloc[10])
    df2_columns = ["age_15-19","age_20-24","age_25-29","age_30-34","age_35-39","age_40-44",
                   "age_45-49","age_50-54","age_55-59","age_60-64","age_65_over"]
    df2 = df[df2_columns]
    print(df2.dtypes)
    

