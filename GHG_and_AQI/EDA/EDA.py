"""
This program performs Exploratory Data Analysis (EDA) on GHG and AQI
data for Washington State.
"""
import textwrap
import pandas as pd
import matplotlib.pyplot as plt


def has_missing_values(df: pd.DataFrame) -> bool:
    """
    Takes a DataFrame as input and returns whether it has any missing values
    as a boolean.
    """
    original_rows = len(df)
    df_dropped = df.dropna()
    new_rows = len(df_dropped)

    return original_rows - new_rows > 0


def num_rows_and_num_columns(df: pd.DataFrame) -> tuple[int, int]:
    """
    Returns the number of rows and columns in a DataFrame as a tuple.
    """
    num_rows = df.shape[0]
    num_columns = df.shape[1]
    return num_rows, num_columns


def seven_number_summary(df: pd.DataFrame, column: str) -> None:
    """
    Takes in a DataFrame and a column and prints the seven number summary
    for the values in that column
    """
    df_summary = df.describe()

    mean = df_summary.loc['mean', column]
    std = df_summary.loc['std', column]
    min_value = df_summary.loc['min', column]
    q1 = df_summary.loc['25%', column]
    median = df_summary.loc['50%', column]
    q3 = df_summary.loc['75%', column]
    max_value = df_summary.loc['max', column]

    print(f"Seven-number summary for {column}:")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std}")
    print(f"Minimum: {min_value}")
    print(f"1st Quartile (Q1): {q1}")
    print(f"Median: {median}")
    print(f"3rd Quartile (Q3): {q3}")
    print(f"Maximum: {max_value}")


def line_plot(df: pd.DataFrame) -> None:
    """
    Takes in a DataFrame and creates a line plot showing how the average
    values in columns Reported Emissions and Median AQI change over the
    years 2012 to 2024.
    """
    yearly_avg = (
        df.groupby("Year")[["Reported Emissions (MTCO2e)", "Median AQI"]]
        .mean()
        .reset_index()
    )

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.plot(
        yearly_avg["Year"],
        yearly_avg["Reported Emissions (MTCO2e)"],
        color="green"
    )
    ax2.plot(yearly_avg["Year"], yearly_avg["Median AQI"], color="blue")

    ax1.set_xlabel("Year")
    ax1.set_ylabel("Average Emissions (MTCO2e)")
    ax1.set_title("Emissions Over Time in Washington State (2012-2024)")

    ax2.set_xlabel("Year")
    ax2.set_ylabel("Average Median AQI")
    ax2.set_title("AQI Over Time in Washington State (2012-2024)")

    caption = (
        "Figure 2. Trends in average reported emissions and "
        "median Air Quality Index (AQI) from 2012 to 2024 in Washington "
        "State. While reported emissions generally increased, median AQI "
        "decreased."
    )

    wrapped_caption = textwrap.fill(caption, width=70)

    fig.text(
        0.5, 0.01,
        wrapped_caption,
        ha="center",
        fontsize=10,
        style="italic"
    )

    plt.subplots_adjust(bottom=0.18)
    plt.show()


def box_plot(df: pd.DataFrame) -> None:
    """
    Takes in a DataFrame and creates a box plot showing the distribution
    of Median AQI across different levels of reported emissions
    (Low, Medium, High).
    """

    df["Emissions Group"] = pd.qcut(
        df["Reported Emissions (MTCO2e)"],
        q=3,
        labels=["Low", "Medium", "High"]
    )

    fig, ax = plt.subplots(figsize=(10, 8))

    df.boxplot(
        column="Median AQI",
        by="Emissions Group",
        ax=ax
    )

    ax.set_xlabel("Reported Emissions Level")
    ax.set_ylabel("Median AQI")
    fig.suptitle("")
    ax.set_title(
        "Median AQI Distribution by Emissions Level in Washington State"
    )

    caption = (
        "Figure 1. Distribution of median Air Quality Index (AQI) across "
        "counties grouped by low, medium, and high reported emissions. "
        "Counties with higher reported emissions generally exhibit higher "
        "median AQI values."
    )

    wrapped_caption = textwrap.fill(caption, width=70)

    fig.text(
        0.5, 0.01,
        wrapped_caption,
        ha="center",
        fontsize=10,
        style="italic"
    )

    plt.subplots_adjust(bottom=0.18)
    plt.show()


def main():
    df = pd.read_csv('GHG_Plus_AQI.csv')

    missing_values = has_missing_values(df)
    missing_values_message = "Yes" if missing_values else "No"
    print(
        f"Are there any missing values in the DataFrame? "
        f"{missing_values_message}"
    )
    print()

    rows, columns = num_rows_and_num_columns(df)
    print(f"Number of rows: {rows}")
    print(f"Number of columns: {columns}")
    print()

    seven_number_summary(df, 'Reported Emissions (MTCO2e)')
    print()
    seven_number_summary(df, 'Median AQI')

    line_plot(df)
    box_plot(df)


if __name__ == "__main__":
    main()
