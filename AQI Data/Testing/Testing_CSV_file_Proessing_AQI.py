import CSV_file_processing

FILE_PREFIX = "Testing/Original CSV Files/annual_aqi_by_county"

def main():
    common_counties = CSV_file_processing.find_common_counties_each_year(2023, 2024, FILE_PREFIX)
    CSV_file_processing.all_washington_rows_with_common_counties(common_counties)