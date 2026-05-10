import os
import json
import pandas as pd

from src.utils.db_utils import engine

path = "pulse/data/top/user/country/india/state/"

data = {
    "State": [],
    "Year": [],
    "Quarter": [],
    "Pincode": [],
    "Registered_Users": []
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

                    pincodes = content["data"]["pincodes"]

                    for item in pincodes:

                        data["State"].append(
                            state.replace("-", " ").title()
                        )

                        data["Year"].append(int(year))

                        data["Quarter"].append(
                            int(file.strip(".json"))
                        )

                        data["Pincode"].append(item["name"])

                        data["Registered_Users"].append(
                            item["registeredUsers"]
                        )

                except:
                    pass

df = pd.DataFrame(data)

print(df.head())

df.to_csv(
    "data/processed/top_user.csv",
    index=False
)

df.to_sql(
    name="top_user",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nTop User Data Inserted Successfully!")
print(df.shape)