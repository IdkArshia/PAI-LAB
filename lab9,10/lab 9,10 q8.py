import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

data = {
    'OverallQual': [7, 6, 8, 5, 9, 4, 7, 8, 6, 5],
    'GrLivArea': [1710, 1262, 1786, 1717, 2198, 1362, 1694, 2090, 1774, 1077],
    'GarageCars': [2, 2, 2, 1, 3, 1, 2, 3, 2, 1],
    'YearBuilt': [2003, 1976, 2001, 1915, 2000, 1993, 2004, 1973, 1931, 1939],
    'SalePrice': [208500, 181500, 223500, 140000, 250000, 130000, 215000, 240000, 178000, 120000]
}

df = pd.DataFrame(data)
features = ['OverallQual','GrLivArea','GarageCars','YearBuilt']
dff = df[features + ['SalePrice']].dropna()

X = dff[features]
y = dff['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)
lr = LinearRegression(); lr.fit(X_train, y_train)
pred = lr.predict(X_test)

print("Coefficients:")
for feat, coef in zip(features, lr.coef_):
    print(f"  {feat}: {coef:.2f}")
print("Intercept:", lr.intercept_)
print("R^2:", r2_score(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
impacts = sorted(zip(features, np.abs(lr.coef_)), key=lambda x: -x[1])
print("Most impactful feature (by abs coef):", impacts[0])