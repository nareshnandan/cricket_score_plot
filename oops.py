class Car:
    def start(self):
        print("Car started")

my_car = Car()
my_car.start()

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I am {self.name}")
    
p1 = Person("Naresh")
p1.greet()

class Persons:
    def __init__(self, name):
        self.name = name

    def greeti(self):
        print(f"Hi, I am {self.name}")

p2 = Persons("Deepak")
p2.greeti()

class Animals:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def greet(self):
        print(f"I am {self.name}, I make sound as {self.sound}")


dog = Animals("Tommy", "Bow bow")
dog.greet()


class Vehicle:
    def __init__(self, name, color):
        self.name =  name
        self.color = color

    def car(self):
        print(f"This car model is {self.name} and color is {self.color} ")

maruti = Vehicle("Suziki", "Red")
maruti.car()

class Fan:
    def switch_on(self):
        print("Fan is ON")

my_fan = Fan()
my_fan.switch_on()