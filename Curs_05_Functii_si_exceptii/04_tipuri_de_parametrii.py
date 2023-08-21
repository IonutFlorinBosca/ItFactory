def plus(a, b):  # a si b sunt parametrii(numele folosite pentru argumentele unei functii)
    return a + b


plus(1, 2)  # 1 si 2 sunt argumente(argumentele sunt valorile parametrilor)


################################################################
# Default arguments(parametrii cu valoare implicita)
def plus(a, b=2):
    return a + b


plus(1)  # Daca nu specificam o valoare explicita pentru b, atunci va lua valoarea implicita 2
plus(1, 3)


#################################################################
# Keyword arguments (argumente cu nume)
def plus_keyword(a, b):
    return a + b


plus_keyword(a=1, b=2)
plus_keyword(b=2, a=1)  # Specificand argumentele prin nume nu mai este necesar sa pastram ordinea lor


###############################################################
# Variable number of arguments
def plus_many(*args):
    print(args)
    return sum(args)


plus_many(1, 2, 3, 4, 5, 6, 7, 8)
plus_many()
plus_many(*[1, 2, 3])  # Steluta se mai numeste unpacking (scoate toate elem din lista)


def plus_many_2(**kwargs):
    print(kwargs)
    print(sum(kwargs.values()))


plus_many_2(a=1, b=2)
plus_many_2(k=5, x=17)


def plus_many_3(*args, **kwargs):
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())

plus_many_3(1, 2, 3, a=7, b=9)
plus_many_3(1, 2)
plus_many_3(a=7, c=9)
plus_many_3()
# plus_many_3(a=1, 3) !!! -> Parametrii pozitionali pot fi pusi doar inainte de cei cu nume
