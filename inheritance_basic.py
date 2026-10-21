# Topic: Inheritance - parent and child
class Animal:
    def eat(self):
        print("Eating...")
class Dog(Animal):  # Dog gets everything from Animal
    def bark(self):
        print("Woof!")
d = Dog()
d.eat()
d.bark()
