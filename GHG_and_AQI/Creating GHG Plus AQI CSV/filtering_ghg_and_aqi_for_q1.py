"""
This program combines GHG and AQI data for Washington State between the years
2012 and 2024 to be used for Exploratory Data Analysis (EDA)
"""

import csv
import pandas as pd

def common_counties_ghg_aqi(ghg_file: str, aqi_file: str) -> list[str]:
    """
    This function takes two CSV files as input. One contains GHG emissions
    data and the other contains AQI data. It returns a list of counties that
    are present in both datasets.
    """
    ghg_counties = set()
    aqi_counties = set()

    # Read GHG emissions data
    with open(ghg_file, mode='r') as ghg_csv:
        reader = csv.reader(ghg_csv)
        for row in reader:
            ghg_counties.add(row[8])

    # Read AQI data
    with open(aqi_file, mode='r') as aqi_csv:
        reader = csv.reader(aqi_csv)
        for row in reader:
            aqi_counties.add(row[1]) 

    # Find common counties
    common_counties = ghg_counties.intersection(aqi_counties)

    return list(common_counties)

def filter_for_same_counties(ghg_file: str, aqi_file: str, common_counties: list[str]) -> None:
    """
    Takes in a GHG emissions CSV file, an AQI CSV file, and a list of common counties.
    Filters both datasets to only include rows whose entry in the county column
    appears in common counties. Writes the filtered data to new CSV files.
    """
    
    with open('filtered_ghg_data_for_same_counties_as_aqi.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        with open(ghg_file, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[8] in common_counties:
                    writer.writerow(row)

    with open('filtered_aqi_data_for_same_counties_as_ghg.csv', 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        with open(aqi_file, mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row[1] in common_counties:
                    writer.writerow(row)


def convert_to_float(value: str) -> float:
    """
    Takes in a string and casts it into float before returning it
    """
    return float(value.replace(",", ""))


def ghg_combine_rows_with_same_county(ghg_file: str) -> None:
    """
    Takes in a file and combines the data in the emissions
    column for rows with the same year and county.
    Writes the combined data to a new CSV file.
    """
    ghg_data = pd.read_csv(ghg_file)
    ghg_data["Reported Emissions (MTCO2e)"] = ghg_data["Reported Emissions (MTCO2e)"].apply(convert_to_float)
    ghg_data_grouped = ghg_data.groupby(['Year','County'])['Reported Emissions (MTCO2e)'].sum().reset_index()
    ghg_data_grouped.to_csv('GHG_fully_processed_for_aqi.csv', index=False)


def ghg_plus_aqi(ghg_file: str, aqi_file: str) -> None:
    """
    Takes in a GHG emissions CSV file and an AQI CSV file.
    Combines the rows of each file together based on the year and county.
    """
    ghg_data = pd.read_csv(ghg_file)
    aqi_data = pd.read_csv(aqi_file)
    aqi_data = aqi_data[['Year', 'County', 'Median AQI']]
    merged_data = pd.merge(ghg_data, aqi_data, on=['Year', 'County'], how='inner')
    merged_data.to_csv('GHG_plus_AQI.csv', index=False)


def main():
    ghg_file = 'GHG_Reporting_Program_Publication_processed.csv' 
    aqi_file = 'annual_aqi_by_county_washington_all.csv'       

    common_counties = common_counties_ghg_aqi(ghg_file, aqi_file)

    filter_for_same_counties(ghg_file, aqi_file, common_counties)

    ghg_combine_rows_with_same_county('filtered_ghg_data_for_same_counties_as_aqi.csv')

    ghg_plus_aqi('GHG_fully_processed_for_aqi.csv', 'filtered_aqi_data_for_same_counties_as_ghg.csv')


if __name__ == "__main__":
    main()

