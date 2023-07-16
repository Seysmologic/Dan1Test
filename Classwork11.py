import sqlite3
from faker import Faker

fake = Faker()

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)''')

    for i in range(1, 16):
        conn.execute("INSERT INTO person (id, name, surname) VALUES (?, ?, ?)",
                     (i, fake.first_name(), fake.last_name()))

    conn.commit()

    cursor.execute("SELECT id, name, surname FROM person")
    rows = cursor.fetchall()

    for row in rows:
        print(row)