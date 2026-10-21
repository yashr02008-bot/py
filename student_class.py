# Topic: Practical - Student class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # list of marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def grade(self):
        a = self.average()
        return "A" if a >= 75 else "B" if a >= 50 else "C"
s = Student("Riya", [80, 90, 70])
print(s.name, s.average(), s.grade())
