# Topic: Polymorphism - payment methods
class Cash:
    def pay(self, amt): print("Paid", amt, "in cash")
class UPI:
    def pay(self, amt): print("Paid", amt, "using UPI")
class Card:
    def pay(self, amt): print("Paid", amt, "by card")
for method in (Cash(), UPI(), Card()):
    method.pay(500)
