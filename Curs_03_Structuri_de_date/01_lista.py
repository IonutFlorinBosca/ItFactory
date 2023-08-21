# Lista de elemente - list

"""
- o insiruire de elemente ordonate
- pot avea diferite valori
- este MUTABILA (MUTABLE)
- putem accesa orice index
- putem pune valori repetabile
- se defineste : []

"""

lista_diversa = [2, 3.14, False, 'Elefant', 12345]
print(f'lista diversa: {lista_diversa}')

#Accesam elementul al 2-lea:
element2 = lista_diversa[1]
print(f'element2: {element2}')

#ultimul element din lista:
ultimul_element = lista_diversa[-1]
print(f'ultimul_element: {ultimul_element}')

#Verificam ce lungime are lista:
lungime_lista = len(lista_diversa)
print(f'lungime_lista: {lungime_lista}')

#Incercam sa accesam un element care depaseste lungimea listei:
#un_elem = lista_diversa[5]
#print(f'un_elem: {un_elem}')

print("-"*30)

##OPERATII cu elemente

#Inlocuirea / Schimbarea unui element din lista
lista_diversa[2] = True #am modificat-o datorita proprietatii de mutabilitate (este mutabila)
print(f'lista_diversa: {lista_diversa}')

#Adaugarea unui nou element intr-o lista
#la coada, se face cu append()
lista_diversa.append('hasta la vista')
print(f'lista_diversa: {lista_diversa}')

#In interiorul listei
lista_diversa.insert(3, 10*10)
print(f'lista_diversa: {lista_diversa}')

#Stergerea ultimului element din lista:
lista_diversa.pop()
print(f'lista_diversa: {lista_diversa}')

#Stergerea unui element pe baza de index:
lista_diversa.pop(2)
print(f'lista_diversa: {lista_diversa}')

print('-'*30)

#LIST SLICING
#Inversarea listei:
lista_inversa = lista_diversa[::-1] #de la inceput, pana la sfarsit, incepe cu -1; start-stop si indexul de unde incepe
print(f'lista_inversa: {lista_inversa}')

#Parte din lista:
#ultimele 3 elemente din lista:
print(f'lista_inversa ultimele 3 element: {lista_inversa[-3:]}')