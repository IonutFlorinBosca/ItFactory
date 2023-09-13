import csv
from model.task import Task


def _read_tasks():
    with open("D:\workspace\IT_Factory\Curs_14_Flask_framework_task_app/data/tasks.csv", "r") as f:
        reader = csv.DictReader(f)
        return list(reader)
    # transformam iteratorul reader in lista de dictionare


print(_read_tasks())


def get_tasks():
    tasks = _read_tasks()
    # return [Task(*task.values()) for task in tasks] # List comprehension
    # in list comprehension scapam de necesitatea de a introduce o variabila noua si de
    # a apela append
    new_tasks = []
    for task in tasks:
        # new_tasks.append(Task(*task.values())) -> varianta 1
        new_tasks.append(Task(task["title"], task["todo"], task["status"]))
    return new_tasks


def add_task(task_data):
    with open("D:\workspace\IT_Factory\Curs_14_Flask_framework_task_app/data/tasks.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "todo", "status"])
        writer.writerow(task_data)


def _write_tasks(tasks):
    with open("D:\workspace\IT_Factory\Curs_14_Flask_framework_task_app/data/tasks.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "todo", "status"])
        writer.writeheader()
        writer.writerows(tasks)


def update_task(title, task_data):
    tasks = _read_tasks()
    for task in tasks:
        if task["title"] == title:
            task.update(task_data)
            break  # break e folosit ca si punct de optimizare ca sa nu mai trebuiasca
            # sa iteram dupa ce am gasit elementul, pentru ca l-am gasit deja
    _write_tasks(tasks)

def delete_task(title):
    tasks = _read_tasks()
    new_tasks = [task for task in tasks if task["title"]!= title]
    _write_tasks(new_tasks)

