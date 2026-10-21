# Topic: Student marks report class
class Student:
    def __init__(self, name, **marks):
        self.name, self.marks = name, marks
    def total(self): return sum(self.marks.values())
    def percent(self): return self.total() / len(self.marks)
    def report(self):
        print(f"{self.name}: total={self.total()}, percent={self.percent():.1f}")
Student("Riya", maths=90, science=85, english=80).report()
