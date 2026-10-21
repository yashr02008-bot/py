# Topic: raise - trigger an exception
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Caught:", e)
