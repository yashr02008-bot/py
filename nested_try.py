# Topic: Nested try-except
try:
    try:
        int("abc")
    except ValueError:
        print("Inner caught ValueError")
        raise TypeError("Passed to outer")
except TypeError as e:
    print("Outer caught:", e)
