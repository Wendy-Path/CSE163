import csv 

def find_common_counties_each_year(start_year: int, end_year: int, file: str):
    counties_each_year = {}

    for i in range(start_year, end_year + 1):  # Assuming years from start_year to end_year
        counties_each_year[i] = set()

    with open(file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        next(reader)
        
        for row in reader:
            counties_each_year[int(row[1])].add(row[8])  # index 1 is Year, index 8 is County            

    # Keep ONLY counties that appear in EVERY single year
    common_counties = set.intersection(*counties_each_year.values())
    return common_counties


def rows_with_common_counties(common_counties: set[str],
                              input_file: str,
                              output_file: str) -> None:
    with open(input_file, "r", newline="", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        header = next(reader, None)  # Read the header row

        with open(output_file, "w", newline="", encoding="utf-8") as outfile:
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

def main():

    common_counties = find_common_counties_each_year(2012, 2024, "GHG_Reporting_Program_Publication_20261115.csv")
    rows_with_common_counties(common_counties, "GHG_Reporting_Program_Publication_20261115.csv", "GHG_Reporting_Program_Publication_processed.csv")

if __name__ == "__main__":
    main()