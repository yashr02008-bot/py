# Topic: Simple calculator with if-elif
a = float(input("First number: "))
b = float(input("Second number: "))
op = input("Operator (+ - * /): ")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b if b != 0 else "Cannot divide by zero")
else:
    print("Invalid operator")
