"""
This file tests CSV_file_processing.py
"""
import pandas as pd
from AQI_Data import CSV_file_processing

FILE_PREFIX = "AQI_Data/Testing/Original CSV Files/annual_aqi_by_county"
PROCESSED_FILE = "AQI_Data/Testing/annual_aqi_by_county_washington_all.csv"


def test_find_common_counties_each_year():
    """
    Tests the find_common_counties_each_year function
    """

    assert (
        {"Adams", "Asotin", "Benton"}
        == CSV_file_processing.find_common_counties_each_year(
            2023, 2024, FILE_PREFIX
        )
    )


def test_all_washington_rows_with_common_counties():
    """
    Tests the all_washington_rows_with_common_counties function
    """

    CSV_file_processing.all_washington_rows_with_common_counties(
        {"Adams", "Asotin", "Benton"},
        FILE_PREFIX, 2023, 2024,
        "AQI_Data/Testing/annual_aqi_by_county_washington_all.csv"
    )

    df = pd.read_csv(PROCESSED_FILE)

    assert "Alabama" not in df["State"].values
    assert {"Adams", "Asotin", "Benton"} == set(df["County"].values)


def main():

    test_find_common_counties_each_year()
    test_all_washington_rows_with_common_counties()
    print("All tests passed!")


if __name__ == "__main__":
    main()
