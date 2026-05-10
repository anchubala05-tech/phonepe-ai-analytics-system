import os
import json
import pandas as pd

from src.utils.db_utils import engine

path = "pulse/data/aggregated/user/country/india/state/"

data = {
    "State": [],
    "Year": [],
    "Quarter": [],
    "Brand": [],
    "Count": [],
    "Percentage": []
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

                    users = content["data"]["usersByDevice"]

                    for item in users:

                        brand = item["brand"]
                        count = item["count"]
                        percentage = item["percentage"]

                        data["State"].append(
                            state.replace("-", " ").title()
                        )

                        data["Year"].append(int(year))

                        data["Quarter"].append(
                            int(file.strip(".json"))
                        )

                        data["Brand"].append(brand)
                        data["Count"].append(count)
                        data["Percentage"].append(percentage)

                except:
                    pass

df = pd.DataFrame(data)

print(df.head())

df.to_csv(
    "data/processed/aggregated_user.csv",
    index=False
)

df.to_sql(
    name="aggregated_user",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nAggregated User Data Inserted Successfully!")
print(df.shape)