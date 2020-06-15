import pandas as pd
import numpy as np
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['X','Y','Z','S'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['X','Y','Z','S'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['X','Y','Z','測試S'])

print(df1)
print(df2)
print(df3)
