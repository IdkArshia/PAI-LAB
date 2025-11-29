import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mobile Reviews Sentiment.csv")
avg=df.groupby("brand")['price_usd'].mean()
brand=avg.index
plt.bar(brand,avg)
plt.xlabel("brands")
plt.ylabel("average prices(USD)")
plt.title("average prices for brands")
plt.show()