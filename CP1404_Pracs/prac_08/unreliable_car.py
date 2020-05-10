"""
Unreliable Car which won't drive when the car
becomes unreliable (using randint), this is derived
from class Car.
"""


from random import randint
from prac_08.car import Car

class UnreliableCar(Car):
    "Unreliable Car type from main class Car"
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        "Drive car dependent on reliability of said Car"
        random_number = randint(0, 100)
        if random_number > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven