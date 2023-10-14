from functools import reduce
from Task_01 import input_list
def red():
    result = reduce(lambda x,y: x*y,input_list(),1)
    print(result)
red()