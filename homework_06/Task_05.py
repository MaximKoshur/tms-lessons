def my_decorator(original_func):
    def update_func(x):
        print(f'Функция получила на вход значение {x}')
        result = original_func(x)
        print('Результат функции:', result)
        return result
    return update_func
@my_decorator
def my_func(x):
     return x**3

print('x =',my_func(int(input())))
