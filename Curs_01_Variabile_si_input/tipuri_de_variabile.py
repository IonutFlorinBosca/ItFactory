# TIPURI DE VARIABILE

# variabila de tip "INT" (numar intreg)
a = 12
b = -16

# variabila de tip "FLOAT" (numar zecimal)
pi = 3.14159

# variabila de tip "STRING" (sir de caractere)
# intotdeauna intre ghilimele duble/simple
d = "Ana are mere 1231!@#!!@#!@#!$!%(((&@$ Multe :))DNFakfadsAFDK3DSA"
e = 'Ana are mere'
# e = Ana are mere          # nu e corect definit pentru ca nu are ""


# variabila de tip "BOOLEAN" (valori adevarat/fals)
f = True
g = False


# acesta este un comentariu pe o singura linie
# alt comentariu pe o singura linie

"""Acesta este un comentariu
Pe mai multe linii
Folosim ghilimele triple
simple sau duble"""

'''Hai sa facem 
cu ghilimele simple'''


# variabilele sunt mereu cu litere mici si "_" daca e nume compus
# ASIGNARE MULTIPLA DE VARIABILA
mama, tata = "Oana", "George"
varsta_mama = 40

# TIPURI DE PRINT
print(mama) # daca vreau sa printez doar variabile - nu am nevoie de ghilimele
print("pe mama o cheama:", mama,'; pe tata il cheama:', tata) # la printare de variabila nu se folosesc ghilimele
print("pe mama o cheama:" + mama + '; pe tata il cheama:' + tata) # "+" elimina spatiul, fata de "," care adauga
print("pe mama o cheama:" + mama + " " + str(varsta_mama))
print(f"pe mama o cheama {mama} si are {varsta_mama} ani") #{} includ variabila in cardul ""
# "f" = formatting - permite introducerea de variabile in cadrul unui string
# "f" - formatting - ajutor pentru introducerea tipurilor de date
# string = "" / ''

