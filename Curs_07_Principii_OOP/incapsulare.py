"""
Incapsuarea se refera la ascunderea detaliilor de implementare
ale unei clase fata de alte clase.
Exista 3 tipuri de metode si atribute:
 - Public --> accesibile peste tot
 - Protected --> accesibile doar in ierarhia de mostenire (_atribut) "_"
 - Private --> accesibile doar in clasa (__atribut) "__"
"""


class Car():
    def __init__(self, model):
        self.__model = model

    @property  # Setare ca proprietate a campului __model
    def model(self):
        print("Setare ca proprietate")
        return self.__model

    @model.setter
    def model(self, value):
        if value.startswith("B"):  # Restrictionare asignare valori setter
            return
        print("Schimbare valoare model..")
        self.__model = value

    @model.getter
    def model(self):
        print("Returnare valoare..")
        return self.__model

    @model.deleter  # Eliberarea din memorie a valorii din campul __model
    def model(self):
        print("Stergere valoare...")
        self.__model = None


c = Car("Dacia")
print(c.model)  # Se apeleaza getterul

c.model = "Volvo"  # Se apeleaza setterul
print(c.model)

del c.model  # Se apeleaza deleterul
print(c.model)
