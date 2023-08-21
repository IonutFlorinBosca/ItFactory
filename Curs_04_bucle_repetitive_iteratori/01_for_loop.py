"""
ITERATORI (BUCLE REPETITIVE)
- este un obiect care poate fi iterat (parcurs unul cate unul)
Ex: lista, tuple, set, dict, string
    (nu pot fi iterate: Bool, Int, Float)
- contin un numar de valori care se pot numara (itera)
"""

fructe = ['mar', 'para', 'banana', 'portocala', 'cireasa']
print(f'fructe: {fructe}')

s = "-" * 40
print(s)

for fruct in fructe:
    print(fruct, end=' ') #printam pe o singura linie

print('\n')
print(s)

for fructul_meu in fructe: #for poate avea else la sfarsit ca si alternativa de terminare
    print(fructul_meu)
else:
    print('Am terminat bucla repetitiva for.') # Este o particularitate Python

print(s)

lista_mixta = ['avocado', 2023, True, 5.66, 'Mihai', (11,12)]

for elem in lista_mixta:
    if type(elem) is str:
        elem = elem.upper()
        print(elem)
    else:
        print(f'{elem} nu este un string')

print(s)

#Iteratie la numere:

for numar in range(0, 11, 2):  #in functia range ultimul numar nu este accesat
    print(numar)

print(s)

for nr in range(10, 0, -1): #parcurgem descrescator
    print(nr, end=', ')
print()

print(s)
