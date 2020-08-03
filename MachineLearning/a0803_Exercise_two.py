import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["Microsoft Jhenghei"] #中文設定

diabetes = datasets.load_diabetes()
print(diabetes.keys())
print(diabetes.DESCR)


X = pd.DataFrame(diabetes.data,columns=diabetes.feature_names)
print(X.head) # 取得data，並轉成二維資料型態 (自變數、解釋變數)
y = pd.DataFrame(diabetes.target, columns=["target"])
print(y) # 取得實際一年病患定量指標 的資料，並轉成二維資料型態 
lr = LinearRegression() # 產生物件
lr.fit(X,y) # 模型建立(自變數、應變數)
print("迴歸係數:",lr.coef_) # 迴歸係數
print("截距:",lr.intercept_) # 截距
predicted_target = lr.predict(X) # predict預測函數
plt.scatter(y,predicted_target) # 繪圖 - 散佈圖
plt.xlabel("實際一年後的定量指標",fontsize=12)
plt.ylabel("預\n測\n一\n年\n後\n的\n定\n量\n指\n標",rotation=0,ha="right",fontsize=12)
plt.show()
print("="*50)

df_X = X[["age","sex","bmi","bp"]] # 新增自變數資料
lr2 = LinearRegression() # 產生物件
lr2.fit(df_X,y) # 模型建立(自變數、應變數)

print("迴歸係數:",lr2.coef_) # 迴歸係數
print("截距:",lr2.intercept_) # 截距

predicted_target2 = lr2.predict(df_X) # predict預測函數
print(predicted_target2) # 以["age","sex","bmi","bp"]預測值
plt.scatter(y,predicted_target2) # 繪圖 - 散佈圖
plt.xlabel("實際一年後的定量指標",fontsize=12)
plt.ylabel("預\n測\n一\n年\n後\n的\n定\n量\n指\n標",rotation=0,ha="right",fontsize=12)
plt.show()

