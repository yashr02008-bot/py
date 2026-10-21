# Topic: Class attributes (shared by all)
class Student:
    school = "ABC School"  # class attribute
    def __init__(self, name):
        self.name = name
a, b = Student("Amit"), Student("Riya")
print(a.name, a.school)
print(b.name, b.school)
Student.school = "XYZ School"  # change once, all see it
print(a.school, b.school)
