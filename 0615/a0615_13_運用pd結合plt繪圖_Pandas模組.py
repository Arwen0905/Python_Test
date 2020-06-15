# 台灣地區，從1970-2020年間的人口統計
# 單位:萬人
import pandas as pd
import matplotlib.pyplot as plt
population = [860,1100,1450,1800,2020,2200,2260]
tw = pd.Series(population, index=range(1950, 2011, 10))
tw.plot(title='Population in Tanwan')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

