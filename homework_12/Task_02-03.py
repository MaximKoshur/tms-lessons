import re


def is_date(date: str) -> bool:
    return re.fullmatch("\d{2}-\d{2}-\d{4}",date) is not None


def is_float_number(number: str) -> bool:
    return re.fullmatch("\d+\.\d+",number) is not None


print(is_date("11-11-1111"))
print(is_float_number("234.234"))