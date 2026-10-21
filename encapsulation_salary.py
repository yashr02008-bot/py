# Topic: Encapsulation - protect salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    def raise_salary(self, percent):
        if 0 < percent <= 20:
            self.__salary += self.__salary * percent / 100
    def get_salary(self):
        return self.__salary
e = Employee("Sam", 30000)
e.raise_salary(10)
e.raise_salary(50)  # rejected
print(e.get_salary())
