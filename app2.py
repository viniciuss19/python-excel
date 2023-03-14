import openpyxl

book = openpyxl.load_workbook('Planilha de Frutas.xlsx')
pagfrutas = book['Frutas']

for rows in pagfrutas.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        if cell.value == 'Banana':
            cell.value = 'Fruta 1'

book.save('Planilha de Frutasv2.xlsx')