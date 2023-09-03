class Car:
    def go(self):
        print("Vrum vrum")

    def start(self):
        print("Starting car")


class Flyable:
    def fly(self):
        print("flu, flu")

    def start(self):
        print("starting flyable")

# Mostenire multipla - noua clasa FlyingCar mosteneste atributele si metodele atat clasei Car cat si a clasei Flyable
class FlyingCar(Car,Flyable):
    pass

# la initializarea instantei punem doar paranteze, deoarece clasa nu are constructor, deci nu are argumente
fc = FlyingCar()
fc.fly()
fc.go()
# mai jos se apeleaza metoda start care exista atat in clasa Car cat si in Flyable si este definita cu acelasi nume
# deoarece in clasa FlyingCar s-a mostenit prima data din clasa Car si apoi din Flyable, cand se va apela metoda
# start intr-o instanta a clasei, aceasta se va apela din clasa Car.
# Deci, ordinea mostenirii multiple conteaza!!!
# aceasta regula este specifica Python si se numeste Method Resolution Order(MRO) - ordinea de rezolvare a metodelor
fc.start()

print("*"*40)
# Method resolution order (MRO) --> regula dupa care se decide
#care este functia ce se apeleaza atunci cand avem o mostenire
#multipla si functii cu acelasi nume (de la stanga la dreapta)
# REGULA SPECIFICA PYTHON

class FlyingCar2(Flyable, Car):
    pass

fc2 = FlyingCar2()
fc2.start()