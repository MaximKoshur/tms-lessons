def filter_negative_numbers(*args):
    return (list(filter(lambda x: int(x) >= 0, *args)))

print(filter_negative_numbers(input().split()))
