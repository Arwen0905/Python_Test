import matplotlib.pyplot as plt
# 設定字型、樣式、大小
font = {'family' : 'Microsoft JhengHei','weight' : 'bold','size'  : '16'}
# 設定python繪圖系統的字型項目
plt.rc('font', **font) 
# 解決坐標軸的負數的負號顯示問題↓
# 設定unicode_minus=False 可解決座標軸負號問題
plt.rc('axes',unicode_minus=False)
# 外部文字
labels = ["北部","東部","南部","中部"]
#! 圖面佔比例的數值
sizes = [20,5,10,15]
# 設定顏色
colors = ["#fff555","#ff2244","#55ff55","#55aaff"]

# explode: 圖的炸裂間距 (設定圓形分離區塊的距離，以串列設定對應主資料項目)
explode = (0, 0.2, 0, 0)

# startangle: 順時鐘 (繪圖的起始角度)
# pctdistance: 字型距離 (百分比文字與圓心的距離是半徑的幾倍)
plt.pie(sizes,explode = explode, labels = labels, colors=colors,\
# labeldistance: 外部文字離心距(資料標籤與圓心的距離是半徑的幾倍)
        labeldistance = 1.2, autopct = "%3.1f%%",shadow=True,\
            startangle = 90,pctdistance=0.6) # shadow: 設定陰影
plt.axis("equal")
# 小視窗的位置
plt.legend(loc="lower right",fontsize=10)
plt.show()

# Q:圖片炸裂間距、文字位置、陰影、外部文字離心距、圓形圖擅長占比顯示
