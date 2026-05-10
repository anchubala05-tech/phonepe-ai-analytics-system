import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sqlalchemy import create_engine

password = "Anchitha%402005"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/phonepe_ml"
)

# Load master dataset
df = pd.read_sql(
    "SELECT * FROM master_dataset",
    con=engine
)

print("Original Shape:", df.shape)

# -----------------------------
# Missing Value Handling
# -----------------------------

df.fillna(0, inplace=True)

# -----------------------------
# Duplicate Removal
# -----------------------------

df.drop_duplicates(inplace=True)

# -----------------------------
# Feature Engineering
# -----------------------------

df["Transaction_Growth"] = (
    df.groupby("State")["Transaction_Amount"]
    .pct_change()
)

df["User_Growth"] = (
    df.groupby("State")["User_Count"]
    .pct_change()
)

df["Transaction_Growth"] = df["Transaction_Growth"].fillna(0)
df["User_Growth"] = df["User_Growth"].fillna(0)

# -----------------------------
# Outlier Detection (Z-Score)
# -----------------------------

df["ZScore_Transaction"] = (
    (
        df["Transaction_Amount"] -
        df["Transaction_Amount"].mean()
    )
    /
    df["Transaction_Amount"].std()
)

# -----------------------------
# Scaling
# -----------------------------

features = [
    "Transaction_Count",
    "Transaction_Amount",
    "User_Count",
    "Avg_Transaction_Value",
    "Transactions_Per_User",
    "Transaction_Growth",
    "User_Growth"
]

scaler = StandardScaler()

scaled_features = scaler.fit_transform(df[features])

scaled_df = pd.DataFrame(
    scaled_features,
    columns=[f"{col}_Scaled" for col in features]
)

df = pd.concat([df, scaled_df], axis=1)

print(df.head())

# Save processed dataset
df.to_csv(
    "data/processed/advanced_processed_dataset.csv",
    index=False
)

# Store in SQL
df.to_sql(
    name="advanced_processed_dataset",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nAdvanced Preprocessing Completed!")
print("Final Shape:", df.shape)