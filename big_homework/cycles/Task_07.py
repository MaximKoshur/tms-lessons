my_dict = {'a':1,'b':2,'c':7,'d':19}
max = 0
k = 0
for key, value in my_dict.items():
    if value>max:
        max = value
        k = key
print(k)
