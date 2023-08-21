class Dog:
    age = 12
    species = "mammal"
    name = "Rex"

print(Dog.age) #-->accesare atribute direct prin referire la clasa lor
print(Dog.species)

d = Dog() #--> crearea unui obiect(instanta) din clasa Dog
print(d.name, d.age, d.species)
"""
In exemplul de mai sus variabila b este o instanta
a clasei Dog, iar Dog este o clasa, deci defineste un nou tip de data

Prin obiectul d, se pot accesa toate atributele clasei Dog
"""