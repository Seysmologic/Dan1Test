import numpy as np
import sqlite3
from faker import Faker

# create a connection to the database
conn = sqlite3.connect('example.db')

print(conn)
# create a table
conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

# commit the changes
conn.commit()



fake = Faker()

for i in range(1, 10):
    print(fake.first_name())





conn = sqlite3.connect('example.db')

for i in range(60, 70):
    conn.execute("INSERT INTO users (id, name) VALUES (?, ?)", (i, fake.name()))

conn.commit()


# create a connection to the database
conn = sqlite3.connect('example.db')

# retrieve data from the table
cursor = conn.execute("SELECT id, name FROM users")


rows = cursor.fetchall() # fetchone
print(rows)

# print the data
for row in rows:
    print(row)

# close the connection
conn.close()


with sqlite3.connect('example.db') as conn:
    # create a cursor
    cursor = conn.cursor()

    # create a table
    # cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')

    # insert some data
    #cursor.execute("INSERT INTO users (id, name) VALUES (21, 'Alice')")
    #cursor.execute("INSERT INTO users (id, name) VALUES (22, 'Bob')")

    # commit the changes
    # conn.commit()

    # retrieve data from the table
    cursor.execute("SELECT  id, name FROM users")
    rows = cursor.fetchmany(5) #fetchall, fetchone

    # print the data
    for row in rows:
        print(row)

with sqlite3.connect('example.db') as conn:
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