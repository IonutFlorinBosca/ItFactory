from dataclasses import dataclass
from enum import Enum
# daca vrem sa definim o lista cu niste optiuni ca si constrangeri se foloseste Enum

# ca sa fie mai usor de scris se folosesc data classes
class TaskStatus(Enum):
    d = "done"
    t = "todo"
    p = "in progress"

# clasa TaskStatus defineste cele 3 concepte, iar fiindca aceasta este valoarea unui
# atribut din clasa de mai jos(este o dependenta), valorile acelui atribut sunt restrictionate
# la una dintre cele 3 valori

@dataclass
class Task:
    title: str
    todo: str
    status: TaskStatus

# status nu vrem sa fie string(asta permite sa se scrie acolo orice)
# ca sa restrictionam accesul se va creea o noua clasa care va avea doar cateva atribute