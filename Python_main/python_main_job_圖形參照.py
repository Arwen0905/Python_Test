import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ['Microsoft JhengHei']
    
file1 = '失業率－婚姻狀況別.csv'
file1 = '年齡組別失業率.csv'
file1 = '人力資源調查失業率.csv'
with open(file1,encoding="utf-8") as f:
    df1 = df = pd.read_csv(f)
    df = df.rename(columns={"項目別_Iterm":"日期"}) #重新命名
    # for i in df1: print(i) #檢查類別

    df1 = df1[["男_Male","女_Female"]] #取需要資料
    df1.index = df["日期"]
    print(df1)
 
width = 0.35
Men = df1["男_Male"].iloc[:10]
Women = df1["女_Female"].iloc[:10]
date = df["日期"].iloc[:10]
x = np.arange(len(date))
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Men, width, label='男性失業率')
rects2 = ax.bar(x + width/2, Women, width, label='女性失業率')

ax.set_ylabel("失業率")
ax.set_title('失業率 - 男女比例')
ax.set_xticks(x)
ax.set_xticklabels(date)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)