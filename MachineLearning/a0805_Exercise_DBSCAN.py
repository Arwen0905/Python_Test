import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn import neighbors
from sklearn import cluster
from sklearn import tree
import matplotlib.pyplot as plt
import sklearn.metrics as sm

url = "2019_World Happiness Report.csv"
df = pd.read_csv(url)
score = pd.DataFrame(df["Score"]).astype(int)

# 建立 自變數資料集
df.index = df['Country or region'] # 將國家名設為索引
df = df.drop(["Country or region"],axis=1) # 將國家欄位與資料刪除
X = pd.DataFrame(df[["GDP per capita",
                     "Social support",
                     "Healthy life expectancy",
                     "Freedom to make life choices",
                     "Generosity",
                     "Perceptions of corruption",]]) # 應變數

y = score["Score"]
for v,i in enumerate(y):
    if i == 2:
        y[v] = 0
    if i == 3:
        y[v] = 0
    if i == 4:
        y[v] = 1
    if i == 5:
        y[v] = 2
    if i == 6:
        y[v] = 3
    if i == 7:
        y[v] = 4

# =========================================================================
# 請求出 MSE(平均誤差) 及 R-squared(R係數)
lr = LinearRegression() # 產生物件
lr.fit(X, y) # 建立模型
pred_train = lr.predict(X) # 預測 訓練結果

# 計算 平均誤差 =  觀察值(應變數) - 預測值 **2
MSE_train = np.mean((y - pred_train)**2) # 測量迴歸線距離(誤差值)，平方和再計算平均值
print("\n#1【以下排除3個標籤(國家名稱、幸福排名、幸福分數)】分析")
print("#1 完整資料的 MSE: %12.4f (越小越好)" %MSE_train) # 平均誤差值:越小越好
print("#1 完整資料的 R-squared: %6.4f (接近1越好)" %lr.score(X, y)) # 越接近1.0越有解釋能力

print("="*50)
# =========================================================================


logistict = linear_model.LogisticRegression(max_iter=2000) #建立物件
logistict.fit(X,y) # 建立模型"邏輯回歸"
preds = logistict.predict(X) # 預測值

print("#2 混淆矩陣:")
print(pd.crosstab(y, preds)) # 混淆矩陣
print("#2 邏輯迴歸 準確率:")
print(logistict.score(X, y)) # 準確率

print("="*50)
# =========================================================================

print("#2 決策樹 準確率:")
dtree = tree.DecisionTreeClassifier(max_depth = 3)
dtree.fit(X,y)
print(dtree.score(X, y))

print("="*50)
# =========================================================================

print("#2 KNN 準確率:")
k=3
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
knn_preds = knn.predict(X)
print(knn.score(X,y))

print("="*50)
print("\n上述結論:\n KNN > 決策樹 >邏輯迴歸")
print("="*50)
# =========================================================================

print("\n#3【原始資料(分群結果)】分析")
k=5
kmeans = cluster.KMeans(n_clusters=k, random_state=12)
kmeans.fit(X)
wine_preds = kmeans.labels_
# print("分群結果",wine_preds)
# print("實際結果",y)
print("混淆矩陣:\n",sm.confusion_matrix(y, wine_preds))
print("分群結果的準確率:",sm.accuracy_score(y, wine_preds))

# 修正分群標籤錯誤 (依情況使用此功能)
wine_preds = np.choose(kmeans.labels_,[2,4,1,3,0]).astype(np.int64)
print("修正! 分群結果的準確率:",sm.accuracy_score(y, wine_preds))

# 跑圖
#3 分群結果 - 散佈圖
colmap = np.array(["r","g","y","b","c"])
plt.scatter(X["GDP per capita"],X["Social support"], color=colmap[wine_preds])
plt.show()

#3 真實結果(對比用) - 散佈圖
colmap = np.array(["r","g","y","b","c"])
plt.scatter(X["GDP per capita"],X["Social support"], color=colmap[y])
plt.show()

print("="*50)
# ==================================================================

print("\n#4【分群演算法 設定條件:分成5群】分析")
from sklearn.cluster import DBSCAN
from sklearn import cluster
clustering = DBSCAN(eps=0.2, min_samples=3)
clustering.fit(X)
Y_pred = clustering.labels_
print(Y_pred)

colmap = np.array(["r","g","y","b","c"])
plt.scatter(X["GDP per capita"],X["Social support"], color=colmap[Y_pred])
plt.show()
print("\n條件:eps=0.2, min_samples=3 可以分成5群")
