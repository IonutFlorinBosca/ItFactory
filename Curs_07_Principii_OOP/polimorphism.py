#La runtime, interpretorul isi da seama ca metoda label este apelata din clasa copil sau clasa parinte
#si astfel va da functionalitate acelei clase din acel moment si va afisa corespunzator tipul clasei!!!
# Polimorfismul este conceptul care ne zice ca putem accesa obiecte de diferite tipuri prin aceeasi interfata!!
# In exemplul meu, acel label este accesat din mai multe clase prin mostenire, chiar daca face parte dint-o
#singura clasa - Product

from abc import ABC, abstractmethod

# se declara clasa abstracta
class Buyable(ABC):
    @abstractmethod
    def label(self):
        pass

# se declara clasa copil care mosteneste in clasa abstracta
class Product(Buyable):
    # se declara constructorul care are 2 atribute specifice acestei clase
    def __init__(self, price, name):
        self.price = price
        self.name = name

    # se redefineste metoda label(mostenita din clasa parinte abstracta) si i se schimba comportamentul
    def label(self):
        # __class__ reprezinta clasa curenta si __name__ reprezinta numele clasei curente
        print(f"Eu sunt {self.__class__.__name__}: {self.name}")

# se declara o noua clasa care mosteneste din clasa parinte
# Product(care la randul ei mosteneste din clasa abstacta Buyable)
class BioProduct(Product):
    def __init__(self, price, name, source):
        super().__init__(price, name)
        self.source = source

# se declara o noua clasa care mosteneste din clasa parinte
# Product(care la randul ei mosteneste din clasa abstacta Buyable)
class RawProduct(Product):
    def __init__(self, price, name, time_on_shelf):
        super().__init__(price, name)
        self.time_on_shelf = time_on_shelf

# se declara o noua clasa care mosteneste din clasa parinte
# Product(care la randul ei mosteneste din clasa abstacta Buyable)
class ExpiredProduct(Product):
    def __init__(self, price, name, days_since_expired):
        super().__init__(price, name)
        self.days_since_expired = days_since_expired


# declar o functie care ia o lista ca si parametru si pentru fiecare item din lista
# se apeleaza metoda label() care este mostenita in fiecare clasa din clasa parinte Product
# Aceasta metoda returneaza "print(f"Eu sunt {self.__class__.__name__}: {self.name}")" in clasa Product
# Celelalte clase, BioProduct, RawProduct, ExpiredProduct au ca si clasa parinte pe clasa Product
# Datorita mostenirii, se mosteneste si metoda label() din clasa parinte in celelalte clase
# Datorita polimorfismului, cand aceasta metoda va fi apelata in celelalte clase
# aceasta metoda va actiona ca si cum ar apartine acestor clase!!!!!!
def see_product_labels(products):
    for product in products:
        product.label()


ps = [
    Product(10, "Branza de vaca"),
    BioProduct(15.66, "Branza de vaca", "La bunici"),
    Product(9.67, "Oua"),
    ExpiredProduct(3.44, "Oua", 2),
    BioProduct(17.54, "Oua", "La bunici"),
    RawProduct(4.99, "Mere", 2),
    BioProduct(3.88, "Mere", "La bunici"),
    Product(45.99, "Detergent rufe"),
    BioProduct(67.99, "Detergent rufe", "Lab Detergent Bio"),
    RawProduct(13.89, "Struguri", 1)
]

see_product_labels(ps)

# Polimorfismul este conceptul de a furniza o singura interfata
# catre diferite tipuri de obiecte.
# In exemplul de mai sus apare ideea de subtipare prin care
# in momentul in care codul este rulat isi va da seama din ce
# clasa este apelate functia 'label' pentru a afisa numele clasei
# corespunzator
