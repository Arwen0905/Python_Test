import pandas as pd
import numpy as np
lst = {"10,33","30,33"}
print(lst)
df = pd.DataFrame(lst)

# print(df.iloc[:])
# print(df.iloc[:,0])

df.iloc[:,0] = df.iloc[:,0].str.replace(',','')
print(df)