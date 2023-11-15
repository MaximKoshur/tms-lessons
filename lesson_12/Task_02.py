class SquaresIterable:
    def __init__(self, count):
        self.count = count
        self.current_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_number += 1
        if self.current_number > self.count:
            raise StopIteration()
        return self.current_number ** 2


for i in SquaresIterable(10):
    print(i)
