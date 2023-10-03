def is_year_leap(year):
    if year%400==0:
        print(True)
    elif(year%100==0):
        print(False)
    else:
        print(True)

is_year_leap(int(input()))