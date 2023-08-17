import xlsxwriter
from . парсинг_сайта_usastring import arrows_north
import pandas as pd

def writer(param):

    book = xlsxwriter.Workbook(r"C:\Users\Admin\Desktop\Запись парса с usastring.xlsx")
    page = book.add_worksheet('Описание струн')

    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)
    # page.set_column('E:E', 50)

    for item in param:
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        # page.write(row, column+4, item[4])
        row += 1

    book.close()
writer(arrows_north())