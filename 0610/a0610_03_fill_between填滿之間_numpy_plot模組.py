import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5*np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2*x)

# plt.fill 填充區域繪圖區的顏色
plt.fill(x, y1, c="g")
plt.fill(x, y2, c="r")
# plt.fill_between 兩個繪圖區之間的填塞
plt.fill_between(x, y1, y2, facecolor="yellow")

plt.show()