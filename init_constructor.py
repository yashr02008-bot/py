# Topic: __init__ constructor
class Student:
    def __init__(self, name, age):  # runs when object is created
        self.name = name
        self.age = age
s = Student("Amit", 20)
print(s.name, s.age)
