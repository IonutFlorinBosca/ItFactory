# Abstractizarea nu poate sta de sine statatoare, conceptul il alegem noi, poate fi orice
# Daca vorbim despre o figura geometrica, nu poate exista un obiect de tipul figura
# Abstractizarea vine la pachet cu conceptul ca nu poate exista de sine statatoare
# Aceasta abstractizare forteaza anumite comportamente asupra anumitor obiecte, obiecte concrete
# O clasa abstracta este o clasa care are cel putin o functie abstracta(fara implementare)
# De exemplu, toate figurile geometrice au arie si perimetru(cerc, patrat, triunghi) asa ca in
# teorie se poate defini o clasa numita "Figura" care sa oblige toate obiectele care mostenesc din ea
# sa aiba metodele arie si perimetru!!!

# ca sa declar o clasa si metode abstracte trebuie sa import ABC(Abstract Base Class) si abstractmethod din abc
from abc import ABC, abstractmethod  # ABC --> Abstract Base Class

class Animal(ABC):  # clasele abstracte trebuie sa mosteneasca din ABC
    # metodele clasei abstracte trebuie anotate cu @abstractmethod
    @abstractmethod
    def sound(self):
        # exista 2 lucruri ce pot fi gasite in interiorul corpului metodelor abstracte, si anume:
        # 1. pass -> nu se implementeaza functiile abstracte
        # 2. eroarea NotImplementedError
        pass  # functiile abstracte sunt functii fara implementare

    # metoda "sleep" se va redefini intr-o clasa copil, si i se va schimba comportamentul(ca si metoda sound)
    # Suntem obligati sa redefinim toate metodele si sa le schimbam comportamentul pentru ca avem
    # de a face cu o clasa abstracta!!!
    @abstractmethod
    def sleep(self):
        raise NotImplementedError

# Concretizare a clasei Animal, si anume clasa care mosteneste din Animal
# Clasa Dog trebuie sa implementeze toate metodele abstracte!!!!
# O clasa concreta ofera implementare pentru toate metodele abstracte!!!!
class Dog(Animal):
    #implementarea metodei sound in clasa concreta
    def sound(self):
        print("woph")

    #implementarea metodei sleep in clasa concreta
    def sleep(self):
        print("zzzzz")


class Cat(Animal):
    def sound(self):
        print("miau")

    def sleep(self):
        print("rrrrr")

# a = Animal() --> EROARE PENTRU CA NU SE POT INSTANTIA CLASE ABSTRACTE
# a.sleep()
