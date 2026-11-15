import pandas as pd
import tabula as tb
from pathlib import Path


temp_pdf_folder = 'Weather-Data/Weather-Data-Files/temp/temp-pdf/'
temp_csv_folder = 'Weather-Data/Weather-Data-Files/temp/temp-csv/'

prec_pdf_folder = 'Weather-Data/Weather-Data-Files/prec/prec-pdf/'
prec_csv_folder = 'Weather-Data/Weather-Data-Files/prec/prec-csv/'

def convert_pdf2csv(tb, folder):
    df = tb.convert_into_by_batch(folder, output_format='csv', pages=1, lattice=True)

def file_mover(folder1, folder2):
    for file in Path(folder1).glob('*.csv'):
        file.move_into(folder2)
    

def main():
    print('hi')
    #convert_pdf2csv(tb, temp_pdf_folder)
    #file_mover(temp_pdf_folder, temp_csv_folder)
    convert_pdf2csv(tb, prec_pdf_folder)
    file_mover(prec_pdf_folder, prec_csv_folder)
    
if __name__ == '__main__':
    main()