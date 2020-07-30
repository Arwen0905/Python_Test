import json

data = {'name':'IT Xiao Ang Zai','number':100,'age':19.5}
jsonStr = json.dumps(data)  #python資料結構(一般為字典)轉換為JSON編碼的字串
print(jsonStr)

# data2 = json.loads(jsonStr) #將一個JSON編碼的字串轉換回一個python資料結構
# print(data2)
# print(type(data2))
# #我們現在試著寫入json型別資料
# with open("my_data.json",'w') as f:
# 	json.dump(data2,f)

# #我們現在進行讀入json型別資料
# with open("my_data.json",'r') as g:
# 	result_data = json.load(g)
# print(result_data)

