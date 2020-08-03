
#1 - 不分割資料集
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression as LR
from sklearn.model_selection import train_test_split as tts

diabetes = datasets.load_diabetes()

x = pd.DataFrame(diabetes.data, columns = diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns = ["QM"])
y = target["QM"]

lm = LR()
lm.fit(x, y)
pred = lm.predict(x)

MSE = np.mean((y - pred)**2)
R = lm.score(x, y)

print("【#1 不分割資料集】")
print("完整資料的 MSE：", MSE)
print("完整資料的 R^2：", R)
print()


#2 - 分割比例為 3:1
x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.25, random_state = 100)

lm = LR()
lm.fit(x_train, y_train)

pred_test = lm.predict(x_test)

MSE_test = np.mean((y_test - pred_test)**2)
R_test = lm.score(x_test, y_test)

print("【#2 分割資料集 - 比例 3:1】")
print("測試資料的 MSE：", MSE_test)
print("測試資料的 R^2：", R_test)
print()


#3 - 分割比例為 4:1
x_train, x_test, y_train, y_test = tts(x, y, test_size = 0.20, random_state = 100)

lm = LR()
lm.fit(x_train, y_train)

pred_test = lm.predict(x_test)

MSE_test = np.mean((y_test - pred_test)**2)
R_test = lm.score(x_test, y_test)

print("【#3 分割資料集 - 比例 4:1】")
print("測試資料的 MSE：", MSE_test)
print("測試資料的 R^2：", R_test)
print()


#4
print("【選擇較好的模型】")
print("MSE 越小越好： #3 < #2 < #1")
print("R^2 越大越好： #2 > #1 > #3")
print()
print("ANS：#1採用了完整資料，準確性較低；綜合上述比較，#2模型的績效較佳")
