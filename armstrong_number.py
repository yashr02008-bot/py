# Topic: Armstrong number
n = 153
digits = len(str(n))
total = sum(int(d) ** digits for d in str(n))
print("Armstrong" if total == n else "Not Armstrong")
