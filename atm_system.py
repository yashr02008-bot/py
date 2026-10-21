# Topic: ATM with PIN (encapsulation)
class ATM:
    def __init__(self, pin, balance):
        self.__pin, self.__balance = pin, balance
    def withdraw(self, pin, amt):
        if pin != self.__pin:
            return "Wrong PIN"
        if amt > self.__balance:
            return "Insufficient funds"
        self.__balance -= amt
        return f"Take cash. Balance {self.__balance}"
atm = ATM(1234, 5000)
print(atm.withdraw(1111, 500))
print(atm.withdraw(1234, 9000))
print(atm.withdraw(1234, 500))
