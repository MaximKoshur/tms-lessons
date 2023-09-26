import random
number = random.randint(0, 101)
while True:
    a = int(input())
    if a == number:
        print("Congratulations!")
        break
    elif a > number:
        print("The number is lower")
    elif a < number:
        print("The number is bigger")