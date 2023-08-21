"""
Partea 1- Funcții

Exerciții - studiu în workshopul de weekend

Pentru toate exercițiile.
Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
Dacă funcția are return, printează răspunsul.
"""

# 1.Funcție care să calculeze și să returneze suma a două numere
def calculeaza_suma(a, b):
    #initializez o noua variabila care va stoca suma a celor doua arg.
    suma = a + b
    #returnez suma
    return suma

suma1 = calculeaza_suma(2, 4)
print(suma1)
print("*"*40)

# 2. Funcție care să returneze
# TRUE dacă un număr este par, FALSE pentru impar
def numar_impar(numar):
    #verific conditional daca catul impartirii argumentului la 2 este 1;
    #daca catul este 1, numar este impar si functia va returna False
    #daca catul este 0, numar este par si functia va returna True
    if numar % 2 == 1:
        return False
    else:
        return True

ni = numar_impar(5)
np = numar_impar(6)
print(ni)
print(np)
print("*"*40)

# 3. Funcție care returnează numărul total de caractere din numele
# tău complet.
# (nume, prenume, nume_mijlociu)
def numar_total_caractere_nume(nume, prenume, nume_mijlociu):
    #declar 3 variabile care vor stoca valorile argumentelor din functie
    nume, prenume, nume_mijlociu = nume, prenume, nume_mijlociu
    #declar 1 variabila care va stoca concatenarea valorilor
    #rezultand 1 string complet
    nume_complet = nume + prenume + nume_mijlociu
    #pentru a verifica numarul total de caractere din string
    #voi folosi functia len(), si voi returna rezultatul
    return len(nume_complet)

numele_meu = numar_total_caractere_nume("Bosca", "Ionut", nume_mijlociu='')
print(numele_meu)
print("*"*40)

# 4. Funcție care returnează aria dreptunghiului
def calculeaza_aria_dreptunghiului(lungime, latime):
    #returnez lungime * latime
    return lungime * latime

arie = calculeaza_aria_dreptunghiului(9, 5)
print(arie)
print("*"*40)


# 5. Funcție care returnează aria cercului
#Formula aria cercului --> π(pi) inmultit cu R²(raza cercului la patrat)
#Import libraria math pentru a accesa valoarea lui pi
import math

def calculeaza_aria_cercului(raza):
    #declar o variabila care va stoca valoarea lui pi
    pi = math.pi
    #declar o variabila care va stoca rezultatul formulei
    #ariei cercului
    aria_cercului = pi * raza**2
    #returnez rezultatul final
    return aria_cercului

c1 = calculeaza_aria_cercului(2)
print(c1)
print("*"*40)

# 6. Funcție care returnează True dacă un caracter
# x se găsește într-un string dat și False dacă nu găsește.
#creez o functie care poate accepta 2 argumente; 1 caracter si 1 string
def gaseste_caracter(c, str):
    #apelez metodele de string lower() si contains();
    #lower() pentru ca argumentele sa nu fie case sensitive
    #si contains() pentru a verifica daca 1 caracter este inclus
    #in string
    #daca caracterul este inclus, returnez True,
    #altfel returnez False
    if str.lower().__contains__(c.lower()):
        return True
    else:
        return False

f1 = gaseste_caracter("a", "Ionut")
print(f1)
print("*"*40)

# 7. Funcție fără return, primește un string și printează pe ecran:
def numar_caractere(str):
    #definesc o variabila in care se va stoca numarul de caractere lower
    lower = 0
    #definesc o variabila in care se va stoca numarul de caractere upper
    upper = 0
    #iterez peste string si verific fiecare caracter
    for caracter in str:
        #daca caracterul este majuscula, incrementez valoarea variabilei upper
        if caracter.isupper():
            upper += 1
        #daca caracterul nu este majuscula, incrementez valoarea variabilei lower
        elif caracter.islower():
            lower += 1
    #printez valorile la sfarsitul iteratiei
    print(f"Numarul de caractere lower este: {lower}")
    print(f"Numarul de caractere upper este: {upper}")
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y

numar_caractere("CiotoAscAOE00")
print("*"*40)

# 8. Funcție care primește o LISTĂ de numere
# și returnează o LISTĂ doar cu numerele pozitive.
def doar_numere_pozitive(numere):
    #initializez o variabila care ca stoca o lista goala
    numere_pozitive = []
    #iterez peste argument
    for numar in numere:
        #daca numarul este mai mare decat 0, il introduc in lista goala
        if numar > 0:
            numere_pozitive.append(numar)
    #dupa iteratie returnez valorile din variabila numere_pozitive
    return numere_pozitive

np = doar_numere_pozitive([0, -1, 2, -2, -3, 3, 28, 1244])
print(np)
print("*"*40)

# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
def compara_numere(x, y):
    #compar valorile folosid if else
    if x > y:
        print(f"Primul număr {x} este mai mare decat al doilea număr {y}")
    elif y > x:
        print(f"Al doilea numar {y} este mai mare decat primul număr {x}")
    else:
        print("Numerele sunt egale!")
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.

compara_numere(2, 10)
compara_numere(21, -10)
compara_numere(-21, -21)
print("*"*40)

# 10. Funcție care primește un număr și un set de numere.
def adauga_numar_in_set(numar, set):
    #verific daca numar este in set
    if set.__contains__(numar):
        #daca setul contine numar atunci returnez False
        print(f"nu am adaugat numărul {numar} în set. Acesta există deja!")
        return False
    else:
        #daca setul nu contine numar atunci adaug numarul in set
        set.add(numar)
        print(f"am adaugat numărul {numar} în set.")
        print(f"Setul acum este {set}")
        return True
# Printează ‘am adaugat numărul nou în set’ + returnează True
# Printează ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False

ss = {1,2,3,4,5,6}
adauga_numar_in_set(-1, ss)
print("*"*40)

# 11. Funcție care primește o lună din an
# și returnează câte zile are acea lună.
def cate_zile_in_luna(luna):
    #tratez numerele din afara zonei cautate
    if luna < 1 or luna > 12:
        print("Luna introdusa este incorecta!")
        return
    #tratez exceptia lunii a doua din an
    elif luna == 2:
        print(f"Luna {luna} are 28 de zile!")
    #daca luna are numar impar si nu este egala cu 2 atunci are 31 de zile
    elif luna % 2 == 1 and luna != 2:
        print(f"Luna {luna} are 31 de zile!")
    #daca luna are numar par atunci are 30 de zile
    else:
        print(f"Luna {luna} are 30 de zile!")

ll = 7
cate_zile_in_luna(ll)
print("*"*40)

# 12. Funcție calculator care să returneze 4 valori.
# Suma, diferența, înmulțirea, împărțirea a două numere.
def calculator(numar1, numar2):
     suma = numar1 + numar2
     diferenta = numar1 - numar2
     inmultirea = numar1 * numar2
     impartirea = numar1 / numar2
     return suma, diferenta, inmultirea, impartirea
# În final vei putea face:
a, b, c, d = calculator(10, 2)

print("Suma: ", a)
print("Suma: ", b)
print("Suma: ", c)
print("Suma: ", d)
print("*"*40)


# 13. Funcție care primește o listă de cifre (adică doar 0-9)
li = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
def returneaza_dictionar_numere(lista):
    dictionar_numere = {}
    for numar in range(10):
        dictionar_numere[numar] = 0
        for nr in lista:
            if nr == numar:
                dictionar_numere[numar] += 1
    return dictionar_numere
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
ex1 = returneaza_dictionar_numere(li)
print(ex1)
print("*"*40)

