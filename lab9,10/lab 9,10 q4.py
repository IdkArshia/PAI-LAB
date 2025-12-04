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
print("orignal slope: ",model.coef_[0])
print("original intercept: ",model.intercept_)
print("orignal r^2:",r2_score(Y,model.predict(X)))

dataN={
    'height':[150,155,160,165,170,175,180,190],
    'weight':[50,55,60,63,68,72,75,60]
}
dfN=pd.DataFrame(dataN)
Xn=dfN[['height']]
Yn=dfN['weight']
modelN=LinearRegression()
modelN.fit(Xn,Yn)
print("new slope: ",modelN.coef_[0])
print("new intercept: ",modelN.intercept_)
print("new r^2:",r2_score(Yn,modelN.predict(Xn)))