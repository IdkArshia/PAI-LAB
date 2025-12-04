import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
data={
    'height':[150,155,160,165,170,175,180],
    'weight':[50,55,60,63,68,72,75]
}
df=pd.DataFrame(data)
X=df[['height']]
Y=df['weight']
model=LinearRegression()
model.fit(X,Y)
Y_172=model.predict([[172]])
print("Predicted weight for height 172 cm:", Y_172[0])
Y_pred=model.predict(X)
plt.scatter(X, Y)
plt.plot(X, Y_pred, linestyle='--')
plt.show()
residuals=Y-Y_pred
print('residuals mean: ',residuals.mean())
print('linear regression is reasonable' if abs(residuals.mean())<1e-10 else 'linear regression is not reasonable')