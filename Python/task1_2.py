# Нужно написать программу - “Замечательная телефонная книжка”. Нужно реализовать самые замечательные функции:
# - показать все контакты
# - добавить контакт
# - удалить контакт
# - изменить контакт
# Данные должны храниться в базе данных.

import mysql.connector


class UseDatabase:

    def __init__(self):
        self.configuration = {
            "host": "localhost",
            "user": "example",
            "password": "example",
            "database": "task2"}

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.configuration)
        if self.conn.is_connected():
            print("Connected to MySQL database")
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


def all_contact():
    _SQL = "SELECT * FROM contact"

    with UseDatabase() as cursor:
        cursor.execute(_SQL)
        data = cursor.fetchall()

    for contact in data:
        print("ФИО: {0}\t\t\t\tТелефон: {1}".format(contact[1], contact[2]))


def add_contact(name, phone):
    _SQL = "INSERT INTO contact (name, phone) VALUES ( %s, %s )"

    with UseDatabase() as cursor:
        cursor.execute(_SQL, (name, phone, ))


def dell_contact(name):
    _SQL = "DELETE FROM contact WHERE name=%s"

    with UseDatabase() as cursor:
        cursor.execute(_SQL, (name, ))


def set_contact(name, newname, phone):
    _SQL = "UPDATE contact SET name=%s, phone=%s WHERE name=%s"

    with UseDatabase() as cursor:
        cursor.execute(_SQL, (newname, phone, name))


if __name__ == "__main__":
    add_contact("New_USER", "89273333333")
    all_contact()
    set_contact("New_USER", "USER", "89274444444")
    all_contact()
    dell_contact("USER")
    all_contact()


