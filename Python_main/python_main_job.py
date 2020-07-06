import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams["font.family"] = ['Microsoft JhengHei'] #微軟正黑體

file1 = '人力資源調查失業率.csv'
with open(file1,encoding="utf-8") as f:
    # df1 = df = pd.read_csv(f).dropna() #刪除空白列會有index中斷代價
    df1 = df = pd.read_csv(f) 
    df = df.rename(columns={"項目別_Iterm":"年份"}) #重設列表名稱(日期)
    df["年份"] = df["年份"].str.replace("M","/") #處理字串結構，並設定年份為索引值
    # for i in df: print(i) #檢查列表名稱用

    # df = df.fillna(0) #若空則0計算
    # df = df.fillna({'總計_Total':888}) #針對某位置處理，若空則替換
    # print(df["總計_Total"][546]) #檢視nan


    # 分析項目:男女別————————————————————————————————————————————————————————————————————————
    df1 = df1[["男_Male","女_Female"]] #取得資料
    # df1.index = pd.to_datetime(df["年份"],format=("%Y/%m")) #取消:將日期格式化
    df1.index = df["年份"] #直接設定即可
    df1 = df1.dropna() #刪除2020年及其他可能空白的列資料
    
    # 測試:不刪除空白列的作法=============================================================
    # print(df1[["男_Male","女_Female"]].iloc[-10:]) #檢視到2020年資料:NaN
    # df1["男_Male"].iloc[-6] = (df1["男_Male"].iloc[-5]+df1["男_Male"].iloc[-7])/2 #將前後月除2
    # df1["女_Female"].iloc[-6] = (df1["女_Female"].iloc[-5]+df1["女_Female"].iloc[-7])/2
    #! 將某筆索引名稱更換
    # df1 = df1.rename(index=({"2020":"2020\n( 空窗資料:補值 )"})) #可接受換行符
    # print(df1.index)
    # 結束===================================================================================
    
    # 資料年份從1978年起，至2020年5月，設定為可依需求取得範圍分析------------------------------
    df1 = df1[df1.index >= "1992/00"] # 這裡設定跑圖的年份
    df1 = df1[df1.index <= "1993/00"] # 這裡設定跑圖的年份
    df1_name01 = "失業率-男女別 (1992年)" #檔案命名
    print("失業率-男女別 設定:"+df1.index[0]+" 至 "+df1.index[-1]) #檢視範圍用
    # 設定結束-------------------------------------------------------------------------------
    
    # 視覺化:走勢圖
    # df1[["男_Male","女_Female"]].\
    #     plot(kind="line",color=["#3498DB","#FF525B"],figsize=[10,5],linewidth=1.5) #走勢圖設定    
    # # plt.ylabel("😂",fontname="symbola",size=16,rotation=0,ha="right") #Y軸
    # plt.ylabel("失\n業\n率",size=16,rotation=0,ha="right",color="r") #Y軸
    # plt.title(df1_name01,y=1.01,size=18) #標題
    # plt.legend(["男生","女生"],loc="upper left",fontsize=14) #小圖位置
    # plt.xlabel("日期",size=16) #X軸標題
    # plt.grid(True,color="#555555",linewidth=0.6) #網格
    # plt.gca().set_facecolor("#DDDDDD") #背景顏色
    
    # 出圖===================================================================================
    # plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/png/{df1_name01}.png", #檔名
    #             bbox_inches="tight",transparent=True,dpi=300) #大圖
    # plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/{df1_name01}.jpg", #檔名
    #             bbox_inches="tight",transparent=False,dpi=300) #大圖
    # 結束===================================================================================
    
    
    # 分析項目:年齡別————————————————————————————————————————————————————————————————————————
    # 處理資料內不正確字元，例如: - 程式運算會無法判斷
    df["age_60-64"] = df["age_60-64"].replace("-",np.nan) #轉成空值
    df["age_65_over"] = df["age_65_over"].replace("-",np.nan)
    df["age_60-64"] = df["age_60-64"].astype(float) #轉浮點數
    df["age_65_over"] = df["age_65_over"].astype(float)
    # check = [i for i in  df["age_60-64"]] #檢查元素用
    # print(check) #檢查元素用
    # print(df["age_60-64"].sum()) #檢查元素用OK
    
    df2_columns = ["age_15-19","age_20-24","age_25-29","age_30-34","age_35-39","age_40-44",
                    "age_45-49","age_50-54","age_55-59","age_60-64","age_65_over"]
    df2 = df[df2_columns] #將指定欄位名稱賦予給df2
    df2.index = df["年份"] #index索引值設定為年份
    # print(df2.dtypes) #檢查類型:float64 轉換完成
    
    df2_columns=[i.replace("age_","")+"歲" for i in df2_columns] #處理字串
    df2_columns[-1] = df2_columns[-1].replace("_over歲","歲以上") #處理特殊字串
    # print(df2_columns) #欄位名稱檢查OK
    
    explode = [0.02]*(len(df2_columns)) #爆炸圖結構製作
    explode[1]=0.15 #自定義
    explode[0]=0.03 #first自定義
    explode[-1]=0.3 #final自定義
    
    # 視覺化:圓餅圖
    pie_color = ["#3498DB","#FF525B","#9B59B6","#1ABCCA","#2ECC71","#F1C40F",
                   "#DC7633","#839192","#AADDCC","#CDE2D0","#D5D8DC"] #配色

    # 資料年份從1978年起，至2020年5月，設定為可依需求取得範圍分析------------------------------
    df2 = df2[df2.index >= "1980/00"] # 這裡設定跑圖的年份
    df2 = df2[df2.index <= "2020/05"] # 這裡設定跑圖的年份
    df2_name02 = "1980-2000年" #檔案命名
    df2_sum = df2.sum() #各年齡總和
    print("失業率-年齡別 設定:"+df2.index[0]+" 至 "+df2.index[-1]) #檢視範圍用
    # 設定結束-------------------------------------------------------------------------------
    
    # 測試:程式配色==========================================================================
    # df2_sum = [int(i) for i in df2_sum]
    # s = pd.Series(df2_sum,index=df2_columns)
    # print(s)
    # labels = s.index
    # sizes = s.values
    # pie_color = cm.rainbow(np.arange(len(sizes))/len(sizes))
    # 結束===================================================================================

    
    # plt.figure(figsize=(13,8)) #畫布比例
    # patches,out_text,in_text = plt.pie(df2_sum,labels=df2_columns,
    #             autopct="%1.1f%%",startangle=90,radius=2, #圓餅圖設定
    #             shadow=False,pctdistance=0.8,explode=explode,colors=pie_color)
    # plt.axis("equal") #xy軸一致(圓形)
    # plt.title("失業率 - 年齡別\n"+df2_name02,x=0.20,y=0.92,size=36) #標題
    # plt.legend(loc="lower left",fontsize=14) #小圖設定
    # # 改變字體大小
    # in_text = [i.set_size(14) for i in in_text] #內圍字體大小
    # out_text = [i.set_size(14) for i in out_text] #外圍字體大小

    # 出圖===================================================================================
    # plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/png/失業率 - 年齡別 {df2_name02}.png", #檔名
    #             bbox_inches="tight",transparent=True,dpi=300) #大圖
    # plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/失業率 - 年齡別 {df2_name02}.jpg", #檔名
    #             bbox_inches="tight",transparent=False,dpi=300) #大圖
    # 結束===================================================================================

