import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ['Microsoft JhengHei']
    
file1 = '失業率－婚姻狀況別.csv'
file1 = '年齡組別失業率.csv'
file1 = '人力資源調查失業率.csv'
with open(file1,encoding="utf-8") as f:
    df1 = df = pd.read_csv(f).dropna() #處理掉空白列
    df = df.rename(columns={"項目別_Iterm":"年份"}) #重新命名
    df["年份"] = df["年份"].str.replace("M","/") #修改結構
    #【男女別】------------------------------------------------------
    plt.ylabel("😂",fontname="symbola",size=12,rotation=0,ha="right") #Y軸
    
    for i in df: print(i) #檢查類別

    df1 = df1[["男_Male","女_Female"]] #取需要資料
    df1.index = df["年份"] #替換index元素
    # df1 = df1.dropna() #沒有刪除會有空窗年份
    
    fig = plt.figure(dpi=800, figsize=(5,3)) #出圖設定
    # 數量龐大，抓近年數量觀察
    df1[["男_Male","女_Female"]].iloc[-10:].plot(kind="line") # !年份軸
    
    plt.title("失業率－男女別", fontsize=14) #標題
    plt.xlabel("年份",size=16) #X軸
    plt.gca().set_facecolor("#001111") #背景顏色
    fig.autofmt_xdate()
    plt.show()
    print('='*60)

    #【年齡別】------------------------------------------------------
    df["age_60-64"] = df["age_60-64"].replace("-",np.nan)#轉空值
    df["age_65_over"] = df["age_65_over"].replace("-",np.nan)
    df["age_60-64"] = df["age_60-64"].astype(float)#轉浮點數
    df["age_65_over"] = df["age_65_over"].astype(float)
    check = [i for i in  df["age_60-64"]]#檢查元素用
    print(check) #檢查元素用
    # print(df["age_60-64"].sum()) #檢查元素用OK
    df2_columns = ["age_15-19","age_20-24","age_25-29","age_30-34","age_35-39","age_40-44",
                   "age_45-49","age_50-54","age_55-59","age_60-64","age_65_over"]
    # print(df2.dtypes) #修改後，全都是float64了
    df2 = df[df2_columns]
    lst=[]
    df2_columns=[i.replace("age_","").replace("_over","以上") for i in df2_columns]
    print(df2_columns)
    df2_sum = df2.sum()
    print(df2_sum)
    # colors = ["#fff555","#ff2244","#55ff55","#55aaff"]
    
    explode = [0]*(len(df2_columns)) #爆炸圖
    explode[1]=0.2
    print(explode)
    plt.figure(figsize=(12,8)) #圓餅圖大小
    plt.pie(df2_sum,labels=df2_columns, autopct="%1.1f%%",shadow=True,
            pctdistance=0.6,explode=explode)
    plt.axis("equal")
    plt.legend(loc="lower right",fontsize=10) #小窗位置
    #【學歷別】------------------------------------------------------
    # # 圓餅圖測試
    # x = [10,20,30,40]
    # y = "一","二","三","四"
    # colors = ["#fff555","#ff2244","#55ff55","#55aaff"]
    # plt.pie(x, labels=y,explode=explode, autopct="%2.1f%%",shadow=True,
    #         pctdistance=0.6,colors=colors)
    # plt.axis("equal")
    

    
    

