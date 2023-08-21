lista_cumparaturi = ["oua", "lapte", "branza"]

while True:
    print("""
     1 - Afisare lista de cumparaturi
     2 - Adaugare element
     3 - Stergere element
     4 - Sterere lista de cumparaturi
     5 - Cautare lista de cumparaturi
     6 - Iesire din program""")
    optiune = int(input("Introduceti optiunea dorita: "))
    if optiune == 1:
        print(lista_cumparaturi)
    elif optiune == 2:
        lista_cumparaturi.append(input("Adaugati elementul dorit: "))
    elif optiune == 3:
        lista_cumparaturi.pop(lista_cumparaturi.index(input("Scoateti element din lista: ")))
    elif optiune == 4:
        lista_cumparaturi.clear()
    elif optiune == 5:
        for elem in lista_cumparaturi:
            if input("Elementul cautat este: ") == elem:
                print(f"Elementul {elem} face parte din lista!")
            else:
                print(f"Elementul {elem} nu face parte din lista!")
    elif optiune == 6:
        break