print("第二階段"+"="*50)
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
    # 結束===================================================================================
    # 視覺化:長條圖(比較圖)
    # width = 0.3 #條寬度
    # x = np.arange(len(ax_name))
    # fig, ax = plt.subplots()
    # rects1 = ax.bar(x - width/2, df1_col_values, width, label=None, color="#F39C12")
    # rects2 = ax.bar(x + width/2, df1_col_values2, width, label=None, color="#3498DB")
    
    # ax.set_ylabel("失\n業\n率",size=14,rotation=0,ha="right",color="r")
    # ax.set_title(df1_Taiwan_name03)
    # ax.set_xticks(x)
    # ax.set_xticklabels(ax_name)
    # plt.gca().set_facecolor("#17202A")
    # ax.legend()
    
    # def autolabel(rects):
    #     for rect in rects:
    #         height = rect.get_height()
    #         ax.annotate('{}'.format(height),
    #                     xy=(rect.get_x() + rect.get_width() / 2, height),
    #                     xytext=(0, 3),  # 3 points vertical offset
    #                     textcoords="offset points",
    #                     ha='center', va='bottom',fontsize=8,color="white")
            
    # autolabel(rects1)
    # autolabel(rects2)
    # fig.tight_layout()
    # 出圖===================================================================================
    # plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/png/{df1_Taiwan_name03}.png", #檔名
    #             bbox_inches="tight",transparent=True,dpi=300) #大圖
    # plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/{df1_Taiwan_name03}.jpg", #檔名
    #             bbox_inches="tight",transparent=False,dpi=300) #大圖
    # 結束===================================================================================
    
