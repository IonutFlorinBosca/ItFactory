"""
Write a SQL statement to create a table called continents, with the following columns:
continent_id
continent_name
continent_code – 2 letters code
"""
import sqlite3

# importa libraria sqlite3
# import sqlite3
#
# # conecteaza-te la baza de date(creeaza un fisier nou daca nu exista)
# conn = sqlite3.connect("continents.db")
# cursor = conn.cursor()
#
# # creeaza tabelul continents
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS continents(
#     continent_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     continent_name TEXT NOT NULL,
#     continent_code TEXT NOT NULL CHECK (length(continent_code) = 2)
# );
# """)
#
# # commit schimbarile si inchide conexiunea
# conn.commit()
# conn.close()
#
# # conecteaza-te la baza de date(creeaza un fisier nou daca nu exista)
# conn = sqlite3.connect("continents.db")
# cursor = conn.cursor()
#
# # interogheaza baza de date pentru a vedea daca tabelul exista
# cursor.execute("""
# SELECT name FROM sqlite_master WHERE type="table" AND name="continents";
# """)
#
# # printeaza rezultatul
# print(cursor.fetchall())
#
# # commit schimbarile si inchide conexiunea
# conn.commit()
# conn.close()
#
# # conectare la baza de date
# conn = sqlite3.connect("continents.db")
# cursor = conn.cursor()
#
# # inserare in baza de date
# cursor.execute("""
# INSERT INTO continents (continent_name, continent_code)
# VALUES ("Europe", "EU"), ("Asia", "AS"), ("Africa", "AF");
# """)
#
# conn.commit()
#
# # retragere date din baza de date
# cursor.execute("""
# SELECT * FROM continents;
# """)
#
# print(cursor.fetchall())
# conn.close()
# print("--" * 40)
#
# # conectare la baza de date
# conn = sqlite3.connect("continents.db")
# cursor = conn.cursor()
#
# # stergere completa din baza de date
# cursor.execute(
#     """
#     DELETE FROM continents;
#     """
# )
#
# # commit schimbari si inchidere conexiune la baza de date
# conn.commit()
# conn.close()
#
# # conectare la baza de date
# conn = sqlite3.connect("continents.db")
# cursor = conn.cursor()

# inserare date in baza de date
# cursor.execute(
#     """
#     INSERT INTO continents (continent_name, continent_code)
#     VALUES ("Europe", "EU"), ("Africa", "AF"), ("Antartica", "AN"), ("Asia", "AS"),
#             ("Australia", "AU"), ("North America", "NA"), ("South America", "SA");
#     """
# )
#
# # commit schimbari si inchidere conexiune la baza de date
# conn.commit()
# conn.close()

# A doua metoda de inserare multi-linii in baza de date

# conectare la baza de date
# conn = sqlite3.connect("continents.db")
# cursor = conn.cursor()
#
# # stergere toate informatiile din baza de date
# cursor.execute(
#     """
#     DELETE FROM continents
#     """
# )
#
# conn.commit()

# lista date care urmeaza sa fie adaugate in baza de date
lista_continente = [
    ("Antartica", "AN"),
    ("Asia", "AS"),
    ("Africa", "AF"),
    ("Australia", "AU"),
    ("North America", "NA"),
    ("South America", "SA"),
    ("Europe", "EU")
]

# defineste SQL query ca si un string si stocheaza-l in variabila query
# "INSERT INTO continents" -> ii spune bazei de date ca vrei sa inserezi un nou rand
# in tabelul continents
# "(continent_name, continent_code)" -> acestea sunt coloanele din tabelul continents
# "VALUES (?, ?)" -> asta specifica valorile care vor fi inserate
# semnele de intrebare sunt inlocuitoare pentru valorile actuale
# query = "INSERT INTO continents(continent_name, continent_code) VALUES(?, ?)"
# # voi folosi metoda obiectului cursor executemany pentru a insera mai multe randuri
# # in baza de date creata anterior
# # metoda ia 2 argumente: stringul query si secventa de parametrii
# # metoda va executa afirmatia INSERT pentru fiecare tuplu in lista_containere,
# # si va inlocui semnele de intrebare din stringul query cu valorile din tuplu
# cursor.executemany(query, lista_continente)
# conn.commit()

# cursor.execute(
#     """
#     SELECT * FROM continents;
#     """
# )
#
# print(cursor.fetchall())
print("--" * 40)

"""
Write a SQL statement to create a table called countries, with the following columns:
country_code – 2 letters code (e.g. RO, US, IT, etc)
country_name
continent_id – foreign key
population – number
"""

# executing the cursor and creating the table
# continent_id este cheia straina care face referinta la continent_id
# din cealalta baza de date, continents.db, formand astfel o conexiune intre cele 2
# creeaza tabelul countries doar daca nu exista deja
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS countries(
#     country_code CHAR(2) PRIMARY KEY,
#     country_name TEXT NOT NULL,
#     continent_id INTEGER,
#     population INTEGER,
#     FOREIGN KEY(continent_id) REFERENCES continents(continent_id)
# );
# """)
#
# # commit schimbarile si inchide conexiunea
# conn.commit()
print("--" * 40)

"""
Write a few SQL statements to add some countries. 
Here is a list of countries with their codes. 
Feel free to invent or approximate their populations, 
and use your geography knowledge for their continent. 
Add at least 10 countries, as diverse as possible (INSERT)
"""
list_countries = [
    ("RO", "Romania", "EU", 19000000),
    ("US", "United States Of America", "NA", 330000000),
    ("FR", "France", "EU", 70000000),
    ("HU", "Hungary", "EU", 9000000),
    ("CA", "Canada", "NA", 40000000),
    ("CH", "China", "AS", 1450000000),
    ("BE", "Belgium", "EU", 12000000),
    ("AU", "Australia", "AUS", 25000000)
]

# query_countries = "INSERT INTO countries(country_code, country_name, continent_id, population) VALUES(?, ?, ?, ?)"
# cursor.executemany(query_countries, list_countries)
# conn.commit()

"""
Write a SQL statement to select all countries, ordered by name. 
Write another statement to count them all.
"""
# conectare la baza de date
conn = sqlite3.connect("continents.db")
cursor = conn.cursor()

# selectare tari, ordonare dupa nume
cursor.execute(
    """
    SELECT * FROM countries ORDER BY (country_name);
    """
)
print(cursor.fetchall())
print("--" * 40)

# selectare tari, numarare toate tarile
cursor.execute(
    """
    SELECT COUNT(*) FROM countries;
    """
)
print(cursor.fetchall())
print("--" * 40)

"""
Write a SQL statement to select only countries with a population greater than 20 millions.
"""

# Varianta 1
cursor.execute(
    """
    SELECT * FROM countries WHERE population > 20000000;
    """
)
print(cursor.fetchall())
print("--" * 40)

# Varianta 2
query = "SELECT * FROM countries WHERE population > 20000000 ORDER BY population"
list = cursor.execute(query)
for item in list:
    print(item)
print("--" * 40)

"""
Write a SQL statement to select only countries that start with a certain letter 
(choose one that exists for you, e.g. C in the example above).
"""

# Varianta 1
query2 = "SELECT * FROM countries WHERE country_name LIKE 'C%'";
list = cursor.execute(query2)
for i in list:
    print(i)

print("--" * 40)

# Varianta 2
cursor.execute(
    """
    SELECT * FROM countries WHERE country_name LIKE 'B%';
    """
)
print(cursor.fetchall())
print("--" * 40)

"""
Write a SQL statement that groups all countries by continents, and counts them.
"""
# SELECT continent_id, COUNT(*) -> 'selecteaza continent_id si numara toare randurile'
# FROM countries -> 'din tabelul countries'
# GROUP BY continent_id -> 'grupeaza rezultatele in functie de continent_id'
# Cu alte cuvine, arata cate tari sunt in fiecare continent din fisier
cursor.execute(
    """
    SELECT continent_id, COUNT(*) 
    FROM countries 
    GROUP BY continent_id;
    """
)
print(cursor.fetchall())
print("--" * 40)

selectall = "SELECT * FROM countries"
all = cursor.execute(selectall)
for c in all:
    print(c)
print("--" * 40)

select_all_continent_id = "SELECT continent_id, COUNT(*) from countries;"
all_continent_id = cursor.execute(select_all_continent_id)
for all in all_continent_id:
    print(all)
print("--" * 40)

"""
Write a SQL statement that groups all countries by continent, 
and computes the total population per continent (SUM)
"""

# Varianta 1
cursor.execute(
    """
    SELECT continent_id, SUM(population)
    FROM countries
    GROUP BY continent_id
    """
)
pop = cursor.fetchall()
for o in pop:
    print(o)
print("--" * 40)

# Varianta 2
v2 = """
SELECT continent_id, SUM(population) as total_population
FROM countries GROUP BY continent_id;
"""

# executarea query-ului si stocare intr-un cursor obiect
exec = cursor.execute(v2)

# returnarea si accesarea datelor
see_inside_exec = exec.fetchall()
for continent, population in see_inside_exec:
    print(continent, population)
