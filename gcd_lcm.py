# Topic: GCD and LCM
a, b = 12, 18
x, y = a, b
while y:
    x, y = y, x % y  # Euclid's method
print("GCD =", x, "LCM =", a * b // x)
