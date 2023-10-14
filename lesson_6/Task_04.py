from Task_01 import input_list
def my_map():
    lst = list(map(lambda num: str(num),input_list()))
    print(lst)
my_map()