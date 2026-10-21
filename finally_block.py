# Topic: finally - always runs
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Error")
finally:
    print("This always runs (cleanup)")
