# METODE DE STRING
elf = "alpha 0123456789 ASD"
# se numara incepand cu 0 index => elf = 0-19 caractere

# len = "metoda de string"
# len = se aplica datelor care au "lungime" (daca este transformat in string)
# lunigmea string-ului
print(len(elf))

# replace
# inlocuire caractere din variabila existenta
druid = elf.replace("alpha", "beta")
print(f"druid = {druid}")
print(f"elf = {elf}")

# replace inlocuieste doar daca gaseste
druid2 = elf.replace("ASD", "bon")
print(druid2)

# printare de string partiala (SLICING)
print(elf[:10]) # metoda de slicing - primele caractere
print(elf[-10:]) # metoda de slicing - ultimele caractere
print(elf[4:8]) # metoda de slicing - ce "zona anume"


# string-ul este un tip de data IMMUTABLE (nu pot schimba variabila respectiva)
print(elf[0])
print(elf[19])
# elf[0] = "X"
elf = "X - a inlocuit ce scria anterior / suprascriere"
print(elf)
# !!! 'str' object does not support item assignment

print("-"*30) # separator pentru vizualizare in consola


# numar de aparitii a unui caracter - COUNT
elf = "alpha 0123456789 ASD"
print(elf.count("a")) # numararea caracterului "a" in string (! case sensitive)
print(elf.count("alpha1"))

print("-"*30)

nume = "kogalniceanu"
print(nume.upper()) # transforma in upper case
print(nume.capitalize()) # capitalizare la prima litera

separator = "-"*40
print(separator)

print(nume.find("ala")) # "-1" - nu gaseste
print(nume.find("cea")) # returneaza de unde gaseste
