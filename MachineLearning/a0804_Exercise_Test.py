import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model
import matplotlib.pyplot as plt

# 建立 乳房癌資料集
breast_cancer = datasets.load_breast_cancer()
X = pd.DataFrame(breast_cancer.data,columns=breast_cancer.feature_names) # 解釋變數:乳房癌資料集
y = pd.DataFrame(breast_cancer.target, columns=["target"]) # 應變數
# y["target"] = np.where(1,"惡性","良性") #測試
# print(X)
# print(y)


logistict = linear_model.LogisticRegression(max_iter=4000)
logistict.fit(X,y)
# print("迴歸係數:",logistict.coef_) # 迴歸係數
# print("截距:",logistict.intercept_) # 截距

print("#1 混淆矩陣")
preds = logistict.predict(X)
coef = logistict.coef_.T
print(coef)
print(pd.crosstab(y["target"], preds))
print(logistict.score(X, y))



df = pd.DataFrame([0]*30)
df.index = breast_cancer.feature_names
print(df) # 空的DataFrame

for i in range(1,31):
    df.iloc[i-1] = coef[i-1]

df.sort_values(by=0,inplace=True,ascending=False)
print(df)


nameHead = df[:5].index
print(nameHead)
x2 = X[nameHead]
print(x2)
logistict = linear_model.LogisticRegression(max_iter=4000)
logistict.fit(x2,y)

print("#2 混淆矩陣")
preds = logistict.predict(x2)
print(pd.crosstab(y["target"], preds))
print(logistict.score(x2, y))

