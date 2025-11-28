import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mobile Reviews Sentiment.csv")
avg=df.groupby("brand")['rating'].mean()
brand=avg.index
plt.bar(brand,avg)
plt.xlabel("brands")
plt.ylabel("average rating")
plt.title("average ratings for brands")
plt.show()