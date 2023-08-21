ske = ('-' * 44)
print(ske)


class PresedinteRomania:
    _instance = None

    def __new__(cls):
        """
        Metoda speciala new este responsabila pentru crearea instantei obiectului.
        In majoritatea cazurilor nu avem nevoie sa suprascriem aceasta metoda,
        dar pentru 'Singleton' acesta e locul in care ne asiguram ca exista doar o singura instanta
        """
        if cls._instance is None:
            cls._instance = super(PresedinteRomania, cls).__new__(cls)
            """
            Verificam daca exista deja o instanta, daca nu, cream una noua.
            Metoda super() ofera o cale de a apela metode din clasa de baza (parinte).
            In acest caz ---> obiect
            """

        return cls._instance

    def __str__(self):
        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'


a = PresedinteRomania()
b = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Acelasi obiect? {a is b}')

print(ske)


class Fabrica:
    def __init__(self, translations):
        self.translations = translations

    def localize(self, word):
        return self.translations.get(word, 'Translation not available')


class EnglishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'car',
                'barbat': 'man',
                'femeie': 'wonan',
                'copil': 'child'

            })


class FrenchTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'voiture',
                'barbat': 'homme',
                'femeie': 'femme',
                'copil': 'enfant'

            })


class SpanishTranslator(Fabrica):
    def __init__(self):
        super().__init__(
            {
                'masina': 'coche',
                'barbat': 'hombre',
                'femeie': 'mujer',
                'copil': 'nino'

            })


class TranslatorFactory():
    @classmethod
    def get_translator(cls, language):
        if language == 'en':
            return EnglishTranslator()
        elif language == 'fr':
            return FrenchTranslator()
        elif language == 'es':
            return SpanishTranslator()
        else:
            return ValueError('Invalid language code')


factory = TranslatorFactory()

english_trans = factory.get_translator('en')
french_trans = factory.get_translator('fr')
spanish_trans = factory.get_translator('es')

print(f'In engleza zicem {english_trans.localize("masina")}')
print(f'In spaniola zicem {spanish_trans.localize("masina")}')
print(f'In franceza zicem {french_trans.localize("masina")}')

print(ske)

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
        'femeie': 'wonan',
        'copil': 'child'

    }

    @staticmethod
    def localize(word):
        return EnTranslator.traduceri.get(word, word)  # prima - ce returneaza, a doua - ce returneaza daca NU


class FrTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'voiture',
        'barbat': 'homme',
        'femeie': 'femme',
        'copil': 'enfant'

    }

    @staticmethod
    def localize(word):
        return FrTranslator.traduceri.get(word, word)


class EsTranslator(TranslatorInterface):
    traduceri = {
        'masina': 'coche',
        'barbat': 'hombre',
        'femeie': 'mujer',
        'copil': 'nino'

    }

    @staticmethod
    def localize(word):
        return EsTranslator.traduceri.get(word, word)


print(f'In engleza ii zicem {EnTranslator.localize("masina")}')
print(f'In franceza ii zicem {FrTranslator.localize("masina")}')
print(f'In spaniol ii zicem {EsTranslator.localize("masina")}')

print(ske)
