import pandas as pd
from datetime import datetime,timedelta
#  日期時間可以做數學運算
ndays= 5 #天數
start = datetime(2019,3,11) #開始時間
dates = [start + timedelta(days=x) for x in range(0,ndays)]
data = [34,44,65,53,39]
ts1 = pd.Series(data, index=dates)

data2 = [34,44,65,53,39]
ts2 = pd.Series(data2,index=dates)
print('ts1、ts2')
print(ts1)
print(ts2)

addts = ts1 + ts2
print("ts1+ts2")
print(addts)

meants = (ts1+ts2)/2
print("(ts1+ts2)/2")
print(meants)

