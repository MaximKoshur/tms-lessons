import copy

import test

a = test.generate_list(10)
print(a)


def bubble_sort(a):
    lst = copy.deepcopy(a)
    for k in range(len(lst)):
        for i in lst:
            if i < lst[lst.index(i) - 1] and lst.index(i) != 0:
                print(f"index i - {lst.index(i)}")
                print(f"number i - {lst[lst.index(i)]}")
                buf = i
                lst[lst.index(i)] = lst[lst.index(i)-1]
                print(lst)
                lst[lst.index(i) - 1] = buf
                print(lst)
    return lst


# if __name__ == '__main__':
#     test.test_sort(bubble_sort)
print(bubble_sort(a))
