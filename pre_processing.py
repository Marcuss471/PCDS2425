import itertools
import sklearn.preprocessing as skl_pre


def process(train, test):
    new_train = train.copy()
    new_test = test.copy()

    add_booleans(new_train, new_test)
    add_time_probability(new_train, new_test)
    scale_data(new_train, new_test)

    return [new_train, new_test]


def add_booleans(train, test):
    train["no_rain"] = train["precip"] == 0
    test["no_rain"] = test["precip"] == 0

    train["no_snow"] = train["snowdepth"] == 0
    test["no_snow"] = test["snowdepth"] == 0

    train["good_visibility"] = train["visibility"] == 16
    test["good_visibility"] = test["visibility"] == 16


def add_time_probability(train, test):
    cols = ["hour_of_day", "weekday", "summertime"]
    unique_combinations = list(
        itertools.product(*[train[col].unique() for col in cols])
    )

    train["time_probability"] = 0.0
    test["time_probability"] = 0.0
    for combination in unique_combinations:
        mask_train = (train[cols] == combination).all(axis=1)
        mask_test = (test[cols] == combination).all(axis=1)

        data_filtered = train[mask_train]
        high = (data_filtered["increase_stock"] == "high_bike_demand").sum()
        low = (data_filtered["increase_stock"] == "low_bike_demand").sum()

        # Historic propbability that it is high_bike_demand for given combination of cols
        probability = high / (high + low) if high + low > 0 else 0
        train.loc[mask_train, "time_probability"] = probability
        test.loc[mask_test, "time_probability"] = probability


def scale_data(train, test):
    cols = [
        "time_probability",
        "temp",
        "dew",
        "humidity",
        "snowdepth",
        "windspeed",
        "cloudcover",
        "visibility",
    ]
    std_scaler = skl_pre.RobustScaler()
    for col in cols:
        train[col] = std_scaler.fit_transform(train[[col]])
        test[col] = std_scaler.fit_transform(test[[col]])