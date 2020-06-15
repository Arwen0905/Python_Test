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
print(iris)
s = iris.describe()
print(s)
# step3
# url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url, names=names)
print(dataset.describe())
dataset.hist()
