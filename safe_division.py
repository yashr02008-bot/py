# Topic: Safe division function
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(safe_divide(10, 2), safe_divide(1, 0))
