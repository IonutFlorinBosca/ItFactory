# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# O variabile este o cutie care poate tine inauntrul ei mai multe chestii.


# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# string
numele_meu = 'Ionut'
# int
varsta = 30
# float
marime_cot = 43.6
# bool
zece_degete = True
# Observație: Valorile vor fi alese de tine după preferințe.

# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(numele_meu))
print(type(varsta))
print(type(marime_cot))
print(type(zece_degete))
print("-"*40)

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia.
marime_cot = round(marime_cot)
print(marime_cot)
print(type(marime_cot))
print("-"*40)

# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f"Eu sunt : {numele_meu}")
print(f"Eu am : {varsta} de ani!")
print(f"Marimea cotului meu este : {marime_cot} cm!")
print(f"Este {zece_degete} ca sunt barbat!")
print("-"*40)

# 6. Citește de la tastatură:
# numele;
# prenumele.
#     Afișează: 'Numele complet are x caractere'.
# numele = input("Numele tau este: ")
# prenumele = input("Prenumele tau este: ")
# print(f"{numele} {prenumele} are {len(numele) + len(prenumele)} caractere!")
# print("-"*40)

# 7. Citește de la tastatură:
# lungimea;
# lățimea.
#    Afișează: 'Aria dreptunghiului este x'.
# lungimea = int(input("Lungimea dreptunghiului este: "))
# latimea = int(input("Latimea dreptunghiului este: "))
# aria_dreptunghiului = lungimea**2 + latimea**2
# print(f"Aria dreptunghiului este: {aria_dreptunghiului}")
s = "-"*40

# 8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
# afișează de câte ori apare cuvântul 'the';

propozitie = 'Coral is either the stupidest animal or the smartest rock'
cuvant_cautat = 'the'
rezultat = propozitie.count(cuvant_cautat)
print(rezultat)
print(s)

# # 10. Același string:
# # Folosește un assert ca să verifici dacă acest string conține doar numere.
# assert propozitie.isdigit()

# 11. Exercițiu:
# citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.
# string_impar = input("Stringul este: ")
# caracter_mijloc = int(len(string_impar)/2)
# print(string_impar[caracter_mijloc])

# 12. Folosind o singură linie de cod :
# citește un string de la tastatură (ex: 'alabala portocala');
# salvează fiecare cuvânt într-o variabilă;
# printează ambele variabile pentru verificare.
# una, doua = input("Scrie primul cuvant: "), input("Scrie al doilea cuvant: ")
# print(una)
# print(doua)

"""
# 13. Exercițiu:
# citește un string de la tastatură (ex: alabala portocala);
# salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
# capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

#am citit si am stocat stringul de la tastatura
stringul_meu = input("Scrie aici stringul: ")
#am salvat primul caracter din string
primul_caracter = stringul_meu[0]
#am initializat un string nou care va deveni
#noul string conform cerintei
string_nou = ''
#se initializeaza o variabila cu 1 si se incrementeaza cu fiecare iteratie,
#atat timp cat variabila este mai mica decat lungimea stringului,
i=1
while i < len(stringul_meu) - 1 : #practic iterez peste tot stringul,
                                  #exceptand primul si ultimul caracter
    # daca caracterul este egal cu primul caracter din
    # string, se face MAJUSCULA apoi se concateneaza, altfel
    # se concateneaza pur si simplu.
    if stringul_meu[i] == primul_caracter:
        string_nou += stringul_meu[i].upper()
    else:
        string_nou += stringul_meu[i]
    i+=1
#se stocheaza versiunea finala a stringului conform cerintei
string_final = primul_caracter + string_nou + stringul_meu[-1]
print(string_nou)
print(string_final)
"""

# 14.Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
# eg: parola abc => ***
#       parola abcd => ****
# user, parola = input("User: "), input("Parola: ")
# print(parola, len(parola))
# parola_pixelata = parola.replace(parola, '*'*len(parola))
# print(parola_pixelata)
