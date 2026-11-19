"""
This program reads all the annual AQI CSV files for the United States from
2012 to 2024. It creates a new CSV file that contains all rows corresponding
to Washington state which have counties that are present in every year's data.
"""
import csv

FILE_PREFIX = "Original CSV Files/annual_aqi_by_county"


def find_common_counties_each_year(start_year: int,
                                   end_year: int,
                                   FILE_PREFIX: str) -> set[str]:
    """
    This function reads all the annual AQI CSV files from start_year(int)
    to end_year(int) and returns a set of counties(str) that are present in
    every year's data for Washington state."
    """
    counties_each_year = []

    for year in range(start_year, end_year + 1):
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


def all_washington_rows_with_common_counties(common_counties: set[str],
                                             FILE_PREFIX: str, start_year: int,
                                             end_year: int,
                                             output_file: str) -> None:
    """
    This function reads all the annual AQI CSV files from start_year(int)
    to end_year(int), and writes all rows with the State set to Washington
    and County in the common counties(a set of Strings) into a new CSV file
    with name output_file.
    """

    with open(output_file, "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        header_written = False  # Track whether we have written the header yet

        for year in range(start_year, end_year + 1):
            filename = f"{FILE_PREFIX}_{year}.csv"

            with open(filename, "r", newline="", encoding="utf-8") as infile:
                reader = csv.reader(infile)
                header = next(reader, None)

                # Write the header ONLY from the very first file
                if not header_written and header:
                    writer.writerow(header)
                    header_written = True

                # Write all Washington rows from the current file
                for row in reader:
                    if (row and row[0] == "Washington"
                            and row[1] in common_counties):
                        writer.writerow(row)


def main():

    common_counties = find_common_counties_each_year(2012, 2024, FILE_PREFIX)
    all_washington_rows_with_common_counties(
        common_counties,
        FILE_PREFIX, 2012, 2024,
        "annual_aqi_by_county_washington_all.csv"
        )


if __name__ == "__main__":
    main()
