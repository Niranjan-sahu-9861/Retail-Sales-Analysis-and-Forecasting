import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("output/cleaned_data.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

monthly_sales = df.groupby(df['Order Date'].dt.to_period("M"))["Sales"].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()

model = ARIMA(monthly_sales, order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=6)

monthly_sales.plot(label="Actual")
forecast.plot(label="Forecast")
plt.legend()
plt.title("Sales Forecast")
plt.show()

print("STEP 5 DONE: Forecast Generated")
