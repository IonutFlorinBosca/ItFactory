#DICT - DICTIONARUL

"""
-dictionarul este o colectie de date de tip cheie-valoare (fiecare cheie are o valoare)
-dictionarul in sine este MUTABIL
-cheile ( keys ) sunt unice!!!
-valorile (values) se pot repeta
-cheile trebuie sa fie IMMUTABLE ( doar de tip : int, str, tuple )
"""

#Initializare dictionar
persoana = {
    'nume': 'Stefan',
    'prenume': 'Cel Mare',
    'varsta': 47
}
print(f'persoana: {persoana}')

#adaugam un element in dictionar
persoana['initiala tatalui'] = 'P'
print(f'persoana: {persoana}')

#accesarea unui element non-existent => eroare(ca si la set)

print("-"*40)

#lungimea dictionarului
lungime_dict = len(persoana)
print(f"lungime_dict: {lungime_dict}")

print("-"*40)

#modificarea unui element existent (folosesc cheia pe care o doresc)
persoana['initiala tatalui'] = 'Y'
print(f'persoana: {persoana}')


#stergere elemente
persoana.pop("initiala tatalui")
print(f'persoana: {persoana}')