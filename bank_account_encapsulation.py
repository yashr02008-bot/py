# Topic: BankAccount with encapsulation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private
    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt
    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt
            return True
        return False
    def get_balance(self):
        return self.__balance
a = BankAccount("Riya", 1000)
a.deposit(500)
print(a.withdraw(2000), a.withdraw(700))
print("Balance:", a.get_balance())
