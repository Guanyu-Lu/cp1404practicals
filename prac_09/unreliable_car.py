import random
from prac_09.car import Car

class UnreliableCar(Car):

    """Unreliable car is a car that can only be driven under certain circumstances."""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on reliability."""
        if random.randint(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven =  0
        return distance_driven

    def __str__(self):
        """Return a string representation of the UnreliableCar."""
        return super().__str__()