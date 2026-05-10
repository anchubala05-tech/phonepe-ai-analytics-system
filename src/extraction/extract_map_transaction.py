import os
import json
import pandas as pd

from src.utils.db_utils import engine

path = "pulse/data/map/transaction/hover/country/india/state/"

data = {
    "State": [],
    "Year": [],
    "Quarter": [],
    "District": [],
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

                with open(current_year + file, "r") as f:

                    content = json.load(f)

                try:

                    districts = content["data"]["hoverDataList"]

                    for item in districts:

                        district = item["name"]

                        count = item["metric"][0]["count"]

                        amount = item["metric"][0]["amount"]

                        data["State"].append(
                            state.replace("-", " ").title()
                        )

                        data["Year"].append(int(year))

                        data["Quarter"].append(
                            int(file.strip(".json"))
                        )

                        data["District"].append(district)

                        data["Transaction_Count"].append(count)

                        data["Transaction_Amount"].append(amount)

                except:
                    pass

df = pd.DataFrame(data)

print(df.head())

df.to_csv(
    "data/processed/map_transaction.csv",
    index=False
)

df.to_sql(
    name="map_transaction",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nMap Transaction Data Inserted Successfully!")
print(df.shape)