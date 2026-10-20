# Topic: Pattern - hollow square
n = 5
for i in range(n):
    for j in range(n):
        print("*" if i in (0, n - 1) or j in (0, n - 1) else " ", end=" ")
    print()
