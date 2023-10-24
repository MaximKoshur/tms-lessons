import csv
header = ('name', 'surname', 'gender')
my = ('Maxim', 'Koshur', 'warhelicopter')
with open('file_06.csv','w') as f:
    writer  = csv.writer(f, delimiter=",")
    writer.writerow(header)
    writer.writerow(my)