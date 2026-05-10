import pandas as pd

from prophet import Prophet
from src.utils.db_utils import engine

# Load dataset
df = pd.read_sql(
    "SELECT * FROM master_dataset",
    con=engine
)

# Create date column
df["Date"] = pd.to_datetime(
    df["Year"].astype(str) + "-" +
    (df["Quarter"] * 3).astype(str) + "-01"
)

# Aggregate quarterly transactions
forecast_df = df.groupby("Date").agg({
    "Transaction_Amount": "sum"
}).reset_index()

# Prophet format
forecast_df.columns = ["ds", "y"]

# Prophet model
model = Prophet()

model.fit(forecast_df)

# Future predictions
future = model.make_future_dataframe(
    periods=8,
    freq="QE"
)

forecast = model.predict(future)

# Save results
forecast.to_csv(
    "data/processed/transaction_forecast.csv",
    index=False
)

print(
    forecast[
        ["ds", "yhat", "yhat_lower", "yhat_upper"]
    ].tail()
)

print("\nForecasting Completed!")