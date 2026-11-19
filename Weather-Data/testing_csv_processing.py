"""
Wendy Barben
CSE 163
This program tests the CSV_processing file
"""
import CSV_processing


def test_get_county():
    """
    Tests the get_county function
    """
    assert CSV_processing.get_county(
        'Republic', CSV_processing.counties) == 'Ferry'
    assert CSV_processing.get_county(
        'Clearbrook', CSV_processing.counties) == 'Whatcom'
    assert CSV_processing.get_county(
        'ConcretePplFishStation', CSV_processing.counties) == 'Skagit'


def main():
    test_get_county()
    print('hi')


if __name__ == '__main__':
    main()
