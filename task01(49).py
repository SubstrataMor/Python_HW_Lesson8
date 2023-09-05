# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
#  характеристик для поиска определенной
#  записи(Например имя или фамилию
#  человека)
# 4. Использование функций. Ваша программа
#  не должна быть линейной

import sqlite3 as sq

with sq.connect("phonebook.db", timeout = 5.0) as con:
    cur = con.cursor()

def create_table():
    cur.execute("""CREATE TABLE IF NOT EXISTS contact (
    name TEXT,
    surname TEXT,
    phone_number INTEGER
    )""")
    con.commit()

def default_empty():
    cur.execute("SELECT * FROM contact")
    if not cur.fetchall():
        cur.execute("INSERT INTO contact VALUES ('Уорен','Баффет', 8888888888)")
        cur.execute("INSERT INTO contact VALUES ('Илон','Маск', 7777777777)")
        con.commit()

def show_data():
    cur.execute("SELECT * FROM contact")
    for i in cur.fetchall():
        print(i)

def search_contact():
    print("""Какие данные хотите найти?
    1- Name
    2- Surname
    3- Phone number""")
    com = {1: 'name', 2: 'surname', 3: 'phone_number'}
    choice = int(input())
    search = input(f"Введите {com.get(choice)}: ")
    cur.execute(f"SELECT * FROM contact WHERE {com.get(choice)} = '{search}'")
    for i in cur.fetchall():
        print(i)

def update_contact():
    print("""Что хотите изменить?
    1- Name
    2- Surname
    3- Phone number""")
    com = {1: 'name', 2: 'surname', 3: 'phone_number'}
    choice = int(input())
    search = input(f"Введите {com.get(choice)}: ")
    new_data = input("Введите изменения: ")
    cur.execute(f"UPDATE contact SET {com.get(choice)} = '{new_data}' WHERE {com.get(choice)} = '{search}'")
    con.commit()
    for i in cur.fetchall():
        print(i)

def del_contact():
    name = input("Имя: ")
    cur.execute(f"DELETE FROM contact WHERE name = '{name}'")
    con.commit()

def add_contact():
    name = input("Имя: ")
    surname = input("Фамилия: ")
    phone = input("Номер телефона: ")
    cur.execute(f"INSERT INTO contact VALUES('{name}','{surname}','{phone}')")
    con.commit()

create_table()
default_empty()

my_choice = -1
while my_choice != 0:
    print("""
    Выберите одно из действий:
    «1 — Вывести инфо на экран»
    «2 — Найти контакт»
    «3 — Изменить данные»
    «4 — Удалить данные»
    «5 — Добавить контакт»
    «0 — Выход из программы»
    """)
    action = int(input('Действие:'))
    if action == 1:
        show_data()
    elif action == 2:
        search_contact()
    elif action == 3:
        update_contact()
    elif action == 4:
        del_contact()
    elif action == 5:
        add_contact()
    else:
        my_choice = 0

con.close()