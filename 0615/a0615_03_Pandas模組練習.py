import pandas as pd
years = range(2020,2023)
beijing = pd.Series([20,21,19],index=years)
hongkong = pd.Series([25,26,27],index=years)
singapore = pd.Series([30,29,31],index=years)
city_df = pd.concat([beijing, hongkong, singapore],axis=1)
citi_es = ["beijing","hongkong","singapore"]
city_df.columns = citi_es

print(city_df)
