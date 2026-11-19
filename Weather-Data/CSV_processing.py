'''
Wendy Barben
CSE 163
This program processes the individual csv files for temperature and
precipitation data into one csv file for each, then adds counties
and GHG data to temperature data and filters rows with no emmisions data
'''

import pandas as pd
from pathlib import Path

# file = 'Weather-Data/Weather-Data-Files/temp/temp-csv/Temp-Aberdeen.csv'
# 1/3 toggles for weather and precipication
folder = 'Weather-Data/Weather-Data-Files/temp/temp-csv'
# folder = 'Weather-Data/Weather-Data-Files/prec/prec-csv'

counties = {
        'Adams': ['RitzVille-1SSE', 'Lind-3NE'],
        'Asotin': ['Asotin-14SW'],
        'Benton': ['Prosser', 'Richland', 'Kennewick'],
        'Chelan': ['Leavenworth', 'Stehekin-4NW', 'Wenatchee', 'Plain',
                   'Chelan', 'HoldenVillage', 'EntiatFishHatchery'],
        'Clallam': ['QuillayuteAP', 'Forks', 'PortAngelesFairChildIntlAP',
                    'Sequim-2E'],
        'Clark': ['Vancouver', 'BattleGround'],
        'Columbia': ['Dayton-1WSW'],
        'Cowlitz': ['Longview', 'Cougar', 'KalamaFallsHatchery'],
        'Douglas': ['WenatcheePangbornMemorialAP', 'ChiefJosephDam',
                    'Waterville'],
        'Ferry': ['Republic'],
        'Franklin': ['IceHarborDam'],
        'Garfield': ['Pomeroy'],
        'Grant': ['CouleeDam-1SW', 'EphrataAP', 'PriestRapidsDam', 'Quincy'],
        'Grays Harbor': ['HumptulipSalmonHatchery', 'Aberdeen', 'Elma',
                         'HoquiamBowermanAP'],
        'Island': [],
        'Jefferson': ['Chimacum-4S', 'Quilcene-2SW'],
        'King': ['MudMountainDam', 'SeattleBoeingField', 'Landsburg',
                 'Palmer-3ESE', 'RentonMunicipalAP',
                 'ToltSouthForkReservoir', 'CedarLake',
                 'SeattleTacomaAP', 'Kent', 'SnoqualmieFalls', 'Baring'],
        'Kitsap': ['Bremerton', 'Poulsbo-1NW'],
        'Kittitas': ['Ellensburg', 'CleElum', 'Easton'],
        'Klickitat': ['Snowden', 'MountAdamsRS', 'Goldendale',
                      'DallesportAP', 'Bickleton'],
        'Lewis': ['MayfieldPowerPlant', 'Centralia', 'Dryad'],
        'Lincoln': ['Odessa', 'Wilbur', 'Harrington', 'DavenPort'],
        'Mason': ['SheltonAP', 'CushmanPowerhouse2', 'Matlock-8S'],
        'Okanogan': ['Conconully', 'Mazama', 'Methow-2S', 'Winthrop-1WSW'],
        'Pacific': ['Naselle-2ENE', 'Naselle', 'Raymond-2S'],
        'Pend Oreille': ['Newport', 'BoundaryDam'],
        'Pierce': ['RainierParadiseRS', 'LongmireRainierNPS', 'TacomaNo1',
                   'McmillinReservoir'],
        'San Juan': [],
        'Skagit': ['ConcretePplFishStation', 'SedroWoolley'],
        'Skamania': [],
        'Snohomish': ['Everett', 'EverettSnohomishCountyAP',
                      'DarringtonRangerStation', 'Startup-1E', 'Monroe'],
        'Spokane': ['SpokaneWFO', 'SpokaneInternationalAP', 'DeerParkAP'],
        'Stevens': ['Chewelah', 'Northport', 'Colville-5NE', 'Colville'],
        'Thurston': ['OlympiaAP'],
        'Wahkiakum': [],
        'Walla Walla': ['WhitmanMission', 'WallaWallaRegionalAP',
                        'MillCreekDam'],
        'Whatcom': ['Bellingham-3SSW', 'Clearbrook', 'UpperBakerDam',
                    'DiabloDam', 'Blaine', 'RossDam', 'Bellingham-INTL',
                    'Newhalem'],
        'Whitman': ['Pullman-2NW', 'Rosalia', 'Lacrosse', 'StJohn'],
        'Yakima': ['Selah-2NE', 'YakimaAP', 'Sunnyside1', 'Sunnyside2']
    }


