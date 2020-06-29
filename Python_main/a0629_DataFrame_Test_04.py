import pandas as pd
import matplotlib.pyplot as plt

file2 = './data/離婚統計_離婚登記對數-按區域別分.csv'
with open(file2,encoding="utf-8") as f:
    f = pd.read_csv(f) 

print(f["離婚對數.1"])
print(f["粗離婚率"].head(10))
n = f["離婚對數.1"].str.replace(",","")
print(n)
s = list(n)
print(s)
print(type(s))
x=[]
for i in s:
    if i != "-":
        q = int(i)
        x.append(q)
    elif i == "-":
        print(i,"髒東西")
print(x)


population = [860,1100,1450,1800,2020,2200,2260]

tw = pd.Series(x)
tw.plot(title='Population in Tanwan')
# plt.xlabel('Year')
# plt.ylabel('Population')
# plt.show()

