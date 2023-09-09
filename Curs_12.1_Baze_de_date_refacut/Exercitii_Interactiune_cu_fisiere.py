# Create a text file called “hello.txt” and add the following text inside of it:
# Python
# Java
# Javascript
# C/C++/C#
# PHP
# Node.js
# Write a short program to read and display the text file

# Varianta 1
# Citire date in mod clasic

# creez o functie reutilizabila care ia ca parametru un fisier text
def read_clasic(f):
    # deschid fisierul si il stochez in variabila f
    f = open(f, "r")
    try:
        return f.read()  # citesc datele din fisier
    # in cazul unei erori, o prind aici si o stochez in ex
    except Exception as ex:
        print(f"Error: {ex}")
    # la sfarsit, e important sa inchid fisierul
    finally:
        f.close()


a = read_clasic("hello.txt")
print(a)


# Varianta 2
# Citire folosind context manager

def read_safe(fisierul_aici):
    # deschid fisierul si il stochez in variabila f
    with open(fisierul_aici, "r") as f:
        return f.read()
        # aici nu mai este nevoie de f.close(), "with" face asta automat


print("--" * 40)

a1 = read_safe("hello.txt")
print(a1)

print("--" * 40)

"""
Write a short program to append the following lines to 
“hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file.
"""
# aici definesc lista de siruri de caractere care urmeaza sa fie adaugate
# la fisierul txt
li = ["Go", "Kotlin", "Swift"]


# definesc functia care ia ca parametrii fisierul original si lista care va fi
# adaugata la fisier
def append_lang(original, list):
    print(f"Original file is: {original}")
    print(f"Original list is: {list}")
    # iterez prin lista si scriu fiecare sir de caractere(string), unul cate unul
    # in fisierul original, plus notatia "\n" pentru a trece pe o linie noua dupa
    # ce stringul este adaugat in fisierul txt.
    for item in list:
        print(f"Item is... \n{item}")
        with open(original, "a") as f:
            f.writelines(item + "\n")


append_lang("hello.txt", li)
a2 = read_safe("hello.txt")
print(a2)

print("--" * 40)

"""
Write a short program that reads the “hello.txt” 
file and displays every other line (only odd lines).
"""


# definesc functia care ia ca parametru fisierul original
def display_every_other_line(fisier_aici):
    # deschid fisierul si il stochez in variabile file
    with open(fisier_aici, "r") as file:
        # accesez metoda "readlines()" prin "file" si stochez rezultatul returnat
        # care este un obiect de tip list in variabila file_content
        file_content = file.readlines()
        print(file_content)
        # iterez prin lista, folosesc metoda enumerate() pentru a accesa atat
        # itemul cat si indexul acestuia, iar daca indexul este par, loop-ul
        # va continua, si astfel se vor returna doar liniile impare
        for index, line in enumerate(file_content):
            print(f"Indexul este: {index}")
            print(f"Linia curenta este: {line}")
            if index % 2 == 0:
                print(f"Linia care ne intereseaza este: {line}")


display_every_other_line("hello.txt")

print("--" * 40)

"""
Create a csv file called “students.csv” and add the following text inside of it:
id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0
Read the file using Python’s `csv` standard library, 
and display it in the terminal as a table, using the options for 
string formatting from Python:

id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu   21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa		29	9.0
"""
import csv


# import libraria csv(comma separated values) pentru a putea citi
# si stoca fisierul intr-o variabila in python
# definesc functia care ia ca parametru fisierul care va fi afisat ca si tabel
def display_file_as_table(fisierul_aici):
    # cu open deschid fiesrul si il salvez in variabila file
    # petru a putea lucra cu datele din fisier
    with open(fisierul_aici, "r") as file:
        # salvez obiectul returnat prin accesarea metodei reader intr-o variabila
        reader = csv.reader(file)
        # iterez prin obiectul returnat care contine mai multe liste
        for row in reader:
            # print(row)
            # pentru a afisa datele din obiect in forma de tabel, voi folosi
            # formatare de string cu ajutorul metodei format
            # in fiecare acolada dintre ghilimele se va folosi sintaxa
            # {:<(numarul_care_da_latimea_coloanei)}, iar apoi
            # dupa ghilimele se va apela metoda format cu argumentul(*row)
            # care va despacheta lista si va formata corespunzator fiecare acolada
            print("{:<5} {:<10} {:<15} {:<5} {:<5}".format(*row))


display_file_as_table("students.csv")

print("--" * 40)

"""
Read again the information from the csv file above, 
store it all in a list of data, and then write a new file, 
called “students.json”, which will contain a valid JSON object.
Use the following format for each student (and use Python’s standard JSON module):
[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]
"""

import json
from pprint import pprint


# pentru a crea obiectul json am nevoie de libraria json
# definesc o functie care are un parametru si care ia un fisier csv
# si creeaza alt fisier cu aceleasi date in format json
def write_json_from_csv(fisierul_aici):
    # data din obiectul reader va fi stocata intr-o lista, va fi o lista de dictionare
    # se creeaza o lista goala
    lista_dictionare = []
    # with open va deschide fisierul specificat ca si primul argument in modul read
    # se poate face referinta la fisierul deschis prin variabila "file"
    # with asigura inchiderea fisierului dupa ce toate operatiile s-au efectuat
    with open(fisierul_aici, "r") as file:
        # se va crea un obiect DICTReader care este rezultatul apelarii metodei DictReader
        # din libraria csv cu argumentul file de adineaori
        reader = csv.DictReader(file)
        # se va crea obiectul json
        # se va itera prin obiectul reader si se va popula lista cu dictionare
        for row in reader:
            print(f"Randul este: {row}")
            student = {
                "id": int(row["id"]),
                "fname": row["fname"],
                "lname": row["lname"],
                "age": int(row["age"]),
                "grade": float(row["grade"])
            }
            lista_dictionare.append(row)
        print(f"Lista de dictionare este: {lista_dictionare}")
        with open("students.json", "w") as json_file:
            json.dump(lista_dictionare, json_file, indent=4)


write_json_from_csv("students.csv")

print("--" * 40)

"""
Create a new PyCharm project. Make sure it has a virtualenv. 
Install all the following packages from PYPI:
behave
behave-html-formatter
requests
selenium
webdriver-manager
Use pip to create a `requirements.txt` file. 
Send your project to a colleague and ask them to install all dependencies using pip.
"""
