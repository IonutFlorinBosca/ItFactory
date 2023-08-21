"""
1. Functie care sa calculeze si sa returneze suma a doua numere
"""


def calcul_suma(a, b):
    suma = a + b
    return suma


rezultat = calcul_suma(4, 10)
print(rezultat)
print("*" * 40)

"""
2. Funcție care să 
returneze TRUE dacă un număr este par, FALSE pentru impar
"""


def numar_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False


rezultat = numar_par(4)
print(rezultat)
print("*" * 40)

"""
3. Funcție care returnează numărul total de caractere din 
numele tău complet.
(nume, prenume, nume_mijlociu) 
"""


def calcul_caractere(nume, prenume, nume_mijlociu):
    nume_complet = nume + prenume + nume_mijlociu
    numar_caractere = len(nume_complet)
    return numar_caractere


print(calcul_caractere("Bosca", "Ionut", "Florin"))
print("*" * 40)

"""
4. Funcție care returnează aria dreptunghiului
"""


def calcul_arie(lungime, latime):
    aria = lungime * latime
    return aria


print(calcul_arie(4, 2))
print("*" * 40)

"""
5. Funcție care returnează aria cercului
"""
import math


def calcul_aria_cercului(raza):
    aria = math.pi * raza ** 2
    return aria


print(calcul_aria_cercului(5))
print("*" * 40)

"""
6. Funcție care returnează True dacă un caracter x se găsește 
într-un string dat și False dacă nu găsește.
"""


def gaseste_caracter(x, string):
    if x in string:
        return True
    else:
        return False


print(gaseste_caracter("b", "zxc"))
print("*" * 40)

"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y 
"""


def numara_caracter(str):
    lower = 0
    upper = 0

    for caracter in str:
        if caracter.islower():
            lower += 1
        elif caracter.isupper():
            upper += 1

    print("numar caractere lower: ", lower)
    print("numar caractere upper: ", upper)

numara_caracter("Masina")
print("*" * 40)

"""
8. Funcție care primește o LISTĂ de numere 
și returnează o LISTĂ doar cu numerele pozitive.
"""
def numere_pozitive(lista):
    lista_numere_pozitive = []
    for numar in lista:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive

print(numere_pozitive([0, -1, 4, 5, 6]))
print("*" * 40)

"""
9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
Primul număr x este mai mare decat al doilea număr y
Al doilea număr y este mai mare decat primul număr x
Numerele sunt egale. 
"""
def compara_numere(x, y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
    elif y > x:
        print(f"Al doilea numar {y} este mai mare decat primul numar {x}")
    else:
        print("Numerele sunt egale!")

compara_numere(6,0)
compara_numere(2,6)
compara_numere(0,0)
print("*" * 40)

"""
10. Funcție care primește un număr și un set de numere.
Printează ‘am adaugat numărul nou în set’ + returnează True
Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False
"""

def adauga_numar_in_set(numar, set):
    if numar in set:
        print(f"Nu am adaugat {numar} in set. Acesta exista deja!")
        return False
    else:
        set.add(numar)
        print(f"Am adaugat {numar} nou in set!")
        return True

set = {1,2,3}
rezultat = adauga_numar_in_set(4, set)
rezultat = adauga_numar_in_set(3, set)
print("*" * 40)

"""
11. Funcție care primește o lună din an și 
returnează câte zile are acea lună.
"""
def numar_zile_luna(luna):
    if luna == 2:
        return 28
    elif luna % 2 == 0:
        return 30
    else:
        return 31

numar_zile = numar_zile_luna(6)
print(numar_zile)
print("*" * 40)

"""
12. Funcție calculator care să returneze 4 valori. 
Suma, diferența, înmulțirea, împărțirea a două numere.
"""
def calculator(a, b):
    suma = a + b
    diferenta = a - b
    inmultirea = a * b
    impartirea = a / b
    return suma, diferenta, inmultirea, impartirea

a, b, c, d = calculator(10, 3)
print(f"Suma: {a}")
print(f"Diferenta: {b}")
print(f"Inmultirea: {c}")
print(f"impartirea: {d}")
print("*" * 40)

"""
13. Funcție care primește o listă de cifre (adică doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returnează un DICT care ne spune de câte ori apare fiecare cifră
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

