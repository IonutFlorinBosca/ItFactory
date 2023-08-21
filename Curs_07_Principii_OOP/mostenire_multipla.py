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

class FlyingCar(Car,Flyable):
    pass

fc = FlyingCar()
fc.fly()
fc.go()
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