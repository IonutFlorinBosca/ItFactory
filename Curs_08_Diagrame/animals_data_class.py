from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Creature(ABC):
    @abstractmethod
    def eat(self):
        pass


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Animal(Creature):
    age: int
    weight: int

    def eat(self):
        print(f"I am an eating {self.__class__.__name__}")


@dataclass
class WildAnimal(Animal):
    _location: str

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value


@dataclass
class DomesticAnimal(Animal):
    owner: Person


@dataclass
class JungleAnimal(WildAnimal):
    _location: str = field(init=False, default="jungle")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        raise Exception("Nu se poate schimba aceasta valoare")


@dataclass
class ForestAnimal(WildAnimal):
    _location: str = field(init=False, default="Forest")
    #folosind functia field putem specifica
    #ca nu vrem ca atributul _location sa fie
    #inclus in constructor si sa ia implicit
    #valoarea "forest"
    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        raise Exception("Nu se poate schimba aceasta valoare!")


@dataclass
class Pet(DomesticAnimal):
    name: str


me = Person("Vlad", 29)
cow = DomesticAnimal(10, 150, me)
dog = Pet(5, 25, me, "Puffy")
wolf = ForestAnimal(10, 60)

#wolf.location = "Ferma" #Aici da eroare pentru ca
# am creat un setter in clasa ForestAnimal
# care nu lasa sa se modifice acest atribut

l = [cow, dog, wolf]
for a in l:
    print(a.age)
    a.eat()  # aici va aparea numele corespunzator
    # fiecarei clase deoarece avem POLIMORFISM
