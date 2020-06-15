import pandas as pd
import matplotlib.pyplot as plt
cities = {'population':[1000,850,800,1500,600,800],
          'town':['New York','Chicago','Bangkok','Tokyo',
                  'Singapore','Hongkong']}
tw = pd.DataFrame(cities,columns=['population'],index=cities['town'])
print(tw) # 檢視
tw.to_csv('tw_csv.csv') # 很好寫入

# 畫圖
tw.plot(title="Population in the world")
plt.xlabel('City')
plt.ylabel('Population')
plt.show()

