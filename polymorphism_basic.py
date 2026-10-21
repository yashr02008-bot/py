# Topic: Polymorphism - same method, different behaviour
class Cat:
    def sound(self): return "Meow"
class Dog:
    def sound(self): return "Woof"
for animal in [Cat(), Dog()]:
    print(animal.sound())
