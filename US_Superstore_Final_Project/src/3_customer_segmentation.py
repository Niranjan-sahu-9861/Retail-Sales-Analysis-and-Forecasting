import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("output/cleaned_data.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

rfm = df.groupby("Customer ID").agg({
    "Order Date": lambda x: (df["Order Date"].max() - x.max()).days,
    "Order ID": "count",
    "Sales": "sum"
})

rfm.columns = ["Recency", "Frequency", "Monetary"]

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

kmeans = KMeans(n_clusters=4, random_state=42)
rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

print("STEP 4 DONE: Customer Segmentation")
print(rfm.head())
