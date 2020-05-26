# 1. 題目說明:
# 請開啟PYD109.py檔案，依下列題意進行作答，
# 計算正五邊形之面積，使輸出值符合題意要求。
# 作答完成請另存新檔為PYA109.py再進行評分。

# 2. 設計說明：
# 請撰寫一程式，讓使用者輸入一個正數s，
# 代表正五邊形之邊長，計算並輸出此正五邊形之面積（Area）。

# 提示1：建議使用import math模組的math.pow及math.tan
# 提示2：正五邊形面積的公式： Area=(5∗s2)/(4∗tan(pi/5))

# 提示3：輸出浮點數到小數點後第四位。

# 3. 輸入輸出：
# 輸入說明
# 正數s

# 輸出說明
# 正五邊形面積

# 輸入輸出範例
# 範例輸入
# 5
# 範例輸出
# Area = 43.0119
# TODO
import math
# s = 5
s = eval(input())
pi = math.pi
Area = (5*math.pow(s,2))/(4*math.tan(pi/5))
print('Area = %.4f' % Area)
# Area=(5∗s2)/(4∗tan(pi/5))
  # 主要是 └ s2 的運算方式，使用math.pow(s,2)
"""
Area = _
"""