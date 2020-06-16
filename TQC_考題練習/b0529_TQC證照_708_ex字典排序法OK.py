# 合併兩個字典，並排序輸出
dict1 = {'2':'A','1':'B'}
dict2 = {'3':'A','4':'C'}
# 合併作業步驟
dict3 = dict1.copy() # 字典3 先複製 字典1的內容
dict3.update(dict2)  # 字典3 再加入 字典2的內容
# 排序作業步驟
dict3 = sorted(dict3.items()) # 此排序以後，資料型態會轉串列
# print(dict3,type(dict3),'被轉成串列型態')
dict3 = dict(dict3) # 可以再轉回字典
# print(dict3)
for i in dict3:
    print('%s: %s'%(i,dict3[i]))

