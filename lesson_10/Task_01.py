class MyTime:
    def __init__(self, seconds):
        self.seconds = seconds

    @property
    def hours(self) -> int:
        return int(self.seconds // 3600)

    @property
    def minutes(self):
        return int((self.seconds - self.hours*3600) // 60)

    def __mul__(self, other):
        return MyTime(self.seconds * other)

    def __truediv__(self, other):
        return MyTime(self.seconds / other)

    def __add__(self, other):
        return MyTime(self.seconds + other)

    def get_formatted_str(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds % 60:04.1f}"

    def __str__(self):
        return f"{self.seconds}s"

    def __eq__(self, other):
        return self.seconds == other.seconds

    def __ne__(self, other):
        return self.seconds != other.seconds

    def __lt__(self, other):
        return self.seconds < other.seconds

    def __gt__(self, other):
        return self.seconds > other.seconds

    def __le__(self, other):
        return self.seconds <= other.seconds

    def __ge__(self, other):
        return self.seconds >= other.seconds


class MyTimeInterval:
    def __init__(self, start_seconds, finish_seconds):
        self.start = MyTime(start_seconds)
        self.finish = MyTime(finish_seconds)

    def is_inside(self, time: MyTime) -> bool:
        return self.start <= time <= self.finish

    def intersects(self, other):
        pass


if __name__ == '__main__':
    assert MyTime(10) * 2 == MyTime(20)
    assert MyTime(10) / 2 == MyTime(5)
    assert MyTime(10) + 2 == MyTime(12)
    assert MyTime(10) == MyTime(10)
    assert MyTime(10) != MyTime(11)
    assert MyTime(10) >= MyTime(9)
    assert MyTime(10) <= MyTime(11)
    assert MyTime(10) > MyTime(9)
    assert MyTime(10) < MyTime(11)
    print(MyTime(4567.8).get_formatted_str())


