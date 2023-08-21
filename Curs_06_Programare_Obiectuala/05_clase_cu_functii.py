class Dog:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def bark(self):  # -->self este referinta catre obiectul curent(trebuie sa apara mereu, primul)
        print("ham ham")
    def get_name(self):
        return f"Eu sunt {self.name}"

d = Dog(age=5, name="Rex")
d.bark()
print(d.get_name())