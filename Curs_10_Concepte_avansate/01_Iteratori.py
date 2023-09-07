"""
l = [1, 2, 3]
x = iter(l) --> se obtine iteratorul specific listei 'l'
next(x) --> se parcurge element cu element - '1'
next(x) --> '2'
next(x) --> '3'

next(x) --> acesta ar produce eroarea 'StopIteration ' pentru ca
s-au parcurs toate elementele
"""
print("*" * 40)

"""
Iterator = obiect care poate fi iterat
Orice clasa care este iterabila (adica este un iterator)
trebuie sa implementeze doua metode:
    __iter__(self):
    ->aici se initializeaza iteratorul si se returneaza clasa curenta
    __next__(self):
    ->aici se va returna mereu urmatoarea valoare din colectia iterabila
    ->contine mecanismul de obtinere a valorii urmatoare in colectie
    ->atunci cand nu mai sunt valori disponibile se arunca exceptia 'StopIteration'
"""


class EvenIterator:
    def __init__(self, n):
        self.n = n  # n -> cate numere pare vrem sa generam

    def __iter__(self):
        self.generated_numbers = 0  # cate numere pare am generat pana acum
        self.current = 0  # numarul curent
        return self

    def __next__(self):
        self.current += 1
        if self.generated_numbers >= self.n:  # daca am generat mai multe
            # numere decat s-au cerut ne oprim
            raise StopIteration
        if self.current % 2 == 0:  # urmatorul numar gasit
            self.generated_numbers += 1  # crestem contorul numerelor gasit pana acum
            return self.current  # returnam numarul gasit
        return self.__next__()  # aici nu s-a gasit numar si se apeleaza mecanismul inca o data
        #METODA RECURSIVA


it = EvenIterator(10)
for i in it:
    print(i)

print("--"*40)

it = EvenIterator(10)
i = iter(it)
x = next(i)

while x:
    print(x)
    try:
        x = next(i)
    except StopIteration:
        x = None