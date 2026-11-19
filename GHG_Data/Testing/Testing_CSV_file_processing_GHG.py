"""
This file tests CSV_file_processing_GHG.py
"""
import pandas as pd
from GHG_Data import CSV_file_processing_GHG

PREPROCESSED_FILE = (
    "GHG_Data/Testing/GHG_Reporting_Program_Publication_20261115_small.csv"
)
PROCESSED_FILE = (
    "GHG_Data/Testing/"
    "GHG_Reporting_Program_Publication_20261115_small_processed.csv"
)


def test_find_common_counties_each_year():
    """
    Tests the find_common_counties_each_year function
    """

    assert (
        {"Yakima", "King"}
        == CSV_file_processing_GHG.find_common_counties_each_year(
            2023, 2024, PREPROCESSED_FILE
        )
    )


def test_all_washington_rows_with_common_counties():
    """
    Tests the all_washington_rows_with_common_counties function
    """

    CSV_file_processing_GHG.rows_with_common_counties(
        {"Yakima", "King"},
        PREPROCESSED_FILE,
        PROCESSED_FILE
    )

    df = pd.read_csv(PROCESSED_FILE)

    assert {"Yakima", "King"} == set(df["County"].values)


def main():

    test_find_common_counties_each_year()
    test_all_washington_rows_with_common_counties()
    print("All tests passed!")


if __name__ == "__main__":
    main()
