from functools import reduce
def my_join(lst,znak):
    a=(str(reduce(lambda x,y:x+znak+y,lst)))
    return(a)
print(my_join(input().split(),input()))