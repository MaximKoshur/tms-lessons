import sqlite3


def save_contact():
    with sqlite3.connect('TelephoneBase.bd') as connection:
        name = input("Введите имя контакта: ")
        number = input("Введите номер контакта: ")
        result = connection.execute("INSERT INTO TelephoneBase VALUES(?, ?)", (name, number))
    print("Контакт сохранен!")


def show_contacts():
    with sqlite3.connect('TelephoneBase.bd') as connection:
        result = connection.execute("SELECT * FROM TelephoneBase")
    print(result.fetchall())


def update_number():
    with sqlite3.connect('TelephoneBase.bd') as connection:
        name = input("Введите имя контакта номер которого хотите изменить: ")
        number = input("Введите новый номер контакта: ")
        result = connection.execute("UPDATE TelephoneBase SET number = ? WHERE name = ?", (number, name))
    print("Контакт сохранен!")


def main():
    while True:
        chislo = input("0.Выйти из программы\n1.Добавить новый контакт\n2.Вывести весь список контактов в алфавитном "
                       "порядке\n3.Обновить номера контактов\n")
        if chislo == '0':
            break
        if chislo == '1':
            save_contact()
        if chislo == '2':
            show_contacts()
        if chislo == '3':
            update_number()


if __name__ == "__main__":
    main()
