# Ca sa facem o exceptie custom trebuie sa cream o clasa care mosteneste din clasa "Exception"
class CustomException(Exception):  # -> preia din clasa din paranteza toate atributele
    pass # Nu definim nimic special, doar numele acestei functii ne intereseaza


"""
Sa se scrie o functie care verifica daca o lista de numere intregi
primite ca parametru contine numere negative.
Daca da, sa se arunce o exceptie specifica
"""


class ContainsNegativeNumbersException(Exception):
    pass


def verify_negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            raise ContainsNegativeNumbersException(f"Contine {num}")


verify_negative_numbers([4, 5, 6, -1])
