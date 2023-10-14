from Task_01 import input_list
def filt():
    listok = input_list()
    print(listok)
    lst = list(filter(lambda num: num > 0,listok))
    print(f'Kolichestvo +:{len(lst)}')
    lst = list(filter(lambda num: num < 0, listok))
    print(f'Kolichestvo -:{len(lst)}')
    lst = list(filter(lambda num: num == 0, listok))
    print(f'Kolichestvo 0:{len(lst)}')
filt()