def is_year_leap(year):
    if year%400==0:
        return(True)
    elif year%100==0:
        return(False)
    elif year%4==0:
        return(True)
    else:
        return(False)

print(is_year_leap(int(input())))