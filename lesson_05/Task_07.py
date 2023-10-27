def sum_and_max(*args):
    s = sum(args)
    m = max(args)
    return(s,m)
list = [5,4,2,6,8,6,4,9]
print(sum_and_max(*list))