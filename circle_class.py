# Topic: Circle class
import math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def circumference(self):
        return 2 * math.pi * self.r
c = Circle(5)
print(round(c.area(), 2), round(c.circumference(), 2))
