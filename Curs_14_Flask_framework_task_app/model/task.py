from dataclasses import dataclass
from enum import Enum
# daca vrem sa definim o lista cu niste optiuni ca si constrangeri se foloseste Enum

class TaskStatus(Enum):
    d = "done"
    t = "todo"
    p = "in progress"


@dataclass
class Task:
    title: str
    todo: str
    status: TaskStatus