print("第三階段"+"="*50)
# file3 = '失業率－婚姻狀況別.csv'
file3_104 = '104年教育程度別失業率-按年齡分.json'
file3_105 = '105年教育程度別失業率-按年齡分.json'
file3_106 = '106年教育程度別失業率-按年齡分.json'
file3_107 = '107年教育程度別失業率-按年齡分.json'
file3_108 = '108年教育程度別失業率-按年齡分.json'
with open(file3_108,encoding="utf-8") as f:
    df1 = df = pd.read_json(f)
    df = df.rename(columns={"年":"年份"}) #重設列表名稱(日期)
    # print(df.dtypes)
    df1_name04 = "失業率-教育別 (108年)" #檔案命名
    
    df1 = pd.DataFrame(df[["國中及以下_國小及以下_Junior_high_and_below_Primary_school_and_below",
                         "高中_職_合計_Senior_high_and_vocational_Total",
                         "大專及以上_專科_Junior_college_and_above_Junior_college",
                         "大專及以上_大學_Junior_college_and_above_University",
                         "大專及以上_研究所_Junior_college_and_above_Graduate_school"]])
    
    # print(df["項目別_Item"][2:4])
    print(df1.index.values)
    print(df1.columns.values)

    # 將資料取得，因為需要列值，用迴圈取
    df1_male = []
    df1_female = []
    for i in df1:
        df1_male.append(float(df[i][2]))
        df1_female.append(float(df[i][3]))

    # 視覺化:走勢圖
    df1_col = ["國中以下","高中職","專科","大學","研究所"]
    df1_row = ["男生","女生"]
    df1 = pd.DataFrame([df1_male,df1_female] ,columns=df1_col, index=df1_row).T
    print(df1)
    df1.plot(kind="line",color=["#3498DB","#EC7063"],figsize=[10,6],
              fontsize=18,linewidth=4)
    plt.grid(True,color="#555555",linewidth=0.6)
    plt.title(df1_name04, size=21)
    plt.xlabel("學歷",fontsize=12)
    plt.ylabel("失\n業\n率",rotation=0,ha="right",fontsize=14,color="r")
    plt.legend(["男生","女森"],loc="upper left" ,fontsize=14)
    
    plt.gca().set_facecolor("#DDDDDD") #設定背景色
    
    # 出圖===================================================================================
    plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/png/{df1_name04}.png", #檔名
                bbox_inches="tight",transparent=True,dpi=300) #大圖
    plt.savefig(f"C:/Users/user/Desktop/Python_Test/Python_main/output/{df1_name04}.jpg", #檔名
                bbox_inches="tight",transparent=False,dpi=300) #大圖
    # 結束===================================================================================
    