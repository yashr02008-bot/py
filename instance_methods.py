# Topic: Instance methods
class Rectangle:
    def __init__(self, l, w):
        self.l, self.w = l, w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2 * (self.l + self.w)
r = Rectangle(4, 5)
print(r.area(), r.perimeter())
