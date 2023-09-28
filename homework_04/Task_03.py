a=0
for i in range(0,101):
    if a == 'yes':break
    print(i)
    while True:
        a = input("Should we break? ")
        if a =='yes':
            break
        elif a == 'no':
            break
        else:
            print('Dont understand you')






