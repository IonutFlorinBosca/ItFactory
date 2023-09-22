"""
Calculator simplu:
Interfață de intrare pentru a introduce două numere și o operație
(adunare, scădere, înmulțire, împărțire).
Implementare a operațiilor matematice.
Afișare a rezultatului.
"""

# Se defineste o functie in care se vor face operatiile si care va printa rezultatul
def calculator():
    # introdu primul numar
    numar1 = float(input("Introdu primul numar: "))
    # alege tipul de operatie
    operatie = input("Introdu una dintre 'adunare', 'scadere', 'inmultire', 'impartire': ")
    # introdu al doilea numar
    numar2 = float(input("Introdu al doilea numar: "))

    # fa calculele si printeaza rezultatul
    if operatie == 'adunare':
        rezultat = numar1 + numar2
    elif operatie == 'scadere':
        rezultat = numar1 - numar2
    elif operatie == 'inmultire':
        rezultat = numar1 * numar2
    elif operatie == 'impartire':
        if numar2 != 0:
            rezultat = numar1 / numar2
        else:
            print('La impartire numarul 2 nu trebuie sa fie 0!')
            return
    else:
        print('Incorrect input!')

    print(f"Rezultatul final este {rezultat}")

calculator()