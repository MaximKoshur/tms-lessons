def generate_squares(count):
    start = 1
    while start <= count:
        yield start ** 2
        start += 1


for i in generate_squares(10):
    print(i)
