# 載入 numpy 模組
import numpy as np
# 載入 pandas 模組縮
import pandas as pd

# 讀入 read.csv 檔案
df = np.array(pd.read_csv("read.csv"))

# 判斷資料型態
# print('資料型態：%s' % df.dtypes)
print('資料型態：%s' % type(df))
# 計算平均數
print('平均值：%.2f' % np.mean(df))
# 計算中位數
print('中位數：%.2f' % np.median(df))
# 計算標準差
print('標準差：%.2f' % np.std(df))
# 計算變異數
print('變異數：%.2f' % np.var(df))
# 計算極差值
print('極差值：%.2f' % np.ptp(df))
