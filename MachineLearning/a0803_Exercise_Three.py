import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 建立 糖尿病資料集
diabetes = datasets.load_diabetes()
X = pd.DataFrame(diabetes.data,columns=diabetes.feature_names) # 解釋變數:糖尿病資料集
y = pd.DataFrame(diabetes.target, columns=["target"]) # 應變數:實際病例
# 1 =========================================================================
# 不分割資料集，請求出 MSE(平均誤差) 及 R-squared(R係數)

lr = LinearRegression() # 產生物件
lr.fit(X, y) # 以 糖尿病的完整資料 與 實際病例數 建立模型
pred_train = lr.predict(X) # 預測 訓練結果 (不切割資料)

# 計算 平均誤差 =  觀察值(應變數) - 預測值 **2
MSE_train = np.mean((y - pred_train)**2) # 測量迴歸線距離(誤差值)，平方和再計算平均值
print("\n#1")
print("完整資料的 MSE: %12.4f" %MSE_train) # 平均誤差值:越小越好
print("完整資料的 R-squared: %6.4f" %lr.score(X, y)) # R係數:越接近1.0越有解釋能力

# 2 =========================================================================
# 分割 訓練資料集 及 測試資料集的比例為 3:1，亂數種子為100，請求出 MSE 及 R^2
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25,random_state=100)
lr = LinearRegression() # 產生物件
lr.fit(XTrain, yTrain) # 以 訓練資料(自變數,應變數) 建立模型
pred_test = lr.predict(XTest) # 模型預測: 分割出來的 0.25 測試資料集
MSE_test = np.mean((yTest - pred_test)**2) # 用測試資料(減)預測資料 計算出 平均誤差值

print("\n#2")
print("測試資料的 MSE: %12.4f" %MSE_test) # 平均誤差值:越小越好
print("測試資料的 R-squared: %6.4f" %lr.score(XTest, yTest)) # R係數:越接近1.0越有解釋能力

# 3 =========================================================================
# 分割 訓練資料集 及 測試資料集的比例為 3:1，亂數種子為100，請求出 MSE 及 R^2
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.20,random_state=100)
lr = LinearRegression() # 產生物件
lr.fit(XTrain, yTrain) # 以 訓練資料(自變數,應變數) 建立模型
pred_test = lr.predict(XTest) # 模型預測: 分割出來的 0.20 測試資料集
MSE_test = np.mean((yTest - pred_test)**2) # 用測試資料(減)預測資料 計算出 平均誤差值

print("\n#3")
print("測試資料的 MSE: %12.4f" %MSE_test) # 平均誤差值:越小越好
print("測試資料的 R-squared: %6.4f" %lr.score(XTest, yTest)) # R係數:越接近1.0越有解釋能力

print("\n比較結果:")
print("平均誤差比較(越小越好): #3【勝出】 < #2 < #1")
print("決定係數比較(越大越好): #2【勝出】 > #1 > #3")
print("\n結論:\n應採用 #2 其次 #3 模型較適合")
