class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_name(self):
        print(f"My name is: {self.name}")

# clasa Student mosteneste din clasa Person
class Student(Person):
    pass


p = Person(30, "Tom")
p.print_name()
# Cand o clasa mosteneste dint-o clasa de baza, aceasta ia toate functiile si atributele din clasa de baza
# si si le insuseste
# "un student este o persoana, astfel ca studentul va mosteni constructorul si metodele clasei Person"
s = Student(22, "Andi")
s.print_name()

print("*" * 40)


class Angajat(Person):
    # in aceasta clasa noua care mosteneste din clasa Person vreau sa adaug un nou atribut - loc_de_munca
    # Ce este important, daca vreau sa adaug un nou atribut, trbuie sa creez un nou constructor,
    # constructor in care se vor declara si atributele din clasa parinte impreuna cu noul atribut
    def __init__(self, age, name, loc_de_munca):
        # vom apela constructorul clasei parinte, si asta se face prin metoda speciala 'super()'
        # acest 'super()' este de fapt clasa parinte - Person
        super().__init__(age, name)
        # mai ramane doar sa insusesc noul atribut acestei clase, folosind 'self'
        self.loc_de_munca = loc_de_munca

    def print_work(self):
        print(f"Lucrez la {self.loc_de_munca}")

a = Angajat(30, "John", "Wolt")
a.print_name()
a.print_work()

print("*" * 40)
# Toate metodele speciale folosite mai sus, si anume 'super()', __init__ apartin clasei de baza object in Python