import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mobile Reviews Sentiment.csv")
count=df.groupby("sentiment")['review_id'].count()
sentiment=count.index
plt.pie(count,labels=sentiment)
plt.title("distribution of reviews by sentiment")
plt.show()