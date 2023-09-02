class Dog:
    age = 12  # atribut de clasa (class atribute) -> are aceeasi valoare pentru toate obiectele din clasa
    # atributele de clasa sunt in general folosite pentru a defini constante in interiorul unei clase
    species = "mammal"
    name = "Rex"


d = Dog()
print(d.name)  # --> ordinea obligatorie este obiect + atribut

d2 = Dog()
d2.name = "Pufi"  # !!!name devine atribut de instanta(instance atribute) pentru ca a fost modificat din obiect!!!
print(d2.name)

Dog.name = "Bruno"
print(d.name, d2.name)
print("*" * 40)

# AR TREBUI SA FACEM O DIFERENTA INTRE ATRIBUTELE DE CLASA SI ATRIBUTELE DE INSTANTA
# Vrem sa avem posibilitatea sa cream direct ATRIBUTE DE INSTANTA!!!
# Daca creez obiectul "persoana", as vrea ca acea persoana sa aiba nume si prenume

class Cat:
    species = "mammal"

    # conceptul de constructor - ca sa cream atribute de instanta, trebuie sa ne definim un constructor,
    # care in Python este functia __init__!!!
    # ca sa pasam valori catre aceste atribute, va trebui sa le punem ca si parametrii la constructor
    def __init__(self, age, name): # cand cream un obiect/instanta a clasei "self" va deveni acel obiect
        # ca sa putem da valori atributelor acestei clase trebuie sa folosim "self.parametru = parametru"
        # parametrii si atributele nu trebuie sa se numeasca la fel
        self.age = age
        self.name = name


c = Cat(age=5, name="Floxi")
print(c.age, c.name)
# print(Cat.name)-->incorect pentru ca un atribut de instanta poate fi accesat
# doar printr-un obiect

#!!! O clasa cu constructor este ca si o functie cu parametrii!!

