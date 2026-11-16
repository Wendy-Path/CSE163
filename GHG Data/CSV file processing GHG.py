import csv 

counties_each_year = {}

for i in range(2012, 2025):  # Assuming years from 2012 to 2024
    counties_each_year[i] = set()

with open("GHG_Reporting_Program_Publication_20261022.csv", "r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    next(reader)
    
    for row in reader:
        counties_each_year[int(row[1])].add(row[8])  # index 1 is Year, index 8 is County            

# Keep ONLY counties that appear in EVERY single year
common_counties = set.intersection(*counties_each_year.values())

with open("GHG_Reporting_Program_Publication_20261022.csv", "r", newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    header = next(reader, None)  # Read the header row

    with open("GHG_Reporting_Program_Publication_processed.csv", "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        header_written = False  # Track whether we have written the header yet
    

        # Write the header ONLY from the very first file
        if not header_written and header:
            writer.writerow(header)
            header_written = True
        
        # Write all Washington rows from the current file
        for row in reader:
            if row and row[8] in common_counties:
                writer.writerow(row)