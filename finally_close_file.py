# Topic: finally for closing a file
f = None
try:
    f = open("fc.txt", "w")
    f.write("data")
    print(1 / 0)
except ZeroDivisionError:
    print("Error happened")
finally:
    if f:
        f.close()  # file closes even after error
        print("File closed:", f.closed)
