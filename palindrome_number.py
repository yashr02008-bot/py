# Topic: Palindrome number
n = 12321
original, rev = n, 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Palindrome" if original == rev else "Not palindrome")
