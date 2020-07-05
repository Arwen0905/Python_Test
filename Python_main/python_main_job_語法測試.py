import numpy as np
import pandas as pd
df1 = np.arange(9).reshape(3,3)
df2 = np.random.randint(10,20,[10,3])

# d1 = pd.DataFrame(df1,index=list("ABC"))
# d1 = d1.rename(index={"A":"Q","C":"QQ"},columns={0:"列改"}) #可以選擇任何爛列名稱做更名
# d1.index = ["索引1","索引2","索引3"]
# d1.columns = ["再改","列再改","最後改"]

# q = pd.DataFrame(np.arange(4).reshape(4,1),columns=list("A")) #自產一維
# print(q) 先用不到

# d1 = pd.DataFrame(df1,index=list("ABC"))

# 開始:測試合併自選資料=====================================================
file2 = './data/離婚統計_離婚登記對數-按區域別分.csv'
with open(file2,encoding="utf-8") as f2:
    df1 = pd.read_csv(f2)
    d1 = pd.DataFrame(df1["離婚對數"],df1)
    d1["QQQ"] = np.arange(len(d1))
    print(d1)
# 結束=====================================================

# print(d1.count())
# d1.index=["改","欄","位"]
# d1.columns=["改","欄","位"]
# print(d1.index)
# print(d1)

scores = {"姓名":["啊德","師傅"],
          "喜歡":["素肚","可樂"],
          "旅遊":["菲律賓","日本"]}
dic = pd.DataFrame.from_dict(scores)
# print(dic.count(0))
# print(dic)

file1 = '人力資源調查失業率.csv'
with open(file1,encoding="utf-8") as f:
    df = pd.read_csv(f)
    df1 = pd.DataFrame(df["女_Female"])
    df1.columns = ["取代的新名字"]
    df1 = df1.rename({"取代的新名字":"替換"})
    # print(df1.dtypes)
    # print(df1)
    

# for i in range(len(df["年份"])): #index序列
#     ans=0
#     for index,col in enumerate(df_col_tem):
#         if 3< index <15: #總是從第三筆開始
#             # print(df[col],'檢視計算過程')
#             # print(df[col][i]) #設計過程檢視用
#             if df[col][i] == "-": #避開不正確值
#                 continue
#             ans+=float(df[col][i]) #由第一維迴圈取值；第二維換圈的反巢狀取值
#     df1_average.append(ans/11) #年齡層7項
    
print("第四階段"+"="*50)
file4 = '職業訓練_就業人數.csv'
with open(file4,encoding="utf-8") as f:
    df1 = df = pd.read_csv(f)
    df1_name04 = "職業訓練-就業人數(新北市)" #檔案命名
    print(df1.dtypes)
    
    df1 = pd.DataFrame(df[["接受市府職業訓練人數_男","職業訓練就業人數_男",
                           "接受市府職業訓練人數_女","職業訓練就業人數_女"]])
    df1.index = df["年份"]
    # print(df1)
    # job = 0
    # print(job)