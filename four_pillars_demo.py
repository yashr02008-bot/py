# Topic: Four pillars in one program
from abc import ABC, abstractmethod
class Animal(ABC):  # Abstraction
    def __init__(self, name):
        self._name = name  # Encapsulation
    @abstractmethod
    def speak(self): pass
class Dog(Animal):  # Inheritance
    def speak(self): return self._name + " says Woof"  # Polymorphism
class Cat(Animal):
    def speak(self): return self._name + " says Meow"
for a in (Dog("Tommy"), Cat("Kitty")):
    print(a.speak())
