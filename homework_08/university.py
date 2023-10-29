from student import Student


def calc_sum_scholarship(students):
    money = []
    [money.append(i.get_scholarship()) for i in students]
    print(f'Sum scholarship - {sum(money)}')
def get_excellent_student_count(students):
    count = []
    [count.append(1) for i in students if i.is_excellent() == True]
    print(f'Excellent student - {sum(count)}')


students = [Student("Danick", 1),
            Student("Lexa", 1),
            Student("Dasha", 1),
            Student("Liza", 1),
            Student("Yra", 1),
            Student("Anasteisha", 1)]

calc_sum_scholarship(students)
get_excellent_student_count(students)
