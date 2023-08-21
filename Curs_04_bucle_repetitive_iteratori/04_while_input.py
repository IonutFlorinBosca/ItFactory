"""
Program care verifica input-ul de la tastatura
"""

"""
DEFINIREA EXACTA A PROBLEMEI:
1. Vrem ca sa verificam ca inputul de la keyboard sa fie
    de tip FLOAT, moment in care sa se opreasca
2. Daca nu este de tip FLOAT, continua bucla while (la nesfarsit)
"""

while True:
    numar = input('Prompter: ')
    if numar.isnumeric() or (numar.count('.') == 1 and numar.replace('.', '0').isnumeric()):
        print(f'Da, acesta este un float: {numar}')
        print(f'Inmultit cu 5 = {float(numar) * 5}')
        break
    else:
        print(f'Imi pare rau, {numar} nu este un numar')