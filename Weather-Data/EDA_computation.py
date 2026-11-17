import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from CSV_processing import counties
import statistics

sns.set_theme()

file_temp = 'Weather-Data/all_temp_data_counties.csv'
file_prec = 'Weather-Data/all_prec_data_counties.csv'

def dataset_information(df, pd):
    rows = len(df)
    columns = len(df.columns)
    print('Rows: ' + str(rows) + ' | Columns: ' + str(columns))
    
    df = df.replace('M', np.nan)
    missing_value_count = df.isna().sum().sum()
    total_values = rows*(columns-3)
    print("Total missing value count: " + str(missing_value_count))
    percentage = (missing_value_count/total_values)
    print('Percentage of missing values: ' + str(percentage))
    
    #print('location list: ')
    '''
    location_list = set()
    for loc in df['location'].unique():
        location_list.add(loc)
    print(location_list)
    print('county counts:')
    '''
    
    county_df = df['county']
    #print(county_df)
    county_df = county_df.value_counts()
    print(county_df)

    #print(df['location'].unique())
    '''
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.relplot(x='Annual', y='Year', data=df, ax=ax)
    ax.set_xlim(10, 80)
    plt.show()
    '''
    

def plot_annual_temperature_by_county(df_temp):
    plot_data = df_temp.assign(
        Annual=pd.to_numeric(df_temp['Annual'], errors='coerce')
    )
    county_year = (
        plot_data.pivot_table(
            index='county',
            columns='Year',
            values='Annual',
            aggfunc='mean',
        )
        .sort_index()
    )

    fig, ax = plt.subplots(figsize=(8, 8), constrained_layout=True)
    sns.heatmap(
        county_year,
        ax=ax,
        cmap='viridis',
        mask=county_year.isna(),
        cbar_kws={'label': 'Mean annual temperature'},
    )
    ax.set(title='Mean annual temperature by county', xlabel='Year', ylabel='County')

    plt.show()
    

def plot_location_by_county(df_temp):
    df_temp = df_temp[['county', 'location']]
    df_temp = df_temp.drop_duplicates()
    location_count = df_temp.groupby('county').count()
    #print(type(location_count))
    fig, ax = plt.subplots(figsize=(8, 8), constrained_layout=True)
    sns.barplot(
        ax = ax,
        x=location_count['location'],
        y=location_count.index,
    )
    ax.set(title='Number of locations by county', ylabel='County', xlabel='Number of locations')
    
    plt.show()
    
    

def sorting_annual_data(df, pd):
    df = df['Annual']
    df = df.replace('M', np.nan)
    df = df.dropna()
    #df['Annual'] = pd.to_numeric(df['Annual'], errors='coerce')
    df = df.sort_values(ascending=True)
    df = pd.to_numeric(df)
    #print(list(df))
    return (list(df))


def median(numbers):
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


def five_number_summary(numbers):
    """
    Given a sorted list of numbers, returns a tuple of the five-number
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

    print('Mean: ' + str(mean))
    print('Standard Deviation: ' + str(pop_sd))
    print('Minimum: ' + str(numbers[0]))
    print('First quartile: ' + str(median(lower_half)))
    print('Median: ' + str(median(numbers)))
    print('Third quartile: ' + str(median(upper_half)))
    print('Maximum: ' + str(numbers[-1]))


def adding_GHG_data(temp_df, GHG_df):
    GHG_df = GHG_df[['County', 'Year', 'Reported Emissions (MTCO2e)']]
    return temp_df
    


def main():
    print('hi')

    print('Temperature stuff: ')
    df_temp = pd.read_csv(file_temp)
    print(df_temp)
    dataset_information(df_temp, pd)
    sorted_annual_temps = sorting_annual_data(df_temp, pd)
    print('Seven number summary for annual temperatures: ')
    five_number_summary(sorted_annual_temps)
    
    # plotting data
    #plot_annual_temperature_by_county(df_temp)
    #plot_location_by_county(df_temp)
    
    # Adding GHG data to temperature data
    GHG_df = pd.read_csv('GHG Data/GHG_Reporting_Program_Publication_processed.csv')
    new_temp_df = adding_GHG_data(df_temp, GHG_df)
    
    print(new_temp_df)
    new_temp_df.to_csv('temporary.csv', index=False)


    print('Precipitation stuff: ')
    df_prec = pd.read_csv(file_prec)
    #dataset_information(df_prec, pd)

    '''
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