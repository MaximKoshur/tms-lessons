def filter_odd_numbers(*list):
    array = [i for i in list if i%2==0]
    return(array)
list = [34,7,12,33,98,97]
print(filter_odd_numbers(*list))