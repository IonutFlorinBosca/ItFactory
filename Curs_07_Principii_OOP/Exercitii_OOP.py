# 1.Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are {self.raza} si culoarea {self.culoare}")

    def aria(self):
        return 3.14 * self.raza ** 2

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * 3.14 * self.raza


cerc1 = Cerc(5, "Mov")
cerc1.descrie_cerc()
print(f"Aria cercului este: {cerc1.aria()}")
print(f"Diametrul cercului este: {cerc1.diametru()}")
print(f"Circumferinta cercului este: {cerc1.circumferinta()}")

print("*" * 40)


#  Clasa Dreptunghi
#      Atribute: lungime, lățime, culoare
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# aria()
# perimetrul()
# schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Poți verifica schimbarea culorii prin apelarea metodei descrie().
class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f"Dreptunghiul are lungimea {self.lungime}, latimea {self.latime}, culoarea {self.culoare}")

    def aria(self):
        return self.lungime * self.latime

    def perimetru(self):
        return (self.lungime + self.latime) * 2

    def schimba_culoare(self, noua_culoare):
        self.culoare = noua_culoare
        print(f"Noua culoare este {self.culoare}")


dreptunghi1 = Dreptunghi(5, 10, "Alb")
dreptunghi1.descriere()
print(dreptunghi1.aria())
print(dreptunghi1.perimetru())
dreptunghi1.schimba_culoare("Albastru")

print("*" * 40)


# 3. Clasa Angajat
#      Atribute: nume, prenume, salariu
#      Constructor pentru toate atributele
#      Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul egal cu {self.salariu}")

    def nume_complet(self):
        return self.nume + ' ' + self.prenume

    def salariu_lunar(self):
        return self.salariu

    def salariu_anual(self):
        return self.salariu * 12

    def marire_salariu(self, procent):
        self.procent = procent
        return self.salariu * (1 + procent / 100)


angajat1 = Angajat("Andrei", "Caisim", 100000)
angajat1.descriere()
print(f"Numele complet este {angajat1.nume_complet()}")
print(f"Salariul lunar este {angajat1.salariu_lunar()}")
print(f"Salariul anual este {angajat1.salariu_anual()}")
print(f"Dupa marire salariul este {angajat1.marire_salariu(25)}")

print("*" * 40)

#  5. Clasa Factură
#      Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
#      Constructor: toate atributele, fără serie
#      Metode:
# schimbă_cantitatea(cantitate)
# schimbă_prețul(pret)
# schimbă_nume_produs(nume)
# generează_factura() - va printa tabelar dacă reușiți
#
# Factura seria x număr y
# Data: generează automat data de azi
# Produs | cantitate | preț bucată | Total
# Telefon |      7       |       700       | 49000

from datetime import date
from tabulate import tabulate


class Factura:
    seria = "X"

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def genereaza_factura(self):
        total = self.pret_buc * self.cantitate
        print(f"Factura seria {self.seria} numar {self.numar}")
        print(f"Data: {date.today().strftime('%d.%m.%Y')}")
        header = ["Produs", "Cantitate", "Pret bucata", "Total"]
        main = [[self.nume_produs, self.cantitate, self.pret_buc, total]]
        print(tabulate(main, headers=header, tablefmt="grid"))


f1 = Factura(32511, "machine-gun", 2, 1800)
f1.genereaza_factura()

factura1 = Factura("zv15", "faina", 10, 5.2)
factura1.genereaza_factura()
