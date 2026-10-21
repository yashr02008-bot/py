# Topic: TypeError
try:
    print("5" + 5)  # text + number
except TypeError as e:
    print("TypeError:", e)
