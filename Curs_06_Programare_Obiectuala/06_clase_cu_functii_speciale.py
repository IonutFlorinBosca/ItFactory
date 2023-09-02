# Daca definim aceste functii speciale in clasa noastra se intampla niste lucruri
# fara sa trebuiasca sa facem mai multe ajustari
class Dog:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    # Magic methods / Dunder methods
    def __str__(self):  # --> se va apela de fiecare data cand
        # se printeaza un obiect de tipul Dog sau se apeleaza functia str()
        return f"Age: {self.age}, Name: {self.name}"

    def __repr__(self):
        # Metoda __repr__ functioneaza foarte frumos atunci cand avem nevoie sa printam colectii de obiecte
        # deoarece colectiile de obiecte contin referinte catre obiectele noastre, ci nu obiectele in sine!!
        return str(self)  # sau return self.__str__()
    # return f"Age: {self.age}, Name: {self.name}" --> folosim varianta de pe linia anterioara ca sa nu avem cod duplicat

    def __eq__(self, other):  # comparatia se face self == other
        # Metoda __eq__ defineste comportamentul de comparatie dintre obiectul meu
        # cu alt obiect de acel tip
        if not isinstance(other, Dog):  # verificam daca obiectul other apartine clasei Dog
            return False
        # precizam explicit ce sa compare atunci cand este apelata aceasta metoda
        return self.age == other.age and self.name == other.name


d = Dog(age=4, name="Rex")
d2 = Dog(age=14, name="Bruno")
print(d)
print(d2)

print("*" * 30)
t = str(d)  # aici se apeleaza tot functia __str__ din clasa Dog
print(t)

# ----------------------------------------------------------------
print("*" * 30)
l = [d, d2]  # lista cu obiecte de tip Dog
print(l)  # --> lista contine referinte catre obiectele de tipul Dog,
# asa ca NU SE APELEAZA functia __str__ ci functia __repr__
# lista in sinea ei contine referinte catre obiectele din interior

# ----------------------------------------------------------------

print("*" * 30)
d3 = Dog(1, "Pufi")
d4 = Dog(1, "Pufi")

print(d3 == d4)
print(d3 == 7)