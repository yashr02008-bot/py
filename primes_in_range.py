# Topic: Primes from 1 to 50
for n in range(2, 51):
    for i in range(2, n):
        if n % i == 0:
            break
    else:  # runs only if no break happened
        print(n, end=" ")
print()
