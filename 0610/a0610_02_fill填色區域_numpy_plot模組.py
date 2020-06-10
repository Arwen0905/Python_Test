import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5*np.pi, 1000)

y1 = np.sin(x)
y2 = np.sin(2*x)

# plt.plot(x, y1, color="g", label="$y=sin(x)$",\
#           linestyle="solid",linewidth=2)
# plt.plot(x, y2, color="b", label="$y=sin(2*x)$",\
#           linestyle="solid",linewidth=1)

# plt.fill 填充區域繪圖區的顏色
plt.fill(x, y1, color="g", alpha=0.3)
plt.fill(x, y2, color="b", alpha=0.3)

plt.show()