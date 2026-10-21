# Topic: ValueError
try:
    n = int("12abc")
except ValueError:
    print("Please enter digits only")
