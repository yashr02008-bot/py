# Topic: Public, protected and private attributes
class Demo:
    def __init__(self):
        self.public = "anyone can use"
        self._protected = "use inside class and children"
        self.__private = "only inside this class"
d = Demo()
print(d.public)
print(d._protected)  # works, but it is a warning to others
try:
    print(d.__private)
except AttributeError:
    print("Private attribute is hidden")
