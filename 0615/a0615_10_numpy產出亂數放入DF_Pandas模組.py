import pandas as pd
import numpy as np
name = ['Frank','Peter','John']
score = ['First','second','final']
# 建立 3*3 陣列，每一格的數據在 60~99 之間。
df = pd.DataFrame(np.random.randint(60,100,size=(3,3))\
                  ,columns=name,index=score)
print(df)

# index = 左側title
# columns = 上方title

data = [i for i in range(5)]
print(data)
