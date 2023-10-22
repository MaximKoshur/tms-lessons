my_dict = {'a':1,'b':2,'c':7,'d':4}
max = 0
for value in tuple(my_dict.values()):
    if value>max:
        max = value
print(max)
