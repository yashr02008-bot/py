# Topic: Multilevel inheritance
class Grandparent:
    def a(self): print("Grandparent method")
class Parent(Grandparent):
    def b(self): print("Parent method")
class Child(Parent):
    def c(self): print("Child method")
x = Child()
x.a(); x.b(); x.c()
