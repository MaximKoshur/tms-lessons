sum = 0
for i in range(0,101):
    sum+=i
print(f'1:{sum}')

sum = 0
for i in range(100,1001):
    sum+=i
print(f'2:{sum}')


sum = 0
for i in range(100,1001,2):
    sum+=i
print(f'3:{sum}')



sum = 1
for i in range(1,11):
    sum*=i
print(f'4:{sum}')


sum = 1
for i in range(10):
    sum*=2
print(f'5:{sum}')


sum = 0
for i in range(0,1001):
    sum +=i
    if sum >= 1000:
        break
print(f'6:{sum,i}')

