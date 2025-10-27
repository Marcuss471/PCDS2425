import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def numerical(df, column, remove_dominant=False):
    fig, ax = plt.subplots()

    high_demand_data = df[(df["increase_stock"] == "high_bike_demand")][column]
    low_demand_data = df[(df["increase_stock"] == "low_bike_demand")][column]

    if remove_dominant:

        def filter_dominant(data):
            return data[(data != 0)]
            # return data[(data != 16)]

        high_demand_data = filter_dominant(high_demand_data)
        low_demand_data = filter_dominant(low_demand_data)

    bins = 10
    ax.hist(
        [high_demand_data, low_demand_data],
        bins=bins,
        stacked=True,
        label=["High Demand", "Low Demand"],
        color=["red", "blue"],
    )

    ax.set_title(column)
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    ax.legend()

    fig.savefig(f"{column}.png")
    plt.close()


def qualitative(df, column):
    percentage = (
        df.groupby(column)["increase_stock"]
        .value_counts(normalize=True)
        .mul(100)
        .unstack()
    )
    percentage.plot(kind="bar", stacked=True, title=column, color=["red", "blue"])
    plt.ylabel("Percentage [%]")
    plt.xlabel(column)
    plt.savefig(f"{column}.png")
    plt.close()


def boolean(df, column):
    percentage = (
        df.groupby(column)["increase_stock"]
        .value_counts(normalize=True)
        .mul(100)
        .unstack()
    )
    percentage.plot(
        kind="bar", stacked=True, title="is " + column, color=["red", "blue"]
    )
    plt.ylabel("Percentage [%]")
    plt.xlabel(column)
    plt.savefig(f"{column}.png")
    plt.close()


def scatter_matrix(df, numerical_cols):
    color_map = {"low_bike_demand": "blue", "high_bike_demand": "red"}
    mapped_colors = df["increase_stock"].map(color_map)
    pd.plotting.scatter_matrix(
        df.loc[:, numerical_cols], figsize=(10, 10), c=mapped_colors, alpha=0.3
    )
    plt.savefig("scatter_plot.png")
    plt.close()