"""
JSON -> JavsScript Object Notation
    -> seamana cu o liste de dictionare
    -> foloseste la transfer de date
"""
import json
from pprint import pprint


def read():
    with open("Angajati.json", "r") as f:
        return json.load(f)


l = read()
pprint(l)
print("--" * 40)

data = [
    {"Nume": "Sergiu", "Varsta": "24"},
    {"Nume": "Andrei", "Varsta": "31"},
    {"Nume": "Dan", "Varsta": "22"},
    {"Nume": "Ioana", "Varsta": "20"}
]


def write(d):
    with open("Angajati2.json", "w") as f:
        json.dump(d, f, indent=4)

write(data)