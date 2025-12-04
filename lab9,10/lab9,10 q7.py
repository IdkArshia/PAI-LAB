import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('Mall_Customers.csv')
X = df[['Annual Income (k$)','Spending Score (1-100)']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
k = 5
km = KMeans(n_clusters=k, random_state=42)
labels = km.fit_predict(X_scaled)
df['Cluster'] = labels
plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=labels)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score')
plt.title('KMeans clusters (k=4)')
plt.show()
