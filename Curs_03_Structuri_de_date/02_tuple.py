##TUPLE

"""
-tuple este un tip de date IMMUTABLE (NU SE POT STERGE, ADAUGA, MODIFICA VALORI)
-sunt valori ordonate, indexabile
-pot exista mai multe valori repetate
"""

#Definim un tuple - ()
tuple_numere = (1,2,3)
print(f'tuple_numere: {tuple_numere}')

#nu se pot schimba valori => imposibil
#tuple_numere[-1] = 4

print("-"*40)

lista_valori = ["a", "b", "c"]
print(f'lista_valori: {lista_valori}')
lista_valori.append("d")
print(f'lista_valori: {lista_valori}')

#Transform o lista intr-un tuple:
tuple_litere = tuple(lista_valori)
print(f'tuple_litere: {tuple_litere}')

print("-"*40)

#Pot sa le numar si sa le accesez cu index
elem1 = tuple_litere[0]
print(f'elem1: {elem1}')
print(f'verific lungime tuple: {len(elem1)}')
print(f"numar cate elemente aceleasi sunt in tuple: {tuple_litere.count('a')}")

#Exemplu de utilizare a tuple-ului
triunghi_dat = ((0,0), (0,4), (2, 4))