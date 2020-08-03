import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Height_cm = np.array([147.9,163.5,159.8,155.1,163.3,
               158.7,172.0,161.2,153.9,161.6])
Weight_kg = np.array([41.7,60.2,47.0,53.2,48.3,55.2,
               58.5,49.0,46.7,52.5])

X = pd.DataFrame(Height_cm,columns=["Height"])
y = pd.DataFrame(Weight_kg,columns=["Weight"])

lm = LinearRegression() # 建模
lm.fit(X,y) # 模型分析(自變數、應變數)
print("迴歸係數:",lm.coef_) # 迴歸係數
print("截距:",lm.intercept_) #截距

new_Height = pd.DataFrame(np.array([155,165,180])) # 新增資料，轉二維
predicted_Weight = lm.predict(new_Height) # predict預測函數
print(predicted_Weight) # 預測結果

plt.scatter(Height_cm,Weight_kg) # 繪圖 - 散佈圖
regression_Weight = lm.predict(X) # 繪製資料的整體長度
print(Height_cm)
print("="*50)
print(regression_Weight)
plt.plot(Height_cm,regression_Weight,color="b")
plt.plot(new_Height,predicted_Weight,color="r",marker="*",markersize=20)
plt.show()
