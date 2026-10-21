# Topic: What is an exception
print("Before")
try:
    print(10 / 0)  # crashes the program normally
except ZeroDivisionError:
    print("Exception handled")
print("After - program continues")
