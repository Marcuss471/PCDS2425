import pandas as pd

csv_path = "./training_data_vt2025.csv"
x_numerical = [
    "temp",
    "dew",
    "humidity",
    "precip",
    "snowdepth",
    "windspeed",
    "cloudcover",
    "visibility",
]
x_qualitative = ["hour_of_day", "day_of_week", "month"]
x_boolean = ["summertime", "weekday", "holiday"]


def get_data(x_cols):
    bike_demand = pd.read_csv(csv_path, dtype={col: bool for col in x_boolean})

    # Handle qualitative variables
    bike_demand_original = bike_demand[x_qualitative].copy()
    bike_demand_with_dummies = pd.get_dummies(
        bike_demand, columns=x_qualitative, prefix_sep="-"
    )
    bike_demand_with_dummies = pd.concat(
        [bike_demand_with_dummies, bike_demand_original], axis=1
    )

    # Find the newly created dummy columns (weekday -> weekday-1, weekday-2...)
    new_x_cols = []
    for col in x_cols:
        if col not in x_qualitative:
            new_x_cols.append(col)
        else:
            new_x_cols.extend(
                filter(
                    lambda c: c.startswith(col + "-"), bike_demand_with_dummies.columns
                )
            )

    return [bike_demand_with_dummies, new_x_cols]