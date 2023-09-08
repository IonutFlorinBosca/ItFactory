import sqlite3
from pprint import pprint

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO students(name, email, age)
    VALUES ("Adam", "adam@genesis.com", 28);
    """
)

cursor.execute(
    """
    INSERT INTO students(name, email, age)
    VALUES ("Eva", "eva@genesis.com", 25);
    """
)

conn.commit()  # pentru a salva toate datele in baza de date trebuie dat de fiecare
# data commit la final

cursor.execute(
    """
    SELECT * FROM students;
    """
)

pprint(cursor.fetchall())

grades = [
    ("Web dev", 8, 1),
    ("Db dev", 10, 1),
    ("Db dev", 6, 2),
    ("front end", 10, 2),
    ("web dev", 9, 2),
    ("web dev", 8, 2),
    ("web dev", 8, 1)
]

query = """
    INSERT INTO grades(topic, grade, student_id)
    VALUES (?, ?, ?);
"""

cursor.executemany(query, grades)
cursor.execute("SELECT * FROM grades")
pprint(cursor.fetchall())
conn.commit()
