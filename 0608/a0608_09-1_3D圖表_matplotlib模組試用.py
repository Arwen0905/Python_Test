import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
fig = plt.figure(5)
ax=fig.add_subplot(1,1,1,projection='3d')     #繪製三維圖
x,y=np.mgrid[-2:2:20j,-2:2:20j]  #獲取x軸資料，y軸資料
z=x*np.exp(-x**2-y**2)   #獲取z軸資料
ax.plot_surface(x,y,z,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=0.8)  #繪製三維圖表面
ax.set_xlabel('x-name')     #x軸名稱
ax.set_ylabel('y-name')     #y軸名稱
ax.set_zlabel('z-name')     #z軸名稱
plt.show()