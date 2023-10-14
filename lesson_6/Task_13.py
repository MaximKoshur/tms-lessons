def check_types(original_func):
    def update_func(arg1, arg2):
        if isinstance(arg1, int):
            print("Expected int type")
            return 123
        if isinstance(arg2, int):
            print("Expected int type")
            return 123
        original_func(arg1, arg2)
        return update_func


@check_types
def plus(x, y):
    return x + y


@check_types
def minus(x, y):
    return x - y


@check_types
def mult(x, y):
    return x * y


@check_types
def div(x: int, y: int):
    return x / y


minus(4, 2)
