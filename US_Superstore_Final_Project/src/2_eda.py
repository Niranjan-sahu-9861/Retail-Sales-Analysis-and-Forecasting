import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output/plots", exist_ok=True)

df = pd.read_csv("output/cleaned_data.csv")

# Sales by Category
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.savefig("output/plots/sales_by_category.png")
plt.close()

# Profit by Region
sns.barplot(x="Region", y="Profit", data=df, estimator=sum)
plt.title("Profit by Region")
plt.savefig("output/plots/profit_by_region.png")
plt.close()

print("STEP 3 DONE: EDA plots saved")
