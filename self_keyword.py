# Topic: self keyword
class Dog:
    def __init__(self, name):
        self.name = name  # self = this object
    def bark(self):
        print(self.name, "says Woof")
Dog("Tommy").bark()
Dog("Bruno").bark()
