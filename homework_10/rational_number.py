class Rational:
    def __init__(self, numeration, denominator):
        self.__numerator = numeration
        self.__denominator = denominator
        self.__normalize()

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __normalize(self):
        a = self.__numerator
        b = self.__denominator

        if b < 0:
            self.__denominator = b * -1
            self.__numerator = a * -1

        while b:
            a, b = b, a % b

        if self.__numerator % a == 0 and self.__denominator % a == 0:
            self.__numerator = self.__numerator / a
            self.__denominator = self.__denominator / a

    def __str__(self):
        return f"{int(self.__numerator)} / {int(self.__denominator)}"

    def __mul__(self, number2):
        return Rational(self.__numerator * number2.__numerator, self.__denominator * number2.__denominator)

    def __truediv__(self, number2):
        return Rational(self.__numerator * number2.__denominator, self.__denominator * number2.__numerator)

    def __add__(self, number2):
        return Rational((self.__numerator * number2.__denominator) + (self.__denominator * number2.__numerator),
                        self.__denominator * number2.__denominator)

    def __sub__(self, number2):
        return Rational((self.__numerator * number2.__denominator) - (self.__denominator * number2.__numerator),
                        self.__denominator * number2.__denominator)

    def __eq__(self, other):
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __ne__(self, other):
        return self.__numerator != other.__numerator or self.__denominator != other.__denominator

    def __lt__(self, other):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __gt__(self, other):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __le__(self, other):
        return self.__numerator * other.__denominator <= other.__numerator * self.__denominator

    def __ge__(self, other):
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator


if __name__ == "__main__":
    print(Rational(1, 4) * (Rational(3, 2) + Rational(1, 8)) + Rational(156, 100))
    print(Rational(1, -2))
    assert Rational(1, 2) == Rational(2, 4)
