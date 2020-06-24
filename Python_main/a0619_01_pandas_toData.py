import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# dic1 = [i for i in range(4)]
# print(dic1)
# pd1 = pd.Series(dic1,index=['a','b','c','d'])
# print(pd1)

df = pd.read_csv(r'./data/臺中市百大名攤名產_1.csv',encoding="utf-8")

# print(df.head(10))
# print(df.tail(10))
# print(df.ndim)
# print(df.shape)
# print(df.dtypes)
# print(df.loc[:,['區域','攤名','地址']])
# dfc = pd.DataFrame(np.random.rand(5,5),index=list('abcde'),columns=list('xyzef'))
# print(dfc.iloc[0:,0:])
df_data = pd.DataFrame(df)
# print(df_data.values)
df_class = df_data.groupby('區域')
# print(df_class.groups)
print(df_class.get_group("中區"))
# print(df_class.get_group("北區"))


# plt.plot(df["攤名"],df["地址"],"--",color="r")
# plt.plot(df_class["中區"],"--",color="r")
# df_mean = df_class.groupby("中區",as_index=False).mean()
# df_mean.plot(kind="bar",stacked=True)
# plt.xticks(df_mean.index,df_mean['中區'], rotation=0)
# plt.show()

