# Topic: IndexError
a = [1, 2, 3]
try:
    print(a[10])
except IndexError:
    print("Index is out of range")
