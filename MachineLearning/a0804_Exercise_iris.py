import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import tree
from sklearn import neighbors

iris = datasets.load_iris()
X = pd.DataFrame(iris.data,columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=["target"])
y = y["target"] # 需轉成一維才不會洗頻

print("【KNN】")
k = 50
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
print("KNN - k值為 50，準確率: %.4f\n" %knn.score(X, y))


print("【決策樹分類】")
dtree = tree.DecisionTreeClassifier(max_depth = 3)
dtree.fit(X,y)
print("決策樹分類 - 準確率: %.4f\n" %dtree.score(X, y))


print("【邏輯回歸】")
logistict = linear_model.LogisticRegression(max_iter=1000)
logistict.fit(X,y)
print("邏輯回歸 - 準確率: %.4f" %logistict.score(X, y))
print()
print("上述比較結果:\n邏輯回歸、決策樹 > KNN")


print("\n【KNN】分割資料3:2，取出最高、最低的k值與結果")
max_ans = 0
min_ans = 1
min_k = 100
max_k = 0

for k in range(1,91):
    
    XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.40,random_state=50)
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(XTrain, yTrain)
    ans = (knn.score(XTest,yTest))
    
    if ans > max_ans:
        max_ans = ans
        max_k = k
    elif ans < min_ans:
        min_ans = ans
        min_k = k

print("\nKNN - k值為 %d，準確率最高: %.4f" %(max_k,max_ans))
print("\nKNN - k值為 %d，準確率最低: %.4f" %(min_k,min_ans))





