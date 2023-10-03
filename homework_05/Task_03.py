def generate_squares(*args):
    squares = []
    for i in args:
        squares.append(i**2)
    return squares
print(generate_squares(1,3,5,6,74,3))