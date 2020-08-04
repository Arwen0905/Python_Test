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
print(X)
print(y)


logistict = linear_model.LogisticRegression()
logistict.fit(X,y)
# print("迴歸係數:",logistict.coef_) # 迴歸係數
# print("截距:",logistict.intercept_) # 截距

print("#1 混淆矩陣")
preds = logistict.predict(X)
print(pd.crosstab(y["target"], preds))
print(logistict.score(X, y))


X_new = X.iloc[:,2:7]
logistict = linear_model.LogisticRegression()
logistict.fit(X_new,y)

print("#2 混淆矩陣")
preds = logistict.predict(X_new)
print(pd.crosstab(y["target"], preds))
print(logistict.score(X_new, y))

dic = {};
dic.setdefault("QQ")
# for i in X.columns.values:
#     print(i)
#     # print(X[i])
#     X_new = X[i]
#     logistict = linear_model.LogisticRegression()
#     logistict.fit(X_new,y)
#     ans = logistict.score(X_new, y)
#     dic.setdefault(i) = ans

print(dic)




