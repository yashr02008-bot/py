# Topic: super() function
class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)  # call parent constructor
        self.roll = roll
s = Student("Amit", 101)
print(s.name, s.roll)
