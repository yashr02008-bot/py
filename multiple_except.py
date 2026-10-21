# Topic: Multiple except clauses
for value in ["10", "abc", "0"]:
    try:
        print(100 / int(value))
    except ValueError:
        print(value, "-> not a number")
    except ZeroDivisionError:
        print(value, "-> cannot divide by zero")
