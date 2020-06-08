import matplotlib.pyplot as plt
import random

# list_x1 = [1,5,7,9,13,16]
# list_y1 = [15,50,80,40,70,50]
# list_x2 = [2,6,8,11,14,16]
# list_y2 = [10,40,30,50,80,60]
list_x1 = []
list_y1 = []
list_x2 = []
list_y2 = []
for i in range(4):
    list_x1.append(random.randint(1,50))
    list_y1.append(random.randint(1,50))
for i in range(6):
    list_x2.append(random.randint(1,50))
    list_y2.append(random.randint(1,50))

plt.plot(list_x1, list_y1,color="#ffff55",linewidth="5",\
         linestyle="-.",label=list_x2)
plt.plot(list_x2, list_y2, color="#ff2244",linewidth=5,\
         linestyle=":",label=list_y2)
# 顯示圖例
plt.legend()
# plt.xlim(0,18) #顯示x軸的線條→ 顯示比例
# plt.ylim(0,120) #顯示y軸的線條→ 顯示比例
plt.title("Pocket Money") #上方標題
plt.xlabel("Age") # 列標題
plt.ylabel("Money") #欄標題
plt.gca().set_facecolor('black') #背景設定
plt.show()

