import pandas as pd

from sklearn.cluster import KMeans
from sqlalchemy import create_engine

from src.utils.db_utils import engine

# Load processed dataset
df = pd.read_sql(
    "SELECT * FROM advanced_processed_dataset",
    con=engine
)

# Aggregate state-level metrics
state_df = df.groupby("State").agg({
    "Transaction_Amount": "mean",
    "Transaction_Count": "mean",
    "User_Count": "mean"
}).reset_index()

# Features for clustering
X = state_df[
    [
        "Transaction_Amount",
        "Transaction_Count",
        "User_Count"
    ]
]

# KMeans Model
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

state_df["Cluster"] = kmeans.fit_predict(X)

# Rename clusters
cluster_names = {
    0: "High Activity",
    1: "Emerging",
    2: "Medium Activity",
    3: "Low Activity"
}

state_df["Cluster_Name"] = (
    state_df["Cluster"].map(cluster_names)
)

print(state_df.head())

# Save results
state_df.to_csv(
    "data/processed/state_clusters.csv",
    index=False
)

# Store in SQL
state_df.to_sql(
    name="state_clusters",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nState Clustering Completed!")
print(state_df['Cluster_Name'].value_counts())