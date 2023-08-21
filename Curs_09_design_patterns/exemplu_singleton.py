"""
Singleton -> design pattern care ne permite sa avem o clasa care returneaza
mereu aceeasi instanta
          -> de obicei se foloseste in situatii in ca nu ne intereseaza obiectul
          in sine ci doar anumite functionalitati ale acestuia
Avantaje: -> poti fi sigur ca o clasa Singleton are doar o singura instanta
        -> poti avea acces global catre aceasta instanta
        -> obiectul Singleton este initializat doar o singura data(prima data cand este cerut)
Dezavantaje: -> poate masca un design defectuos , de exemplu atunci cand
conponentele unui sistem stiu prea multe unele despre celelalte
"""


class SingletonLogger:
    _instance = None

    # functia __init__ in Python nu este un constructor traditional, ci doar
    # un initializator. Inainte de __init__ este apelata functia __new__
    # unde se creeaza de fapt obiectul
    def __new__(cls, *args, **kwargs):  # Functia new apartine clasei
        # Functia new nu are self ca prim argument pentru ca self nu
        # exista inca la momentul rularii, in schimb avem cls care este
        # o referinta catre clasa curenta
        if cls._instance is None:  # prima data cand este apelata SingletonLogger
            # se creeaza obiectul
            print("Creating object")
            cls._instance = super().__new__(cls)
        return cls._instance  # returnam acelasi obiect de fiecare data


# logger = SingletonLogger()
# logger2 = SingletonLogger()
# print(logger, logger2)
# print(logger is logger2)


class SingletonFileLogger(SingletonLogger):  # Mostenirea facuta in acest fel duce la problema
    # ca obiectul instantei Singleton poate fi de tipul SingletonLogger,
    # nu SingletonFileLogger, daca el se creaaza inainte
    # Ca si solutie vezi exemplul de mai joc cu SingletonLoggerMultiClass
    def __init__(self, file_name):
        self.file_name = file_name


sfl = SingletonFileLogger("Hello.txt")
sfl2 = SingletonFileLogger("Hello2.txt")
print(sfl, sfl2)
print(sfl.file_name, sfl2.file_name)

print("*" * 40)


class SingletonLoggerMultiClass:
    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance.get(cls) is None:  # verifica daca exista o instanta pentru clasa curenta
            # daca nu exista, o creeaza
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


class SingletonFileLogger2(SingletonLoggerMultiClass):
    def __init__(self, file_name):
        self.file_name = file_name


l = SingletonLoggerMultiClass()
s = SingletonFileLogger2("Hello.txt")
print(l, s)
l2 = SingletonLoggerMultiClass()
s2 = SingletonFileLogger2("Hello.txt")
print(l2, s2)
