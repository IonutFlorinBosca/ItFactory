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
plus_many(*[1, 2, 3, 6, 7, 8])  # Steluta se mai numeste unpacking (scoate toate elem din lista)
# Steluta este o modalitate de a scoate toate acele elemente din lista
# Steluta scoate valorile din lista si le pune ca si cum am apela functia plus_many(1,2,3)
# !!!Argumentele trebuie sa fie pozitionale, nu trebuie sa fie argumente cu nume!!!

def plus_many_2(**kwargs): # ** este aceeasi treaba ca si inainte doar ca in loc de tupluri sunt dictionare
    # daca vrem sa apelam o functie cu oricate argumente, dar ele sa fie argumente cu nume, adica nume=valoare,
    # va trebui sa le punem in kwargs!!
    print(kwargs)
    print(sum(kwargs.values())) # aici accesam valorile cheilor si facem suma valorilor


plus_many_2(a=1, b=2)
plus_many_2(k=5, x=17)


def plus_many_3(*args, **kwargs): #aici combinam cele explicate mai sus
    print(args, kwargs)
    return sum(args) + sum(kwargs.values())


plus_many_3(1, 2, 3, a=7, b=9) # aici specificam atat parametrii pozitionali cat si parametrii cu nume
plus_many_3(1, 2) # merge si daca specificam doar parametrii pozitionali
plus_many_3(a=7, c=9)   # merge si daca specificam doar parametrii cu nume
plus_many_3()# merge sa apelam si fara nici un argument
# plus_many_3(a=1, 3) !!! -> Parametrii pozitionali pot fi pusi doar inainte de cei cu nume
# Parametrii pozitionali ii pune in tupluri si pe ceilalti ii pune in dictionare, chit ca sunt, chit ca nu!
