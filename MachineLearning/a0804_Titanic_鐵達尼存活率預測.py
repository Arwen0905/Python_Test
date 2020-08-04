import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

url = "titanic.csv"
titanic = pd.read_csv(url)
print("原始資料")
print(titanic.info())
age_temp = np.nanmedian(titanic["Age"])
print(age_temp)
titanic["Age"] = np.where(titanic["Age"].isnull(),age_temp,
                          titanic["Age"])
print(titanic.info())
