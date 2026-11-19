"""
Wendy Barben
CSE 163
This program converts the pdf files for temperature and precipitation data
in their respective folders into csv files, then moves them to their
respective csv folders.
"""

import tabula as tb
from pathlib import Path

temp_pdf_folder = 'Weather-Data/Weather-Data-Files/temp/temp-pdf/'
temp_csv_folder = 'Weather-Data/Weather-Data-Files/temp/temp-csv/'

prec_pdf_folder = 'Weather-Data/Weather-Data-Files/prec/prec-pdf/'
prec_csv_folder = 'Weather-Data/Weather-Data-Files/prec/prec-csv/'


def convert_pdf2csv(folder):
    """
    This function converts the pdf files into csv files
    """
    tb.convert_into_by_batch(folder, output_format='csv', pages=1,
                             lattice=True)


def file_mover(folder1, folder2):
    """
    This function moves the csv files from the pdf folder to the csv folder
    """
    for file in Path(folder1).glob('*.csv'):
        file.move_into(folder2)


def main():
    print('hi')
    # These are commented out as this process does not need to run again
    '''
    convert_pdf2csv(tb, temp_pdf_folder)
    file_mover(temp_pdf_folder, temp_csv_folder)
    convert_pdf2csv(tb, prec_pdf_folder)
    file_mover(prec_pdf_folder, prec_csv_folder)
    '''


if __name__ == '__main__':
    main()
