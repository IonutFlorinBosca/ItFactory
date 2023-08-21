class CustomException(Exception):  # -> preia din clasa din paranteaza toate atributele
    pass


"""
Sa se scrie o functie care verifica daca o lista de numere intregi
primite ca parametru contine numere negative.
Daca da, sa se arunce o exceptie specifica
"""


class ContaineNegativeNumbersException(Exception):
    pass


def verify_negative_numbers(numbers):
    for num in numbers:
        if num < 0:
            raise ContaineNegativeNumbersException(f"Contine {num}")


verify_negative_numbers([4, 5, 6, -1])
