import pandas as pd
from pathlib import Path

#file = 'Weather-Data/Weather-Data-Files/temp/temp-csv/Temp-Aberdeen.csv'
# 1/3 toggles for weather and precipication
#folder = 'Weather-Data/Weather-Data-Files/temp/temp-csv'
folder = 'Weather-Data/Weather-Data-Files/prec/prec-csv'

counties = {
        'Adams': ['RitzVille-1SSE', 'Lind-3NE'],
        'Asotin': ['Asotin-14SW'],
        'Benton': ['Prosser', 'Richland', 'Kennewick'],
        'Chelan': ['Leavenworth', 'Stehekin-4NW', 'Wenatchee', 'Plain', 'Chelan', 'HoldenVillage', 'EntiatFishHatchery'],
        'Clallam': ['QuillayuteAP', 'Forks', 'PortAngelesFairChildIntlAP', 'Sequim-2E'],
        'Clark': ['Vancouver', 'BattleGround'],
        'Columbia': ['Dayton-1WSW'],
        'Cowlitz': ['Longview', 'Cougar', 'KalamaFallsHatchery'],
        'Douglas': ['WenatcheePangbornMemorialAP', 'ChiefJosephDam', 'Waterville'],
        'Ferry': ['Republic'],
        'Franklin': ['IceHarborDam'],
        'Garfield': ['Pomeroy'],
        'Grant': ['CouleeDam-1SW', 'EphrataAP', 'PriestRapidsDam', 'Quincy'],
        'Grays Harbor': ['HumptulipSalmonHatchery', 'Aberdeen', 'Elma', 'HoquiamBowermanAP'],
        'Island': [],
        'Jefferson': ['Chimacum-4S', 'Quilcene-2SW'],
        'King': ['MudMountainDam', 'SeattleBoeingField', 'Landsburg', 'Palmer-3ESE', 'RentonMunicipalAP', 'ToltSouthForkReservoir', 'CedarLake', 'SeattleTacomaAP', 'Kent', 'SnoqualmieFalls', 'Baring'],
        'Kitsap': ['Bremerton', 'Poulsbo-1NW'],
        'Kittitas': ['Ellensburg', 'CleElum', 'Easton'],
        'Klickitat': ['Snowden', 'MountAdamsRS', 'Goldendale', 'DallesportAP', 'Bickleton'],
        'Lewis': ['MayfieldPowerPlant', 'Centralia', 'Dryad'],
        'Lincoln': ['Odessa', 'Wilbur', 'Harrington', 'DavenPort'],
        'Mason': ['SheltonAP', 'CushmanPowerhouse2', 'Matlock-8S'],
        'Okanogan': ['Conconully', 'Mazama', 'Methow-2S', 'Winthrop-1WSW'],
        'Pacific': ['Naselle-2ENE', 'Naselle', 'Raymond-2S'],
        'Pend Oreille': ['Newport', 'BoundaryDam'],
        'Pierce': ['RainierParadiseRS', 'LongmireRainierNPS', 'TacomaNo1', 'McmillinReservoir'],
        'San Juan': [],
        'Skagit': ['ConcretePplFishStation', 'SedroWoolley'],
        'Skamania': [],
        'Snohomish': ['Everett', 'EverettSnohomishCountyAP', 'DarringtonRangerStation', 'Startup-1E', 'Monroe'],
        'Spokane': ['SpokaneWFO', 'SpokaneInternationalAP', 'DeerParkAP'],
        'Stevens': ['Chewelah', 'Northport', 'Colville-5NE', 'Colville'],
        'Thurston': ['OlympiaAP'],
        'Wahkiakum': [],
        'Walla Walla': ['WhitmanMission', 'WallaWallaRegionalAP', 'MillCreekDam'],
        'Whatcom': ['Bellingham-3SSW', 'Clearbrook', 'UpperBakerDam', 'DiabloDam', 'Blaine', 'RossDam', 'Bellingham-INTL', 'Newhalem'],
        'Whitman': ['Pullman-2NW', 'Rosalia', 'Lacrosse', 'StJohn'],
        'Yakima': ['Selah-2NE', 'YakimaAP', 'Sunnyside1', 'Sunnyside2']
    }

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
        # 2/3 toggles for weather and precipication
        #location_name = location_name.replace('Temp-', '')
        location_name = location_name.replace('Prec-', '')
        df['location'] = location_name
        df['county'] = df['location'].map(lambda x: get_county(x, counties))
        #df = df.set_index(['location', 'Year'])
            
        df_all = pd.concat([df_all, df])
    print(df_all)
    return df_all


def get_county(location, counties):
    for county, locations in counties.items():
        if location in locations:
            return county
    return None


def main():
    print('hi')
    
    df = df_combining(pd, folder)
    df = df.set_index(['county', 'location', 'Year'])
    print(df)
    # 3/3 toggles for weather and precipication
    #df.to_csv('all_temp_data_counties.csv')
    df.to_csv('all_prec_data_counties.csv')
    

if __name__ == '__main__':
    main()
    