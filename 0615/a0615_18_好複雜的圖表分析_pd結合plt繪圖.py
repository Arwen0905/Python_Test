import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[10000000,8500000,8000000,15000000,6000000,8000000],
          'area':[400,500,850,300,200,320],
          'town':['New York','Chicago','Bangkok','Tokyo',
                  'Singapore','Hongkong']}

tw = pd.DataFrame(cities,columns=['population','area'],index=cities['town'])

fig,ax=plt.subplots() # 在一個圖表中繪製不同軸的數據
fig.suptitle("City Statistics") # 主標題
ax.set_ylabel('Popu lation') # Y軸標題
ax.set_xlabel('City')  # X軸標題

ax2 = ax.twinx() # 產生一新軸
ax2.set_ylabel("Area") # Y軸標題
tw["population"].plot(ax=ax,rot=45,style='b-.',kind='line') # 第一個軸=ax，角度為45
tw["area"].plot(ax=ax2, style='r-') # 第一個軸=ax2，角度45
ax.legend(loc=1) # 小圖，圖立位置
ax2.legend(loc=2) # 小圖，圖立位置
plt.show()
