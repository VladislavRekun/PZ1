# Приложение БЮРО ПО ТРУДОУСТРОЙСТВУ для некоторой организации. БД
# должна содержать таблицу Работник со следующей структурой записи: фамилия, имя,
# отчество, возраст, пол, профессия, стаж работы.

import sqlite3 as sq
from workers_data import w_data

with sq.connect('employment.db') as con:
    cur = con.cursor()

    cur.execute("""create table if not exists workers (
    worker_id integer primary key autoincrement,
    surname varchar(30) not null,
    name varchar(20) not null,
    patronymic varchar(30),
    age integer not null,
    sex integer not null default 1,
    profession text not null,
    experience text not null)""")

with sq.connect('employment.db') as con:
    cur = con.cursor()
    columns = "(surname, name, patronymic, age, sex, profession, experience)"
    cur.executemany(f"INSERT INTO workers {columns} VALUES (?, ?, ?, ?, ?, ?, ?)", w_data)


# Поиск
with sq.connect('employment.db') as con:
    cur = con.cursor()
    cur.execute("select * from workers where age > 30")
    cur.execute("select name, age, profession, experience from workers where sex = 1 and age < 40 ")
    cur.execute("select name, age, profession, experience from workers where experience like '9%'")

# Удаление
with sq.connect('employment.db') as con:
    cur = con.cursor()
    cur.execute("delete from workers where worker_id between 5 and 10")
    cur.execute("delete from workers where sex = 2")
    cur.execute("delete from workers where name like 'А%'")

# Редактирование
with sq.connect('employment.db') as con:
    cur = con.cursor()
    cur.execute("update workers set age = 30 where worker_id between 5 and 10")
    cur.execute("update workers set profession = 'Программист' where sex = 1")
    cur.execute("update workers set name = 'Антон', surname = 'Михайличенко'  where sex = 1")

with sq.connect('employment.db') as con:
    cur = con.cursor()
    cur.execute("select * from workers")

    for i in cur:
        print(i)