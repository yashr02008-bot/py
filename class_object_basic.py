# Topic: Class vs object (class = design, object = real thing)
class Car:  # blueprint
    pass
c1 = Car()  # real car made from the blueprint
c2 = Car()
print(type(c1), c1 is c2)
