import pandas as pd
years = range(2020,2023)
beijing = pd.Series([20,21,19], index = years)
hongkong = pd.Series([25,26,27], index = years)
# pandas 透過 index索引對應 data(資料)
singapore = pd.Series([30,29,31], index = years)

# pandas的 concat方法為 資料合併
citydf = pd.concat([beijing, hongkong, singapore],axis=1)
print(type(citydf))
print(citydf)

