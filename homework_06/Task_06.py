from functools import reduce
def my_decorator(original_func):
    def update_func(*args,**kwargs):
        print(f'Функция получила на вход значение {args} и {kwargs}')
        result = original_func(*args,**kwargs)
        print('Результат функции:', result)
        return result

    return update_func


@my_decorator
def my_func(*args, **kwargs):
    a = int(reduce(lambda x, y: x + y, args, 0))
    b = int(reduce(lambda x, y: x + y, tuple(kwargs.values()), 0))
    return (a+b)


print('x =', my_func(1, 2, d=3, c=4))
