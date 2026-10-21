# Topic: Vehicle family
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels
class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)
class Car(Vehicle):
    def __init__(self):
        super().__init__(4)
print(Bike().wheels, Car().wheels)
