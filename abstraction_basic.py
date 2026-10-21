# Topic: Abstraction - hide details, show essentials
from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amt): ...
class UPI(Payment):
    def pay(self, amt):
        print("Paying", amt, "via UPI")
UPI().pay(250)
try:
    Payment()
except TypeError as e:
    print("Cannot create abstract class")
