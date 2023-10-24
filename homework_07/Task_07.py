import csv
header = ('name', 'surname', 'gender')
my = list(input().split())
with open('file_07.csv','w') as f:
    writer  = csv.writer(f, delimiter=",")
    writer.writerow(header)
    writer.writerow(my)