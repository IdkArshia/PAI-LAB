import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mobile Reviews Sentiment.csv")
# avg=df.groupby("brand")['rating'].mean()
# brand=avg.index
plt.bar(df['sentiment'],df["rating"])
plt.xlabel("brands")
plt.ylabel("rating")
plt.title("sentiment vs rating")
plt.show()