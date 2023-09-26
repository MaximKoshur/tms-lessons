import random
number = random.randint(1,5)
a = int(input("Input number "))
while a!=number:
    print("Not true")
    a=int(input("Input number "))
print("Congratulations")