lst = input().split()
max = 0
for i in lst:
    if int(i)>max:
        max= int(i)
print(max)