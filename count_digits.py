# Topic: Count digits in a number
n = 98765
count = 0
while n > 0:
    n //= 10
    count += 1
print("Digits:", count)
