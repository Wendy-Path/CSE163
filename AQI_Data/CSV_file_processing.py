import csv

FILE_PREFIX = "Original CSV Files/annual_aqi_by_county"

def find_common_counties_each_year(start_year, end_year, FILE_PREFIX):
    counties_each_year = []

    for year in range(start_year, end_year + 1):  # Loops from start_year up to end_year (inclusive)
        filename = f"{FILE_PREFIX}_{year}.csv"
        year_counties = set()
        
        with open(filename, "r", newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            
            for row in reader:
                if row and row[0] == "Washington":
                    year_counties.add(row[1])  # index 1 is County
                    
        counties_each_year.append(year_counties)

    # Keep ONLY counties that appear in EVERY single year
    common_counties = set.intersection(*counties_each_year)
    return common_counties


def all_washington_rows_with_common_counties(common_counties):
    """
    This function reads all the annual AQI CSV files for Washington state from 2012 to 2024,
    and writes all rows corresponding to the common counties into a new CSV file.

    Parameters:
    common_counties (set): A set of counties that are present in every year's data.
    """
    with open("annual_aqi_by_county_washington_all.csv", "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        header_written = False  # Track whether we have written the header yet

        for year in range(2012, 2025):  # Loops from 2012 up to 2024 (13 files)
            filename = f"Original CSV Files/annual_aqi_by_county_{year}.csv"
            
            with open(filename, "r", newline="", encoding="utf-8") as infile:
                reader = csv.reader(infile)
                header = next(reader, None)  # Read the header of the current file
                
                # Write the header ONLY from the very first file
                if not header_written and header:
                    writer.writerow(header)
                    header_written = True
                    
                # Write all Washington rows from the current file
                for row in reader:
                    if row and row[0] == "Washington" and row[1] in common_counties:
                        writer.writerow(row)


def main():
    
    common_counties = find_common_counties_each_year(2012, 2024, FILE_PREFIX)
    all_washington_rows_with_common_counties(common_counties)

if __name__ == "__main__":
    main()