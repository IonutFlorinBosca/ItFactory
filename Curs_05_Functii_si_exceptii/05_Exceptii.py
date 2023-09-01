# a=1/0 -> Zero division error
# a = 2+b -> Name error
############################################################
# Aruncarea exceptiilor
x = 2
if x < 0:
    raise Exception("X mai mic ca 0") # asa se arunca o exceptie, Exception este clasa de baza a exceptiilor
############################################################
# Tratarea exceptiilor
try:  # Verifica un bloc de cod pentru exceptii
    # Daca codul din blocul try arunca o exceptie, se va opri exceptia in blocul except,
    # nu se va propaga mai departe in consola
    # Asta este de foarte mare ajutor pentru ca putem trata exceptiile inainte sa ajunga la utilizator!!
    print("C")
except:  # Trateaza diferitele tipuri de erori
    print("A aparut o exceptie")
# -----------------------------------------------------------
try:
    print(1 / 0)
except NameError: # In cazul in care in blocul try avem o eroare, iar la unul din blocurile
    # except specificam acea eroare, atunci se va duce direct la acea eroare!
    # Daca eroarea nu este specificata atunci va merge pe ultima ramura except!!
    print("Variabila C nu este definita")
except ZeroDivisionError as ex:  # Stocheaza exceptia in valoarea ex
    print(f"Eroarea: {ex}")
except:
    print("Alta a fost eroarea")
# -----------------------------------------------------------
try:
    print("Hello")
except:
    print("Eroare")
else:
    print("Se executa cand nu apare eroare")
# Ramura try,except, else este folosita pentru a rula o bucata de cod daca nu apare eroare in blocul try
# Nu este atat de intalnita!
# -----------------------------------------------------------
try:
    print("c")
except:
    print("Eroare")
finally:
    print("Eu ma execut mereu")  # Finally se executa de fiecare data, indiferent daca avem eroare sau nu
############################################################

"""
try: (blocul try)
    Bloc de cod unde ar putea aparea o eroare
    (sfarsitul blocului try)
except NumeEroare: -->prinderea tuturor exceptiilor de tipul nume eroare
    Se executa doar daca se prinde nume eroare
except (AltNumeEroare, IncaUnNumeEroare): --> Gruparea mai multor tipuri de exceptii
    Se executa doar daca se prinde una dintre cele doua erori
except Eroare4 as ex: --> Stocarea mesajului unei erori intr-o variabila
    Se poate accesa mesajul erorii prin variabila ex
except:
    Se executa pentru orice alt tip de eroare nespecificat
else:
    Se executa doar daca nu se arunca eroare in blocul "try"
finally:
    Se executa indiferent daca se arunca eroare sau nu
"""
