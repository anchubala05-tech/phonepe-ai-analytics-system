import os
import json
import pandas as pd
from sqlalchemy import create_engine

path = "pulse/data/aggregated/transaction/country/india/state/"

data = {
    "State": [],
    "Year": [],
    "Quarter": [],
    "Transaction_Type": [],
    "Transaction_Count": [],
    "Transaction_Amount": []
}

states = os.listdir(path)

for state in states:

    current_state = path + state + "/"

    years = os.listdir(current_state)

    for year in years:

        current_year = current_state + year + "/"

        files = os.listdir(current_year)

        for file in files:

            if file.endswith(".json"):

                current_file = current_year + file

                with open(current_file, "r") as f:

                    content = json.load(f)

                try:
                    for item in content["data"]["transactionData"]:

                        name = item["name"]

                        count = item["paymentInstruments"][0]["count"]

                        amount = item["paymentInstruments"][0]["amount"]

                        data["State"].append(state.replace("-", " ").title())
                        data["Year"].append(int(year))
                        data["Quarter"].append(int(file.strip(".json")))
                        data["Transaction_Type"].append(name)
                        data["Transaction_Count"].append(count)
                        data["Transaction_Amount"].append(amount)

                except:
                    pass

df = pd.DataFrame(data)

print(df.head())

# Save CSV backup
df.to_csv("data/processed/aggregated_transaction.csv", index=False)

print("\nData Extracted Successfully!")
print(df.shape)


password = "Anchitha%402005"

engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/phonepe_ml"
)

df.to_sql(
    name="aggregated_transaction",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data Inserted into MySQL Successfully!")