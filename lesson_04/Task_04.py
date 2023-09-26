a = input('Is it moving? ')
b = input('Should it move? ')
if  a == 'yes' and b == 'yes':
    print("Don't touch")
elif a == 'no' and b == 'no':
    print("Don't touch")
elif a == 'yes' and b == 'no':
    print('Use glue')
else: print('Use oil')

