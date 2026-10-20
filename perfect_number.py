# Topic: Perfect number
n = 28
total = sum(i for i in range(1, n) if n % i == 0)
print("Perfect" if total == n else "Not perfect")
