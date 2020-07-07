import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams["font.family"] = ['Microsoft JhengHei'] #微軟正黑體

file2 = '人力資源調查縣市別失業率.csv'
with open(file2,encoding="utf-8") as f:
    df1 = df = pd.read_csv(f)
    df = df.rename(columns={"項目別_Iterm":"年份"}) #重設列表名稱(日期)
    df["年份"] = df["年份"].str.replace("Jan.-June","/1-6月").str.replace("July-Dec.","/7-12月") #處理結構，設定索引
    
    # 分析項目:縣市別失業率——————————————————————————————————————————————————————————————————————
    # 小程式:自訂縣市並計算其失業率關係
    df1_list = []
    df_col_tem = [i for i in df]
    # print(df1.loc["1987"]) #只取某一列欄位資料
    # print(df1_South.iloc[:,[1]].head()) #可只取一筆欄位資料，檢視好用  
    # print(df_col_tem) #檢視:取得所有列名稱!
    df.index = df["年份"] #設定df1索引值為日期
    df1_city = df[["臺北市_Taipei_City","臺中市_Taichung_City","臺南市_Tainan_City",
                    "高雄市_Kaohsiung_City","北部地區_Northern_region","中部地區_Central_region"]]
    df1_county = df[["新北市_New_Taipei_City","臺中縣_Taichung_County","臺南縣_Tainan_County",
                      "高雄縣_Kaohsiung_County","南部地區_Southern_region","東部地區_Eastern_region"]]
    # 更換縣市需對應下方X軸名稱
    ax_name = ['台北/新北', '台中市/縣', '臺南市/縣', '高雄市/縣', "北部/南部", "中部/東部"] # X軸名稱
    # 台灣
    df1_Taiwan = df[df.columns[3:]] # 取得概念:由 df[資料內 [ 篩選df的列表範圍 ] ]
    df1_Taiwan = df1_Taiwan.drop(["中部地區_Central_region", #刪除不必要的區縣市
                                  "南部地區_Southern_region","東部地區_Eastern_region"],axis=1)
    
    # 可更換欲顯示的縣市區域，設定為可依需求取得範圍分析---------------------------------------
    df1_county = df1_county # 更換:右側為欲分析的資料
    df1_Taiwan = df1_city # 更換:右側為欲分析的資料
    # 各縣市名稱處理，將多餘贅字移除，只取前3個字元就好 例:台北市
    for i in df1_city.columns:
        df1_city = df1_city.rename(columns={i:i[:3]})
    for i in df1_county.columns:
        df1_county = df1_county.rename(columns={i:i[:3]})

    # print(df1_city.columns) # !檢視整理好的列表範圍
    # print(df1_city.index) # !檢視整理好的列表範圍
    # 資料年份從1978年起，至2019年7月，設定為可依需求取得範圍分析------------------------------
    df1_Taiwan_name03 = "失業率-縣市別 (2010-2020)" #檔案命名
    df1_city = df1_city[df1_city.index >= "2010/1"] # 這裡設定跑圖的起使
    df1_city = df1_city[df1_city.index <= "2020/1"] # 這裡設定跑圖的結束
    df1_county = df1_county[df1_county.index >= "2010/1"] # 這裡設定跑圖的起使
    df1_county = df1_county[df1_county.index <= "2020/1"] # 這裡設定跑圖的結束

    print("失業率-縣市別(1) 設定:"+df1_city.index[0]+"起至 "+df1_city.index[-1]) #檢視範圍用
    print("失業率-縣市別(2) 設定:"+df1_county.index[0]+"起至 "+df1_county.index[-1]) #檢視範圍用
    # 設定結束-------------------------------------------------------------------------------
    
    # 計算縣市失業率
    df1_city_ans = df1_city.sum() / df1_city.count().values # 加總值 / 加總量 (取出值)
    df1_city_ans = round(pd.DataFrame(df1_city_ans,columns=["失業率"]),1) # 轉pd二維及限制小數位
    # print(df1_city_ans) #檢視格式OK
    df1_county_ans = df1_county.sum() / df1_county.count().values # 加總值 / 加總量 (取出值)
    df1_county_ans = round(pd.DataFrame(df1_county_ans,columns=["失業率"]),1) # 轉pd二維及限制小數位
    # print(df1_county_ans) #檢視格式OK

    # print(df1_city.sum().head(),"取得加總值") #取五筆檢視就好
    # print(df1_city.count().head().values,"取得加總")
    # print(df1_county.sum().head(),"取得加總值") #取五筆檢視就好
    # print(df1_county.count().head().values,"取得加總")
    
    # 長條圖需先取得串列values，萃取資料處理==================================================
    df1_col_name = [i for i in df1_city_ans.index]
    df1_col_values = [i for i in df1_city_ans["失業率"]]
    df1_col_name2 = [i for i in df1_county_ans.index]
    df1_col_values2 = [i for i in df1_county_ans["失業率"]]
    # print(len(df1_col_name)) #長度一致
    # print(len(df1_col_name2)) #長度一致
    # print(df1_col_values) #確認內容OK 市
    # print(df1_col_values2) #確認內容OK 縣
#     # 結束===================================================================================
#     # 視覺化:長條圖(比較圖)
    
    
  
