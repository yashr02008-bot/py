# Topic: Count objects using class attribute
class Visitor:
    count = 0
    def __init__(self):
        Visitor.count += 1
Visitor(); Visitor(); Visitor()
print("Total visitors:", Visitor.count)
