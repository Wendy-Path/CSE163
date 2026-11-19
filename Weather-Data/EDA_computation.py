"""
Wendy Barben
CSE 163
This program calculated information needed for the eda for the
combined_temp_GHG_filtered.csv
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

sns.set_theme()

# file_temp = 'Weather-Data/all_temp_data_counties.csv'
# file_prec = 'Weather-Data/all_prec_data_counties.csv'


def dataset_information(df: pd.DataFrame) -> None:
    """
    This function calculates and prints the rows, columns, missing values,
    and the number of unique counties
    """
    rows = len(df)
    columns = len(df.columns)
    print('Rows: ' + str(rows) + ' | Columns: ' + str(columns))

    df = df.replace('M', np.nan)
    missing_value_count = df.isna().sum().sum()
    total_values = rows*(columns-3)
    print("Total missing value count: " + str(missing_value_count))
    percentage = (missing_value_count/total_values)
    print('Percentage of missing values: ' + str(percentage))

    county_df = df['county']
    # print(county_df)
    county_df = county_df.value_counts()
    print(county_df)

    # The following code is commented out since it is not needed for the eda
    # but is kept in case data is changed
    '''
    #print('location list: ')
    location_list = set()
    for loc in df['location'].unique():
        location_list.add(loc)
    print(location_list)
    print('county counts:')
    '''


def plot_annual_temperature_by_county(df_temp: pd.DataFrame) -> None:
    """
    This function plots the data by temperature, year, and county
    """
    plot_data = df_temp.assign(
        Annual=pd.to_numeric(df_temp['Annual'], errors='coerce'))
    county_year = (
        plot_data.pivot_table(
            index='county',
            columns='Year',
            values='Annual',
            aggfunc='mean',)
        .sort_index())

    fig, ax = plt.subplots(figsize=(8, 8), constrained_layout=True)
    sns.heatmap(
        county_year,
        ax=ax,
        cmap='viridis',
        mask=county_year.isna(),
        cbar_kws={'label': 'Mean annual temperature'},)
    ax.set(title='Mean annual temperature by county',
           xlabel='Year',
           ylabel='County')
    plt.show()


def plot_emmisions_by_county(df_temp: pd.DataFrame) -> None:
    """
    This function plots the data by emmisions, year, and county
    """
    plot_data = df_temp.assign(
        Annual=pd.to_numeric(
            df_temp['County Emissions (MTCO2e)'], errors='coerce'))
    county_year = (
        plot_data.pivot_table(
            index='county',
            columns='Year',
            values='Annual',
            aggfunc='mean',)
        .sort_index())

    fig, ax = plt.subplots(figsize=(8, 8), constrained_layout=True)
    sns.heatmap(
        county_year,
        ax=ax,
        cmap='viridis',
        mask=county_year.isna(),
        cbar_kws={'label': 'Mean annual emissions'},)
    ax.set(title='Mean annual emissions by county',
           xlabel='Year',
           ylabel='County')

    plt.show()


def sorting_data(df: pd.DataFrame, column: str) -> list:
    """
    This function takes a dataframe and column name and returns the column
    as a list with the values sorted in ascending order
    (without missing values)
    """
    df = df[column]
    df = df.replace('M', np.nan)
    df = df.dropna()
    df = df.sort_values(ascending=True)
    df = pd.to_numeric(df)
    # print(list(df))
    return (list(df))


def median(numbers: list) -> float:
    """
    Given a sorted list of numbers, returns the median.
    """
    n = len(numbers)
    result = None
    if len(numbers) % 2 != 0:
        result = numbers[n // 2]
    else:
        upper_num = numbers[n // 2]
        lower_num = numbers[n // 2 - 1]
        result = (upper_num + lower_num) / 2
    return result


def seven_number_summary(numbers: list) -> str:
    """
    Given a sorted list of numbers, returns a string of the seven-number
    summary: the minimum, first quartile, median, third quartile,
    and maximum.
    """
    n = len(numbers)

    if n % 2 == 0:
        lower_half = numbers[:n // 2]
        upper_half = numbers[n // 2:]
    else:
        lower_half = numbers[:n // 2]
        upper_half = numbers[n // 2 + 1:]

    mean = sum(numbers)/len(numbers)
    pop_sd = statistics.pstdev(numbers)
    return ('Mean: ' + str(mean) +
            ' | Standard Deviation: ' + str(pop_sd) +
            ' | Minimum: ' + str(numbers[0]) +
            ' | First quartile: ' + str(median(lower_half)) +
            ' | Median: ' + str(median(numbers)) +
            ' | Third quartile: ' + str(median(upper_half)) +
            ' | Maximum: ' + str(numbers[-1]))


def main():
    print('hi')

    df_temp = pd.read_csv('Weather-Data/combined_temp_GHG_filtered.csv')
    print('Temperature and GHG data: ')
    dataset_information(df_temp)
    sorted_annual_temps = sorting_data(df_temp, 'Annual')
    sorted_emmisions = sorting_data(df_temp, 'County Emissions (MTCO2e)')
    print('Seven number summary for annual temperatures: ')
    print(seven_number_summary(sorted_annual_temps))

    print('Seven number summary for county emissions: ')
    print(seven_number_summary(sorted_emmisions))

    plot_annual_temperature_by_county(df_temp)
    plot_emmisions_by_county(df_temp)

    '''
    print('Temperature stuff: ')
    df_temp = pd.read_csv(file_temp)
    print(df_temp)
    dataset_information(df_temp, pd)
    sorted_annual_temps = sorting_annual_data(df_temp, pd)
    print('Seven number summary for annual temperatures: ')
    seven_number_summary(sorted_annual_temps)

    # plotting data
    #plot_location_by_county(df_temp)

    new_temp_df = pd.read_csv('combined_temp_GHG.csv')
    new_temp_df = filtering_GHG_data(new_temp_df, pd)

    new_temp_df.to_csv('combined_temp_GHG_filtered.csv', index=False)


    # Adding GHG data to temperature data

    GHG_df = pd.read_csv(
        'GHG Data/GHG_Reporting_Program_Publication_processed.csv')
    new_temp_df = adding_GHG_data(df_temp, GHG_df)

    print(new_temp_df)

    print('Precipitation stuff: ')
    df_prec = pd.read_csv(file_prec)
    #dataset_information(df_prec, pd)

    location_list_temp = dataset_information(df_temp, pd)
    diff = location_list_temp.difference(location_list_prec)
    print('Locations in temperature data but not in precipitation data: ')
    for loc in diff:
        print(loc)

    location_list_prec = dataset_information(df_prec, pd)
    diff2 = location_list_prec.difference(location_list_temp)
    print('Locations in precipitation data but not in temperature data: ')
    for loc in diff2:
        print(loc)
    '''


if __name__ == '__main__':
    main()
