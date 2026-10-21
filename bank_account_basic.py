# Topic: BankAccount class (basic)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner, self.balance = owner, balance
    def deposit(self, amt):
        self.balance += amt
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Not enough money")
acc = BankAccount("Amit", 500)
acc.deposit(200); acc.withdraw(1000); acc.withdraw(300)
print(acc.owner, acc.balance)
