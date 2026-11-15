import pandas as pd
import tabula as tb
from pathlib import Path

#file_name = 'weather/temp/Temp-BattleGround.pdf'
folder = 'Weather-Data/Weather-Data-Files/temp/temp-pdf/'

def convert_pdf2csv(tb, folder):
    #use batch?
    df = tb.convert_into_by_batch(folder, 
                     output_format='csv', pages=1, lattice=True)

def main():
    print('hi')
    convert_pdf2csv(tb, folder)
    
if __name__ == '__main__':
    main()