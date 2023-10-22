month = int(input())
if month in [12,1,2]:
    print("winter")
elif month in [3,4,5]:
    print("spring")
elif month in [6, 7, 8]:
    print("summer")
else:
    print("autumn")