import pandas as pd

from sklearn.ensemble import IsolationForest
from sqlalchemy import create_engine

password = "Anchitha%402005"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/phonepe_ml"
)

# Load processed dataset
df = pd.read_sql(
    "SELECT * FROM advanced_processed_dataset",
    con=engine
)

features = [
    "Transaction_Count_Scaled",
    "Transaction_Amount_Scaled",
    "User_Count_Scaled",
    "Avg_Transaction_Value_Scaled"
]

X = df[features]

# Isolation Forest Model
model = IsolationForest(
    contamination=0.03,
    random_state=42
)

df["Anomaly"] = model.fit_predict(X)

# Convert labels
df["Anomaly"] = df["Anomaly"].map({
    1: "Normal",
    -1: "Fraud/Suspicious"
})

# Save anomalies
df.to_csv(
    "data/processed/anomaly_detection_results.csv",
    index=False
)

# Store in SQL
df.to_sql(
    name="anomaly_detection_results",
    con=engine,
    if_exists="replace",
    index=False
)

# Display suspicious rows
anomalies = df[
    df["Anomaly"] == "Fraud/Suspicious"
]

print(anomalies[
    [
        "State",
        "Year",
        "Quarter",
        "Transaction_Amount",
        "Anomaly"
    ]
].head())

print("\nAnomaly Detection Completed!")
print("Total Suspicious Records:", anomalies.shape[0])