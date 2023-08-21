class Dog:
    age = 12  # atribut de clasa (class atribute) -> are aceeasi valoare pentru toate obiectele din clasa
    # atributele de clasa sunt in general folosite pentru a defini constante in interiorul unei clase
    species = "mammal"
    name = "Rex"


d = Dog()
print(d.name)  # --> ordinea obligatorie este obiect + atribut

d2 = Dog()
d2.name = "Pufi"  # name devine atribut de instanta(instance atribute) pentru ca a fost modificat din obiect
print(d2.name)

Dog.name = "Bruno"
print(d.name, d2.name)
print("*" * 40)


class Cat:
    species = "mammal"

    def __init__(self, age, name):
        self.age = age
        self.name = name


c = Cat(age=5, name="Floxi")
print(c.age, c.name)
# print(Cat.name)-->incorect pentru ca un atribut de instanta poate fi accesat
# doar printr-un obiect
