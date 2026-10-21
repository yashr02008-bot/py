# Topic: Method overriding
class Bird:
    def fly(self):
        print("Bird can fly")
class Penguin(Bird):
    def fly(self):  # same name, new behaviour
        print("Penguin cannot fly")
Bird().fly()
Penguin().fly()
