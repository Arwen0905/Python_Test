import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Height_cm = np.array([147.9,163.5,159.8,155.1,163.3,
               158.7,172.0,161.2,153.9,161.6])
Weight_kg = np.array([41.7,60.2,47.0,53.2,48.3,55.2,
               58.5,49.0,46.7,52.5])
X = pd.DataFrame(Height_cm,columns=["cm"])
y = pd.DataFrame(Weight_kg,columns=["kg"])

lm = LinearRegression()
lm.fit(X,y)
print("迴歸係數:",lm.coef_)
print("截距:",lm.intercept_)

new_Height = pd.DataFrame(np.array([155,165,180]))
predicted_Weight = lm.predict(new_Height)
print(predicted_Weight)

plt.scatter(Height_cm,Weight_kg) #繪圖
regression_Weight = lm.predict(X)
plt.plot(Height_cm,regression_Weight,color="blue")
plt.plot(new_Height,predicted_Weight,color="red",marker="o",markersize=10)
plt.show()
