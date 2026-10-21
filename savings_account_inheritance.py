# Topic: SavingsAccount inherits BankAccount
class BankAccount:
    def __init__(self, bal): self._bal = bal
    def deposit(self, a): self._bal += a
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self._bal += self._bal * rate / 100
s = SavingsAccount(1000)
s.deposit(500)
s.add_interest(10)
print(s._bal)
