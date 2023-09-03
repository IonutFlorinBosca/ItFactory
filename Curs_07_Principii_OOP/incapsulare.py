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
        # __model inseamna ca acest atribut este accesibil doar in clasa Car
        # practic acest atribut este ascuns fata de alte clase
        #(de exmplu daca vom instantia un obiect c = Car("Dacia") si voi face print(c.__model) voi primi eroare!)
        # Uneori vrem sa ascundem si sa restrictionam accesul catre anumite metode si atribute spre alte clase!
        self.__model = model

    # Cum am putea face access catre aceste atribute?
    # Este o modalitate in Python, cu ajutorul "property"
    # Prin intermediul metodelor si a decoratorilor property, setter, getter, si deleter
    # putem accesa, schimba, folosi, sterge valoarea unui atribut privat(__) sau protejat(_)
    @property  # Setare ca proprietate a campului __model
    def model(self):
        # Practic, cu ajutorul property obtin acces la properietatea __model si o sa o pot accesa mai tarziu
        # dintr-o instanta a clasei, astfel ca daca folosesc exemplul de mai sus:
        # pot accesa proprietatea obiectului c folosindu-ma de proprietate, si anume c.model!!!!
        print("Setare ca proprietate")
        return self.__model

    #daca vrem sa modificam valoarea acelui atribut, va trebui sa folosim o noua proprietate, si anume
    # @model.setter -> model setter
    # se defineste o noua metoda, metoda setter, care are paramentrii self si valoarea care va suprascrie vechea valoare
    @model.setter
    def model(self, value):
        if value.startswith("B"):  # Restrictionare asignare valori setter
            print("Nu se pot adauga modele care incep cu litera B")
            return
        print("Schimbare valoare model..")
        self.__model = value
        # folosind exemplul de mai sus, ca sa facem asta in cod se va face o simpla asignare, si anume
        # c.model = "Volvo"(inainte era "Dacia")

    # exista si corespondentul pentru a obtine valoarea, ca sa nu se seteze, sa se reseteze valoarea
    # de fiecare data cand folosim model, vrem doar sa ia valoarea, nu sa accesam property!!!
    # Pentru a accesa doar valoarea se foloseste metoda getter!!!!
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

# Prin aceste metode noi putem restrictiona in ce masura vrem accesul catre anumite atribute
# si putem sa impunem orice fel de reguli ne dorim!!!