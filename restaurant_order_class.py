# Topic: Restaurant order class
class Order:
    GST = 5  # class attribute
    def __init__(self, table):
        self.table, self.items = table, []
    def add(self, name, price):
        self.items.append((name, price))
    def bill(self):
        sub = sum(p for _, p in self.items)
        return sub + sub * Order.GST / 100
o = Order(7)
o.add("Pasta", 220); o.add("Mojito", 120)
print("Table", o.table, "Bill:", o.bill())
