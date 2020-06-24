# step1
# 下載資料集並儲存為csv檔
import requests
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
try:
    htmlFile = requests.get(url)
    print('下載成功')
except Exception as err:
    print('下載失敗')
fn = 'iris.csv'
with open(fn,'wb') as fileObj:
    for diskstorage in htmlFile.iter_content(10240):
        size = fileObj.write(diskstorage)
# step2
# 讀取csv檔並轉換為DataFrame
# count:數量，mean:平均值，std:標準差，min:最小值，max:最大值
# **%:分位數，50%:二分位，
import pandas as pd
colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv',names=colName)
print('資料集長度: ',len(iris))
# print(iris)
s = iris.describe()
# print(s)
# step3
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url, names=names)
# print(dataset.describe())
# dataset.plot(x="sepal-length",y="sepal-width",kind="scatter")
# dataset.plot(kind="kde")
# dataset.plot(kind="box",subplots=True,layout=(2,2),sharex=True,sharey=True)

#散佈圖、密度圖
dataset.plot(kind="box",layout=(1,4),subplots=True)

# 盒鬚圖
import matplotlib.pyplot as plt
colName = ["sepal_len","sepal_wd","patal_len","petal_wd","species"]
iris = pd.read_csv('iris.csv',names=colName)
plt.plot(iris["sepal_len"],iris["sepal_wd"],"*",color="g")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Sepal length and width anslysis")
# plt.show()

# 值條圖 → 三種品種各自四個特徵值
iris_mean = iris.groupby("species",as_index=False).mean()
iris_mean.plot(kind="bar")
plt.xticks(iris_mean.index,iris_mean["species"],rotation=0)
# plt.show()
print("===============================================")
iris["species"] = iris["species"].apply(lambda x: x.replace("Iris-","QQ"))
# 堆疊圖:開啟
# iris_mean.plot(kind="bar")
# iris_mean.plot(kind="bar",stacked=True)
# 橫條圖:開啟
iris_mean.plot(kind="barh",stacked=True)
plt.xticks(iris_mean.index,iris_mean['species'], rotation=0)
plt.show()
print(dataset.describe(),"檔尾")


from sklearn.datasets import load_iris
import numpy as np
hua = load_iris()
# 獲得花瓣的長跟寬
x = [n[0] for n in hua.data]
y = [n[1] for n in hua.data]
# 把list轉換成陣列，並且執行 reshape重新調整資料大小
x = np.array(x).reshape(len(x),1)
y = np.array(y).reshape(len(y),1)
from sklearn.linear_model import LinearRegression #線性回歸
# 將LR的方法設定變數
clf = LinearRegression()
# fit將(x,y)資料帶入機器學習??? 訓練??????
clf.fit(x,y)
# predict(x) 預測資料
pre = clf.predict(x)
# s=大小
plt.scatter(x,y,s=50)
# r:紅色 -:實線 線寬
plt.plot(x,pre,"r-",linewidth=4)
ans=0
s=0
for idx,m in enumerate(x):
    plt.plot([m,m],[y[idx],pre[idx]],'r-')
    ans+=m
    s=idx
    print(m[0])
print(clf.predict([[5.0]]))
print(ans,"總數")
print(s,"數量")
print(ans/idx,"平均")

