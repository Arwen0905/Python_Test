#=============================================================================
#1 KNN模型正確率（K = 50）
#=============================================================================
from sklearn import datasets
from sklearn import neighbors
from sklearn import linear_model
from sklearn import tree
from sklearn.model_selection import train_test_split as tts
import pandas as pd

iris = datasets.load_iris()

x = pd.DataFrame(iris.data, columns = iris.feature_names)
target = pd.DataFrame(iris.target, columns = ["target"])
y = target["target"]
k = 50

knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(x, y)

pred = knn.predict(x)
print("【KNN模型 - 混淆矩陣】")
print(pd.crosstab(iris.target, pred))
print()

c1 = (knn.score(x, y))*100

print("將全部資料使用 KNN 建立模型，有 {:f}％ 的正確率".format(c1))
print()

#邏輯迴歸 =====================================================================
logistic = linear_model.LogisticRegression(max_iter = 5000)
logistic.fit(x, y)

predl = logistic.predict(x)
print("【邏輯迴歸 - 混淆矩陣】")
print(pd.crosstab(iris.target, predl))
print()

c2 = (logistic.score(x, y))*100

print("將全部資料使用邏輯迴歸建立模型，有 {:f}％ 的正確率".format(c2))
print()

#決策樹 =======================================================================
dtree = tree.DecisionTreeClassifier(max_depth = 3)
dtree.fit(x, y)

predt = dtree.predict(x)
print("【決策樹 - 混淆矩陣】")
print(pd.crosstab(iris.target, predt))
print()

c3 = (dtree.score(x, y))*100

print("將全部資料使用決策樹建立模型，有 {:f}％ 的正確率".format(c3))
print()

#模型比較 =====================================================================
print("#1\n正確率：")
print("邏輯迴歸（{:f}％）= 決策樹（{:f}％）> KNN（{:f}％）".format(c3, c2, c1))
print("邏輯迴歸和決策樹模型有相同的正確率，皆比KNN為佳")
print()


#=============================================================================
#2 訓練資料集及測試資料集比率為7:3，找出最適當的K值
#=============================================================================

def KNN(k):
    x = pd.DataFrame(iris.data, columns = iris.feature_names)
    target = pd.DataFrame(iris.target, columns = ["target"])
    y = target["target"]
    K = k
    
    xtrain, xtest, ytrain, ytest = tts(x, y, test_size = 0.4, random_state = 50)
    
    knn = neighbors.KNeighborsClassifier(n_neighbors=K)
    knn.fit(xtrain, ytrain)
    
    c = (knn.score(xtest, ytest))*100
    
    return c
   
c_min = 100
c_max = 0
k_best = 1
k_worst = 1

for k in range(1, 91):  #因為測試資料集比例是0.6，所以K值最高只能是 150*0.6=90
    c = KNN(k)
    #print(c)
    if c > c_max:
        c_max = c
        k_best = k
    elif c < c_min:
        c_min = c
        k_worst = k

print("#2\n將資料分割成 3:2，並使用 KNN 建立模型...")
print("當K值為 {:d} 時，有最高的正確率：{:f}％ ".format(k_best, c_max))
print("當K值為 {:d} 時，有最低的正確率：{:f}％ ".format(k_worst, c_min))
