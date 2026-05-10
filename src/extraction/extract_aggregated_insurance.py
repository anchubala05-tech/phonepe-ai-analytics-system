import os
import json
import pandas as pd

from src.utils.db_utils import engine

path = "pulse/data/aggregated/insurance/country/india/state/"

data = {
    "State": [],
    "Year": [],
    "Quarter": [],
    "Insurance_Type": [],
    "Count": [],
    "Amount": []
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

                with open(current_year + file, "r") as f:

                    content = json.load(f)

                try:

                    transactions = content["data"]["transactionData"]

                    for item in transactions:

                        ins_type = item["name"]

                        count = item["paymentInstruments"][0]["count"]

                        amount = item["paymentInstruments"][0]["amount"]

                        data["State"].append(state.replace("-", " ").title())
                        data["Year"].append(int(year))
                        data["Quarter"].append(int(file.strip(".json")))
                        data["Insurance_Type"].append(ins_type)
                        data["Count"].append(count)
                        data["Amount"].append(amount)

                except:
                    pass

df = pd.DataFrame(data)

print(df.head())

df.to_csv(
    "data/processed/aggregated_insurance.csv",
    index=False
)

df.to_sql(
    name="aggregated_insurance",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nAggregated Insurance Data Inserted Successfully!")
print(df.shape)