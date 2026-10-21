# Topic: Practical - restaurant menu class
class MenuItem:
    def __init__(self, name, price, veg=True):
        self.name, self.price, self.veg = name, price, veg
    def __str__(self):
        return f"{self.name} - Rs {self.price} ({'Veg' if self.veg else 'Non-veg'})"
menu = [MenuItem("Paneer Tikka", 250), MenuItem("Chicken Wrap", 180, False)]
for item in menu:
    print(item)
