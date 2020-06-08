import pandas as pd #匯入模組命名為pd
# 設定二維串列
datas = [[65,92,78,83,70],[90,72,76,93,56],[81,85,91,89,77],[79,53,47,94,80]]
# 列標題
indexs = ["李大年","王大同","黃美娟","陳美玲"]
# 欄標題
columns = ["國文","數學","英文","自然","社會"]
# 代入以上相關資料，建立Pandas格式資料
df = pd.DataFrame(datas,columns=columns,index=indexs)
print(df)
# 使用DataFrame的資料儲存方法 之一 to_csv
# 這是生成資料表(csv)
df.to_csv('pdout2.csv',encoding='utf-8-sig')
# 這是讀取
rd = pd.read_csv("pdout.csv",encoding="utf-8-sig",index_col=0)
print(rd)
