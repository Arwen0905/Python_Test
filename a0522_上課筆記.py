import random
import pymysql
s=6
def output(s=6):
    count=1
    while count<=6:
        alst=[]
        alst.append(random.randint(1, 49))
        print(alst,end=' ')
        count+=1
output(s)
'''
串列:list
轉換方式:
'''
    # └ 數組轉為串列 → 
tuple1=(1,2,3)
list1=list(tuple1)
print()
print(list1)
print(type(list1))

    # └ 串列轉為數組 → 
tuple2=tuple(list1)
print(tuple2)
print(type(tuple2))
'''
=>字典(詞典):dict
    └ 建立:   鍵值1:值1
        └ 字典名稱={元素1,元素2,元素3,...}
dict可寫以下三種格式

# 二維詞典、三維詞典:
dict1([[key1:value1],[key2:value2],[key3:value3]])

# 正常版:
dict2(key1:value1,key2:value2,key3:value3)

# key值為字串:
dict3(str:value1,str:value2,str:value3)

資料結構整理:
    └ 字串元素無依定的順序排列 → 同學記憶體情境
      串列元素則為依序排列 → 記憶體
    └ 字典取值的方式: 字典名稱[key]
      以key(不可重複)作為索引取得 value(可重複)
      若重複，則將key覆蓋，只有最後的key會存在
      
      
'''
