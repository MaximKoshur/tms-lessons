import openpyxl

wb = openpyxl.Workbook()

sheet = wb.active
sheet['A1'] = 'Name'
sheet['B1'] = 'Surname'
sheet['C1'] = 'Age'
sheet['A2'] = input()
sheet['B2'] = input()
sheet['C2'] = input()

wb.save("file_10.xlsx")