def df_formatting(file: str) -> pd.DataFrame:
    """
    Returns a dataframe without the empty columns from the given csv file
    """
    df = pd.read_csv(file)
    df = df.loc[0:12, :]
    df.drop(
        df.columns[
            df.columns.str.contains('unnamed', case=False)],
        axis=1, inplace=True)
    return df


def df_combining(folder) -> pd.DataFrame:
    """
    Returns a dataframe that contains all the csv file data in the given
    folder and adds the county based on the location
    """
    df_all = pd.DataFrame()
    for file in Path(folder).glob('*'):
        df = df_formatting(file)

        location_name = Path(file).stem
        # 2/3 toggles for weather and precipication
        location_name = location_name.replace('Temp-', '')
        # location_name = location_name.replace('Prec-', '')
        df['location'] = location_name
        df['county'] = df['location'].map(lambda x: get_county(x, counties))
        # df = df.set_index(['location', 'Year'])

        df_all = pd.concat([df_all, df])
    print(df_all)
    return df_all


def get_county(location: str, counties: dict) -> str | None:
    """
    If the given location is in the dictionary of counties,
    returns the county. If it is not, return None
    """
    for county, locations in counties.items():
        if location in locations:
            return county
    return None


# These are calculations for only temperature, not including precipitation
def adding_GHG_data(temp_df: pd.DataFrame, GHG_df: pd.DataFrame
                    ) -> pd.DataFrame:
    """
    Returns the temperature dataframe with the total emmisions by county from
    the GHG dataframe data county added
    """
    emissions_column = 'Reported Emissions (MTCO2e)'
    county_emissions = GHG_df[['County', 'Year', emissions_column]].copy()
    county_emissions[emissions_column] = pd.to_numeric(
        county_emissions[emissions_column]
        .astype('string')
        .str.replace(',', '', regex=False),
        errors='raise')

    county_emissions = (
        county_emissions.groupby(['County', 'Year'], as_index=False)
        [emissions_column]
        .sum()
        .rename(columns={
            'County': 'county',
            emissions_column: 'County Emissions (MTCO2e)'}))

    return temp_df.merge(
        county_emissions,
        how='left',
        on=['county', 'Year'],
        validate='many_to_one',)


def filtering_GHG_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns the given dataframe without rows that do not have County
    Emissions (MTCO2e) data
    """
    df = df[df['County Emissions (MTCO2e)'] > 0]
    df = df.dropna(subset=['County Emissions (MTCO2e)'])
    return df


def main():
    print('hi')

    df = df_combining(folder)
    df = df.set_index(['county', 'location', 'Year'])
    print(df)
    # 3/3 toggles for weather and precipication
    # df.to_csv('all_temp_data_counties.csv')
    # df.to_csv('all_prec_data_counties.csv')

    # Adding GHG data to temperature data
    df_temp = pd.read_csv('Weather-Data/all_temp_data_counties.csv')
    GHG_df = pd.read_csv(
        'GHG Data/GHG_Reporting_Program_Publication_processed.csv')
    new_temp_df = adding_GHG_data(df_temp, GHG_df)

    print(new_temp_df)

    new_temp_df = pd.read_csv('Weather-Data/combined_temp_GHG.csv')
    new_temp_df = filtering_GHG_data(new_temp_df)
    print(new_temp_df)

    # This code is temporary information that does not need to be run again
    # unless data changes
    '''
    new_temp_df.to_csv('combined_temp_GHG_filtered.csv', index=False)

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
