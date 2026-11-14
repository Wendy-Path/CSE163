import csv

counties_each_year = []

for year in range(2012, 2025):  # Loops from 2012 up to 2024 (13 files)
    filename = f"annual_aqi_by_county_{year}.csv"
    year_counties = set()
    
    with open(filename, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        
        for row in reader:
            if row and row[0] == "Washington":
                year_counties.add(row[1])  # index 1 is County
                
    counties_each_year.append(year_counties)

# Keep ONLY counties that appear in EVERY single year
common_counties = set.intersection(*counties_each_year)

with open("annual_aqi_by_county_washington_all.csv", "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    header_written = False  # Track whether we have written the header yet

    for year in range(2012, 2025):  # Loops from 2012 up to 2024 (13 files)
        filename = f"annual_aqi_by_county_{year}.csv"
        
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