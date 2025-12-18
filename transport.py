class Transport:
    def move(self):
        print("Taşıt Hareket Ediyor")

class Car(Transport):
    def move(self):
        print("Araba kaaradan gidiyor.")

class Plane(Transport):
    def move(self):
        print("Uçak havadan uçuyor")

t1 = Transport()
t2 = Car()
t3 = Plane()

t1.move()
t2.move()
t3.move()