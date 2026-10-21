# Topic: Mini project - withdraw with exceptions
balance = 1000
def withdraw(amount):
    global balance
    if amount > balance:
        raise ValueError("Insufficient balance")
    balance -= amount
for amt in [300, 900]:
    try:
        withdraw(amt)
        print("Withdrew", amt, "Balance:", balance)
    except ValueError as e:
        print("Failed:", e)
