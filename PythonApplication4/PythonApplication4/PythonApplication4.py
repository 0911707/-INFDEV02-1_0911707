class Tyre:
    def __init__(self, presure, size):
        self.presure = presure
        self.size = size

class Wheel:
    def __init__(self, brand):
        self.brand = brand

class Engine:
    def __init__(self, capacity, power):
        self.capacity = capacity
        self.power = power

class Seat:
    def __init__(self, height):
        self.height = height

class Light:
    def __init__(self, watt):
        self.watt = watt

class Person:
    def __init__(self, gender, age, length):
        self.gender = gender
        self.age = age
        self.length = length

class Car:
    def __init__(self, presure, size, brand, capacity, power , height, watt, gender, age, length):
        self.Tyre = Tyre(presure, size)
        self.Wheel = Wheel(brand)
        self.Engine = Engine(capacity, power)
        self.Seat = Seat(height)
        self.Light = Light(watt)
        self.Person = Person(gender, age, length)

bmw = Car(1.5, 24, "bmw", "v8", 500, 1.80, 20, "man", 17, 1.80)
print(bmw.Tyre.presure)
print(bmw.Tyre.size)
print(bmw.Wheel.brand)
print(bmw.Engine.capacity)
print(bmw.Engine.power)
print(bmw.Seat.height)
print(bmw.Light.watt)
print(bmw.Person.gender)
print(bmw.Person.age)
print(bmw.Person.length)


