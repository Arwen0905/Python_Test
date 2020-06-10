import numpy as np
import matplotlib.pyplot as plt
# 產生模擬資料
x = np.arange(0.0, 4.0*np.pi, 0.01)
y = np.sin(x)
plt.plot(x,y)
# 畫水平基準線 x.mix,x.max 從0,0開始
plt.plot((x.min(), x.max()), (0,0),color="#ff2244")

plt.xlabel("x")
plt.ylabel("y")
# 兩繪圖區域之間的部分區域填色
# 若是 (2.3小於x 和 x小於4.3) 或者 x大於10的話 填上"紫色"
plt.fill_between(x, y, where=(2.3<x) & (x<4.3) | (x>10), facecolor="purple" )
plt.fill_between(x, y, where=(7<x) & (x<8), facecolor="green" )
plt.show()

