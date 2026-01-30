# Retail Sales Analysis & Forecasting using Python

**Project:** End-to-end retail sales analytics and forecasting built with Python.

---

## Project Overview

This project cleans and analyzes the *US Superstore* sales dataset, segments customers using RFM + K‑Means, and forecasts future monthly sales using an ARIMA model. All modules are implemented as standalone Python scripts so the project is reproducible and easy to run.

---

## Features

* Data cleaning and feature engineering
* Exploratory Data Analysis (sales, profit, region, category)
* Customer segmentation (RFM + K‑Means)
* Time series forecasting (ARIMA)
* Plots saved to `output/plots/` and cleaned CSV saved to `output/cleaned_data.csv`

---

## Project Structure

```
US_Superstore_Final_Project/
├── data/
│   └── US Superstore data.xls
├── src/
│   ├── 1_data_cleaning.py
│   ├── 2_eda.py
│   ├── 3_customer_segmentation.py
│   ├── 4_sales_forecasting.py
├── output/
│   └── plots/
├── requirements.txt
└── README.md
```

---

## 🛠 Requirements

* Python 3.9+
* Install packages:

```bash
pip install -r requirements.txt
```

> If your Excel file is `.xls` install `xlrd`:

```bash
pip install xlrd
```

---

## How to run (order matters)

Run commands from **project root** (`US_Superstore_Final_Project`):

```bash
# 1. Clean data (generates output/cleaned_data.csv)
python src/1_data_cleaning.py

# 2. Exploratory Data Analysis (saves plots to output/plots)
python src/2_eda.py

# 3. Customer Segmentation (prints RFM clusters)
python src/3_customer_segmentation.py

# 4. Sales Forecasting (shows forecast plot)
python src/4_sales_forecasting.py
```

---

## Expected Outputs

* `output/cleaned_data.csv` — cleaned and feature-engineered dataset
* `output/plots/sales_by_category.png` and other visualizations
* Console output with RFM clusters and basic summaries
* Forecast plot window showing next 6 months

---

## Notes & Tips

* Ensure `data/US Superstore data.xls` filename matches exactly.
* If plots don’t appear on Windows, add `plt.show()` where needed or run the script from an environment that supports plotting.
* Convert `.xls` to `.xlsx` if you prefer using `openpyxl` instead of `xlrd`.

---

## Future Improvements

* Replace ARIMA with Prophet or LSTM for improved forecasting
* Add an interactive dashboard (Streamlit / Dash)
* Integrate MySQL/Postgres for production-ready analytics

---

## License & Author

**Author:** Niranjan Sahu


