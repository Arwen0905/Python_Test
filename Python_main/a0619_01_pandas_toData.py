import pandas as pd
dic1 = [i for i in range(4)]
print(dic1)
pd1 = pd.Series(dic1,index=['a','b','c','d'])
print(pd1)

df = pd.read_csv(r'./data/臺中市百大名攤名產_1.csv')
# print(df.head(10))
# print(df.tail(10))
print(df.info)
print(df['攤名'][:30])

