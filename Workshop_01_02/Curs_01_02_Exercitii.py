"""
Rotunjeste 'float-ul' folosind functia round()si salveaza aceasta modificare
in aceeasi variabila
(suprasciere): Verifica tipul acesteia
"""

#Variabila de tip float
inaltime = 1.79
print("Tipul variabilei 'inaltime este,'", type(inaltime))

#rotunjim valoarea

inaltime = round(inaltime)
print("Tipul variabilei 'inaltime este,'", type(inaltime))
print(inaltime)

"""
5. Foloseste print() si printeaza in consola 4 propozitii folosind
cele 4 variabile.
Rezolva nepotrivirile de tip prin ce modalitate doresti.
"""

print("#"*40)

nume = "Maria"
varsta = 17
inaltime = 1.79
este_minora = True

print(nume + " este colega mea")
print("Eu am " + str(varsta) + " ani")
print("Eu am " + str(inaltime) + " metri inaltime")
print("Este " + str(este_minora) + " ca sunt minora")

"""
6. Citeste de la tastatura:
- numele
- prenumele
Afiseaza: 'Numele complet are x caractere.
"""

print("#"*40)
"""
# Sa citim numele si prenumele de la tastatura
nume = input("Introdu numele...")
prenume = input("Introdu prenumele...")

#Calculam numarul total de caractere din nume si prenume
nume_complet = nume + " " + prenume
lungimea_numelui = len(nume_complet)


#Afisarea rezultatului

print("Numele complet are ", lungimea_numelui, " caractere")
"""
print("#"*40)

"""
Citeste de la tastatura:
- lungimea
- latimea
Afiseaza: 'Aria dreptunghiului este:'
"""
"""
#citim lungimea si latimea
lungime = int(input("Introdu lungimea dreptunghiului..."))
latime = int(input("Introdu latimea dreptunghiului..."))

#aria dreptunghiului
aria = lungime * latime

#afisam rezultatul
print("Aria dreptunghiului este de... ", aria)
"""

"""
'Coral is either the stupidest animal or the smartest rock'
-Afiseaza de cate ori apare cuvantul 'the'
"""
"""
text = 'Coral is either the stupidest animal or the smartest rock'
cuvant_cautat = " the"

numarul_de_aparitii = text.lower().count(cuvant_cautat)

print(f"Cuvantul '{cuvant_cautat}' apare de {numarul_de_aparitii}")
"""

"""
Acelasi string:
- foloseste un assert ca sa verifici daca acest string contine doar numere
"""
"""
text = 'Coral is either the stupidest animal or the smartest rock'
assert text.isdigit() == True
"""

"""
11. Exercitiu:
- citeste de la tastatura un string de dimensiune impara
- afiseaza caracterul din mijloc
"""
"""
#citim string de la tastatura
input_string = input("Introdu un string de dimensiune impara ")

#verificare a stringului, daca dimensiunea e impara
if len(input_string) % 2 != 0:
    #Afisam caracterul din mijloc
    mijloc = len(input_string) // 2
    caracter_mijloc = input_string[mijloc]
    print("Caracterul din mijloc este: ", caracter_mijloc)
else:
    print("Lungimea stringului nu este impara")
"""
"""
Lista [0,1,2,3] - se pot modifica valorile din lista
Tuple (0,1,2,3) - valorile nu se pot modifica
Dictionar {key:valoare}

"""

"""
12. Folsind o singura linie de cod:
- citeste un string de la tastatura 
- salveaza fiecare cuvant intr-o variabila
- printeaza ambele variabile pentru verificare
"""
"""
c1, c2 = input("Introdu un string din doua cuvinte... ").split()
print(c1)
print(c2)
"""

"""
13. Ex:
-citeste un string de la tastatura
-salveaza primul caracter intr-o variabila - indiferent care este el
-capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
=> alAbAlA portocAla
"""
"""
input_string = input("Introdu un string...")
def capitalized_string(input_string):
    #salvam primul caracter intr-o variabila
    primul_caracter = input_string[0]
    capitalized_string = primul_caracter + input_string[1:-1].capitalize() + input_string[-1]
"""

"""
Ex 14:
- citeste un user de la tastatura
- citeste o parola
- afiseaza: 'Parola pt user este **** si are x caractere';
-***** se va calcula dinamic, indiferent de dimensiunea parolei, 
trebuie sa afiseze corect
"""
"""
#citire user si parola de la tastatura
user = input("Introdu un user: ")
parola = input("Introdu o parola: ")

#calcularea numarului de caractere din parola
lungime_parola = len(parola)

#construim stringul cu caracterele asterix in functie de lungimea parolei
caractere_asterix = "*" * lungime_parola

#afisarea rezultatului
print(f"Parola pentru user-ul {user} este {caractere_asterix} si are {lungime_parola} caractere")
"""
"""
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.

Este o structura care controleaza si permite o executare diferita a codului
in functie de evaluarea unei conditii)

O structura decizionala - daca afara ploua imi iau umbrela, da nu nu imi iau umbrela
"""

"""
2. Verifică și afișează dacă x este număr natural sau nu.
"""
"""
x = int(input("Introdu un numar: "))

if x >= 1:
    print(f"{x} este un numar natural.")
else:
    print(f"{x} nu este un numar natural.")
"""

"""
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
"""
"""
x = float(input("Introdu un numar: "))

if x > 0: #verificam daca e pozitiv
    print(f"{x} este un numar pozitiv")
elif x == 0: #verificam daca e neutru
    print(f"{x} este un numar neutru")
else:
    print(f"{x} este un numar negativ")
"""

"""
4. Verifică și afișează dacă x este între -2 și 13.
"""
"""
x = float(input("Introdu un numar: "))

if -2 < x < 13:
    print(f"{x} este in intervalul (-2, 13).")
else:
    print(f"{x} nu este in intervalul (-2, 13).")
"""

"""
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
"""
"""
x = int(input("Introdu primul numar: "))
y = int(input("Introdu al doilea numar: "))

diferenta = abs(x - y) # calcularea valorii absolute a diferentei
if diferenta < 5:
    print(f"Diferenta dintre {x} si {y} este mai mica de 5")
else:
    print(f"Diferenta dintre {x} si {y} nu este mai mica de 5")
"""
"""
6. Verifică dacă x NU este între 5 și 27  - a se folosi ‘not’.
"""
"""
x = int(input("Introdu un numar: "))

if not (5 <= x <= 27): #verificam daca numarul nu se afla in intervalul 4 si 27
    print(f"{x} Nu este intre 5 si 27")
else:
    print(f"{x} Este intre 5 si 27")
"""
"""
7.
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
"""
"""
x = int(input("Introdu primul numar: "))
y = int(input("Introdu al doilea numar: "))

#Verificam egalitatea
if x == y:
    print(f"{x} este egal cu {y}")
elif x > y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{x} este mai mic decat {y}")
"""

"""
8. 
X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
"""
"""
x = float(input("Prima latura este: "))
y = float(input("A doua latura este: "))
z = float(input("A treia latura este: "))

if x == y == z: #echilateral
    print("Triunghiul este echilateral")
elif x == y or y == z or z == x:
    print("Triunhgiul este isoscel")
else:
    print("Triunghiul este oarecare")
"""
