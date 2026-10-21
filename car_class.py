# Topic: Car class with actions
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0
    def accelerate(self, n):
        self.speed += n
    def brake(self, n):
        self.speed = max(0, self.speed - n)
c = Car("Tata")
c.accelerate(60); c.brake(20)
print(c.brand, c.speed)
