import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

data = {
    'ram': [8, 16, 8, 32, 16, 8, 4, 16, 32, 8],       # GB
    'weight': [1.5, 2.0, 1.8, 2.5, 2.2, 1.6, 1.4, 2.1, 2.8, 1.7],  # kg
    'cpu_freq': [2.5, 3.2, 2.8, 3.6, 3.0, 2.4, 2.0, 3.1, 3.8, 2.6],  # GHz
    'storage': [256, 512, 256, 1024, 512, 256, 128, 512, 1024, 256],  # GB
    'price': [700, 1200, 750, 2000, 1300, 720, 500, 1250, 2200, 680]  # USD
}

df = pd.DataFrame(data)

features = ['ram','weight','cpu_freq','storage']
target = 'price'
df = df.dropna()

X = df[['ram','weight','cpu_freq','storage']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state=42)

lr_un = LinearRegression()
lr_un.fit(X_train, y_train)
pred_un = lr_un.predict(X_test)
print("Unscaled R2:", r2_score(y_test, pred_un), "RMSE:", np.sqrt(mean_squared_error(y_test, pred_un)))

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
lr_scaled = LinearRegression()
lr_scaled.fit(X_train_scaled, y_train)
pred_scaled = lr_scaled.predict(X_test_scaled)
print("Scaled R2:", r2_score(y_test, pred_scaled), "RMSE:", np.sqrt(mean_squared_error(y_test, pred_scaled)))

coef_impacts = sorted(zip(features, np.abs(lr_scaled.coef_)), key=lambda x: -x[1])
print("Feature importances (scaled):", coef_impacts)
