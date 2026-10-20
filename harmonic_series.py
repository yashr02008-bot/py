# Topic: Sum of series 1 + 1/2 + 1/3 + ...
n = 5
total = 0
for i in range(1, n + 1):
    total += 1 / i
print("Harmonic sum =", round(total, 4))
