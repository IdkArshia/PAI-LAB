import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

years = np.array([1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7])
salary = np.array([39.0,46.0,47.0,52.0,56.0,64.0,65.0,67.0,68.0,70.0])

X = years
Y = salary
n = len(X)
x_mean = X.mean()
y_mean = Y.mean()

b1 = np.sum((X - x_mean) * (Y - y_mean)) / np.sum((X - x_mean)**2)
b0 = y_mean - b1 * x_mean
print("Scratch OLS intercept:", b0)
print("Scratch OLS slope:", b1)

pred_45_scratch = b0 + b1 * 4.5
print("Predicted salary (thousands) at 4.5 years (scratch):", pred_45_scratch)

y_pred_scratch = b0 + b1 * X
ss_res = np.sum((Y - y_pred_scratch)**2)
ss_tot = np.sum((Y - y_mean)**2)
r2_scratch = 1 - ss_res / ss_tot
print("R^2 (scratch):", r2_scratch)

data={
    "years":[1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7],
    "salary" : [39.0,46.0,47.0,52.0,56.0,64.0,65.0,67.0,68.0,70.0]
}
df = pd.DataFrame(data)
X=df[["years"]]
Y=df["salary"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
lr = LinearRegression()

lr.fit(X_train,Y_train)
print("sklearn intercept:", lr.intercept_)
print("sklearn slope:", lr.coef_[0])

Y_pred= lr.predict([[4.5]])
print("Predicted salary (thousands) at 4.5 years (sklearn):", Y_pred)
print("R^2 (sklearn):", r2_score(Y_test,lr.predict(X_test)))

