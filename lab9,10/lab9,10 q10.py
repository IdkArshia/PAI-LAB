import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

data = {
    'overall': [85, 78, 90, 82, 88, 76, 81, 84, 79, 91],
    'potential': [90, 80, 92, 85, 89, 78, 83, 86, 81, 93],
    'age': [25, 22, 28, 24, 26, 21, 23, 25, 22, 29],
    'international_reputation': [4, 3, 5, 3, 4, 2, 3, 4, 3, 5],
    'value_eur': [75000000, 42000000, 90000000, 50000000, 82000000, 35000000, 48000000, 68000000, 40000000, 95000000]
}

df = pd.DataFrame(data)

selected = ['overall','potential','age','international_reputation','value_eur']  
df = df.dropna()

X = df[['overall','potential','age','international_reputation']]
y = df['value_eur']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=42)
lr = LinearRegression(); lr.fit(X_train, y_train)
pred = lr.predict(X_test)

print("Coefficients:")
for f,c in zip(X.columns, lr.coef_):
    print(f"  {f}: {c:.3f}")
print("Intercept:", lr.intercept_)
print("R^2:", r2_score(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))

X2 = df[['overall','age','international_reputation']]
Y2=df['value_eur']
X2_train, X2_test,Y2_train,Y2_test = train_test_split(X2,Y2, test_size=0.25, random_state=42)
lr2 = LinearRegression(); lr2.fit(X2_train, Y2_train)
pred2 = lr2.predict(X2_test)
print("R^2 without potential:", r2_score(Y2_test, pred2))
