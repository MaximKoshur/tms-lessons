from Task_01 import input_list
def my_map():
    lst = list(map(lambda num: round(num/100), input_list()))
    print(lst)


my_map()