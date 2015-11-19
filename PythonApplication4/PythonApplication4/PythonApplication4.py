class Tyre:
    def __init__(self, presure, size):
        self.presure = presure
        self.size = size

class Wheel:
    def __init__(self, Tyre):
        self.wheel = Tyre

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
    def __init__(self, Wheel, Engine, Seat, Light, Person):
        self.Wheel = Wheel
        self.Engine = Engine
        self.Seat = Seat
        self.Light = Light
        self.Person = Person

bmw = Car()
