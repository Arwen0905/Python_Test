from bs4 import BeautifulSoup
import requests
import os
from urllib.request import urlretrieve
import re
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft Jhenghei"] #中文設定
lst_file=[]

url = 'https://data.gov.tw/dataset/27396' #網址設定
rq = requests.get(url) #取得網址
soup = BeautifulSoup(rq.text,"html.parser") #解析html網址內容
# print(soup.prettify()) #html檢視用

name_q= soup.find_all("div",class_=("field-items")) #找檔名

for i in name_q: #捕捉檔名
    s = i.text
    res = re.findall('\d{2}\d?[年]\w*',s)
    if res == [s]:
        lst_file.append(res[0])
        print(res,"檔名捕捉!")
print("\n檔案名稱串列:\n",lst_file)


rs = soup.find_all("a",{"title":"下載格式為 CSV"}) #找載點
count=0
for index,i in enumerate(rs):
    try:
        csv_url = i.get("href")
        # if count < len(lst_file):
        if index%2==0:
            urlretrieve(csv_url,f'./output/{lst_file[count]}.csv') #存CSV檔
            count+=1
            print(i.get("href"),"正在處理.....")
        else:
            # urlretrieve(csv_url,f'./output/重複檔案{count}.csv') #存重複檔
            print(i.get("href"),"正在排除.....")
        print(lst_file[count],"儲存完畢!")
    except:
        print('資料來源有誤，跳過!')
# ====================================================================================


print("資料彙整 "+"="*50)
lst_f = ["102年結婚對數","103年結婚對數","104年結婚對數",
          "105年結婚對數","106年結婚對數","108年結婚對數",
          "107年結婚對數"] #開發階段用
if len(lst_file) > 1:lst_f = lst_file #若有捕捉檔名就優先，否則使用上述串列名稱

    
df1,df2,df3,df4,df5,df6,df7 = pd.DataFrame(),pd.DataFrame(),pd.DataFrame(),\
                              pd.DataFrame(),pd.DataFrame(),pd.DataFrame(),\
                              pd.DataFrame()
df_all = [df1,df2,df3,df4,df5,df6,df7]
# print(df_all) #多維盒子

for i in range(len(lst_f)): #將載入的csv文件，逐一合併至 多維盒子
    with open(f'.\output\{lst_f[i]}.csv',encoding="utf-8") as f:
        df_all[i] = pd.read_csv(f) #讀入每筆csv檔
        lst_f[i] = lst_f[i][:4] #[串列名稱]字串處理，排除後續贅字
        
        df_all[i]["年索引"] = lst_f[i] #新增"年索引"至列末
        df_all[i].index = df_all[i]["年索引"] #簡化名稱並設為索引值
        df_all[i] = df_all[i].drop(["年索引"],axis=1) #完成上述 就砍掉列表"年索引" !0
        
        lst_f[i] = lst_f[i][:3] #再重新賦予年份，命名只取數字就好
        df_all[i]["年份"] = lst_f[i] #新增"年份"至列的末端
        
        # df_all[i] = df_all[i].rename(columns={"年索引":"年份"}) #避免索引同名 !0


        
print(df_all) #各年份資料併入完成
# ====================================================================================
                
print("資料合併檢視 "+"="*50)        
res = pd.concat(df_all[:]) #列合併
print(res.loc["105年"]) #全部合併顯示

# 寫入:資料核對
res.to_csv("./output/Super_csv.csv",index=True,sep=",",encoding="utf-8-sig")

# 檢視
print(res.size) #顯示資料"筆數"
print(set(res.index)) #找索引，轉不重複

print(res.columns.values) #顯示"列表"
print(set(res["年份"])) #檢查"某列"的欄位，轉set不重複

print("="*50)
# 分組 跟 取出
gp = res.groupby("年份")
gp2 = res.groupby("年份")

# 年份設定 ==========================================================
gp1_name = "102"
gp2_name = "108"
# 結束設定 ==========================================================
print(gp)
print(type(gp))
print(gp.size())
print(gp.get_group(f"{gp1_name}"))
print(gp.get_group(f"{gp2_name}"))

gp = res.groupby("年份").get_group(f"{gp1_name}").sum()
gp2 = res.groupby("年份").get_group(f"{gp2_name}").sum()
# # 視覺化:轉df
gp = pd.DataFrame(gp[1:-1]) #轉df格式，捨去頭尾(!非數值)
gp2 = pd.DataFrame(gp2[1:-1]) #轉df格式，捨去頭尾(!非數值)

# gp.plot(kind="line",title="區域別",figsize=(10,8))
plt.plot(gp) #畫上去
plt.plot(gp2) #畫第二條

plt.legend([f"{gp1_name}年",f"{gp2_name}年"])
plt.title(f"{gp1_name}年、{gp2_name}年 - 年份比較",color="#ff2244")
plt.xlabel("日期")
plt.ylabel("歷\n年\n對\n數\n總\n合\n比\n較",rotation=0,ha="right",fontsize=12,color="b")
plt.grid(color="#555555",linewidth=0.5)
# ==================================================================


print("寫入作業"+"="*50)

csv_list = glob.glob('.\output\*.csv') #查看同文件夾下的csv文件數
print(csv_list)
print('共發現%s個CSV文件'% len(csv_list))
print('正在處理............')

for i in csv_list: #循環讀取同文件夾下的csv文件
    fr = open(i,'rb').read() #迭代讀取:每抓到一筆(i) ，就賦予至(fr)變數
    with open('.\output\All.csv','ab') as f: #迭代寫入:再將讀取的資料，以附加二元模式寫入
        f.write(fr)
print('合併完畢！')
