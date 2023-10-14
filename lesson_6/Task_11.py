from functools import reduce
from Task_01 import input_list
def red():
    result = reduce(lambda x,y: min(x,y),input_list())
    print(result)
red()