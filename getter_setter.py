# Topic: Getter and setter methods
class Person:
    def __init__(self, age):
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")
p = Person(20)
p.set_age(-5)
p.set_age(25)
print(p.get_age())
