# Implementați următorii decoratori:
# timeit – decorator care măsoară timpul de execuție al unei funcții
# logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
import time

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Date intrare args {args}")
        print(f"Date intrare kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Date iesire {result}")
        return result

    return wrapper

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rezultat = func(*args, **kwargs)
        stop = time.time()
        print(f"Functia {func.__name__} a rulat in {stop - start:.5f} secunde")
        # func .__name__ -> permite afisarea numelui functiei preluate
        return rezultat

    return wrapper


def salut(func):
    def wrapper(*args, **kwargs):
        print("Salut")
        return func(*args, **kwargs)

    return wrapper


@logger
def descrie_vremea(grade):
    time.sleep(2)
    return f"Vremea e frumoasa, sunt {grade} de grade"


print(descrie_vremea(30))
print("--" * 40)
