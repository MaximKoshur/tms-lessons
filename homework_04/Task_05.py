number = input()
length = 0

for i in number:
    length += 1

number = int(number)
sum =0
for i in range(1,length):
    buff = number%10
    sum += buff
    number = (number - buff)/10

sum +=number
print(f'Sum of numbers is {int(sum)}')