# 1.Clasa Cerc
#     Atribute: rază, culoare
#     Constructor pentru ambele atribute
#     Metode:
# descrie_cerc() - va PRINTA culoarea și raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
PI = 3.12


class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza {self.raza} si culoarea {self.culoare}")

    def aria(self):
        return PI * self.raza ** 2

    def diametru(self):
        print(f"Diametrul cercului este {2 * self.raza}")

    def circumferinta(self):
        print(f"Circumferinta cercului este {PI * 2 * self.raza}")


c1 = Cerc(5, "Alb")
c1.descrie_cerc()
print(c1.aria())
c1.diametru()
c1.circumferinta()

print("*" * 40)


# 2. Clasa Dreptunghi
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

    def descrie(self):
        print(f"Dreptunghiul are lungimea {self.lungime}, latimea {self.latime}, culoarea {self.culoare}")

    def aria(self):
        return self.latime * self.lungime

    def perimetru(self):
        return (self.latime + self.lungime) * 2

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare


d1 = Dreptunghi(3, 4, "Rosu")
d1.descrie()
print(f"Dreptunghiul are aria {d1.aria()}")
print(f"Dreptunghiul are perimetrul {d1.perimetru()}")
d1.schimba_culoarea("Alb")
d1.descrie()
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

    def descrie(self):
        print(f"Angajatul {self.nume} {self.prenume} are salariul de {self.salariu}")

    def nume_complet(self):
        print(f"Numele complet este {self.nume} {self.prenume}")

    def salariu_lunar(self):
        print(f"Angajatul are salariul lunar de {self.salariu}")

    def salariu_anual(self):
        print(f"Angajatul are salariu anual de {self.salariu * 12}")

    def marire_salariu(self, procent):
        self.salariu = self.salariu * (1 + procent / 100)
        print(f"Salariul s-a marit si este acum {self.salariu}")


ang1 = Angajat("Ionut", "Bosca", 3000)
ang1.descrie()
ang1.nume_complet()
ang1.salariu_lunar()
ang1.salariu_anual()
ang1.marire_salariu(10)
print("*" * 40)


# 4. Clasa Cont
#    Atribute: iban, titular_cont, sold
#    Constructor pentru toate atributele
#    Metode:
# afisare_sold() - Titularul x are în contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
class Cont:
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def afisare_sold(self):
        print(f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        if suma > self.sold:
            print(f"Suma debitata {suma} depaseste soldul curent {self.sold}")
        elif suma == 0 or suma < 0:
            print(f"Suma debitata {suma} este invalida!")
        else:
            print(f"Suma {suma} a fost debitata cu succes si soldul este acum {self.sold - suma}")
            self.sold -= suma

    def creditare_sold(self, suma):
        print(f"Suma de {suma} va fi creditata si soldul va fi {self.sold + suma}")
        self.sold += suma


cont1 = Cont("RO24BU", "Ionut Bosca", 1000)
cont1.afisare_sold()
cont1.debitare_cont(500)
cont1.debitare_cont(500)
cont1.debitare_cont(-2)
cont1.creditare_sold(3000)
cont1.afisare_sold()
print("*" * 40)

# 5. Clasa Factură
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
