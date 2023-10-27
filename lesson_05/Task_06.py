def list_sum(*list):
    sum = 0
    for i in list:
        sum += i
    return (sum)

list = [1,2,3,4,5,6]
print(list_sum(*list))