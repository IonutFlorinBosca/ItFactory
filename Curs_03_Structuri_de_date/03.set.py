#SET ( Setul ) - {}
""" PROPRIETATI SET
-setul este o colectie de elemente UNICE (nu poti avea valori duplicat)
-nu este ordonat
-pot fi de tipuri diferite elementele
-este MUTABILA (se poate adauga, stergere, atat) - NU SE POT MODIFICA ELEMENTE
-fiecare element din set trebuie sa fie IMUTABIL!
-valorile setului fiind unice sunt considerate ca si chei (keys)
"""

#cream un set:
data_curenta = {'iulie', 11, True, 19, 49, 'PM'}
print(f'data_curenta: {data_curenta}')

print("-"*40)

#Adaugam o valoare:
data_curenta.add(11)
print(f'data_curenta: {data_curenta}')

#Adaugam un tuple
data_curenta.add((7,8,19))
print(f'data_curenta: {data_curenta}')

print("-"*40)

#Stergem un element existent:
data_curenta.remove(19)
print(f'data_curenta: {data_curenta}')
#eroare in caz ca cheia nu exista

#print lungime
print(f'lungime set: {len(data_curenta)}')