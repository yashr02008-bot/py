# Topic: Reverse a number
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10  # push last digit to rev
    n //= 10
print("Reversed:", rev)
