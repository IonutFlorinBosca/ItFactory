"""
Serializarea datelor se refera la faptul ca noi dorim persistarea
datelor din aplicatie pentru a fi disponibile in viitor pentru
a putea fi citite sau modificate
"""


# citire date in mod clasic
def read_clasic():
    f = open("date.txt", "r")  # deschiderea fisierului si retinerea
    # lui in variabila 'f'
    try:
        return f.readlines()  # citim toate datele din fisier
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        f.close()  # inchidem fisierul


l = read_clasic()
print(l)

print("--" * 40)


# citire folosind context manager

def read_safe():
    with open("date.txt", "r") as f:
        return f.readlines()


l = read_safe()
print(l)

print("--" * 40)


# Scriere date in fisier
# 'write' suprascrie tot continutul anterior (se pierd datele)
# datele sunt nerecuperabile
def write():
    with open("date.txt", "w") as f:
        f.writelines(["1", "abc", "1 2 3"])


write()

print("--" * 40)


# adaugare date in fisier

def append():
    with open("date.txt", "a") as f:
        f.writelines(["kebab\n"])


append()
