import matplotlib.pyplot as plt
import numpy as np
import matplotlib
# Fixing random state for reproducibility
# 設定亂數種子
np.random.seed(20200608)

x = np.arange(0.0, 50.0, 2.0)
# x = 產生值若為浮點(非整數)
# np.random.rand(整數int)
# 			└ 則以 *x.shape
y = x ** 1.3 + np.random.rand(*x.shape) * 30.0
s = np.random.rand(*x.shape) * 800 +500
# scatter 先代入數據資料 x,y,s,c="顏色",alpha=半透明,marker=
# plt.scatter(x, y, s, c="r", alpha=0.5, marker=r"$\clubsuit$",\
plt.scatter(x, y, s, c="g", alpha=0.5, marker=r"$\star$",\
    label="Luck") #顯示文字
plt.xlabel("Leprechauns") #顯示文字
plt.ylabel("Gold") #顯示文字
plt.legend(loc=2) #小標題顯示位置
plt.show()
