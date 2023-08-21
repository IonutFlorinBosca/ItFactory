def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Date intrare args {args}")
        print(f"Date intrare kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Date iesire {result}")
        return result

    return wrapper

@logger
def suma(a, b):
    return a + b

@logger
def suma2(a, b, c):
    return a + b + c


suma(a=3, b=4)
print("--"*40)
suma(5,6)
print("--"*40)

suma2(1, 2, 5)