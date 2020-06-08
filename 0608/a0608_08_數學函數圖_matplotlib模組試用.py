import numpy as np
import matplotlib.pyplot as plt
x = np.arange(1,11)
y = 2*x +5
# x = np.arange(2, 6*np.pi, 0.1)
# y = np.sinc(x)
plt.title("Matplotlib demo",color="blue")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,color="#ffff55",linewidth="3",linestyle="-.")
# plt.plot(x,y,'oy') #實心圓
# plt.plot(x,y,'sy') #實心方塊
# plt.plot(x,y,'py') #實心五邊形
# plt.plot(x,y,'vy') #倒三角形
# plt.plot(x,y,'^y') #正三角形
# plt.plot(x,y,'*y') #星星
# plt.plot(x,y,'hy') #六邊形
plt.plot(x,y,'xr') #叉叉
plt.gca().set_facecolor("black")
plt.show()

x = np.linspace(1,20,20)
print(x)