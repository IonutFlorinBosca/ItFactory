# 1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

# Folosește un for că să iterezi prin toată lista și să afișezi;
for masina in mașini:
    print(f"Mașina mea preferată este {masina}")
print("-"*40)
# ‘Mașina mea preferată este x’.
# Fă același lucru cu un while.
i = 0
while i < len(mașini):
    print(f"Mașina mea preferată este {mașini[i]}")
    i += 1
print("-"*40)

# 2. Aceeași listă:
# Folosește un for else
# În for
# Modifică elementele din listă astfel încât să fie scrise cu majuscule,
# exceptând primul și ultimul.
# În else:
#   Printează lista.
#METODA 1 - index()
# for masina in mașini:
#     index_masina = mașini.index(masina)
#     if index_masina == 0 or index_masina == len(mașini) - 1:
#         continue
#     mașini[index_masina] = mașini[index_masina].upper()
# else:
#     print(mașini)
# print("-"*40)

#METODA 2 - enumerate()
# for count, masina in enumerate(mașini):
#     print(count, masina)
#     if count == 0 or count == len(mașini) - 1:
#         continue
#     mașini[count] = mașini[count].upper()
# else:
#     print(mașini)
# print("-"*40)

# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
for masina in mașini:
# Dacă mașina e mercedes:
    if masina == 'Mercedes':
        print("am găsit mașina dorită de dvs")
        break
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
    else:
        print(f"Am găsit mașina {masina}. Mai căutam")
#    Printează ‘Am găsit mașina X. Mai căutam‘
print("-"*40)

# 4. Aceeași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
for m in mașini:
    if m == 'Lăstun' or m == 'Trabant':
        continue
    print(f"S-ar putea să vă placă mașina {m}")
# Dacă mașina e Trabant sau Lăstun:
#    Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.
print("-"*40)

# 5. Modernizează parcul de mașini:
#
# Crează o listă goală, masini_vechi.
masini_vechi = []
# Iterează prin mașini.
for i, mas in enumerate(mașini):
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
    if mas == 'Lăstun' or mas == 'Trabant':
        masini_vechi.append(mas)
        mașini[i] = 'Tesla'
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
    print(f"Modele vechi: {masini_vechi}")
    print(f"Modele noi: {mașini}")
# Printează Modele vechi: x.
# Modele noi: x.
print("-"*40)

# 6. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
#
# Vine un client cu un buget de 15000 euro.
#
# Prezintă doar mașinile care se încadrează în acest buget.
# Iterează prin dict.items() și accesează mașina și prețul.
for masina, pret in pret_masini.items():
    if pret < 15000:
        print(f"Pentru un buget de sub 15000 euro puteți alege mașină {masina}")
# Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# Iterează prin listă.
print("-"*40)

# 7. Având lista:
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
rep = 0
for numar in numere:
    if numar == 3:
        rep += 1
print(rep)
print("-"*40)
# Afișează de câte ori apare 3 (nu ai voie să folosești count).

# 8. Aceeași listă:
sum = 0
# Iterează prin ea
for n in numere:
    sum += n
print(sum)
print("-"*40)
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).

# 9. Aceeași listă:
max = 0
# Iterează prin ea.
for m in numere:
    if m > max:
        max = m
print(max)
print("-"*40)
# Afișază cel mai mare număr (nu ai voie să folosești max).

# 10. Aceeași listă:
# Iterează prin ea.
for i, a in enumerate(numere):
    if a > 0:
        numere[i] = -a
print(numere)
print("-"*40)
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.

# 11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
# Itereaza prin listă alte_numere
for num in alte_numere:
    if num % 2 == 0:
        numere_pare.append(num)
    else:
        numere_impare.append(num)
    if num > 0:
        numere_pozitive.append(num)
    if num < 0:
        numere_negative.append(num)
# Populează corect celelalte liste
# Afișează cele 4 liste la final
print(f"Numere pare: {numere_pare}")
print(f"Numere impare: {numere_impare}")
print(f"Numere pozitive: {numere_pozitive}")
print(f"Numere negative: {numere_negative}")
print('-'*40)

# 12. Aceeași listă:
# Ordonează crescător lista fară să folosești sort.
#Bubble sort
# i = 0
# z = 0
# while z < len(alte_numere) - 1:
#     for x in range(i, len(alte_numere) - 1):
#         n1 = alte_numere[x]
#         for y in range(i + 1, len(alte_numere)):
#             n2 = alte_numere[y]
#             if n1 > n2:
#                 alte_numere[i+1] = n1
#                 alte_numere[i] = n2
#                 print(alte_numere)
#             i += 1
#             break
#     z+=1
#     i=0
# print('-'*40)

#Insertion sort
i = 0
for x in range(i, len(alte_numere) - 1):
    n1 = alte_numere[i]
    for y in range(i + 1, len(alte_numere)):
        n2 = alte_numere[y]
        if n2 < n1:
            alte_numere[x] = n2
            alte_numere[y] = n1
            n1 = n2
            print(alte_numere)
    i += 1
print('-'*40)

# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# import random
# numar_secret = random.randint(1, 30)
# print(numar_secret)
# # Numar_ghicit = None
# numar_ghicit = None
# # Folosind un while
# while True:
#     numar_ghicit = int(input("Tasteaza numar: "))
#     print(numar_ghicit)
# #    User alege un număr
# #    Programul îi spune:
#     if numar_ghicit < numar_secret:
#         print("Nr secret e mai mare")
# # Nr secret e mai mare
#     elif numar_ghicit > numar_secret:
#         print("Nr secret e mai mic")
# # Nr secret e mai mic
#     else:
#         print("Felicitari, ai ghicit!")
#         break
# # Felicitări! Ai ghicit!

# 14. Alege un număr de la tastatură
# rand_num = int(input("Alege un numar: "))
#
# i = 1
# while i <= rand_num:
#     print(str(i)*i)
#     i += 1
# Ex: 7
# Scrie un program care să genereze în consolă următoarea piramidă
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777

# 15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for i in tastatura_telefon:
    for y in i:
        print(f"Cifra curenta este: {y}")
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)
