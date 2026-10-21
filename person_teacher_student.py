# Topic: Person, Teacher, Student hierarchy
class Person:
    def __init__(self, name):
        self.name = name
    def role(self): return "Person"
class Teacher(Person):
    def role(self): return "Teacher"
class Student(Person):
    def role(self): return "Student"
for p in [Teacher("Mr. Shah"), Student("Amit")]:
    print(p.name, "is a", p.role())
