import csv
with open('file_07.csv','r') as f:
    f_reader = csv.reader(f, delimiter=",")
    index = 0
    for row in f_reader:
        if index != 0:
            print(row[1],row[0],row[2])
        index+=1