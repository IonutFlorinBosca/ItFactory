# Singleton
# Se da următoarea clasa:
#
#
class PresedinteRomania:
    _instance = None

    def __new__(cls):
        """
        Motoda speciala __new__ este responsabila pentru crearea
        instantei obiectului.
        In majoritatea cazurilor nu avem nevoie sa suprascriem aceasta
        metoda, dar pentru singleton acesta e locul in care ne asiguram
        ca exista doar o instanta
        """
        if cls._instance is None:
            cls._instance = super(PresedinteRomania, cls).__new__(cls)
            """
            Verificam daca exista deja o instanta, daca nu,
            cream una noua.
            Metoda super() ofera o cale de a apela metode din clasa
            de baza(parinte).
            In acest caz --> obiect
            """

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'


#
# In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:
#
a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

# Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
# Vom folosi functia `__new__` (adevăratul constructor din Python)
# Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
# La orice alta apelare, vom returna obiectul deja existent
print("--" * 40)


class Fabrica:
    def __init__(self, translations):
        self.translations = translations

    def localize(self, word):
        return self.translations.get(word, "Translation not available!")


class EnglishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'car',
                'barbat': 'man',
                'femeie': 'women',
                'copil': 'child'
            }
        )


class FrenchTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'voiture',
                'barbat': 'homme',
                'femeie': 'femme',
                'copil': 'enfant'
            }
        )


class SpanishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'coche',
                'barbat': 'hombre',
                'femeie': 'mujer',
                'copil': 'nino'
            }
        )


class TranslatorFactory:
    @classmethod
    def get_translator(cls, language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator()
        else:
            return ValueError('Invalid language!')


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
spanish_trans = factory.get_translator('es')
french_trans = factory.get_translator('fr')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')
print("--" * 40)

from abc import ABC, abstractmethod


class TranslatorInterface(ABC):
    @staticmethod
    @abstractmethod
    def localize(word):
        pass


class EnTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'car',
        'barbat': 'man',
        'femeie': 'women',
        'copil': 'child'
    }

    @staticmethod
    def localize(word):
        return EnTranslator.traduceri.get(word, word)  # prima - ce returneaza, a doua - ce returneaza daca NU ESTE


class FrTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'voiture',
        'barbat': 'homme',
        'femeie': 'femme',
        'copil': 'enfant'
    }

    @staticmethod
    def localize(word):
        return FrTranslator.traduceri.get(word, word)  # prima - ce returneaza, a doua - ce returneaza daca NU ESTE


class EsTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'coche',
        'barbat': 'hombre',
        'femeie': 'mujer',
        'copil': 'nino'
    }

    @staticmethod
    def localize(word):
        return EsTranslator.traduceri.get(word, word)  # prima - ce returneaza, a doua - ce returneaza daca NU ESTE


print(f"In engleza : {EnTranslator.localize('masina')}")
print(f"In spaniola : {EsTranslator.localize('masina')}")
print(f"In franceza : {FrTranslator.localize('masina')}")
