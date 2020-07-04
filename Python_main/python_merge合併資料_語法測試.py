import pandas as pd
Location = ["高雄", "台南", "台中", "台南"]
PM25 = [30, 35, 20, 15]
NOx= [1, 2, 3, 2]

PM25_df = pd.DataFrame()
PM25_df["Location"] = Location
PM25_df["PM25"] = PM25
# print(PM25_df)

NOx_df = pd.DataFrame()
NOx_df["Location"] = Location
NOx_df["NOx"] = NOx
# print(NOx_df)
qq = pd.merge(PM25_df, NOx_df, on='Location')
print(PM25_df)
print(NOx_df)
print(qq)
