import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mobile Reviews Sentiment.csv")
avg=df.groupby('model')[["price_usd","rating"]].mean()
avgP=df["price_usd"].mean()
avgR=df["rating"].mean()
overpriced=avg[(avg["price_usd"]>avgP)&(avg["rating"]<avgR)]
plt.scatter(avg['rating'],avg['price_usd'],label="other models", color='blue')
plt.scatter(overpriced['rating'],overpriced['price_usd'],label="overpriced models", color='red')
plt.show()
