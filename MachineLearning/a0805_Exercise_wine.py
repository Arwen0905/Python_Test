import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, linear_model
from sklearn import neighbors
from sklearn import cluster
from sklearn import tree
import matplotlib.pyplot as plt
import sklearn.metrics as sm

# 建立 紅酒 資料集
wine = datasets.load_wine() # 引入資料集
X = pd.DataFrame(wine.data,columns=wine.feature_names) # 自變數
y = pd.DataFrame(wine.target, columns=["target"]) # 應變數
# y = y["target"] # 必須轉成一維
y = wine.target


print("\n#1【原始資料(分群結果)】分析")
k=3
kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
wine_preds = kmeans.labels_
# print("分群結果",wine_preds)
# print("實際結果",y)
print("混淆矩陣:\n",sm.confusion_matrix(y, wine_preds))
print("分群結果的準確率:",sm.accuracy_score(y, wine_preds))

# 修正分群標籤錯誤 (依情況使用此功能)
# wine_preds = np.choose(kmeans.labels_,[0,1,2]).astype(np.int64)

# 跑圖
#1 分群結果 - 散佈圖
colmap = np.array(["r","g","y"])
plt.scatter(X["flavanoids"],X["proline"], color=colmap[wine_preds])
plt.show()

#1 真實結果(對比用) - 散佈圖
colmap = np.array(["r","g","y"])
plt.scatter(X["flavanoids"],X["proline"], color=colmap[y])
plt.show()

print("="*50)
# ==================================================================
print("\n#2【準確率(前5高標籤)】分析")
df = pd.DataFrame([0]*13, columns=["SingleAccuracy"]) # 建立二維陣列，預設出30個資料欄位
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

logistict = linear_model.LogisticRegression(max_iter=2000) #建立物件
logistict.fit(X2,y) # 建立模型"邏輯回歸"
preds = logistict.predict(X2) # 預測值

print("#2 混淆矩陣:")
print(pd.crosstab(y, preds)) # 混淆矩陣
print("#2 邏輯迴歸 準確率:")
print(logistict.score(X2, y)) # 準確率

# print(f"下列為 準確率(前5高標籤):\n{X_tag.values}")

print("="*50)
# ==================================================================
print("#3 KNN 準確率:")
k=3
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
knn_preds = knn.predict(X)
print(knn.score(X,y))

print("="*50)
# ==================================================================
print("#4 決策樹 準確率:")
dtree = tree.DecisionTreeClassifier(max_depth = 3)
dtree.fit(X,y)
print(dtree.score(X, y))
print("="*50)
# ==================================================================
print("結論:\n邏輯迴歸(僅5個標籤) > 決策樹 > KNN > 分群(K-Means)")

