import random
print(random.randint(0,100))
while True:

    a = input("Should we break? ")
    if a =='yes':
        break
    elif a == 'no':
        print(random.randint(0, 100))
    else:
        print('Dont understand you')






