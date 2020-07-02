import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ['Microsoft JhengHei']

file1 = '失業率－婚姻狀況別.csv'
file1 = '年齡組別失業率.csv'
file1 = '人力資源調查失業率.csv'
with open(file1,encoding="utf-8") as f:
    df1 = df = pd.read_csv(f).dropna() #刪除空白列，使用index序列可能會出包
    # df1 = df = pd.read_csv(f) 
    df = df.rename(columns={"項目別_Iterm":"年份"}) #重新命名
    df["年份"] = df["年份"].str.replace("M","/") #修改結構
    # for i in df: print(i) #檢查類別

    # df = df.fillna(0) #若空則以0計算
    # df = df.fillna({'總計_Total':777}) #針對某位置處理，若空則替換
    # print(df["總計_Total"][546])
    
    # 小程式:計算每列全年齡加總，並取得平均值
    df1_average = []
    df_col_tem = [i for i in df]
    for i in range(len(df["年份"])):
        ans=0
        for index,col in enumerate(df_col_tem):
            if 3< index <15 and i!=546: #總是從第三筆開始
                print(df[col],'<<<<<<<<<<<<')
                # print(df[col][i]) #設計過程檢視用
                if df[col][i] == "-": #避開不正確值
                    continue
                ans+=float(df[col][i]) #由第一維迴圈取值；第二維換圈的反巢狀取值
        df1_average.append(ans/(len(df_col_tem)-2))
        
    # 【全年齡平均】組裝pd
    df1_average = pd.DataFrame(df1_average)
    df1_average = df1_average.rename(columns={0:"總平均值"}) #欄位名稱命名
    df1_average.index = df["年份"]
    print(df1_average)

    # #【男女別】------------------------------------------------------
    # df1 = df1[["男_Male","女_Female"]] #取需要資料
    # df1.index = df["年份"] #替換index元素
    # # df1 = df1.dropna() #沒有刪除會有空窗年份
    
    # # 走勢圖設定
    # plt.figure(figsize=(16,10)) #走勢圖尺寸
    # # 比數多，取數量觀察
    # df1[["男_Male","女_Female"]].iloc[-10:].plot(kind="line") #走勢圖設定
    # plt.ylabel("😂",fontname="symbola",size=23,rotation=0,ha="right") #Y軸
    # plt.title("失業率 - 男女性別",y=1.01,size=18) #標題
    # plt.legend(["男生","女生"],loc="up left",fontsize=14) #小窗位置
    # plt.xlabel("日期",size=16) #X軸
    # plt.grid(True,color="#ff2244",linewidth=0.5)
    # plt.gca().set_facecolor("#001111") #背景顏色
    
    # # ===================================================================================
    # # plt.savefig(r'C:\Users\user\Desktop\Python_Test\Python_main\output\失業率-男女別走勢.png',
    # #         bbox_inches="tight",transparent=True,dpi=300) #本組提供大圖


    # print("年齡別 圓餅圖"+'='*60)
    # #【年齡別】------------------------------------------------------
    # df["age_60-64"] = df["age_60-64"].replace("-",np.nan)#轉空值
    # df["age_65_over"] = df["age_65_over"].replace("-",np.nan)
    # df["age_60-64"] = df["age_60-64"].astype(float)#轉浮點數
    # df["age_65_over"] = df["age_65_over"].astype(float)
    # # check = [i for i in  df["age_60-64"]] #檢查元素用
    # # print(check) #檢查元素用
    # # print(df["age_60-64"].sum()) #檢查元素用OK
    
    # df2_columns = ["age_15-19","age_20-24","age_25-29","age_30-34","age_35-39","age_40-44",
    #                 "age_45-49","age_50-54","age_55-59","age_60-64","age_65_over"]
    
    # df2 = df[df2_columns] #將指定欄位名稱賦予給df2
    # print(df2.dtypes) #檢查類型:float64 轉換完成
    
    # df2_columns=[i.replace("age_","")+"歲" for i in df2_columns] #處理字串
    # df2_columns[-1] = df2_columns[-1].replace("_over歲","歲以上") #處理字串
    # # print(df2_columns) #欄位名稱
    
    # df2_sum = df2.sum() #年齡層的人數總和
    # # print(df2_sum) #總和
    
    # explode = [0]*(len(df2_columns)) #爆炸圖結構製作
    # explode[1]=0.15 #自定義
    # explode[-1]=0.45 #自定義
    
    # # 圓餅圖設定
    # pie_color = ["#9B59B6","#E74C3C","#3498DB","#1ABC9C","#2ECC71","#F1C40F",
    #               "#DC7633","#DC7633","#DC7633","#DC7633","#FF2244"]
    # plt.figure(figsize=(16,10)) #圓餅圖尺寸
    # plt.pie(df2_sum,labels=df2_columns, autopct="%1.1f%%", #圓餅圖設定
    #         shadow=True,pctdistance=0.75,explode=explode,colors=pie_color)
    # plt.axis("equal")
    # plt.title("失業率 - 各年齡別",x=0.45,y=0.98,size=20) #標題
    # plt.legend(loc="lower left",fontsize=14) #小窗位置
    
    # # ===================================================================================
    # # plt.savefig(r'C:\Users\user\Desktop\Python_Test\Python_main\output\失業率-年齡別圓餅圖.png',
    #         # bbox_inches="tight",transparent=True,dpi=300) #本組提供大圖