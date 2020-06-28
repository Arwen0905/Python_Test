import pandas as pd
import numpy as np

f = pd.read_json('data/資料開放平臺_電影分析.json')
print(f.ndim)
print(f.shape)
print(f.dtypes)
# print(f.values)
print(f.head())
print(f.tail())
print(f.info)
df = pd.DataFrame(f)
print(df.dtypes)
print(df.values)
# print(df['descriptionFilterHtml'][50:56])
print(df[['title','descriptionFilterHtml']].head(5)) #列名稱[["col1","col2"]]多選
print('=== here '+'='*50)
# df.insert(1,column="Sport",value="checked") # insert 插入上方列的名稱

# 檢查有什麼欗列===============================================================
# print(df.columns.values[1:5],index=["電影名稱","介紹"]) #可以產生 列項目的名稱
print(df.columns) # 檢查:col項目名稱
print(df.size) # 全部4704個資料
print(df.ndim) # 是二維陣列
print(df.shape) # 224列,21欄
print(df.iloc[20:25,3:8]) # 超級好用的 iloc 進階索引
print('=== here '+'='*50)
print(df.iloc[20:25,[1,2,3]]) # 超級好用的 iloc 進階索引 "混合設定"
print('=== here '+'='*50)
#自定義列數項目 ↓
df = pd.DataFrame(df,columns=[df.columns[-3],df.columns[-2],df.columns[2]])
# df = pd.DataFrame(df,columns=[df.columns[2]]) #自定義列數項目
df = df.drop(2,axis=0) # 代號0:刪除一筆row,代號1:刪除一筆col 例:df.drop(["title"])
# df = df.dropna() #刪除NAN 空資料
df = df.fillna("你好") #刪除NAN 空資料
print(df.head(10))
# ===============================================================
print(df.sort_values('title',ascending=False).head(5)) #反排序 或 排序
print(df.dtypes) # 檢查:row項目名稱
print(df.loc[10:20,"endDate":"title"])
# == 進階資料選擇(索引應用) ===============================================================
frame = pd.DataFrame(np.random.rand(3,3),index=list("xyz"),columns=list("abc"))
print(frame)
print(frame.loc[['x','z'],['a','c']])
# =============================================================================


print('=== here '+'='*50)
print(df["endDate"].head(10))
# 在索引字串後接(數量條件)，然後再接參數條件 << 低級的思維
print(df["endDate"].head(5).values=="2020/06/30")

# 設定 "搜索條件" 並且 "索引出來"
ddf = df["endDate"].values=="2020/06/29"
print('符合條件的index:',df[ddf].count(1)) # 符合此條件的共有幾筆: count()方法
print(df.iloc[215])
print('=== here '+'='*50)
print(df.head(5)["endDate"].between("2020/06/20","2020/06/30"))
dd = df["endDate"].between("2020/06/20","2020/06/30")
print(df[dd].head(5).sort_values("startDate",ascending=False)) #進階索引+反排序
print('=== here '+'='*50)

# 資料分組 - groupby()

print('*** 資料分組 - groupby() ***')
frame_class = df.groupby(["startDate"]) # 以col名稱做分組
print(frame_class.get_group("2020/06/28")) # 索引row的值出來
# print(frame_class.groups) # 顯示所有值，包含dtype資訊
# 計算總和
print('=== here '+'='*50)
print(df.head(10).groupby("title").sum().sort_values("endDate",ascending=False)) # 複習方法



print('='*50)
lst = pd.DataFrame(np.random.randint(0,101,(7,4),int),index=list("abcdefg"),columns=list("ABCD"))
print(lst)
print('總和 === here '+'='*50)
# 抓一個col值做參照，若重複則將以下的值做相加，若設定["兩","個"]則條件為，必須兩個皆重複才做相加，相對嚴苛
print(lst.groupby(["A"]).sum())



print('資料分組 用key做分組的依據 === here ')
df = pd.DataFrame({"key1":list('ABACBDCDAC'),
                   "key2":("one","tow")*5,
                    "data1":np.random.randint(0,100,10,int),
                   "data2":np.random.randn(10)})
print(df)
print(df.size,'<< 值的總和')
print(df.count(),'<< 各列的 名稱與數量')

sector = df.groupby("key1")
print('key1的值'+'='*50)
print(sector.groups,'<< key1的所有值')
# sector = pd.DataFrame(sector) # 轉成二維檢視 
# print(sector)
print('='*50)
print(type(sector),'<< 類型')
print('='*50)
print(sector.size,'<< 值的總和')
print('取出key1是A的資料'+'='*50)
print(sector.get_group("A"))
print('取出key1是B的資料'+'='*50)
print(sector.get_group("B"))

print('分組("key1")若重複則相加起來'+'='*30)
print(df.groupby(["key1"]).sum())
print('分組key1，只抓分組內的("A")值'+'='*30)
print(df.groupby("key1").get_group("A"))
print('='*30)
print(sector.mean()) # sector設定以key1分組，mean為平均值方法

import random
print('='*30)
# data3 = [1,5,8,20]
data3 = ["a","b","c","d"]
# data3 = pd.Series(data3).str.upper() # pd的Series有針對字串的方法 pdFile.str
random.shuffle(data3) #洗牌
print(data3)
data3 = random.sample(data3,4) #取數隨機
print(data3)
 
data4 = pd.DataFrame(np.random.randint(1,101,(10,8)),index=list('abcdefghij'),columns=list('ABCDEFGH'))
radom = ["class1","class2"]*5
# radom = random.sample(radom,len(radom))
random.shuffle(radom)
data4.insert(0,column="新增一列分組",value=radom)
# s="s".upper()
print(data4)
data4_class = data4.groupby("A").sum()
# print(data4_class.get_group("5"))
print('='*50)
s = random.normalvariate(1000,50) #常態分配亂數，平均數|標準差
print(s)



data = pd.Series(np.random.randint(1,101,5),index=list("abcde"))
print(data,'正常輸出')
print('='*50)
print(data.std(),'標準差')
print(data.sum(),'總和')
print(data.median(),'中位數')
print(data.nlargest(3),'最大3個')
print(data.nsmallest(3),'最小3個')
print(data.max(),'最大')
print(data.min(),'最小')
print(data.mean(),'平均')

strD = pd.Series(["您好","Python","Pandas"])
print(strD.str.upper())
print(strD.str.cat(sep=",")) # 於間距，加入指定逗號
print(strD.str.replace("您好","hello"))
print(strD.str.contains("Py")) # 檢查有沒有某字元
















