import numpy as np
import pandas as pd
print("Pandas Test ========================")
# ss = np.arange(1,11).reshape(5,2)
ss = np.array(np.arange(5))
print(ss)
ss = pd.Series(ss,index=["A","B","C","D","E"])
print(ss)

print(ss.values) # 以row形式檢視

print(ss.index)
print(ss["A"])
print( "A" in ss)
print( 0 in ss )
print( 0 in ss.values )

lst = [i for i in range(10)]
print(lst,'<< 串列')
dic = {"A":123,"B":456,"C":789}
print(dic,'<< 字典')
lst = pd.Series(lst)
print(lst,'<<以上: 串列轉Series')
print('-'*50)
dic = pd.Series(dic)
print(dic,'<<以上: 字典轉Series')
print('='*50)

data = {"name":["Arwen","amy"],"interest":["game","shopping"]}
print(dic,type(dic),'<< dic類型')
print('='*50)
dic = pd.Series(dic)
print(dic,'<< 一維')
dic = pd.DataFrame(dic)
print(dic,'<< 二維')
print('='*50)

dic1 = pd.DataFrame(data,columns=["name","interest","ABC"], index=["A","B"])
print(dic1)

X = [["Amy","F","80"],["Bob","M","65"],["Cindy","F","73"],["Dave","M","46"],["Eva","F","46"]]
df1 = pd.DataFrame(X,columns=["name","gender","mathgrade"])
print(df1)
print(df1['name']) # 顯示index的資訊
print(df1['name'].values) # 僅顯示內容 .values就像np的陣列輸出一樣
print(df1['name'][0:2])

print('=== here '+'='*50)
print(df1.dtypes)




















