class CalculateExitExeption(Exception):
    pass


def input_int_number() -> int:
    while True:
        try:
            number = int(input("Введите целое число: "))
            return number
        except ValueError:
            print("Нужно ввести целое число! Попробуйте еще раз")


def calculate(left: int, right: int, operation: str):
    if operation == "!":
        raise CalculateExitExeption("Завершаем программу")
    if operation in ["+", "-", "*", "/"]:
        return eval(str(left) + operation + str(right))
    else:
        raise ValueError(f"Неподдерживаемая операция {operation}")


def main():
    while True:
        number1 = input_int_number()
        number2 = input_int_number()
        try:
            operation = input("Введите операцию (+, -, *, /) :")
            print(calculate(number1, number2, operation))
        except ArithmeticError as e:
            print(f"Неверно ({e}), арифметическая ошибка!")
        except CalculateExitExeption:
            print("Завершаю программу")
            break


if __name__ == '__main__':
    main()
