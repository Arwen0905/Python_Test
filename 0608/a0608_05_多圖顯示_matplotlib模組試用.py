import matplotlib.pyplot as plt
# figure:創造一個畫面，裡面可以塞很多圖
plt.figure()
# 利用subplot方法，設定(幾欄、幾列、位置)
plt.subplot(2,2,1) # 2欄 2列 左上角第一個
plt.gca().set_facecolor("black")
plt.plot([0,1],[0,1],[0,1],[0,3],[0,5],color="yellow")

plt.subplot(2,2,2) # 2欄 2列 右上角第一個
plt.gca().set_facecolor("black")
plt.plot([0,1],[0,2],color="green")

plt.subplot(2,2,3) # 2欄 2列 左下角第二個
plt.gca().set_facecolor("black")
plt.plot([0,1],[0,3],[0,5],color="blue")

plt.subplot(2,2,4) # 2欄 2列 右下角第二個
plt.gca().set_facecolor("black")
plt.plot([0,1],[0,4],color="#ff2244")
plt.show()
