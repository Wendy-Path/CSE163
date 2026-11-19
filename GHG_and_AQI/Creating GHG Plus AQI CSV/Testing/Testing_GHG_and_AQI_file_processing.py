import pandas as pd

from GHG_and_AQI import filtering_ghg_and_aqi_for_q1

GHG_FILE = "GHG_and_AQI/Testing/GHG_Reporting_Program_Publication_processed_small.csv"
AQI_FILE = "GHG_and_AQI/Testing/annual_aqi_by_county_washington_all_small.csv"


def test_common_counties_ghg_aqi(ghg_file: str, aqi_file: str):
    """
    Tests the common_counties_ghg_aqi function
    """

    assert (
        ["Spokane", "King"]
        == filtering_ghg_and_aqi_for_q1.common_counties_ghg_aqi(
            GHG_FILE, AQI_FILE
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
