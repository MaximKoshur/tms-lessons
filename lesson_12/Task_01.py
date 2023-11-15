import re


def is_car_number(number: str) -> bool:
    return re.fullmatch("\d{4}[A-Z]{2}-\d", number) is not None
def is_phone_number(number:str)->bool:
    return re.fullmatch("\+\d{3} \((25|29|44|33)\) \d{3}-\d{2}-\d{2}", number) is not None



if __name__ == "__main__":
    print(is_car_number("1234AB-5"))
    print(is_phone_number("+375 (44) 123-45-67"))
