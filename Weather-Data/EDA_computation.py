import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

file_temp = 'Weather-Data/all_temp_data.csv'
file_prec = 'Weather-Data/all_prec_data.csv'

def dataset_information(df, pd):
    rows = len(df)
    columns = len(df.columns)
    print('Rows: ' + str(rows) + ' | Columns: ' + str(columns))
    
    df = df.replace('M', np.nan)
    missing_value_count = df.isna().sum().sum()
    total_values = rows*(columns-4)
    print("Total missing value count: " + str(missing_value_count))
    percentage = (missing_value_count/total_values)
    print('Percentage of missing values: ' + str(percentage))
    
    #print('location list: ')
    location_list = set()
    for loc in df['location'].unique():
        #print(loc)
        location_list.add(loc)
    return location_list
    #print(df['location'].unique())

    
    #sns.relplot(x='Year', y='Annual', data=df)
    #plt.show()

def main():
    print('hi')

    print('Temperature stuff: ')
    df_temp = pd.read_csv(file_temp)
    location_list_temp = dataset_information(df_temp, pd)
    
    
    
    print('Precipitation stuff: ')
    df_prec = pd.read_csv(file_prec)
    #dataset_information(df_prec, pd)
    location_list_prec = dataset_information(df_prec, pd)
    
    diff = location_list_temp.difference(location_list_prec)
    print('Locations in temperature data but not in precipitation data: ')
    for loc in diff:
        print(loc)
        
    diff2 = location_list_prec.difference(location_list_temp)
    print('Locations in precipitation data but not in temperature data: ')
    for loc in diff2:
        print(loc)

if __name__ == '__main__':
    main()