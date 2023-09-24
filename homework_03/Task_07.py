number = int(input())
if number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
    print(True)
else:
    print(number%2!=0 and number%3!=0 and number%5!=0 and number%7!=0)