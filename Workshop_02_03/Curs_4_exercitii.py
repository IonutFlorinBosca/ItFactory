# Exercitiul 1

"""
Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
•	‘Mașina mea preferată este x’.
•	Fă același lucru cu un for each.
•	Fă același lucru cu un while.

"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# for loop
for masina in masini:
    print(f"Masina mea preferata este {masina}")

i = 0
while i < len(masini):
    masina = masini[i]
    print(f"Masina mea preferata este {masina}")
    i += 1


# Exercitiul 2
"""
Aceeași listă:
Folosește un for else
În for
Modifică elementele din listă astfel încât să fie scrise cu majuscule, exceptând primul și ultimul.
În else:
  Printează lista.
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for index, masina in enumerate(masini): # utilizam functia enumeratea pentru a obtine indexul fiecarui element din listaimpreuna cu valoarea acestuia.
    if index == 0 or index == len(masini) -1: # primul si ultimul elemen tin lista nu va fi upper
        continue
    masini[index] = masina.upper() # modifica caracterele listei in upper - primul si ultimul element.
else:
    print(masini)

# Exercitiul 3
"""
Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Iterează prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
   Printează ‘am găsit mașina dorită de dvs’
   Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
   Printează ‘Am găsit mașina X. Mai căutam‘
"""
masini = ['Audi', 'Volvo', 'BMW',  'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Mercedes":
        print("am găsit mașina dorită de dvs")
        break
    else:
        print(f"nu am găsit mașina {masina}. Mai căutam")


# tema cu while


# Exercitiul 4
"""
Aceeași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun. 

Dacă mașina e Trabant sau Lăstun:
   Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
Printează S-ar putea să vă placă mașina x.
"""

masini = ['Audi', 'Volvo', 'BMW',  'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina  == "Trabant" or masina == "Lăstun":
        continue
    print(f"Printează S-ar putea să vă placă {masina} ")


# Exercitiul 5
"""
Modernizează parcul de mașini:

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
masini = ['Audi', 'Volvo', 'BMW',  'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []

for index, masina in enumerate(masini):
    if masina == "Lăstun" or masina == "Trabant":
        masini_vechi.append(masina)
        masini[index] = "Tesla" # Tesla va inlocui ambii indecsi (trabant si lastun)
        masini = list(set(masini)) # scoate duplicatul folosind functia set

print(f"modele vechi: {masini_vechi}")
print(f"modele existente + tesla: {masini}")


# Exercitiul 6
"""
Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
Iterează prin listă.

"""
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
buget = 15000

for masina, pret in pret_masini.items():
    if pret <= buget:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașină {masina} ")


# exemplu vizibil pentru indentare.

# Exercitiul 7
"""
Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
aparitii = 0

for numar in numere:
    if numar == 3:
        aparitii = aparitii + 1
        # aparitii += 1
print(f"Numarul 3 aoare de  {aparitii} ori.")

# Exercitiul 8
"""
Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0

for numar in numere:
    suma += numar

print(f"Suma este {suma}")

# Exercitiul 8
"""
Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
maxim  = 0

for numar in numere:
    if numar > maxim:
        maxim = numar

print(f"ce mai mare numar este {maxim}")


#
#
#