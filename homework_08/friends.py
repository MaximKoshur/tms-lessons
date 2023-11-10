from person import Person


def get_oldest_person(friends):
    age = 0
    person = 0
    for i in friends:
        if i.age > age:
            age = i.age
            person = i
    print("The oldest is", end=' ')
    person.print_person_info()
    print("----------------------------------")


def filter_male_person(friends):
    print("Male:")
    [i.print_person_info() for i in friends if "M" in i.gender]


my_friends = [Person("Danick", 35, 'M'),
              Person("Lexa", 12, 'M'),
              Person("Dasha", 65, 'F'),
              Person("Liza", 3, 'F'),
              Person("Yra", 78, 'M'),
              Person("Anasteisha", 40, 'F')]

for i in my_friends:
    i.print_person_info()
print("----------------------------------")

get_oldest_person(my_friends)
filter_male_person(my_friends)
