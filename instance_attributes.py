# Topic: Instance attributes (unique per object)
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
a, b = Phone("Apple", 80000), Phone("Samsung", 50000)
print(a.brand, a.price)
print(b.brand, b.price)
