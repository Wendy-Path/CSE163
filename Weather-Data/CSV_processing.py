import pandas as pd
from pathlib import Path

#file = 'Weather-Data/Weather-Data-Files/temp/temp-csv/Temp-Aberdeen.csv'
#folder = 'Weather-Data/Weather-Data-Files/temp/temp-csv'
folder = 'Weather-Data/Weather-Data-Files/prec/prec-csv'

def df_formatting(pd, file):
    df = pd.read_csv(file)
    df = df.loc[0:12, :]
    df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    return df

def df_combining(pd, folder):
    df_all = pd.DataFrame()
    for file in Path(folder).glob('*'):
        df = df_formatting(pd, file)
        
        location_name = Path(file).stem
        #location_name = location_name.replace('Temp-', '')
        location_name = location_name.replace('Prec-', '')
        df['location'] = location_name
        df = df.set_index(['location', 'Year'])
            
        df_all = pd.concat([df_all, df])
    print(df_all)
    return df_all
    
    

def main():
    print('hi')
    
    df = df_combining(pd, folder)
    #df.to_csv('all_temp_data.csv')
    df.to_csv('all_prec_data.csv')
    
    
    
    

    
if __name__ == '__main__':
    main()
    