# Topic: Practical - employee payroll
class Employee:
    def __init__(self, name, basic):
        self.name, self.basic = name, basic
    def salary(self):
        return self.basic + self.basic * 0.2  # 20% allowance
class Intern(Employee):
    def salary(self):
        return self.basic  # no allowance
for e in [Employee("Amit", 30000), Intern("Neha", 10000)]:
    print(e.name, e.salary())
