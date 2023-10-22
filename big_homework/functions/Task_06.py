def filter_negative_numbers(*args):
    return (list(filter(lambda x: int(x) >= 0, *args)))

def compare(x, y):
    if x > y:
        return (1)
    elif x < y:
        return (-1)
    else:
        return (0)

def simple_compare(x, y):
    return (x < y)

def my_sum(x, y):
    return (x + y)

def hello_world():
    print("Hello world!")

while True:
    task = input("Number of task from 1 to 5 or exit->  ")
    if task == '1':
        hello_world()
        hello_world()
        hello_world()
    elif task == '2':
        print(my_sum(int(input('First number ')), int(input('Second number '))))
    elif task == '3':
        print(simple_compare(int(input('First number ')), int(input('Second number '))))
    elif task == '4':
        print(compare(int(input('First number ')), int(input('Second number '))))
    elif task == '5':
        print(filter_negative_numbers(input("Enter the list of numbers ").split()))
    elif task == 'exit':
        exit()
    else:
        print("Unknown command")