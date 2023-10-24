import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Age'
sheet['A2'] = 'Maxim'
sheet['B2'] = 'Koshur'
sheet['C2'] = 'M'

wb.save("file_09.xlsx")