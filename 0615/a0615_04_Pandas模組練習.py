import pandas as pd
years = range(2020,2023)
beijing = pd.Series([20,21,19],index=years)
hongkong = pd.Series([25,26,27],index=years)
singapore = pd.Series([30,29,31],index=years)

# beijing.name = "Beijing"
beijing.name = "北京"
# hongkong.name = "Hongkong"
hongkong.name = "香港"
# singapore.name = "Singapore"
singapore.name = "新加坡"

city_df = pd.concat([beijing, hongkong, singapore],axis=1)
print(city_df)
