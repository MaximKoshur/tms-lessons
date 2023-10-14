from Task_01 import input_list
def filt():
    lst=list(filter(lambda num: num>=0,input_list()))
    print(lst)
filt()