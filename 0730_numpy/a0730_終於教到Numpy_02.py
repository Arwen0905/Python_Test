import numpy as np
a = np.array([1,2,3])
a = a * 3
a = a + 2
print(f"原本的a: {a}")
b = np.array([2,2,0])
print(f"原本的b: {b}")

print("a+b: ",a+b)
# print("a/b: ",a/b) #除有問題
print("a*b: ",a*b)

#建立陣列: np.array
#建立陣列: np.arange
c = np.arange(10)
print(c)

d = np.linspace(0,10,5) #平均撒點
print(d)

e = np.array([[1,2,3],[4,5,6]])
print(e)

f = np.arange(10).reshape(2,5)
print(f)

d = np.array([[[
              [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
              [[1,2,3],[4,5,6],[7,8,9],[10,11,12]],
              [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
              ]]])
print(d) # 由圖解判斷幾維，從 欄、列 開始往外圈判斷，遇到框即代表一維
print(d.ndim) # 僅檢視該陣列為幾維
print(d.shape) # 由數量判斷有幾組維度，包含欄、列數量
print(d.sum(axis=2)) #指定維度 → 做運算(sum)
print(d.reshape(12,3)) #重整結構，總數必須符合實際元素數量

arr = np.array([[1, 2, 3],[4,5,6]], ndmin=5) # ndmin可設定幾維
print(arr)
print(arr.ndim)
print('shape of array :', arr.shape)



