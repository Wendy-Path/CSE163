import pandas as pd
import tabula as tb

file_name = 'weather/temp/Temp-BattleGround.pdf'

def convert_pdf2csv(tb, file):
    #use batch?
    df = tb.read_pdf(file, output_path='weather/temp/', pages=1, format='CSV')

def main():
    print('hi')
    convert_pdf2csv(tb, file_name)
    
if __name__ == '__main__':
    main()