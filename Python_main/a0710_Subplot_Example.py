import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df1 = np.arange(0,20).reshape(5,4)
df1 = pd.DataFrame(df1,index=list("一二三四五"),columns=list("ABCD"))
print(df1["A"])

plt.figure(figsize=(8,8))
df1,plt.subplot(1,2,1) # 設定(幾欄、幾列、位置) 
df1["A"].plot(kind="line")
df1,plt.subplot(1,2,2) # 設定(幾欄、幾列、位置) 
df1["B"].plot(kind="line")

plt.figure(figsize=(12,8))
width = 0.3 #條寬度
x = np.arange(len(df1))
plt.subplot(1,2,1) # 設定(幾欄、幾列、位置)     
plt.bar(x - width/2, df1["A"], width, color="#F39C12")
plt.subplot(1,2,2) # 設定(幾欄、幾列、位置)
plt.bar(x + width/2, df1["B"], width, color="#3498DB")