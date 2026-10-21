# Topic: Employee and Manager (inheritance)
class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary
    def info(self):
        return f"{self.name} earns {self.salary}"
class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team
    def info(self):
        return super().info() + f" and leads {self.team} people"
print(Employee("Amit", 30000).info())
print(Manager("Riya", 60000, 5).info())
