import pandas as pd
import os

os.makedirs("output", exist_ok=True)

df = pd.read_excel("data/US Superstore data.xls")

df.drop_duplicates(inplace=True)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Profit Margin'] = df['Profit'] / df['Sales']

df.to_csv("output/cleaned_data.csv", index=False)

print("STEP 2 DONE: cleaned_data.csv created")
