# Topic: else clause - runs if no exception
try:
    n = int("42")
except ValueError:
    print("Bad number")
else:
    print("Good number:", n)  # only when no error
