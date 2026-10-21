# Topic: Polymorphism with shapes
class Shape:
    def area(self): return 0
class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
class Triangle(Shape):
    def __init__(self, b, h): self.b, self.h = b, h
    def area(self): return 0.5 * self.b * self.h
for sh in [Square(4), Triangle(6, 3)]:
    print(type(sh).__name__, sh.area())
