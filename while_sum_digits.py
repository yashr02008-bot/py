# Topic: Sum of digits using while
n = 12345
total = 0
while n > 0:
    total += n % 10  # last digit
    n //= 10  # remove last digit
print("Digit sum =", total)
