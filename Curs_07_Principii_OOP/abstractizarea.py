# Abstractizare nu poate sta de sine statatoare
# O clasa abstracta este o clasa care are cel putin o functie
# abstracta(fara implementare)

from abc import ABC, abstractmethod  # ABC --> Abstract Base Class


class Animal(ABC):  # clasele abstracte trebuie sa mosteneasca din ABC
    @abstractmethod
    def sound(self):
        pass  # functiile abstracte sunt functii fara implementare

    @abstractmethod
    def sleep(self):
        raise NotImplementedError


class Dog(Animal):
    def sound(self):
        print("woph")

    def sleep(self):
        print("zzzzz")


class Cat(Animal):
    def sound(self):
        print("miau")

    def sleep(self):
        print("rrrrr")

# a = Animal() --> EROARE PENTRU CA NU SE POT INSTANTIA CLASE ABSTRACTE
# a.sleep()
