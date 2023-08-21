"""
Decoratori -> sunt combinarea a 3 concepte
"""


# Functii ca argumente
def say_hello(name):
    return f"Hello {name}"


def say_hi(name):
    return f"Hi {name}"


def greet_bob(func):
    return func('bob')


print(greet_bob(say_hello))
print(greet_bob(say_hi))


# Functii interne

def parent():
    def first():
        print("Hello from first")

    def second():
        print("Hello from second")

    second()
    first()


parent()


# Returnare de functii

def parent(n):
    def first():
        print("first")

    def second():
        print("second")

    if n == 1:
        return first
    return second


f = parent(1)  # -> este o functie interna
f()

print("--" * 40)

# Decoratori simpli
import functools


def my_decorator(func):
    @functools.wraps(func)  # se adauga pentru a nu se suprascrie functia decorata
    # cu functia wrapper
    def wrapper():
        print("Ceva se intampla inainte de apelul functiei decorate")
        func()
        print("Ceva se intampla dupa de apelul functiei decorate")

    return wrapper


@my_decorator
def say_we():
    print("weeeeeee")


say_we()


# Decoratori pentru functii cu argumente

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twice
def say_salut(name):
    print(f"Salut {name}")

say_salut("Bob")