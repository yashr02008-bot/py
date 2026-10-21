# Topic: Shopping cart class
class Cart:
    def __init__(self):
        self.items = {}
    def add(self, name, price):
        self.items[name] = price
    def total(self):
        return sum(self.items.values())
c = Cart()
c.add("Pizza", 250); c.add("Coke", 60)
print("Total:", c.total())
