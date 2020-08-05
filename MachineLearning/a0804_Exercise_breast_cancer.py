import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model

# 建立 乳房癌 資料集
breast_cancer = datasets.load_breast_cancer() # 引入資料集
X = pd.DataFrame(breast_cancer.data,columns=breast_cancer.feature_names) # 原始資料:自變數
y = pd.DataFrame(breast_cancer.target, columns=["target"]) # 原始資料:應變數
y = y["target"] # 必須轉成一維


logistict = linear_model.LogisticRegression(max_iter=3000) # 建立物件
logistict.fit(X,y) # 建立模型
# print("迴歸係數:",logistict.coef_) # 迴歸係數
# print("截距:",logistict.intercept_) # 截距
print("\n【原始資料(30項標籤)】")
print("#1 混淆矩陣")
preds = logistict.predict(X)
print(pd.crosstab(y, preds))
print("#1 準確率")
print(logistict.score(X, y))

print("="*50)
# =========================================================================================

print("\n【準確率(前5高標籤)】")
df = pd.DataFrame([0]*30, columns=["SingleAccuracy"]) # 建立二維陣列，預設出30個資料欄位
df.index = X.columns.values # 再將30個標籤名字 設定給 df索引值

# 將每個標籤單獨進行 準確性 運算並 賦予給 df二維陣列
for v,i in enumerate(X.columns.values): # v(序列值) i(標稱名稱)
    X_single = pd.DataFrame(X[i]) # 依序 取得每一個標籤 ( X_single必須轉二維 )
    
    logistict = linear_model.LogisticRegression() # 建立物件
    logistict.fit(X_single,y) # 建立模型"邏輯回歸"
    
    df.iloc[v] = logistict.score(X_single, y) # 依序算出的 準確率 設定給 df並對應其標籤名稱
    
# 進行排序，取出 準確率 前五名標籤
df = df.sort_values(by="SingleAccuracy", ascending=False) # 排序

X_tag = df.head().index # 取得前五筆"標籤名稱"
X2 = X[X_tag] # 再從原始資料撈出這五筆的"內容"

logistict = linear_model.LogisticRegression() #建立物件
logistict.fit(X2,y) # 建立模型"邏輯回歸"
preds = logistict.predict(X2) # 預測值

print("#2 混淆矩陣:")
print(pd.crosstab(y, preds)) # 混淆矩陣
print("#2 準確率:")
print(logistict.score(X2, y)) # 準確率

print("\n上述結論:採用了準確率(前5高標籤)，結果僅差距原始資料(30個標籤) 0.01406 %")
print(f"下列為 準確率(前5高標籤):\n{X_tag.values}")
print("="*50)
# =========================================================================================

print("\n【將全部資料分割，比率分別為 7:3】")
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.30,random_state=10)
logistict = linear_model.LogisticRegression(max_iter=3000)
logistict.fit(XTrain,yTrain)
preds = logistict.predict(XTest) # 預測值

print("#3 混淆矩陣:")
print(pd.crosstab(yTest, preds))
print("#3 準確率:")
print(logistict.score(XTest,yTest))

print("="*50)
# =========================================================================================

print("\n【查找 test_size 正確率最高/最低的值】")
max_n = 0
min_n = 1
max_i = 0
min_i = 0
temp_i = 0
for i in range(1,100):
    temp_i = i/100
    
    XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size= temp_i , random_state=10)
    logistict = linear_model.LogisticRegression(max_iter=4000)
    logistict.fit(XTrain,yTrain)
    
    ans = logistict.score(XTest,yTest)
    if ans >= max_n:
        max_n = ans
        max_i = temp_i
    elif ans < min_n:
        min_n = ans
        min_i = temp_i
    
print("#4 準確率:")
print("最高準確率為:%.4f，其test_size值為:%.2f" %(max_n,max_i))
print("最低準確率為:%.4f，其test_size值為:%.2f" %(min_n,min_i))
