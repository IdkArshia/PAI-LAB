import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Mobile Reviews Sentiment.csv")
plt.figure(figsize=(8,5))
plt.hist(df["rating"], bins =5,edgecolor='black')
plt.xlabel("rating")
plt.ylabel("no.of reviews")
plt.title("distribution of ratings across reviews ")
plt.show()