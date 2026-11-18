"""
This file tests CSV_file_processing.py
"""

from AQI Data import CSV_file_processing

FILE_PREFIX = "Original CSV Files/annual_aqi_by_county"

def test_find_common_counties_each_year():
    assert {"Adams", "Asotin", "Benton"} == CSV_file_processing.find_common_counties_each_year(2023, 2024, FILE_PREFIX)

def test_all_washington_rows_with_common_counties():
    pass

def main():
    test_find_common_counties_each_year()

if __name__ == "__main__":
    main()