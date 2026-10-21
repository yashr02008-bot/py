# Topic: Full try-except-else-finally
def divide(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        print("Division by zero")
    else:
        print("Result:", r)
    finally:
        print("Done\n")
divide(10, 2)
divide(5, 0)
