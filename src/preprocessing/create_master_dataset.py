import pandas as pd
from sqlalchemy import create_engine

password = "Anchitha%402005"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/phonepe_ml"
)

agg_trans = pd.read_sql(
    "SELECT * FROM aggregated_transaction",
    con=engine
)

agg_user = pd.read_sql(
    "SELECT * FROM aggregated_user",
    con=engine
)

map_user = pd.read_sql(
    "SELECT * FROM map_user",
    con=engine
)

map_trans = pd.read_sql(
    "SELECT * FROM map_transaction",
    con=engine
)

# Aggregate transaction data
trans_summary = agg_trans.groupby(
    ["State", "Year", "Quarter"]
).agg({
    "Transaction_Count": "sum",
    "Transaction_Amount": "sum"
}).reset_index()

# Aggregate user data
user_summary = agg_user.groupby(
    ["State", "Year", "Quarter"]
).agg({
    "Count": "sum"
}).reset_index()

user_summary.rename(
    columns={"Count": "User_Count"},
    inplace=True
)

# Merge datasets
master_df = pd.merge(
    trans_summary,
    user_summary,
    on=["State", "Year", "Quarter"],
    how="left"
)

# Feature Engineering
master_df["Avg_Transaction_Value"] = (
    master_df["Transaction_Amount"] /
    master_df["Transaction_Count"]
)

master_df["Transactions_Per_User"] = (
    master_df["Transaction_Count"] /
    master_df["User_Count"]
)

print(master_df.head())

master_df.to_csv(
    "data/processed/master_dataset.csv",
    index=False
)

master_df.to_sql(
    name="master_dataset",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nMaster Dataset Created Successfully!")
print(master_df.shape)