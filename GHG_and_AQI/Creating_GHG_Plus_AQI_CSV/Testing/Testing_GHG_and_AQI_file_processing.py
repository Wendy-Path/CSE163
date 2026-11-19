from Creating_GHG_Plus_AQI_CSV import filtering_ghg_and_aqi_for_q1

GHG_FILE = (
    "Creating_GHG_Plus_AQI_CSV/Testing/"
    "GHG_Reporting_Program_Publication_processed_small.csv"
)

AQI_FILE = (
    "Creating_GHG_Plus_AQI_CSV/Testing/"
    "annual_aqi_by_county_washington_all_small.csv"
)

def main():

    common_counties = filtering_ghg_and_aqi_for_q1.common_counties_ghg_aqi(GHG_FILE, AQI_FILE)

    filtering_ghg_and_aqi_for_q1.filter_for_same_counties(GHG_FILE, AQI_FILE, common_counties)

    filtering_ghg_and_aqi_for_q1.ghg_combine_rows_with_same_county(
        "filtered_ghg_data_for_same_counties_as_aqi.csv"
    )

    filtering_ghg_and_aqi_for_q1.ghg_plus_aqi(
        "GHG_fully_processed_for_aqi.csv",
        "filtered_aqi_data_for_same_counties_as_ghg.csv"
    )


if __name__ == "__main__":
    main()
