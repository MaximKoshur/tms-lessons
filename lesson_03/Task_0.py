time = int(input())
days = time // (3600*24)
time = time - days*3600*24
hours = time//3600
time = time - hours*3600
minuti = time//60
time = time - minuti*60
sek = time % 60

print(str(days) + ":" + str(hours) + ":" + str(minuti) + ":" + str(sek))
