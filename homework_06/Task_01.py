def map_to_tuple(lst):
    return list(map(lambda letter: (letter.upper(), letter.lower()), lst))
lst = input().split()
print(map_to_tuple(lst))
