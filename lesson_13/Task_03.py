import sqlite3


def get_sql_older(min_age):
    with sqlite3.connect("TestSQL.db") as connection:
        result = connection.execute('SELECT * FROM user WHERE age>=? ORDER BY age;',
                                    (min_age,))
        print(result.fetchall())


def get_sql():
    with sqlite3.connect("TestSQL.db") as connection:
        result = connection.execute('SELECT * FROM user')
        print(result.fetchall())


if __name__ == '__main__':
    get_sql_older(int(input()))
    get_sql()
