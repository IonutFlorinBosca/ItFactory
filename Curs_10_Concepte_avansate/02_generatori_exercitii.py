# Implementați un generator pentru loteria 6/49 și noroc:
# Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
# Ultima apelare va da un singur număr de “noroc” format din 7 cifre
import random


def LotoGenerator():
    lista = random.sample(range(1, 50), 6)
    for i in lista:
        yield i

    yield random.randint(1_000_000, 9_000_000)


for val in LotoGenerator():
    print(val)

print('--' * 40)


def LotoGenerator2():
    l = []
    for i in range(6):
        numar = random.randint(1, 50)
        while numar in l:
            numar = random.randint(1, 50)
        l.append(numar)
        yield numar

    yield random.randint(1_000_000, 9_000_000)

print(LotoGenerator())
print(LotoGenerator2())

for num in LotoGenerator2():
    print(num)

print('--' * 40)


# def LotoGenerator3():
#     l = []
#     for i in range(6):
#         numar = random.randint(1, 6)
#         if numar not in l:
#             numar = random.randint(1, 6)
#             l.append(numar)
#         yield numar
#
#     yield random.randint(1_000_000, 9_000_000)
#
# for num in LotoGenerator3():
#     print(num)
