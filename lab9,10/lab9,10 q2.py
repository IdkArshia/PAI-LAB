import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
data = {
    "ScreenOnTime": [2, 4, 5, 3, 6, 7, 8, 2, 5, 6],
    "BatteryLife":  [12, 10, 9, 11, 8, 7, 6, 12, 9, 8]
}
df=pd.DataFrame(data)
X = df[['ScreenOnTime']]
y = df['BatteryLife']

lr = LinearRegression()
lr.fit(X, y)
y_pred = lr.predict(X)
print("Coefficient:", lr.coef_[0])
print("Intercept:", lr.intercept_)
print("R^2:", r2_score(y, y_pred))

from scipy.stats import pearsonr
corr, pval = pearsonr(df['ScreenOnTime'], df['BatteryLife'])
if corr < 0:
    print("There is a negative correlation between Screen On Time and Battery Life.")
if pval < 0.05:
    print("The correlation is statistically significant.")
