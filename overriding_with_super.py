# Topic: Overriding and still using parent method
class Base:
    def greet(self):
        print("Hello from Base")
class Child(Base):
    def greet(self):
        super().greet()
        print("Hello from Child")
Child().greet()
