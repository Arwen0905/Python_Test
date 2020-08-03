import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft Jhenghei"] #中文設定

diabetes = datasets.load_diabetes()
# print(diabetes.keys())
# print(diabetes.DESCR)

X = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
# print(X.head) # 取得data，並轉成二維資料型態 (自變數、解釋變數)
y = pd.DataFrame(diabetes.target, columns=["target"])
# print(y) # 取得實際一年病患定量指標 的資料，並轉成二維資料型態 
lr = LinearRegression() # 產生物件
lr.fit(X,y) # 模型建立(自變數、應變數)
# print("迴歸係數:",lr.coef_) # 迴歸係數
# print("截距:",lr.intercept_) # 截距
predicted_target = lr.predict(X) # predict預測函數
plt.scatter(y,predicted_target) # 繪圖 - 散佈圖
plt.xlabel("實際一年後的定量指標",fontsize=12)
plt.ylabel("預\n測\n一\n年\n後\n的\n定\n量\n指\n標",rotation=0,ha="right",fontsize=12)
plt.show()

# 1 =========================================================================
# 不分割資料集，請求出 MSE 及 R^2
XTrain, XTest, yTrain, yTest = train_test_split(X, y)
lr = LinearRegression() # 產生物件
lr.fit(XTrain, yTrain) # 以訓練資料建立模型
pred_train = lr.predict(XTrain)


MSE_train = np.mean((yTrain-pred_train)**2)

print("#1")
print("完整資料的 MSE:",MSE_train)
print("完整資料的 R^2:",lr.score(XTrain, yTrain))
# 2 =========================================================================
# 分割 訓練資料集 及 測試資料集的比例為 3:1，亂數種子為100，請求出 MSE 及 R^2
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33,random_state=100)

pred_train = lr.predict(XTrain)
pred_test = lr.predict(XTest)

MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
print("#2")
print("測試資料的 MSE:",MSE_test)
print("測試資料的 R^2",lr.score(XTest, yTest))
# 3 =========================================================================
# 分割 訓練資料集 及 測試資料集的比例為 3:1，亂數種子為100，請求出 MSE 及 R^2
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.25,random_state=100)

pred_train = lr.predict(XTrain)
pred_test = lr.predict(XTest)

MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
print("#3")
print("測試資料的 MSE:",MSE_test)
print("測試資料的 R^2:",lr.score(XTest, yTest))