"""
Agendă telefonică:
Structură de date (de exemplu, un dicționar) pentru stocarea
perechilor nume-număr de telefon.
Funcții pentru adăugare, ștergere și căutare a unui număr.
Interfață pentru interacțiunea cu utilizatorul.
"""

# se defineste structura de date care stocheaza perechi nume: numar
agenda = {}

# se defineste functia care adauga un numar in agenda
def adauga_numar(nume, numar):
    if isinstance(nume, str) and isinstance(numar, int):
        agenda[nume] = numar
    else:
        raise Exception("Please enter string: integer values!")

adauga_numar("Ionut", 453343)
print(agenda)

# se defineste functia care cauta un nume in agenda
def cauta_nume(nume, agenda):
    if nume in agenda:
        print(f"A fost gasit numele {nume} care are numarul {agenda[nume]}")
    else:
        print(f"Numele {nume} nu a fost gasit! Mai incearca!")

cauta_nume("ionut", agenda)

# se defineste functia pentru stergerea unui numar
def sterge_numar(numar, agenda):
    for key in list(agenda.keys()):
        if agenda[key] == numar:
            del agenda[key]
    return agenda

sterge_numar(453343, agenda)
print(agenda)

# se creeaza interfata pentru a interactiona cu utilizatorul
print(agenda)
while True:
    # declara o variabila care stocheaza intentia user-ului initiala
    intentie = input("Alege dintre: 'adaugare', 'cautare', 'stergere', 'iesire': ")
    if intentie == 'adaugare':
        nume = input("Numele nou pe care vrei sa il adaugi este: ")
        numar = int(input("Numarul nou pe care vrei sa il adaugi este: "))
        adauga_numar(nume, numar)
        print(agenda)
    elif intentie == 'cautare':
        nume_cautat = input("Numele cautat este: ")
        cauta_nume(nume_cautat, agenda)
        print(agenda)
    elif intentie == 'stergere':
        numar = int(input("Numarul care va fi sters este: "))
        sterge_numar(numar, agenda)
        print(agenda)
    else:
        if intentie == 'iesire':
            break



