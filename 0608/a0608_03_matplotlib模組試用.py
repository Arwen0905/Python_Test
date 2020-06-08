import matplotlib.pyplot as plt
import pandas as pd
import random
# 通常是將資料存在串列裡面，再傳給matplotlib處理製作圖表
# arr = []
# arr2 = []
# arr3 = []
# columns = ["國文","數學","英文","自然","社會"]
# for i in range(5):
#     arr.append(random.randint(1, 100))
#     arr2.append(random.randint(1, 100))
#     arr3.append(random.randint(1, 100))
# ans = pd.DataFrame(arr,colums=arr2,index=arr3)
# print(ans)

listX = [1,5,7,9,13,16]
listY = [15,50,80,40,70,50]
for i in range(6):
    listX.append(random.randint(1,100))
    listY.append(random.randint(1,100))
plt.plot(listX, listY)
plt.show()
